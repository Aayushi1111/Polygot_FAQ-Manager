# polygot FAQ Manager

The **polygot FAQ Manager** is a backend application built using Django that allows users to create, manage, and retrieve FAQs (Frequently Asked Questions) with **multi-language translation support**. It integrates a WYSIWYG editor for rich text formatting, a REST API for fetching FAQs in different languages, and a caching mechanism using Redis for improved performance.

---

## Features
- **Multi-language FAQ Management**: Store FAQs with translations in multiple languages (e.g., English, Hindi, Bengali).
- **WYSIWYG Editor**: Use `django-ckeditor` for rich text formatting of FAQ answers.
- **REST API**: Fetch FAQs in different languages via a simple API.
- **Caching**: Improve performance using Redis to cache translations.
- **Admin Panel**: Manage FAQs through a user-friendly Django admin interface.
- **Automated Translations**: Automatically translate FAQs using the `googletrans` library.
- **Docker Support**: Easily deploy the application using Docker.

---

## Technologies Used
- **Backend**: Django, Django REST Framework (DRF)
- **Database**: SQLite (default), but can be configured for PostgreSQL/MySQL
- **Caching**: Redis
- **Translation**: `googletrans` (Google Translate API wrapper)
- **WYSIWYG Editor**: `django-ckeditor`
- **Testing**: `pytest`, `pytest-django`
- **Containerization**: Docker, Docker Compose
- **Version Control**: Git

---

## Installation and Setup

### Prerequisites
1. **Python 3.9+**: Ensure Python is installed on your system.
2. **Redis**: Install and run Redis for caching.
3. **Git**: For version control.

---

