#
from WebApp import db
#
from typing import List
from typing import Optional
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from sqlalchemy.types import String
from werkzeug.security import generate_password_hash, check_password_hash


class Product(db.Model):
    __tablename__ = "product"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(64), unique=True)
    price: Mapped[int] = mapped_column()
    orders: Mapped[List["Order"]] = relationship(back_populates="item")
    
    def __repr__(self):
        return '<Product {}>'.format(self.name)

class Order(db.Model):
    __tablename__ = "order"
    id: Mapped[int] = mapped_column(primary_key=True)
    product_id = mapped_column(ForeignKey("product.id"))
    quantity: Mapped[int]
    item: Mapped[Product] = relationship(back_populates="orders")

    def __repr__(self):
        return '<Order {}x{}>'.format(self.product_id, self.quantity)
