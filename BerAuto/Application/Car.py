from Application import db
from typing import List, Optional
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String, Integer, Boolean


class Car(db.Model):
    __tablename__ = "cars"
    id: Mapped[int] = mapped_column(primary_key=True)
    licensePlate: Mapped[str] = mapped_column(String(20), unique=True)
    brand: Mapped[str] = mapped_column(String(50))
    model: Mapped[str] = mapped_column(String(50))
    year: Mapped[int] = mapped_column(Integer)
    fuelType: Mapped[str] = mapped_column(String(30))
    km: Mapped[int] = mapped_column(Integer)
    state: Mapped[str] = mapped_column(String(50))
    available: Mapped[bool] = mapped_column(Boolean, default=True)


    def __repr__(self) -> str:
        return f"Car(id={self.id!r}, brand={self.brand!s}, model={self.model!s}, licensePlate={self.licensePlate!s})"