# 🧾 Customer Relationship Management (CRM) System

A simple and comprehensive **CRM web application** built using Django. This system allows an admin to securely manage customer (or employee) records, including creating, viewing, and deleting entries.
---
## ✨ Features

- 🔐 Admin Registration and Login
- 🏠 Dashboard view after login
- ➕ Add new customer/employee record
- 📋 View record list
- 🚪 Secure Logout functionality
- 📅 Auto-generated "Created At" field and auto-incrementing IDs

---

## 📸 Screenshots

*(Add your own screenshots here if you'd like)*

---

## ⚙️ Tech Stack

- Python 3
- Django Web Framework
- SQLite3 (default database)
- HTML/CSS (Bootstrap optional)

---

## 📁 Project Structure
dcrm/
├── crm/                  # Django project
│   ├── settings.py
│   └── ...
├── members/              # Your custom app (e.g., for CRM logic)
│   ├── models.py         # Record model
│   ├── views.py          # Login, Dashboard, Add Record
│   ├── forms.py          # Record creation form
│   ├── urls.py
│   └── templates/
│       └── members/
│           ├── dashboard.html
│           ├── login.html
│           ├── add_record.html
├── db.sqlite3
└── manage.py


---

## 🚀 How to Run This Project Locally

##1. Clone the Repository
                      git clone https://github.com/your-username/django-crm.git
                        cd django-crm
##2. Create and Activate Virtual Environment

                            # Windows
                            python -m venv .venv
                            .venv\Scripts\activate
                            
                            # macOS/Linux
                            python3 -m venv .venv
                            source .venv/bin/activate

##3. Install Dependencies
(If you don't have requirements.txt, just install Django manually:)
                pip install -r requirements.txt
                pip install django

##4. Run Migrations
              python manage.py migrate
              
##5. Create a Superuser (Admin)
             python manage.py createsuperuser
             
##6. Start the Development Server
             python manage.py runserver
             
Visit: http://127.0.0.1:8000

👤 Admin Dashboard Workflow
Register/Login as admin

View dashboard

Use "Add Record" to insert new customer details:

Name |Email| Phone| Address| City| State| Zipcode

"Created At" and "ID" are auto-generated

Logout securely
###Future Enhancements
-> Record update & delete functionality
-> Pagination & search
-> Export to CSV
-> REST API support

 #####Contributing🤝 
        Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.



