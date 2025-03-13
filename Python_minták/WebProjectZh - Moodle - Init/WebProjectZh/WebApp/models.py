
#
from WebApp import db

from typing import List, Optional
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from sqlalchemy.types import String, Integer


class Course(db.Model):
### Write your solution here!
    __tablename__ = "course"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
    code: Mapped[str] = mapped_column(unique=True)
    students: Mapped[List["Student"]] = relationship(back_populates="c_course")
###    


class Student(db.Model):
### Write your solution here!
    __tablename__ = "student"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    neptun: Mapped[str] = mapped_column(unique=True)
    course_id = mapped_column(ForeignKey("course.id"))
    c_course: Mapped[Course] = relationship(back_populates="students")
###    
