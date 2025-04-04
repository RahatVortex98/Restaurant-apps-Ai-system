# Restaurant App with AI Recommendation System

This is a Django-based web application for a restaurant with a fully functional frontend and backend. The system supports user authentication, meal ordering, transaction tracking, and integrates AI-driven recommendations. The project uses PostgreSQL as its primary database and includes Bootstrap-styled UI.

## 🌐 Features

- User authentication (Login, Logout)
- Order meals with stock control
- Transaction history page (details view)
- Admin panel management for meals, orders, etc.
- Responsive Bootstrap UI
- Crispy forms for elegant form styling
- AI-powered meal recommendation logic (future scope)

## 🛠 Tech Stack

- Backend: Django 5.1
- Frontend: Bootstrap 5
- Database: PostgreSQL
- Styling: CSS, Bootstrap
- Forms: `django-crispy-forms`, `crispy-bootstrap5`

## 📁 Project Structure

```
RestaurantApp/
├── restaurant/        # Core app (views, models, templates, urls)
├── templates/         # Shared templates (base.html, login, details)
├── static/            # Static assets (CSS, JS, images)
├── media/             # Uploaded media
├── manage.py          # Django project manager
└── requirements.txt   # Python dependencies
```

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/RestaurantApp.git
cd RestaurantApp
```

### 2. Create and activate virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Install additional dependencies manually if needed
```bash
pip install django-crispy-forms crispy-bootstrap5
```

### 5. Configure crispy forms in `settings.py`
```python
INSTALLED_APPS = [
    ...
    'crispy_forms',
    'crispy_bootstrap5',
]

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"
```

### 6. Apply migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Create superuser
```bash
python manage.py createsuperuser
```

### 8. Run the server
```bash
python manage.py runserver
```

## 🧪 Testing
- Visit `http://127.0.0.1:8000/`
- Login/Register as a user
- Browse and order meals
- View transaction details at `/details/`
- Manage data via `/admin/`

## 📷 Screenshots
![db](https://github.com/user-attachments/assets/d1ca20eb-7c4a-4e7c-b4a1-51e035c2a0ba)
![email gone](https://github.com/user-attachments/assets/01bb5419-0b4e-41d8-9f1e-0836abfca23b)


## 📦 Deployment (Heroku Example)
- Set up `Procfile`, `requirements.txt`, and `runtime.txt`
- Add PostgreSQL addon
- Set env variables for DB and Django secret key
- Run migrations and collect static

## ✅ To-Do / Future Improvements
- AI system to suggest meals based on user behavior
- Real-time stock updates with AJAX
- Email notifications for orders
- REST API with Django REST Framework

## 🙌 Acknowledgments
- Bootstrap for UI
- Django documentation
- Mosh Hamedani's Ultimate Django Course

## 📝 License
This project is licensed under the MIT License.

---

> ✨ Built with Django, styled with Bootstrap, and ready to scale. Enjoy coding!

