[![Python](https://img.shields.io/badge/Python-3.8+-blue)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0-green)](https://flask.palletsprojects.com/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple)](https://getbootstrap.com/)
[![License](https://img.shields.io/badge/License-MIT-brightgreen)](LICENSE)
[![SQLite](https://img.shields.io/badge/Database-SQLite-grey)](https://sqlite.org/)

# Student Management System (SMS) - Complete Flask Web Application

**Production-ready Flask web application with full CRUD operations for managing students and lecturers.** 
*Converted from original Tkinter desktop app for SSX361 project into modern responsive web app.*

## 🎯 Project Overview

Complete educational management system featuring:
- **Full CRUD operations** (Create, Read, Update, Delete)
- **SQLite database** with schema matching original desktop app
- **Bootstrap 5 responsive UI** with glassmorphism design
- **Interactive navbar** with hover effects
- **Production deployment** ready for PythonAnywhere/GitHub Pages

<img src="static/images/BCLOGO.png" alt="SMS Logo" width="300"/>

## 🚀 Quick Start (Local Development)

```bash
# Clone & setup
git clone <your-repo>
cd Student_Management_System

# Install dependencies
pip install -r requirements.txt

# Run development server
python app.py
```
**Open**: http://localhost:5000

## ☁️ Production Deployment - PythonAnywhere

### Step-by-Step:

1. **Upload Files**
   ```
   /home/yourusername/mysite/
   └── all project files (app.py, templates/, static/, CRUD/, etc.)
   ```

2. **Virtual Environment**
   ```
   pip install --user flask pillow
   ```

3. **WSGI Configuration** (`/var/www/yourusername_pythonanywhere_com_wsgi.py`):
   ```python
   import sys
   path = '/home/yourusername/mysite'
   if path not in sys.path:
       sys.path.insert(0, path)
   from app import app as application
   ```

4. **Web Tab → Reload yourusername.pythonanywhere.com**

## 📁 Complete Project Structure

```
Student_Management_System/
├── app.py                      # Main Flask app + all routes
├── requirements.txt            # Production dependencies
├── .gitignore                  # Git exclusions (SMS.db, venv, etc.)
├── LICENSE                     # MIT License
├── README.md                   # 📄 This documentation
├── static/
│   ├── css/style.css          # Glassmorphism theme + navbar animations
│   └── images/BCLOGO.png      # Application logo
├── templates/                  # Jinja2 HTML templates (Bootstrap 5)
│   ├── base.html              # Master layout + responsive navbar
│   ├── index.html             # Dashboard/Home page
│   ├── students.html          # Students list + forms
│   └── lecturers.html         # Lecturers list + forms
└── CRUD/                      # Database business logic modules
    ├── __init__.py
    ├── Create.py              # Database initialization + sample data
    ├── Read.py                # Fetch students/lecturers
    ├── Delete.py              # Delete operations
    └── Update.py              # Update operations (extendable)
```

## 🗄️ Database Schema - SMS.db (Auto-Created)

**tblStudents**
```
id INTEGER PRIMARY KEY AUTOINCREMENT
fname TEXT NOT NULL
lname TEXT NOT NULL
snumber TEXT UNIQUE NOT NULL
```

**tblLecturers** 
```
empid INTEGER PRIMARY KEY AUTOINCREMENT
fname TEXT NOT NULL
lname TEXT NOT NULL
course TEXT NOT NULL
```

**Sample Data** (auto-inserted on `/create_db`):
```
Students: "Hugo du Preez" (600987), "John Doe" (000000)
Lecturers: "Wilma Flintstone" (PRG262), "Fred Flintstone" (PRG161), etc.
```

## 🌐 Complete API Routes

| Route | Method | Description |
|-------|--------|-------------|
| `/` | GET | **Home/Dashboard** |
| `/students` | GET/POST | **List/Add students** |
| `/lecturers` | GET/POST | **List/Add lecturers** |
| `/create_db` | GET | **Reset database** (dangerous!) |
| `/delete_student/<id>` | GET | **Delete student** |
| `/delete_lecturer/<id>` | GET | **Delete lecturer** |
| `/add_student` | POST | **Create new student** |
| `/add_lecturer` | POST | **Create new lecturer** |

## 🎨 Design System - Glassmorphism Theme

**Color Palette** (matching original desktop app):
```
Primary: #1e3a8a → #3b82f6 (navbar gradient)
Glass: rgba(255,255,255,0.1-0.2) + backdrop-filter: blur()
Active: subtle glow + border
Hover: lift + scale animations
```

**Features**:
- Responsive navbar with **dynamic active states**
- Card shadows + hover effects
- Sticky table headers
- Form validation styling
- Mobile-first design

## 📦 Requirements & Installation

```txt
flask==3.0.0
pillow==11.0.0  # Image processing (logo)
```

**Local**:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
pip install -r requirements.txt
flask run
```

## 🔧 Development & Testing

### Database Commands
```bash
# Inspect schema
sqlite3 SMS.db \".schema\"

# View data
sqlite3 SMS.db \"SELECT * FROM tblStudents;\"
sqlite3 SMS.db \"SELECT * FROM tblLecturers;\"

# Reset (dangerous - deletes all)
curl http://localhost:5000/create_db
```

### Flask Debug Mode
```bash
export FLASK_ENV=development
flask run --host=0.0.0.0 --port=5000
```

## 📱 Features Demo

**Navbar** (dynamic):
- Home: always visible
- Students/Lecturers: highlight on their pages
- Smooth hover animations
- Mobile hamburger menu

**CRUD Operations**:
- List with delete buttons
- Forms with validation
- Flash messages
- Database persistence

## 🚨 Troubleshooting

| Problem | Solution |
|---------|----------|
| 404 Static files | Check `static/images/BCLOGO.png` exists |
| 500 Internal error | `flask run` with debug + check console |
| No navbar highlight | CSS cached - hard refresh `Ctrl+F5` |
| PythonAnywhere 500 | Error log + verify WSGI path |
| SMS.db not found | Visit `/create_db` first |
| Forms not submitting | Browser console + network tab |

## 📈 Roadmap & Future Enhancements

### Complete ✅
- [x] Flask migration from Tkinter
- [x] Full CRUD implementation
- [x] Responsive Bootstrap UI
- [x] Production deployment config
- [x] Clean file structure

### Planned 🔄
- [ ] User authentication
- [ ] Update forms (edit existing records)
- [ ] Search + pagination
- [ ] CSV/Excel export
- [ ] Docker deployment
- [ ] Unit tests

## 🤝 Contributing Guidelines

1. Fork repository
2. `git checkout -b feature/your-feature`
3. Commit: `git commit -m "feat: add your feature"`
4. Push: `git push origin feature/your-feature`
5. Open Pull Request

**Code style**: PEP8, meaningful commit messages.

## 📄 License

MIT License - see [LICENSE](LICENSE)

## 👨‍💻 Author & Credits

**Hugo du Preez**  
*SSX361 Student Management System Project*

**Tech Stack**:
- Flask 3.0 (Backend)
- SQLite3 (Database)
- Bootstrap 5 (Frontend)
- Jinja2 (Templates)
- Pillow (Images)

---
⭐ **Star this repo if it helped you!** 🚀

