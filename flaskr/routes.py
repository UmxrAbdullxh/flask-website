from flaskr import app
from flask import render_template, request, redirect, url_for, flash
from flaskr.models import Items, User
from flaskr.forms import RegisterForm, LoginForm, PurchaseForm
from flaskr import db
from flask_login import login_user, logout_user, login_required, current_user

@app.route("/")
@app.route("/home")
def index():
	return render_template('home.html')
	
@app.route("/market", methods=['GET', 'POST'])	
@login_required
def market():
	purchase_form = PurchaseForm()
	if request.method == 'POST':
		purchased_item = request.form.get('purchased_item')
		p_item_object = Items.query.filter_by(name=purchased_item).first()
		if p_item_object:
			p_item_object.owner = current_user.id
			db.session.commit()
			flash('Purchase successful!', category='success')
		return redirect(url_for('market'))
	if request.method == 'GET':
		items = Items.query.filter_by(owner=None)
		return render_template('index.html', items=items, purchase_form=purchase_form)
	
@app.route("/register", methods=['GET', 'POST'])
def register_form():
	form = RegisterForm()
	if form.validate_on_submit():
		user = User(username = form.username.data, password_hash = form.password1.data)
		db.session.add(user)
		db.session.commit()
		flash('Thanks for registering')
		return redirect(url_for('market'))
	if form.errors != {}:
		for err in form.errors.values():
			flash(f"Something was wrong! {err}", 'danger')
	return render_template('register.html', form=form)
	
@app.route("/login", methods=['GET', 'POST'])
def login_form():
	form = LoginForm()
	if form.validate_on_submit():
		attempted_user = User.query.filter_by(username=form.username.data).first()
		if attempted_user and attempted_user.check_password_correction(attempted_password=form.password.data):
			login_user(attempted_user)
			flash('Login successful!', category='success')
			return redirect(url_for('market'))
		else:
			flash('Username or password error', category='danger')
	return render_template('login.html', form=form)	
	
@app.route("/logout")
def logout_page():
	logout_user()
	flash('You have been logged out.', category='info')
	return redirect(url_for('index'))
	
@app.route('/owned_items')
def owned_items():
	owned_items = Items.query.filter_by(owner=current_user.id)
	return render_template('owned_items.html', owned_items=owned_items)
	
	
