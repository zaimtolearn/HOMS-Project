from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Length, EqualTo

class RegisterForm(FlaskForm):
    matric_no = StringField('Matric Number', validators=[DataRequired(), Length(min=6, max=20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    role = SelectField('Role', choices=[('student', 'Student'), ('admin', 'Admin')], default='student')
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    matric_no = StringField('Matric Number', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class ComplaintForm(FlaskForm):
    category = SelectField('Category', choices=[
        ('Electrical', 'Electrical (Lights/Fan)'),
        ('Plumbing', 'Plumbing (Water/Toilet)'),
        ('Furniture', 'Furniture (Bed/Table)'),
        ('Internet', 'Internet/Wi-Fi'),
        ('Other', 'Other')
    ], validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired(), Length(min=10)])
    submit = SubmitField('Submit Complaint')