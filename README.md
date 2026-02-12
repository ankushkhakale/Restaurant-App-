# 🍽️ Restaurant App

A simple and elegant restaurant management system built with Django. This application allows restaurant owners to manage their menu and customers to view available dishes.

## ✨ Features

-   **Menu Management**: Organize dishes into categories (e.g., Starters, Main Course, Drinks).
-   **Item Details**: Detailed view for each menu item including image, price, and description.
-   **Admin Dashboard**: Fully functional admin interface to manage categories and items.
-   **Responsive Design**: Mobile-friendly layout for optimal viewing on any device.
-   **Database Seeding**: Includes a script to populate the database with sample data.

## 🛠️ Tech Stack

-   **Backend**: Python, Django 5.x
-   **Database**: SQLite (Development)
-   **Frontend**: HTML5, CSS3
-   **Image Handling**: Pillow

## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

-   Python 3.10+
-   pip (Python package manager)

### Installation

1.  **Clone the repository**
    ```bash
    git clone https://github.com/ankushkhakale/Restaurant-App-.git
    cd Restaurant-App-
    ```

2.  **Create and activate a virtual environment**
    ```bash
    python -m venv .venv
    # Windows
    .venv\Scripts\activate
    # macOS/Linux
    source .venv/bin/activate
    ```

3.  **Install dependencies**
    ```bash
    pip install django pillow
    ```

4.  **Apply migrations**
    ```bash
    python manage.py migrate
    ```

5.  **Create a superuser** (for admin access)
    ```bash
    python manage.py createsuperuser
    ```

6.  **Seed the database** (optional)
    ```bash
    python seed_data.py
    ```

7.  **Run the development server**
    ```bash
    python manage.py runserver
    ```

8.  **Visit the app**
    -   Public Site: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
    -   Admin Panel: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

## 📸 Screenshots

*(Add screenshots of your application here)*

## 📄 License

This project is licensed under the MIT License.