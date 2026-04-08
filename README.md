[![Python](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green.svg)](https://docs.python.org/3/library/tkinter.html)

<div align="center">
  <img src="images/BCLOGO.png" alt="Student Management System Logo" width="380"/>
  <h1>Student Management System (SMS)</h1>
  <p><strong>A cross-platform Tkinter GUI application for managing student and lecturer records using SQLite.</strong></p>
  <p>Built for SSX361 Student Management System Project by <strong>Hugo du Preez</strong></p>
</div>

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Quick Start](#quick-start)
- [Project Structure](#project-structure)
- [Database Schema](#database-schema)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Styling](#styling)
- [Development](#development)
- [Troubleshooting](#troubleshooting)
- [License](#license)
- [Authors](#authors)

## Overview

The Student Management System (SMS) is a fully-featured, zero-dependency Python application using Tkinter for GUI and SQLite3 for persistence. It provides complete CRUD functionality for managing students and lecturers in an educational context.

Key highlights:
- Modular architecture with separate CRUD and Windows modules
- Custom dark blue theme
- Auto-generates DB with sample data
- Cross-platform (Windows/Linux/macOS with Python)

## Features

- **Student Management**
  - Add new students with name and student number
  - View all students
  - Update student information
  - Delete student records

- **Lecturer Management**
  - Add new lecturers
  - View all lecturers
  - Update lecturer information
  - Delete lecturer records

- **Database Operations**
  - Create and initialize database tables
  - SQLite-based persistent storage
  - Data validation

## Project Structure

```
Student_Management_System/
├── design.py                        # UI colors, fonts, titles
├── BCLOGO.png                       # Main logo
├── main.py                          # Entry point & main GUI
├── README.md                        # Documentation
├── SMS.db                           # SQLite DB (gitignored in prod)
├── Spacing.png                      # UI spacer
├── Spacing1.png                     # UI spacer
├── TODO.md                          # Implementation tracker
├── CRUD/                            # DB CRUD modules
│   ├── __init__.py
│   ├── Create.py
│   ├── Delete.py
│   ├── Read.py
│   └── Update.py
├── images/                          # Legacy assets
└── Windows/                         # Tkinter GUI windows
    ├── __init__.py
    ├── DisplayAllLecturers.py
    ├── DisplayAllStudents.py
    ├── InsertLecturer.py
    ├── InsertLecturer2.py
    ├── InsertStudent.py
    ├── InsertStudent2.py
    ├── UpdateLecturerWindow.py
    └── UpdateStudentWindow.py
```


## Quick Start 💨

### Prerequisites
- Python 3.7+

### Run in 1 command
```bash
python main.py
```

**Zero installation needed** - Uses only standard library (tkinter, sqlite3)!

## Requirements
- Python 3.7+
- No pip installs required

## Installation

1. Clone or download the project files
2. Ensure you have Python 3.x installed
3. No additional packages required (all dependencies are in the Python standard library)

## Usage

### Running the Application

```bash
python main.py
```

This will launch the Student Management System GUI window.

### Main Window

The main window (400x680) displays:
- BCLOGO.png logo
- Navigation buttons for all CRUD operations:
  - **Create Database**: Initialize/reset the database with default data
  - **New Lecturer**: Add a new lecturer
  - **New Student**: Add a new student
  - **Read All Lecturers**: Display all lecturers in a list
  - **Read All Students**: Display all students in a list
  - **Update Student**: Modify existing student records
  - **Update Lecturer**: Modify existing lecturer records
  - **Delete Student**: Remove a student (via listbox selection)
  - **Delete Lecturer**: Remove a lecturer (via listbox selection)
  - **Exit**: Close the application

## Database Schema 🗄️

**SMS.db** (auto-created, .gitignore recommended)

### Tables

| Table | Fields | PK | Sample Data |
|-------|--------|----|-------------|
| `tblStudents` | `id` (INT), `fname` (TEXT), `lname` (TEXT), `snumber` (TEXT) | `id` | Hugo du Preez (600987), John Doe (000000) |
| `tblLecturers` | `empid` (TEXT), `fname` (TEXT), `lname` (TEXT), `course` (TEXT) | `empid` | Wilma Flintstone (PRG262), Barney Rubbles (STA161), Fred Flintstone (PRG161), Betty Rubble (SSX361) |

### ERD (ASCII)
```
+---------------+       +-----------------+
| tblStudents   |       | tblLecturers    |
|---------------|       |-----------------|
| id (PK)       |       | empid (PK)      |
| fname         |       | fname           |
| lname         |       | lname           |
| snumber       |       | course          |
+---------------+       +-----------------+
```

**Note**: "Create Database" button drops/recreates tables with defaults.

## Screenshots 📸

**Main Window**
![Main GUI](images/BCLOGO.png)

**Display Students** (example output)
```
=======================================
Students in database:

ID|First Name|Last Name|Student Number
=======================================
1 | Hugo | du Preez | 600987
2 | John | Doe | 000000
=======================================
```

## Features Detail

### Create ➕
- Initialize/reset DB with defaults
- Clears tables to avoid duplicates

### Read 👁️
- Formatted listbox/Text displays
- Separate windows for students/lecturers

### Update ✏️
- Edit all fields by ID
- Direct SQL updates

### Delete 🗑️
- Listbox selection + confirmation

## Styling

The application uses a custom color scheme defined in `design.py`:
- Primary color: `#002855` (Dark Blue)
- Secondary color: `#335C81` (Medium Blue)
- Text color: White
- Button hover color: `#005780` (Lighter Blue)

## License 📄

MIT License - see [LICENSE](LICENSE) 

## Authors 👥

**Hugo du Preez**
- SSX361 Student Management System Project 

## Acknowledgments 🙏

- Python, Tkinter, SQLite3 standard library
- Original project structure

## Development 🛠️

### Running in Dev
```bash
# Run app
python main.py

# View DB
sqlite3 SMS.db ".schema"
sqlite3 SMS.db "SELECT * FROM tblStudents;"
```

### Customization
- Edit `design.py` for colors/fonts
- Modify CRUD/*.py for business logic
- Add windows in Windows/

### Contributing
1. Fork & clone
2. Create feature branch
3. Commit changes
4. Test thoroughly
5. PR to main

## Troubleshooting 🔧

| Issue | Solution |
|-------|----------|
| No tkinter | `sudo apt install python3-tk` (Linux) or reinstall Python |
| DB not created | Run "Create Database" button |
| Image not loading | Check PNG paths relative to main.py |
| Windows buttons not working | Verify imports in main.py |

## Styling 🎨

Custom scheme in `design.py`:
- Primary: `#002855` (Dark Blue)
- Secondary: `#335C81`
- Hover: `#005780`
- Text: White
