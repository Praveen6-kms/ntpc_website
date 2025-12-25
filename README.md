# NTPC Simhadri – Internal Web Portal

This project is a fully functional web portal developed for **NTPC Simhadri Super Thermal Power Station** to provide centralized access to important links, services, daily updates, and internal communications.

---

## 🚀 Features

### 🔷 Frontend
- Modern, clean and responsive UI
- Built using Bootstrap 4
- Optimized for Desktop + Mobile
- Carousel for announcements when no updates exist
- Professional corporate theme

### 🔷 Backend (Flask)
- Admin Login System
- Secure Admin Panel
- Add / Edit / Delete Daily Updates
- Image upload support
- Automatically stores date & time when news is posted
- Data stored in `SQLite` database
- Fully connected with frontend display

---

## 🏗️ Tech Stack

| Component  | Technology Used |
|-----------|------------------|
| Frontend  | HTML, CSS, Bootstrap |
| Backend   | Python Flask |
| Database  | SQLite |
| Hosting   | Render |
| Authentication | Flask Session |

---

## 📂 Project Structure

project-folder /
│
├── app.py                   # Main Flask backend application
├── requirements.txt         # Python dependencies
├── Procfile                 # Render deployment file
├── updates.db               # SQLite database
│
├── templates/               # All frontend HTML pages
│   ├── index.html
│   ├── admin_login.html
│   ├── manage_updates.html
│   ├── add_news.html
│   ├── edit_update.html
│
└── static/                  # Static assets
    ├── ntpc.css             # Custom styles
    ├── uploads/             # Uploaded update images
    └── assets/ (optional)   # Icons, banners etc if added later

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

git clone<repo-link>
cd project-folder


### 2️⃣ Install Dependencies

pip install-r requirements.txt


### 3️⃣ Run Project

python app.py

Project runs at:http://127.0.0.1:5000/


---

## 🔐 Admin Panel
Login → Manage Updates → Post News → Reflects on Homepage 🎉  
Credentials are stored securely in backend code.

---

## 🌐 Deployment
The project is deployed using **Render Free Web Service**, making it accessible online and auto-deployed on new commits.

---

## 🎯 Purpose
This project helps NTPC employees:
- Quickly access important tools
- View latest announcements
- Maintain internal communication efficiently
- Digitize office updates

---

## 👨‍💻 Developer
**KMS Praveen**  
Flask Developer • Frontend Designer • Full Stack Enthusiast


---

## ⭐ Suggestions & Contributions
This is a live evolving project. Suggestions, improvements, and contributions are always welcome.

---

## 🛡️ Disclaimer
This project is intended for **internal organizational use only** and may contain proprietary NTPC references.



