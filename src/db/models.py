from datetime import datetime, timezone

from sqlalchemy import DateTime, Integer, Numeric
from sqlalchemy.orm import Mapped, mapped_column

from db.base import Base


class CalcResult(Base):
    __tablename__ = "calc_results"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    total_cost_rub: Mapped[float] = mapped_column(Numeric, nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=lambda: datetime.now(timezone.utc),
        nullable=False,
    )
