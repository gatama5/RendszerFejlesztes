from Application import db
from typing import List, Optional
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String
from .User import User


class Customer(User):
    __tablename__ = "customers"
    id: Mapped[int] = mapped_column(ForeignKey("users.id"), primary_key=True)
    name: Mapped[Optional[str]] = mapped_column(String(100))
    phone: Mapped[Optional[str]] = mapped_column(String(20))
    address: Mapped[Optional[str]] = mapped_column(String(200))
    driver_license: Mapped[Optional[str]] = mapped_column(String(50))


    __mapper_args__ = {
        "polymorphic_identity": "customer",
    }

    def __repr__(self) -> str:
        return f"Customer(id={self.id!r}, username={self.username!s}, name={self.name!s})"