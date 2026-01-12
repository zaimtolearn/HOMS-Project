from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed  # New Import
from wtforms import StringField, PasswordField, SubmitField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Length, EqualTo

class RegisterForm(FlaskForm):
    full_name = StringField('Full Name', validators=[DataRequired()])  # New
    email = StringField('Email', validators=[DataRequired()])  # New
    matric_no = StringField('Matric Number', validators=[DataRequired(), Length(min=6, max=20)])
    hostel_name = SelectField('Hostel', choices=[
        ('Aman Damai', 'Aman Damai'),
        ('Lembaran', 'Lembaran'),
        ('Restu', 'Restu'),
        ('Tekun', 'Tekun')
    ], validators=[DataRequired()])  # New
    room_number = StringField('Room Number', validators=[DataRequired()])  # New
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
    # New Image Upload Field (Report Page 7)
    evidence = FileField('Upload Evidence', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    submit = SubmitField('Submit Complaint')