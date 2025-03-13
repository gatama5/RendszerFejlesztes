from flask import render_template, flash, redirect, jsonify
from WebApp import app, db
from WebApp.forms.orderForm import OrderForm
from WebApp.models import Product, Order
import json

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", name="PythonWebZh", page = "index" )

#Csak az 1) feladat teszteléséhez szükséges
test_products = [
        { "id": 1, "name": "product1", "price" : 1000},
        { "id": 2, "name": "product2", "price" : 2000},
        { "id": 3, "name": "product3", "price" : 3000}
    ]

@app.route('/products')
def listItems():  
    #1) feladat alapján a megoldás:
    #return render_template("products.html", name="PythonWebZh", products=test_products, page = "products" )

    #3) feladat alapján a megoldás:
    products= Product.query.all()
    return render_template("products.html", name="PythonWebZh", products=products, page = "products" )


@app.route('/order', methods=["GET", "POST"])
def order():
    form = OrderForm()
    if form.validate_on_submit():
        result = db.session.query(Product).filter(Product.name == form.name.data)      

        if list(result):
            
            product = list(result)[0]
            db.session.add(Order(product_id=product.id, quantity = form.quantity.data))
            db.session.commit()

            flash('The order of the {} is successful!Payable: HUF {}'.format(
                    form.name.data, int(form.quantity.data) * int(product.price)))

            return redirect('/index')
        else:
            flash("{} not found! Check the list!".format(form.name.data))
            return redirect("/products")

    return render_template('order.html', name='PythonWebZh', form = form, page="order")



@app.route('/getorders/<pid>', methods=["GET"])
def getOrders(pid):
    result = db.session.query(Product).filter(Product.id == int(pid))
    if list(result):
        order_list = list(list(result)[0].orders)
        return [ order.toDict() for order in order_list]
    else:
        return {}