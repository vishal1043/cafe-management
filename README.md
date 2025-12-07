# Cafe Management REST API (Flask)

A backend-only **REST API built using Flask** to manage cafe items (CRUD operations), JWT authentication, and API testing using Postman.  
This project focuses on **Backend + REST API development** — No frontend required, all requests are tested via **Postman** or Swagger UI.

---

## 🚀 Features

- REST API using **Flask + Flask-Smorest**
- **User Authentication with JWT**
- **Token Blacklisting** for logout
- **Item CRUD API**
- Postman support for API testing
- Swagger UI already included
- Clean & scalable folder structure

---

## 📂 Project Structure

📁 project-folder/
- │── app.py  # Main Application File
- │── blocklist.py # JWT Token Blacklist
- │── schemas.py # Marshmallow Schemas
- │── requirements.txt # Project Dependencies
- │── Dockerfile # (Optional) For deployment
- │── .gitignore
- │── test.py # Optional Testing File
- │
- ├── db/
- │ ├── items.py # Item Database Handler
- │ └── user.py # User Database Handler
- │
- ├── resources/
- │ ├── item.py # Item Route API
- │ └── user.py # User Route API
- │
- ├── templates/ # Optional HTML UI (not needed for pure API)
- ├── static/ # Optional assets for UI
- └── pycache/ # Auto generated


---

## 🛠 Installation & Setup

### 1️⃣ Clone the repository

git clone https://github.com/your-username/cafe-management-api.git
cd cafe-management-api

### 2️⃣ Create & activate virtual environment
python -m venv venv
venv/Scripts/activate     # Windows
# OR
source venv/bin/activate  # Mac/Linux

### 3️⃣ Install dependencies
    pip install -r requirements.txt

### ▶ Run the Server
  python app.py


## 📌 Using Postman for API Testing

Since this is a **pure backend project**, all API requests are handled using **Postman**.

📥 Download Postman:  
https://www.postman.com/downloads/

---

### 🧾 Why Postman?

| Benefit | Description |
|--------|------------|
| Test endpoints without UI | Perfect for backend projects |
| Send JSON body/headers | Easy & fast |
| Preview response neatly | JSON formatted view |
| Token Authentication support | Easily send JWT headers |

---

## 🧪 API Endpoints

---

### 🔐 User Authentication

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/register` | Register new user |
| POST | `/login` | Login user and receive JWT |
| POST | `/logout` | Logout and blacklist token |

#### 📤 Register Example

```json
 POST /register
{
  "username": "vishal",
  "password": "12345"
}
```

### 📤 Login Response

```json
{
  "access_token": "JWT_TOKEN_HERE"
}
```
Save this token and send it in Header:

Authorization: Bearer <token>

## 🛍 Item Management

| Method | Endpoint       | Description       |
|--------|----------------|-------------------|
| GET    | `/item`        | Get all items     |
| POST   | `/item`        | Add new item      |
| GET    | `/item/<id>`   | Get item by ID    |
| PUT    | `/item/<id>`   | Update item       |
| DELETE | `/item/<id>`   | Delete item       |

---

### 📤 Add Item Example

```json
POST /item
{
  "name": "Cold Coffee",
  "price": 120
}
```

## 🗄 Database

Current DB is file-based Python modules inside /db.

You may upgrade later to:
-MySQL
-PostgreSQL
-SQLite
-MongoDB

## 📜 Swagger API Docs

Access API documentation at:

      http://localhost:5000/swagger-ui

### 🔐 Environment Variables

 Create a .env or .flaskenv file and add:

     JWT_SECRET_KEY=your_secret_key_here


### 📈 Future Improvements

-Add role-based permissions (staff/admin)
-Add order & billing module
-Database migration to MySQL
-Create frontend dashboard (React/Next.js)
-Deploy using Docker/Render/AWS

## 👨‍💻 Author

Your Vishal Umath.
Backend Developer | Python & Flask

