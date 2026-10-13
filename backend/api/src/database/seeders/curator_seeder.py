from sqlalchemy import select
from sqlalchemy.orm import Session

from src.core.config import Settings
from src.core.security import hash_password
from src.database.models import Role, User, UserProfile, UserSetting

CURATOR_ROLE_NAME = "curator"
CURATOR_DEFAULT_NAME = "Kurator"


def seed_curator(session: Session, settings: Settings) -> bool:
    if not settings.curator_email or not settings.curator_password:
        return False

    existing = session.scalar(select(User).where(User.email == settings.curator_email))
    if existing is not None:
        return True

    role_id = session.scalar(
        select(Role.role_id).where(Role.role_name == CURATOR_ROLE_NAME)
    )
    if role_id is None:
        raise RuntimeError("Role curator belum ada, jalankan seed_roles lebih dulu")

    user = User(
        role_id=role_id,
        email=settings.curator_email,
        password_hash=hash_password(settings.curator_password),
        email_verified=True,
    )
    user.profile = UserProfile(full_name=CURATOR_DEFAULT_NAME)
    user.settings = UserSetting(notification_enabled=True)
    session.add(user)
    return True
