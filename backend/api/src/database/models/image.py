from datetime import datetime

from sqlalchemy import BigInteger, DateTime, ForeignKey, Index, String, func
from sqlalchemy.orm import Mapped, mapped_column

from src.database.base import Base


class Image(Base):
    __tablename__ = "images"
    __table_args__ = (Index("ix_images_session_id", "session_id"),)

    image_id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    session_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey("identification_sessions.session_id", ondelete="CASCADE"),
    )
    image_type: Mapped[str] = mapped_column(String(30))
    storage_url: Mapped[str] = mapped_column(String(500))
    file_format: Mapped[str] = mapped_column(String(20))
    file_size: Mapped[int | None] = mapped_column(BigInteger)
    uploaded_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
