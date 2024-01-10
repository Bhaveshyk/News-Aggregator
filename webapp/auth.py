from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User, Prefrences
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user
from .constants import PASS_REGEX
import re

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                return render_template("login.html", user=current_user, message='Invalid e-mail and password.')
        else:
            return render_template("login.html", user=current_user, message='No such account exists.')
    return render_template("login.html", user=current_user, message=None)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()

        if user:
            return render_template("signup.html", user=current_user, message='User already exists. Try logging in!')
        else:
            pattern = re.compile(PASS_REGEX)
            match = re.search(pattern, password)
            if not match:
                return render_template("signup.html", user=current_user, message='Password must be atleast 6 characters long consisting atleast one lowercase, uppercase, numberic digit and a symbol.')
            else:
                new_user = User(email=email, password=generate_password_hash(password), isadmin=False)
                db.session.add(new_user)
                db.session.commit()
                return redirect(url_for('auth.login'))
    return render_template("signup.html", user=current_user, message=None)

@auth.route('/change_password', methods=['GET', 'POST'])
@login_required
def change_pass():
    cats = Prefrences.query.filter_by(user_id=current_user.id).all()
    if request.method == 'POST':
        password = request.form.get('password')
        new_pass = request.form.get('new_password')

        pattern = re.compile(PASS_REGEX)
        match = re.search(pattern, new_pass)

        if not match:
            return render_template("change_pass.html", user=current_user, message='Password must be atleast 6 characters long consisting atleast one lowercase, uppercase, numberic digit and a symbol.', preferences=cats)
        if check_password_hash(current_user.password, password):
            current_user.password = generate_password_hash(new_pass, method='sha256')
            db.session.commit()
            return redirect(url_for('views.home'))
        else:
            return render_template('change_pass.html', user=current_user, message='Current password is invalid. Please try again!', preferences=cats)
    return render_template('change_pass.html', user=current_user, message=None, preferences=cats)