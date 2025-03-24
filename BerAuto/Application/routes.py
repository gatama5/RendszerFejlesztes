from Application import app, db
from flask import render_template, request, redirect, url_for, flash
from Application.User import User
from Application.Customer import Customer
from werkzeug.security import generate_password_hash

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", page="index")

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Adatok lekérése a form-ból
        username = request.form['username']
        password = request.form['password']
        name = request.form['name']
        phone = request.form['phone']
        address = request.form['address']
        driver_license = request.form['driver_license']

        # Ellenőrzés, hogy létezik-e már a felhasználó
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash('A felhasználónév már foglalt!')
            return redirect(url_for('register'))

        # Jelszó hash-elése
        hashed_password = generate_password_hash(password)

        # Új Customer létrehozása
        new_customer = Customer(
            username=username,
            password=hashed_password,
            name=name,
            phone=phone,
            address=address,
            driver_license=driver_license
        )

        # Adatbázisba mentés
        try:
            db.session.add(new_customer)
            db.session.commit()
            flash('Sikeres regisztráció!')
            return redirect(url_for('index'))
        except Exception as e:
            db.session.rollback()
            flash(f'Hiba a regisztráció során: {str(e)}')
            return redirect(url_for('register'))

    return render_template("register.html", page="register")