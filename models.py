from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    # Added based on Report Figure 5.1.2
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    matric_no = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    
    # Location details for Complaints (Report Fig 5.2)
    hostel_name = db.Column(db.String(50))  # e.g., "Aman Damai"
    room_number = db.Column(db.String(10))  # e.g., "401"
    
    role = db.Column(db.String(10), default='student')  # student or admin

class Complaint(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)
    # Added Image Path (Report Fig 4.4.1)
    image_file = db.Column(db.String(100), nullable=True, default='default.jpg')
    status = db.Column(db.String(20), default='Pending')
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    # Relationship to access Student Name & Hostel directly
    user = db.relationship('User', backref='complaints')