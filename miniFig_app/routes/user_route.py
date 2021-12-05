from flask import render_template, flash, redirect, url_for, request
from miniFig_app import app, db
from miniFig_app.form import LoginForm, RegistrationForm, UserUpdateForm
from flask_login import current_user, login_user, logout_user, login_required
from flask_bcrypt import Bcrypt
from miniFig_app.models.user import User
from miniFig_app.models.sell_fig import Sell_fig

bcrypt = Bcrypt(app)

@app.route('/user/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.email.data, form.remember_me.data))
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not bcrypt.check_password_hash(user.password, form.password.data):
            flash('Invalid email or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/user/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(bcrypt.generate_password_hash(form.password.data))
        db.session.add(user)  # MySQL insert query
        db.session.commit()
        login_user(user)
        return redirect(url_for('index'))
    return render_template('register.html', title='Register', form=form)

@app.route('/user/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/user/account')
@login_required
def user_profile():
    user_id = current_user.get_id()
    sell_figs = Sell_fig.display_all_by_user_id(user_id)
    return render_template('user_profile.html', sell_figs=sell_figs)

@app.route('/user/account/edit', methods=['GET', 'POST'])
@login_required
def edit_user():
    form = UserUpdateForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        User.update_info(form, current_user.get_id())
        return redirect(url_for('user_profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    return render_template('user_edit.html', title='Edit Information', form=form)
