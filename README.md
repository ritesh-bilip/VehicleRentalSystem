
# 🚗 Vehicle Rental System

A **Django-based web application** for managing vehicle rentals with live route mapping, automatic price calculation, and user-friendly booking workflows. Built to be recruiter-ready, scalable, and production-grade.

---

## ✨ Features
- **User Authentication**: Secure login and registration using Django’s built-in auth system.  
- **Vehicle Management**: Add, update, and track cars/bikes with details like name, number, seating capacity, and owner.  
- **Rental Booking**: Customers can book vehicles with dynamic price calculation.  
- **Live Route Mapping**: Integrated with Google Maps / Leaflet / OpenStreetMap for real-time route visualization.  
- **Admin Dashboard**: Manage vehicles, owners, and bookings with Django Admin.  
- **Scalable Architecture**: Modular design with clean separation of apps, templates, and static files.  

---

## 🛠️ Tech Stack
- **Backend**: Django, Django REST Framework  
- **Database**: PostgreSQL (or SQLite for local dev)  
- **Frontend**: HTML, CSS, Bootstrap (templates adapted)  
- **Maps Integration**: Google Maps API / Leaflet / OpenStreetMap  
- **Version Control**: Git & GitHub  

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/ritesh-bilip/VehicleRentalSystem.git
cd VehicleRentalSystem
```

### 2. Create and activate virtual environment
```bash
python -m venv vrsEnv
vrsEnv\Scripts\activate   # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Apply migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Run the server
```bash
python manage.py runserver
```
Visit `http://127.0.0.1:8000/` in your browser.

---

## 📂 Project Structure
```
VehicleRentalSystem/
│── rental_system/        # Main Django project
│   ├── rentals/          # App for vehicles & rentals
│   ├── templates/        # HTML templates
│   ├── static/           # CSS, JS, images
│── requirements.txt      # Dependencies
│── manage.py             # Django CLI
```

---

## 📸 Screenshots (Optional)
_Add screenshots of your app UI here once ready._

---

## 🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you’d like to change.

---

## 📜 License
This project is licensed under the MIT License — see the `[Looks like the result wasn't safe to show. Let's switch things up and try something else!]` file for details.

---
