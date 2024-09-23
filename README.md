# eLearning Platform

An **eLearning platform** built using **Django**. This project allows users to browse, enroll in, and complete courses. Instructors can create courses, add modules, and upload resources such as videos and documents.

## Features

- **User Registration & Authentication**: Users can register, log in, and manage their profiles.
- **Course Management**: Instructors can create and manage courses, add modules, and upload course resources (videos, PDFs, etc.).
- **Enrollment System**: Students can browse courses, enroll, and track their progress.
- **Content Organization**: Courses are organized into modules, and each module can have various resources.
- **Search Functionality**: Users can search for courses by keywords or categories.
- **Responsive UI**: A clean and responsive design built with Bootstrap.

## Technologies Used

- **Backend**: Django
- **Frontend**: Bootstrap
- **Database**: SQLite (default) for production
- **Authentication**: Django's built-in authentication system
- **Media Management**: Django's static and media files han

## Setup Instructions

### Prerequisites

- Python 3.x
- Django 3.x or higher
- Virtual environment (optional but recommended)
- Git (for version control)

### Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Wahidu1/eLearning.git
    cd eLearning
    ```

2. **Create a virtual environment** (recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Create a `.env` file** in the root of your project and configure your environment variables (e.g., `SECRET_KEY`, `DEBUG`, database credentials, etc.):
    ```makefile
    SECRET_KEY=your-secret-key
    
    ```

5. **Apply migrations**:
    ```bash
    python manage.py makemigrations
    ```

6. ***Apply migrate** ```bash
    python manage.py migrate
    ```
7.  **Create a superuser** to access the admin interface:```bash
    ```bash
    python manage.py createsuperuser
    ```

8. **Run the development server**:
    ```bash
    python manage.py runserver
    ```

   Visit `http://127.0.0.1:8000` to view the application.


    ```


