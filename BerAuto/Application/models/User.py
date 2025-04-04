from Application import db, login_manager
from typing import List, Optional
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from sqlalchemy.types import String
from werkzeug.security import generate_password_hash, check_password_hash
from flask import render_template, request, flash, redirect, url_for
from flask_login import UserMixin, login_required, current_user, login_user, logout_user

class User(UserMixin, db.Model):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(30))
    name: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    email: Mapped[Optional[str]]
    phone = db.Column(db.String(20), nullable=True)
    address = db.Column(db.String(255), nullable=True)
    password: Mapped[str] = mapped_column(String(255))

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!s}, email={self.email!r})"

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def profile():
    if not current_user.is_authenticated:
        flash('Jelentkezzen be a profil megtekintéséhez.', 'danger')
        return redirect(url_for('login'))

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