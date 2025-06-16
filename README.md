# 🧩 RelationProject

RelationProject is a simple Django web application demonstrating **One-to-One**, **One-to-Many**, and **Many-to-Many** relationships using basic models like Doctor, Patient, Course, Student, Employee, and ID Card. It provides web forms to create and relate these objects.

---

## 🚀 Features

- Create and relate Doctors and Patients (One-to-Many)
- Create and relate Students and Courses (Many-to-Many)
- Create Employees and assign unique ID Cards (One-to-One)
- Simple Bootstrap-based UI for all forms

---

## 🗂️ Project Structure

A professional overview of the directory layout for **relationProject**:

- **relationProject/**
  - **manage.py**  
    Django’s command-line utility for administrative tasks.
  - **db.sqlite3**  
    SQLite database file (auto-generated after migrations).
  - **relationProject/**  
    Project-level configuration and settings.
    - `__init__.py`
    - `asgi.py`
    - `settings.py`
    - `urls.py`
    - `wsgi.py`
  - **relationApp/**  
    Main Django application containing business logic.
    - `__init__.py`
    - `admin.py`
    - `apps.py`
    - `models.py`  
      Model definitions for Doctor, Patient, Course, Student, Employee, and IDCard.
    - `tests.py`
    - `urls.py`
    - `views.py`  
      View functions for handling HTTP requests.
    - **migrations/**  
      Database migration files (auto-generated).
      - `__init__.py`
    - **templates/**  
      HTML templates for rendering web pages.
      - `home.html`
      - `create_doctor.html`
      - `create_patient.html`
      - `create_course.html`
      - `create_student.html`
      - `create_employee.html`
      - `create_id.html`

---

## ⚙️ Setup Instructions

1. **Clone the repository:**
    ```sh
    git clone <your-repo-url>
    cd relationProject
    ```

2. **Create and activate a virtual environment:**
    ```sh
    python -m venv venv
    # On Windows:
    venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    ```

3. **Install dependencies:**
    ```sh
    pip install django
    ```

4. **Apply migrations:**
    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Run the development server:**
    ```sh
    python manage.py runserver
    ```

6. **Open your browser and visit:**
    ```
    http://127.0.0.1:8000/
    ```

---

## 🖥️ Usage

- **Home Page:** `/`  
  Links to all creation forms.
- **Create Doctor:** `/create-doctor/`
- **Create Patient:** `/create-patient/` (assign to a doctor)
- **Create Course:** `/create-course/`
- **Create Student:** `/create-student/` (assign courses)
- **Create Employee:** `/create-employee/`
- **Create ID Card:** `/create-idcard/` (assign to employee)

---

## 🧑‍💻 Models & Relationships

- **Doctor** ⟶ **Patient**: One-to-Many  
  (A doctor can have many patients, a patient has one doctor)
- **Student** ⟷ **Course**: Many-to-Many  
  (A student can enroll in many courses, a course can have many students)
- **Employee** ⟷ **IDCard**: One-to-One  
  (Each employee has one unique ID card)

---

## 📦 Dependencies

- Django
- Bootstrap (via CDN in templates)

---

## 📜 License

This project is for educational