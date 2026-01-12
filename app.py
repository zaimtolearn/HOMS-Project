import os
from flask import Flask, render_template, redirect, url_for, flash, request, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf.csrf import CSRFProtect
from dotenv import load_dotenv
from datetime import timedelta

# Import our Models and Forms
from models import db, User, Complaint
from forms import LoginForm, RegisterForm, ComplaintForm

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=10) # Rubric: Session Timeout

# Initialize Extensions
db.init_app(app)
csrf = CSRFProtect(app)

# Login Manager Setup (Rubric: Session Management)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))

# --- ROUTES ---

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        # Check if user exists
        if User.query.filter_by(matric_no=form.matric_no.data).first():
            flash('Matric number already exists!', 'danger')
            return redirect(url_for('register'))
        
        # Hash Password (Rubric: Security Measure #1)
        hashed_pw = generate_password_hash(form.password.data, method='pbkdf2:sha256')
        
        new_user = User(matric_no=form.matric_no.data, password=hashed_pw, role=form.role.data)
        db.session.add(new_user)
        db.session.commit()
        
        flash('Account created! Please login.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(matric_no=form.matric_no.data).first()
        
        # Verify Password (Rubric: Security)
        if user and check_password_hash(user.password, form.password.data):
            login_user(user, remember=False) # Ensure this is False for shared computers
            session.permanent = True  # Activates the 10-minute timeout

            # Redirect based on Role (Rubric: User Roles)
            if user.role == 'admin':
                return redirect(url_for('admin_dashboard'))
            return redirect(url_for('student_dashboard'))
        else:
            flash('Login Unsuccessful. Check matric number and password.', 'danger')
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))

# --- STUDENT ROUTES ---
@app.route('/student/dashboard', methods=['GET', 'POST'])
@login_required
def student_dashboard():
    if current_user.role != 'student':
        return redirect(url_for('admin_dashboard'))
    
    form = ComplaintForm()
    if form.validate_on_submit():
        new_complaint = Complaint(
            category=form.category.data,
            description=form.description.data,
            user_id=current_user.id
        )
        db.session.add(new_complaint)
        db.session.commit()
        flash('Complaint submitted successfully!', 'success')
        return redirect(url_for('student_dashboard'))
    
    # Show only own complaints
    my_complaints = Complaint.query.filter_by(user_id=current_user.id).all()
    return render_template('student_dashboard.html', form=form, complaints=my_complaints)

# --- ADMIN ROUTES ---
@app.route('/admin/dashboard')
@login_required
def admin_dashboard():
    if current_user.role != 'admin':
        return redirect(url_for('student_dashboard'))
    
    # Admin sees ALL complaints
    all_complaints = Complaint.query.all()
    return render_template('admin_dashboard.html', complaints=all_complaints)

@app.route('/admin/update/<int:complaint_id>/<string:status>')
@login_required
def update_status(complaint_id, status):
    if current_user.role != 'admin':
        return redirect(url_for('index'))
        
    complaint = Complaint.query.get_or_404(complaint_id)
    complaint.status = status
    db.session.commit()
    flash(f'Complaint updated to {status}', 'success')
    return redirect(url_for('admin_dashboard'))

@app.after_request
def add_security_headers(response):
    # Enforce HTTPS (HSTS)
    response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
    # Prevent Clickjacking
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    # Prevent MIME-type sniffing
    response.headers['X-Content-Type-Options'] = 'nosniff'
    return response

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)