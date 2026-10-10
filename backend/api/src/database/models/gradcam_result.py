from datetime import datetime

from sqlalchemy import BigInteger, DateTime, ForeignKey, String, func
from sqlalchemy.orm import Mapped, mapped_column

from src.database.base import Base


class GradcamResult(Base):
    __tablename__ = "gradcam_results"

    gradcam_id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    classification_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey("classification_results.classification_id", ondelete="CASCADE"),
        unique=True,
    )
    heatmap_url: Mapped[str] = mapped_column(String(500))
    generated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
