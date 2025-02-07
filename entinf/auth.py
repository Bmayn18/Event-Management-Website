from flask import Blueprint, render_template, redirect, url_for, request, flash
from . forms import RegisterForm, LoginForm
from flask_login import login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User, Address
from . import db

bp = Blueprint('auth', __name__ )

@bp.route('/register', methods = ['GET', 'POST'])
def register():
    register = RegisterForm()
    if (register.validate_on_submit() == True):
        uname = register.username.data,
        fname = register.firstname.data,
        lname = register.lastname.data,
        pwd = register.password.data,
        email = register.emailid.data,
        phone = register.phone.data,
        state = register.state.data,
        street = register.address.data,
        suburb = register.suburb.data,
        postcode = register.postcode.data
        CheckUserName = User.query.filter_by(username = uname[0]).first()
        if CheckUserName is None:
            pwd_hash = generate_password_hash(pwd[0])
            new_address = Address(state = state[0], street = street[0], suburb = suburb[0], postcode = postcode, type = 'user')
            db.session.add(new_address)
            address = Address.query.filter_by(street = street[0], suburb = suburb[0], state = state[0], postcode = postcode).first()
            new_user = User(username = uname[0], firstname = fname[0], lastname = lname[0], email = email[0], phone = phone[0], password_hash = pwd_hash, address_id = address.id)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('auth.login'))
        else:
            flash('Username already exists, choose another')
            return redirect(url_for('auth.register'))
    else:
        return render_template('register.html', form = register, heading = 'Register')

@bp.route('/login/', methods = ['GET', 'POST'])
def login():
    login_form = LoginForm()
    error = None
    if(login_form.validate_on_submit() == True):
        user_name = login_form.user_name.data
        password = login_form.password.data
        u1 = User.query.filter_by(username = user_name).first()
        if u1 is None:
            error = 'Incorrect user name'
        elif not check_password_hash(u1.password_hash, password):
            error = 'Incorrect password'
        if error is None:
            login_user(u1)
            return redirect(url_for('main.index'))
        else:
            flash(error)
    return render_template('login.html', form = login_form, heading = 'Login')

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    #return 'You have successfully logged out'
    return redirect(url_for('main.index'))