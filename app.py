import os
from flask import Flask, render_template
from flask_wtf.csrf import CSRFProtect
from dotenv import load_dotenv
from models import db

# Load variables from .env
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')

# Initialize Database and CSRF Protection
db.init_app(app)
csrf = CSRFProtect(app)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    with app.app_context():
        db.create_all() # This creates the tables in Neon automatically
    app.run(debug=True)