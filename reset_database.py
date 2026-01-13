"""
Database Reset Script
This script will drop all existing tables and recreate them with the new schema.
Use this ONLY in development!
"""
from app import app, db

with app.app_context():
    print("WARNING: Dropping all tables...")
    db.drop_all()
    print("SUCCESS: Tables dropped!")
    
    print("Creating new tables with updated schema...")
    db.create_all()
    print("SUCCESS: Database schema updated successfully!")
    print("\nYou can now run the app with: python app.py")
