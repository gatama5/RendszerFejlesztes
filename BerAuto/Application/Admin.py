from Application import db
from typing import Optional
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, String, Boolean
from werkzeug.security import generate_password_hash, check_password_hash
from .User import User


class Admin(User):
    __tablename__ = "admins"
    id: Mapped[int] = mapped_column(ForeignKey("users.id"), primary_key=True)
    is_superadmin: Mapped[bool] = mapped_column(Boolean, default=False)

    __mapper_args__ = {
        "polymorphic_identity": "admin",
    }

    def __repr__(self) -> str:
        return f"Admin(id={self.id!r}, username={self.username!s}, email={self.email!r}, is_superadmin={self.is_superadmin!r})"