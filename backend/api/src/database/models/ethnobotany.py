from datetime import datetime

from sqlalchemy import BigInteger, DateTime, ForeignKey, Integer, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.base import Base


class Ethnobotany(Base):
    __tablename__ = "ethnobotany"

    ethnobotany_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    species_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("species.species_id", ondelete="CASCADE"), unique=True
    )
    traditional_benefits: Mapped[str | None] = mapped_column(Text)
    plant_parts_used: Mapped[str | None] = mapped_column(Text)
    usage_method: Mapped[str | None] = mapped_column(Text)
    verification_status: Mapped[str] = mapped_column(
        String(30), server_default="pending", default="pending"
    )
    verified_by: Mapped[int | None] = mapped_column(
        BigInteger, ForeignKey("users.user_id", ondelete="SET NULL")
    )
    verified_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )

    species = relationship("Species", back_populates="ethnobotany")
