# 🧩 RelationProject

RelationProject is a Django web application demonstrating **One-to-One**, **One-to-Many**, and **Many-to-Many** relationships using models like Doctor, Patient, Course, Student, Employee, and ID Card. It provides web forms and a RESTful API to create, relate, and view these objects.

---

## 🚀 Features

- Create and relate Doctors and Patients (One-to-Many)
- Create and relate Students and Courses (Many-to-Many)
- Create Employees and assign unique ID Cards (One-to-One)
- Simple Bootstrap-based UI for all forms
- **REST API endpoints** for all models and their relationships

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
    - `serializers.py`  
      DRF serializers for all models.
    - `tests.py`
    - `urls.py`
    - `views.py`  
      View functions for forms and API endpoints.
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
    venv\Scripts\activate  # On Windows
    # source venv/bin/activate  # On macOS/Linux
    ```

3. **Install dependencies:**
    ```sh
    pip install django djangorestframework
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

### Web Interface

- **Home Page:** `/`  
  Links to all creation forms.
- **Create Doctor:** `/create-doctor/`
- **Create Patient:** `/create-patient/` (assign to a doctor)
- **Create Course:** `/create-course/`
- **Create Student:** `/create-student/` (assign courses)
- **Create Employee:** `/create-employee/`
- **Create ID Card:** `/create-idcard/` (assign to employee)
- **View Doctors & Patients:** `/view-doctors-patients/`
- **View Courses & Students:** `/view-courses-students/`
- **View Employees & ID Cards:** `/view-employees-idcards/`

---

### 🛠️ API Endpoints

All API endpoints accept and return JSON. Use tools like [Postman](https://www.postman.com/) or `curl` to interact.

#### CRUD Endpoints

- **Doctors:**  
  - `GET /api_doctors/` — List all doctors  
  - `POST /api_doctors/` — Create a doctor

- **Patients:**  
  - `GET /api_patients/` — List all patients  
  - `POST /api_patients/` — Create a patient

- **Courses:**  
  - `GET /api_courses/` — List all courses  
  - `POST /api_courses/` — Create a course

- **Students:**  
  - `GET /api_students/` — List all students  
  - `POST /api_students/` — Create a student (with courses)

- **Employees:**  
  - `GET /api_employees/` — List all employees  
  - `POST /api_employees/` — Create an employee

- **ID Cards:**  
  - `GET /api_idcards/` — List all ID cards  
  - `POST /api_idcards/` — Create an ID card

#### Relationship Endpoints

- **Doctors with Patients:**  
  - `GET /api_doctors-patients/`  
    Returns each doctor with their patients.

- **Courses with Students:**  
  - `GET /api_courses-students/`  
    Returns each course with its students.

- **Employees with ID Cards:**  
  - `GET /api_employees-idcards/`  
    Returns each employee with their ID card.

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
- djangorestframework
- Bootstrap (via CDN in templates)

---

## 📜 License

This project is for educational and personal use.