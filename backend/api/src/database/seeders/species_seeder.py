from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.orm import Session

from src.database.models import Species

SPECIES = (
    ("Alpinia galanga (L.) Willd.", "Lengkuas"),
    ("Amomum compactum Sol. ex Maton", "Kapulaga"),
    ("Anredera cordifolia (Ten.) Steenis", "Binahong"),
    ("Antidesma bunius (L.) Spreng.", "Buni"),
    ("Blumea balsamifera (L.) DC.", "Sembung"),
    ("Cinnamomum verum J.Presl", "Kayu manis"),
    ("Curcuma sylvatica Valeton", None),
    ("Erythrina hypaphorus Boerl. ex Koord.", "Dadap"),
    ("Euchresta horsfieldii (Lesch.) Benn.", None),
    ("Graptophyllum pictum (L.) Griff.", "Daun ungu"),
    ("Justicia gendarussa Burm.f.", "Gandarusa"),
    ("Piper betle L.", "Sirih"),
    ("Plantago major L.", "Sendok-sendok"),
    ("Symphytum officinale L.", "Comfrey"),
    ("Tabernaemontana sp.", None),
    ("Zingiber officinale Roxb.", "Jahe"),
    ("Zingiber purpureum Roxb.", "Bangle"),
)


def seed_species(session: Session) -> None:
    rows = [
        {
            "scientific_name": scientific_name,
            "local_name": local_name,
            "is_active": True,
        }
        for scientific_name, local_name in SPECIES
    ]
    statement = insert(Species).values(rows)
    session.execute(
        statement.on_conflict_do_nothing(index_elements=["scientific_name"])
    )
