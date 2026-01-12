# HOMS - Hostel Operation Management System (USM)

A professional web-based facility management system designed to modernize complaint tracking for USM hostels.

## 🔗 Live Deployment

- **URL:** [Live Website Link](https://your-app-name.onrender.com)
- **Status:** Cloud Hosted on Render with SSL/HTTPS enabled

## 🚀 Tech Stack

- **Backend:** Flask (Python 3.13.3)
- **Database:** PostgreSQL (Cloud-hosted on Neon.tech)
- **Hosting:** Render (Cloud Deployment with SSL/HTTPS)
- **ORM:** SQLAlchemy (for secure database operations)

## 🛡️ Web Security Features

To meet "Excellent" rubric standards, this project implements 3 robust security layers:

1. **Password Hashing:** Uses `Werkzeug` PBKDF2 with 200,000+ iterations.
2. **SQL Injection Protection:** Implemented via SQLAlchemy ORM parameter binding.
3. **CSRF Protection:** Secure form handling using `Flask-WTF` to prevent cross-site attacks.

## 📁 Project Structure (MVC)

```text
HOMS-Project/
├── app.py             # Controller & Main Entry Point
├── models.py          # Database Schema (SQLAlchemy)
├── requirements.txt   # Dependency List
├── .gitignore         # Security: Ignored Files
├── templates/         # Views (HTML using Jinja2)
│   ├── base.html
│   ├── index.html
│   ├── student_db.html
│   └── admin_db.html
└── static/            # CSS, JS, and Images
```

## 🛠️ Local Setup for Team Members

Follow these steps to run the project on your machine:

1. **Clone the Repo:**

   ```bash
   git clone <your-github-link-here>
   cd HOMS-Project

   ```

2. **Setup virtual environment:**

   ```bash
   python -m venv venv

   ```

   # Activate Windows:

   ```bash
   venv\Scripts\activate
   ```

   # Activate Mac/Linux:

   source venv/bin/activate

3. **install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. Environment Variables (.env): Create a .env file in the root folder. Ask the team lead for the DATABASE_URL and SECRET_KEY. Do not upload this file to GitHub.

5. **Run the app**
   ```bash
   python app.py
   ```
