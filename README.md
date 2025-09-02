# BlogApp 📝

A simple blog application built with **Django**.  
This project uses **SQLite3** as the database (default Django DB) and includes features like authentication, creating/editing posts, and more.

---

## 🚀 Features
- User authentication (sign up, login, logout)
- Create, edit, and delete blog posts
- Comment system
- SQLite3 database (default for local development)
- Django admin panel

---

## 🛠️ Setup Instructions

Follow these steps to run the project locally:

### 1. Clone the repository
```bash
git clone https://github.com/MubeenBhatti563/BlogApp.git
cd BlogApp

# On Linux / macOS
python3 -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

python manage.py runserver
