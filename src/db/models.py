from sqlalchemy import TIMESTAMP, Column, Integer, Numeric, func

from db.base import Base


class CalcResult(Base):
    __tablename__ = "calc_results"

    id = Column(Integer, primary_key=True)
    total_cost_rub = Column(Numeric, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)
