from Application import app, db
from flask import render_template, request, redirect, url_for, flash, session
from Application.User import User
from Application.Customer import Customer
from werkzeug.security import generate_password_hash, check_password_hash

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
        email = request.form['email']

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
            email=email  # Hozzáadtam az email mezőt
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

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Felhasználó keresése email alapján
        user = Customer.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            # Sikeres bejelentkezés
            session['user_id'] = user.id
            session['username'] = user.username
            flash('Sikeres bejelentkezés!')
            return redirect(url_for('index'))
        else:
            flash('Érvénytelen email vagy jelszó!')
            return redirect(url_for('login'))

    return render_template("login.html", page="login")


@app.route('/logout')
def logout():
    session.clear()
    flash('Sikeresen kijelentkezett!')
    return redirect(url_for('index'))