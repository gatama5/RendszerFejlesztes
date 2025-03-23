from Application import db
#
from typing import List
from typing import Optional
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from sqlalchemy.types import String
from werkzeug.security import generate_password_hash, check_password_hash
class User(db.Model):
 __tablename__ = "users"
 id: Mapped[int] = mapped_column(primary_key=True)
 username: Mapped[str] = mapped_column(String(30))
 email: Mapped[Optional[str]]
 password: Mapped[str] = mapped_column(String(30))
 #posts: Mapped[List["Post"]] = relationship(back_populates="owner")

 def __repr__(self) -> str:
    return f"User(id={self.id!r}, name={self.name!s}, email={self.email!r})"

 def set_password(self, password):
    self.password = generate_password_hash(password)

 def check_password(self, password):
    return check_password_hash(self.password, password)
