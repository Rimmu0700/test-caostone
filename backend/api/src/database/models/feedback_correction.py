from datetime import datetime

from sqlalchemy import BigInteger, DateTime, ForeignKey, Index, Integer, Text, func
from sqlalchemy.orm import Mapped, mapped_column

from src.database.base import Base


class FeedbackCorrection(Base):
    __tablename__ = "feedback_corrections"
    __table_args__ = (
        Index("ix_feedback_corrections_classification_id", "classification_id"),
    )

    feedback_id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    classification_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey("classification_results.classification_id", ondelete="CASCADE"),
    )
    curator_id: Mapped[int] = mapped_column(
        BigInteger, ForeignKey("users.user_id", ondelete="RESTRICT")
    )
    corrected_species_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("species.species_id", ondelete="RESTRICT")
    )
    correction_note: Mapped[str | None] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
