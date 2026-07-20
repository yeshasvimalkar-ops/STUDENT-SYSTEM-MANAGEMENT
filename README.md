# Student Management System

## Project Description
This project is a simple Student Management System developed in Python. It allows users to add, search, update, and remove student records. The project also includes unit testing and GitHub Actions for automated testing.

## Project Structure

```
student-management-system/
│── Students.py
│── test_students.py
│── requirements.txt
│── .github/
│   └── workflows/
│       └── python.yml
```

## Features

- Add Student
- Search Student
- Update Student
- Remove Student

## Setup

Clone the repository:

```bash
git clone <repository-url>
```

Move into the project:

```bash
cd student-management-system
```

Install dependencies:

```bash
pip install pytest
```

Run the tests:

```bash
pytest
```

## Git Commands Used

```bash
git init
git add .
git commit -m "Initial commit"
git checkout -b feature-student-search
git push -u origin feature-student-search
git commit -m "Added GitHub Actions workflow"
git push
```

## GitHub Actions Workflow

The GitHub Actions workflow automatically runs unit tests whenever code is pushed or a Pull Request is created.