from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, DataRequired, EqualTo, ValidationError
from flaskr.models import User

class RegisterForm(FlaskForm):

	def validate_username(self, username_check):
		new_user = User.query.filter_by(username=username_check.data).first()
		if new_user:
			raise ValidationError('Username already taken. Please use a different username.')
	
	
	username = StringField(label='Username', validators=[Length(min=4, max=15), DataRequired()])
	password1 = PasswordField(label='Password', validators=[Length(min=6), DataRequired()])
	password2 = PasswordField(label='Confirm Password', validators=[EqualTo('password1', message='Password must match')])
	submit = SubmitField(label='Create Account')
	
class LoginForm(FlaskForm):
	
	username = StringField(label='Username', validators=[DataRequired()])
	password = PasswordField(label='Password', validators=[DataRequired()])
	submit = SubmitField(label='Sign In')
	
class PurchaseForm(FlaskForm):
	submit = SubmitField(label='Purchase Item')
