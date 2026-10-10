from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.orm import Session

from src.database.models import Role

ROLE_NAMES = ("user", "curator")


def seed_roles(session: Session) -> None:
    statement = insert(Role).values([{"role_name": name} for name in ROLE_NAMES])
    session.execute(statement.on_conflict_do_nothing(index_elements=["role_name"]))
