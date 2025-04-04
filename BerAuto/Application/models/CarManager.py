from Application import db
from typing import List, Optional, ClassVar
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer
from sqlalchemy.ext.declarative import declared_attr


class CarManager(db.Model):
    __tablename__ = "car_managers"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    _instance: ClassVar[Optional['CarManager']] = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls.query.first()
            if cls._instance is None:
                cls._instance = cls()
                db.session.add(cls._instance)
                db.session.commit()
        return cls._instance



    def __repr__(self) -> str:
        return f"CarManager(id={self.id!r})"