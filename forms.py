from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed  # New Import
from wtforms import StringField, PasswordField, SubmitField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Length, EqualTo, Email, Regexp

class RegisterForm(FlaskForm):
    full_name = StringField('Full Name', validators=[DataRequired()])
    email = StringField('Email', validators=[
        DataRequired(),
        Email(message='Invalid email format'),
        Regexp(r'^[a-zA-Z0-9._%+-]+@student\.usm\.my$', message='Email must be @student.usm.my')
    ])
    matric_no = StringField('Matric Number', validators=[DataRequired(), Length(min=6, max=20)])
    hostel_name = SelectField('Desasiswa', choices=[
        ('Aman Damai', 'Aman Damai'),
        ('Fajar Harapan', 'Fajar Harapan'),
        ('Bakti Permai', 'Bakti Permai'),
        ('Cahaya Gemilang', 'Cahaya Gemilang'),
        ('Indah Kembara', 'Indah Kembara'),
        ('Restu', 'Restu'),
        ('Saujana', 'Saujana'),
        ('Tekun', 'Tekun'),
        ('Jaya Lembaran Utama', 'Jaya Lembaran Utama'),
        ('Murni', 'Murni'),
        ('Nurani', 'Nurani')
    ], validators=[DataRequired()])
    room_number = StringField('Room Number', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
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
    evidence = FileField('Upload Evidence', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    submit = SubmitField('Submit Complaint')