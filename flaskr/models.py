from flaskr import db, login_manager
from flaskr import bcrypt
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
    
    def get_id(self):
    	return (self.user_id)

class User(db.Model, UserMixin):
	id = db.Column(db.Integer(), primary_key=True)
	username = db.Column(db.String(length=15), nullable=False, unique=True)
	password = db.Column(db.String(length=30), nullable=False)
	item = db.relationship('Items', backref='owned_user', lazy=True)
	
	
	def __repr__(self):
		return f"User {self.username}"
		
		
	@property
	def password_hash(self):
		raise AttributeError('password not readable')
	
	@password_hash.setter
	def password_hash(self, plain_password_text):
		self.password = bcrypt.generate_password_hash(plain_password_text).decode("utf-8")
		
	def check_password_correction(self, attempted_password):
		return bcrypt.check_password_hash(self.password, attempted_password) # returns True
		

class Items(db.Model):
	id = db.Column(db.Integer(), primary_key = True)
	name = db.Column(db.String(length=30), nullable=False, unique=True)	
	barcode = db.Column(db.String(length=12), nullable=False, unique=True)
	price = db.Column(db.Integer(), nullable=False)
	owner = db.Column(db.Integer(), db.ForeignKey('user.id'))
	
	def __repr__(self):
		return f"Item {self.name}"
