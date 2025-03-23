from Application import db
from typing import List, Optional
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String, Integer
from .User import User


class Owner(User):
    __tablename__ = "owners"
    id: Mapped[int] = mapped_column(ForeignKey("users.id"), primary_key=True)
    level: Mapped[int] = mapped_column(Integer, default=1)

    __mapper_args__ = {
        "polymorphic_identity": "owner",
    }

    def __repr__(self) -> str:
        return f"Owner(id={self.id!r}, username={self.username!s}, level={self.level!r})"