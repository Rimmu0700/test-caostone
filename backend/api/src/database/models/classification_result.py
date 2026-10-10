from datetime import datetime
from decimal import Decimal

from sqlalchemy import (
    BigInteger,
    DateTime,
    ForeignKey,
    Index,
    Integer,
    Numeric,
    String,
    func,
)
from sqlalchemy.orm import Mapped, mapped_column

from src.database.base import Base


class ClassificationResult(Base):
    __tablename__ = "classification_results"
    __table_args__ = (Index("ix_classification_results_species_id", "species_id"),)

    classification_id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    session_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey("identification_sessions.session_id", ondelete="CASCADE"),
        unique=True,
    )
    species_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("species.species_id", ondelete="RESTRICT")
    )
    confidence_score: Mapped[Decimal] = mapped_column(Numeric(5, 4))
    result_status: Mapped[str] = mapped_column(String(30))
    model_name: Mapped[str] = mapped_column(String(100))
    model_version: Mapped[str] = mapped_column(String(50))
    classified_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
