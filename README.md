[![Python](https://img.shields.io/badge/Python-3.8+-blue)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0-green)](https://flask.palletsprojects.com/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple)](https://getbootstrap.com/)
[![License](https://img.shields.io/badge/License-MIT-brightgreen)](LICENSE)
[![SQLite](https://img.shields.io/badge/Database-SQLite-grey)](https://sqlite.org/)

# Student Management System (SMS) - Flask Web App

Production-ready Flask application with full CRUD operations for students and lecturers using SQLite database and Bootstrap responsive UI.

**Originally Tkinter desktop app converted to professional web application for SSX361 project.**

## 🚀 Quick Start

```bash
git clone <repo> && cd Student_Management_System
pip install -r requirements.txt
python app.py
```
Open `http://localhost:5000`

## ☁️ PythonAnywhere Deployment

1. Upload all files to PythonAnywhere
2. Virtualenv: `pip install flask pillow`
3. WSGI config:
```python
import sys
path = '/home/USERNAME/mysite'
if path not in sys.path:
    sys.path.append(path)
from app import app as application
```
4. Reload web app

## 📁 Project Structure

```
Student_Management_System/
├── app.py                 # Flask application and routes
├── requirements.txt       # Dependencies: flask, pillow
├── .gitignore            # Git exclusions
├── LICENSE               # MIT License
├── README.md             # This documentation
├── static/
│   ├── css/style.css     # Custom dark blue glassmorphism theme
│   └── images/           # BCLOGO.png
├── templates/            # Jinja2 + Bootstrap templates
│   ├── base.html         # Master layout with navbar
│   ├── index.html        # Dashboard
│   ├── students.html     # Students management
│   └── lecturers.html    # Lecturers management
└── CRUD/                 # Database operations
    ├── Create.py         # Database creation and sample data
    ├── Read.py           # Fetch students/lecturers
    ├── Delete.py         # Delete operations
    └── Update.py         # Update operations (ready for extension)
```

## 🌐 Routes

| Route | Method | Action |
|-------|--------|--------|
| `/` | GET | Home dashboard |
| `/students` | GET/POST | List and add students |
| `/lecturers` | GET/POST | List and add lecturers |
| `/create_db` | GET | Reset database |
| `/delete_student/<id>` | GET | Delete student |
| `/delete_lecturer/<id>` | GET | Delete lecturer |
| `/add_student` | POST | Create student |
| `/add_lecturer` | POST | Create lecturer |

## 🗄️ Database Schema

```
tblStudents:
- id INTEGER PRIMARY KEY AUTOINCREMENT
- fname TEXT
- lname TEXT  
- snumber TEXT

tblLecturers:
- empid INTEGER PRIMARY KEY AUTOINCREMENT
- fname TEXT
- lname TEXT
- course TEXT
```

Sample data auto-loaded on `/create_db`.

## 🎨 Styling System

Dark blue theme matching original desktop app:

```
Primary: #002855
Secondary: #335C81
Accent: #005780 (hover)
Dark: #001a33
```

Features:
- Glassmorphism effects
- Smooth hover animations
- Responsive navbar with logo
- Mobile-first design

## 📦 Requirements

```txt
flask==3.0.0
pillow==11.0.0
```

## 🧪 Testing & Development

```bash
# Virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

pip install -r requirements.txt
FLASK_ENV=development flask run --host=0.0.0.0

# Database inspection
sqlite3 SMS.db \".schema\"
sqlite3 SMS.db \"SELECT * FROM tblStudents;\"
```

## 🔧 Common Issues

| Issue | Solution |
|-------|----------|
| No module named 'flask' | `pip install -r requirements.txt` |
| Static files 404 | Check `static/images/BCLOGO.png` exists |
| Database empty | Visit `/create_db` |
| Forms not submitting | Check browser console |
| PythonAnywhere 500 | Check error log + WSGI path |

## 📈 Roadmap

- [x] Complete CRUD
- [x] Responsive UI
- [x] Production deployment  
- [ ] Authentication
- [ ] Update forms
- [ ] Search & pagination
- [ ] CSV export
- [ ] Docker container

## 🤝 Contributing

1. Fork the project
2. Create feature branch (`git checkout -b feature/YourFeature`)
3. Commit changes (`git commit -m 'Add YourFeature'`)
4. Push (`git push origin feature/YourFeature`)
5. Open Pull Request

## 📄 License

MIT License - see [LICENSE](LICENSE)

## 👨‍💻 Author

**Hugo du Preez**  
SSX361 Student Management System Project 2024

---
⭐ Star if you found this helpful!
