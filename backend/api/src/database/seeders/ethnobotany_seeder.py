from sqlalchemy import select
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.orm import Session

from src.database.models import Ethnobotany, Species


def seed_ethnobotany(session: Session) -> None:
    species_ids = session.scalars(select(Species.species_id)).all()
    if not species_ids:
        return
    rows = [
        {"species_id": species_id, "verification_status": "pending"}
        for species_id in species_ids
    ]
    statement = insert(Ethnobotany).values(rows)
    session.execute(statement.on_conflict_do_nothing(index_elements=["species_id"]))
