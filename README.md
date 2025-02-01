# 📌 FAQ Project

Welcome to the **FAQ Project**, a robust and scalable Django-based FAQ management system. This project allows users to create, manage, and retrieve frequently asked questions via a RESTful API. The application is containerized using **Docker** for seamless deployment and scalability.

## 🚀 Features
- **Django Admin Panel** for managing FAQs
- **REST API** for retrieving FAQs in multiple languages
- **Dockerized Deployment** for easy scalability
- **Multi-language Support** with language query parameter
- **Automated Migrations** for database management

## 📂 Project Structure
```
faq_project/
│── app/                   # Main Django application
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│── faq_app/               # FAQ management app
│── manage.py              # Django's command-line utility
│── requirements.txt       # Dependencies
│── Dockerfile             # Docker configuration
│── docker-compose.yml     # Docker Compose for multi-container setup
│── README.md              # Project Documentation
```

## 🛠️ Setup Instructions

### 1️⃣ Prerequisites
Ensure you have the following installed:
- Python (>=3.10)
- Docker & Docker Compose

### 2️⃣ Clone the Repository
```sh
git clone https://github.com/yourusername/faq_project.git
cd faq_project
```

### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 4️⃣ Database Migrations
```sh
python manage.py migrate
```

### 5️⃣ Run the Django Server
```sh
python manage.py runserver
```

Your API is now accessible at `http://127.0.0.1:8000/` 🎉

## 🐳 Running with Docker
### Build & Run the Docker Container
```sh
docker build -t faq_project .
docker run -p 8000:8000 faq_project
```
OR, if using **docker-compose**:
```sh
docker-compose up --build
```
Now visit `http://127.0.0.1:8000/` in your browser.

## 🔗 API Endpoints
| Method | Endpoint | Description |
|--------|---------|-------------|
| GET | `/api/faqs/` | Retrieve all FAQs |
| GET | `/api/faqs/?lang=hi` | Retrieve FAQs in Hindi |
| POST | `/api/faqs/` | Create a new FAQ (Admin only) |





## 📜 License
This project is licensed under the **MIT License**.

## ✨ Contributing
1. Fork the repo
2. Create a feature branch (`git checkout -b feature-branch`)
3. Commit changes (`git commit -m 'Add new feature'`)
4. Push to branch (`git push origin feature-branch`)
5. Open a Pull Request

---
🚀 **FAQ Project** – Making information accessible, one FAQ at a time!

