
from WebApp import app, db
from WebApp.models import Product, Order

app.app_context().push()

db.session.add_all([
   Product(id=1, name="Product1", price = 1000),
   Product(id=2, name="Product2", price = 2000),
   Product(id=3, name="Product3", price = 3000),
   Product(id=4, name="Product4", price = 4000),
   Product(id=5, name="Product5", price = 5000),
  ]
)
db.session.commit()
