from flask import current_app, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

from Application import db
from Application.models.Customer import Customer

def register_routes(app):
    @app.route('/')
    @app.route('/index')
    def index():
        return render_template("index.html", page="index")

    @app.route('/register', methods=['GET', 'POST'])
    def register():
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            name = request.form['name']
            email = request.form['email']

            existing_user = Customer.query.filter_by(username=username).first()
            if existing_user:
                flash('A felhasználónév már foglalt!')
                return redirect(url_for('register'))

            hashed_password = generate_password_hash(password)

            new_customer = Customer(
                username=username,
                password=hashed_password,
                name=name,
                email=email
            )

            try:
                db.session.add(new_customer)
                db.session.commit()
                flash('Sikeres regisztráció!')
                return redirect(url_for('login'))
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

            user = Customer.query.filter_by(email=email).first()

            if user and check_password_hash(user.password, password):
                login_user(user)
                flash('Sikeres bejelentkezés!')
                return redirect(url_for('index'))
            else:
                flash('Érvénytelen email vagy jelszó!')
                return redirect(url_for('login'))

        return render_template("login.html", page="login")

    @app.route('/logout')
    @login_required
    def logout():
        logout_user()
        flash('Sikeresen kijelentkezett!')
        return redirect(url_for('index'))

    @app.route('/profile', methods=['GET', 'POST'])
    @login_required
    def profile():
        if request.method == 'POST':
            action = request.form.get('action')

            if action == 'update_profile':
                username = request.form.get('username')
                name = request.form.get('name')
                phone = request.form.get('phone')
                address = request.form.get('address')

                if not username or not name:
                    flash('Felhasználónév és teljes név kitöltése kötelező!', 'danger')
                    return render_template('profile.html')

                current_user.username = username
                current_user.name = name
                current_user.phone = phone
                current_user.address = address

                try:
                    db.session.commit()
                    flash('Profiladatok sikeresen frissítve!', 'success')
                    return redirect(url_for('profile'))
                except Exception as e:
                    db.session.rollback()
                    flash('Hiba történt a mentés során.', 'danger')

            elif action == 'change_password':
                current_password = request.form.get('current_password')
                new_password = request.form.get('new_password')
                confirm_password = request.form.get('confirm_password')

                if not current_user.check_password(current_password):
                    flash('A jelenlegi jelszó nem helyes.', 'danger')
                    return render_template('profile.html')

                if new_password != confirm_password:
                    flash('Az új jelszavak nem egyeznek.', 'danger')
                    return render_template('profile.html')

                if len(new_password) < 8:
                    flash('A jelszó legalább 8 karakter hosszú kell legyen.', 'danger')
                    return render_template('profile.html')

                current_user.set_password(new_password)

                try:
                    db.session.commit()
                    flash('Jelszó sikeresen megváltoztatva!', 'success')
                    return redirect(url_for('profile'))
                except Exception as e:
                    db.session.rollback()
                    flash('Hiba történt a jelszó módosítása során.', 'danger')

        return render_template('profile.html')