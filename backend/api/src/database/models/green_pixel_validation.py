from datetime import datetime
from decimal import Decimal

from sqlalchemy import BigInteger, DateTime, ForeignKey, Numeric, String, func
from sqlalchemy.orm import Mapped, mapped_column

from src.database.base import Base


class GreenPixelValidation(Base):
    __tablename__ = "green_pixel_validations"

    validation_id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    session_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey("identification_sessions.session_id", ondelete="CASCADE"),
        unique=True,
    )
    green_pixel_ratio: Mapped[Decimal] = mapped_column(Numeric(5, 4))
    threshold: Mapped[Decimal] = mapped_column(Numeric(5, 4))
    validation_status: Mapped[str] = mapped_column(String(30))
    validated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
