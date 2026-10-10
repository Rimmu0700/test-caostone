from src.core.config import get_settings
from src.database.seeders.curator_seeder import seed_curator
from src.database.seeders.ethnobotany_seeder import seed_ethnobotany
from src.database.seeders.role_seeder import seed_roles
from src.database.seeders.species_seeder import seed_species
from src.database.session import SessionLocal


def run() -> None:
    settings = get_settings()
    with SessionLocal() as session:
        seed_roles(session)
        seed_species(session)
        session.flush()
        seed_ethnobotany(session)
        curator_ready = seed_curator(session, settings)
        session.commit()

    if not curator_ready:
        print(
            "CURATOR_EMAIL dan CURATOR_PASSWORD belum diisi, akun kurator awal dilewati"
        )
    print("Seeding selesai")


if __name__ == "__main__":
    run()
