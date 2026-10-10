from datetime import datetime

from sqlalchemy import BigInteger, Boolean, DateTime, ForeignKey, Index, String, func
from sqlalchemy.orm import Mapped, mapped_column

from src.database.base import Base


class IdentificationSession(Base):
    __tablename__ = "identification_sessions"
    __table_args__ = (
        Index("ix_identification_sessions_user_id_created_at", "user_id", "created_at"),
        Index("ix_identification_sessions_session_status", "session_status"),
    )

    session_id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    user_id: Mapped[int] = mapped_column(
        BigInteger, ForeignKey("users.user_id", ondelete="CASCADE")
    )
    captured_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    session_status: Mapped[str] = mapped_column(
        String(30), server_default="pending", default="pending"
    )
    detection_status: Mapped[str] = mapped_column(
        String(30), server_default="pending", default="pending"
    )
    photo_consent: Mapped[bool] = mapped_column(
        Boolean, server_default="false", default=False
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
