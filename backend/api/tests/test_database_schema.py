import pytest
from alembic.autogenerate import compare_metadata
from alembic.migration import MigrationContext
from sqlalchemy import inspect, select
from sqlalchemy.orm import Session

from src.core.config import get_settings
from src.database.base import Base
from src.database.models import Ethnobotany, Role, Species, User

EXPECTED_TABLES = {
    "roles",
    "users",
    "user_profiles",
    "user_settings",
    "audit_logs",
    "species",
    "ethnobotany",
    "identification_sessions",
    "images",
    "leaf_detections",
    "green_pixel_validations",
    "classification_results",
    "gradcam_results",
    "feedback_corrections",
    "notifications",
}

ONE_TO_ONE_COLUMNS = {
    "user_profiles": "user_id",
    "user_settings": "user_id",
    "ethnobotany": "species_id",
    "leaf_detections": "session_id",
    "green_pixel_validations": "session_id",
    "classification_results": "session_id",
    "gradcam_results": "classification_id",
}


def test_all_erd_tables_exist(db_engine):
    tables = set(inspect(db_engine).get_table_names())
    assert EXPECTED_TABLES <= tables


def test_migration_matches_models(db_engine):
    with db_engine.connect() as connection:
        context = MigrationContext.configure(connection)
        assert compare_metadata(context, Base.metadata) == []


def test_one_to_one_relations_are_unique(db_engine):
    inspector = inspect(db_engine)
    for table, column in ONE_TO_ONE_COLUMNS.items():
        unique_columns = [
            tuple(constraint["column_names"])
            for constraint in inspector.get_unique_constraints(table)
        ]
        assert (column,) in unique_columns, f"{table}.{column} harus unik"


def test_roles_match_openapi_contract(db_engine):
    with Session(db_engine) as session:
        names = set(session.scalars(select(Role.role_name)).all())
    assert names == {"user", "curator"}


def test_seventeen_species_seeded_with_ethnobotany(db_engine):
    with Session(db_engine) as session:
        species_count = len(session.scalars(select(Species.species_id)).all())
        ethnobotany_count = len(
            session.scalars(select(Ethnobotany.ethnobotany_id)).all()
        )
    assert species_count == 17
    assert ethnobotany_count == 17


def test_seeded_curator_is_verified_curator(db_engine):
    if not get_settings().curator_email:
        pytest.skip("CURATOR_EMAIL tidak diisi")
    with Session(db_engine) as session:
        curator = session.scalar(
            select(User).join(Role).where(Role.role_name == "curator")
        )
        assert curator is not None
        assert curator.email_verified is True
        assert curator.profile is not None
        assert curator.password_hash.startswith("$2")
