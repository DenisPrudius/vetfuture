# 🐾 Veterinary Clinic Personal Account

## 📌 Description
A web application for a veterinary clinic that allows clients to manage their personal accounts, add information about their pets.  
Administrators and doctors can view patient data and keep track of medical history and procedures.  

---

## ⚙️ Technologies
- **Python 3.10+**
- **Django 5.x**
- **Django REST Framework**
- **PostgreSQL**
- **Bootstrap 4**
- **Git/GitHub**

---

## 🚀 Features
- 👤 User registration and authentication  
- 🐶 Pet management (name, age, species, etc.)
- 📋 Medical history and procedure records  
- 🔑 Role system (client, doctor, admin)

---

## 🔧 Installation & Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo

    Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

Install dependencies:

pip install -r requirements.txt

Configure environment variables in a .env file (see .env.example):

SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
DATABASE_URL=postgres://user:password@localhost:5432/dbname

Run migrations and start the server:

    python manage.py migrate
    python manage.py runserver

📂 Project Structure

├── users/  
├── pet_health_info/  
├── pets/  
├── vetfuture/  
├── templates/       
├── static/   
├── requirements.txt  
├── manage.py  
└── README.md

📌 Roadmap

    📱 Mobile client / API integration

    📊 Analytics for doctors

    🔔 Email & push notifications for appointments
    
    🏥 Appointment booking with doctors


