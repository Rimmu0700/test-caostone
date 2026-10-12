from datetime import datetime
from decimal import Decimal

from sqlalchemy import BigInteger, DateTime, ForeignKey, Numeric, String, func
from sqlalchemy.orm import Mapped, mapped_column

from src.database.base import Base


class LeafDetection(Base):
    __tablename__ = "leaf_detections"

    detection_id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    session_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey("identification_sessions.session_id", ondelete="CASCADE"),
        unique=True,
    )
    confidence: Mapped[Decimal] = mapped_column(Numeric(5, 4))
    bbox_x: Mapped[Decimal] = mapped_column(Numeric(10, 4))
    bbox_y: Mapped[Decimal] = mapped_column(Numeric(10, 4))
    bbox_width: Mapped[Decimal] = mapped_column(Numeric(10, 4))
    bbox_height: Mapped[Decimal] = mapped_column(Numeric(10, 4))
    detection_status: Mapped[str] = mapped_column(String(30))
    crop_image_url: Mapped[str | None] = mapped_column(String(500))
    detected_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
