# PRODIGY_BD_05
This is  task 4 project for backend development intern hotel booking platform 




# 📘 Overview

This is a backend REST API built using Python, Django REST Framework, and SQLite3 for a hotel booking platform.
Users can register, log in, list hotel rooms, search for available rooms, and make bookings securely using JWT authentication.

This project is part of the Prodigy Infotech Internship Tasks and demonstrates backend development, authentication, and CRUD operations in Django.




# ✨ Features

👤 User Authentication (JWT) — Secure login & registration system

🏨 Hotel Room Management — Create, update, and delete hotel room listings

🔍 Room Search & Filter — Search rooms based on check-in & check-out dates

📅 Room Booking — Reserve available rooms with booking validation

🧱 Database — Uses SQLite3 (default Django relational database)

⚙️ Error Handling & Validation — Clean and safe API responses

🔐 Permission Control — Only authenticated users can create bookings




# 🧰 Technologies Used
Category	Tools


Language	Python


Framework	Django 


Authentication	JWT 


Database	SQLite3


API Testing	Postman


VS Code




# ⚙️ Installation & Setup
🪶 1. Clone the Repository
git clone https://github.com/<your-username>/prodigy_hotel_backend.git
cd prodigy_hotel_backend

🪶 2. Create & Activate Virtual Environment
python -m venv venv
venv\Scripts\activate       # On Windows
source venv/bin/activate    # On Mac/Linux

🪶 3. Install Dependencies
pip install -r requirements.txt


🪶 4. Run Migrations
python manage.py makemigrations
python manage.py migrate

🪶 5. Start Development Server
python manage.py runserver




# 🔗Server will run at:

http://127.0.0.1:8000/




# 🧩 API Endpoints
Action	Method	Endpoint:


Register User	POST	/api/auth/register/


Login User	POST	/api/auth/login/


List Rooms	GET	/api/rooms/


Create Room	POST	/api/rooms/


Search Available Rooms	GET	/api/rooms/search/?check_in=YYYY-MM-DD&check_out=YYYY-MM-DD


Reserve Room	POST	/api/bookings/reserve/


View Bookings	GET	/api/bookings/


 Example JSON (Register)
{
  "username": "harish",
  "email": "harish@example.com",
  "password": "hari2005"
}





# 🪪 License

This project is licensed under the MIT License.
You are free to use, modify, and distribute this project for learning purposes.




# 🎥 Output :
<img width="1920" height="1080" alt="Screenshot 2025-10-19 110715" src="https://github.com/user-attachments/assets/f13d447a-feb1-4bde-9e76-7881a1feadaa" />

