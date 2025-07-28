# 🎥 Multimedia Website Project

A **Django-based web application** designed to showcase images, audio tracks, and video files. It features a responsive frontend built with **Tailwind CSS** and a robust Django backend for content management.

---

## ✨ Features

- 📸 **Dynamic Multimedia Display**  
  View images, listen to audio tracks, and watch videos seamlessly.
  
- 🔧 **Django Admin Integration**  
  Easily upload, manage, and organize multimedia content via Django's admin interface.

- 📱 **Responsive Design**  
  Tailored to look great on mobile, tablet, and desktop devices.

- 🧱 **Scalable Backend**  
  Built on Django, allowing for easy expansion and new features.

---

## ✅ Prerequisites

Ensure you have the following installed:

- **Python 3.x** (Recommended: Python 3.9+)
- **pip** (Usually comes with Python)

---

## ⚙️ Setup Instructions

Follow these steps to get the project running locally:

### 1. Clone the Repository

```bash
git clone https://github.com/SherlockAkj/Multimedia-App.git
cd multimedia_project

```
2. Create a Virtual Environment
```bash
python -m venv venv
```

3. Activate the Virtual Environment

Windows:
```bash
.\venv\Scripts\activate
```
macOS/Linux:
```bash
source venv/bin/activate
```
4. Install Dependencies
```bash
pip install -r requirements.txt
```

5. Apply Database Migrations
```bash
python manage.py migrate
```

6. Run the Development Server
```bash
python manage.py runserver
Visit http://127.0.0.1:8000/ to access the app.
```

**🧪 Usage**

🖥 Accessing the Website
Open http://127.0.0.1:8000/ in your browser.

The homepage will display multimedia content after uploading via admin.

🛠 Managing Multimedia Content
Go to: http://127.0.0.1:8000/admin/

Log in using your superuser credentials.

Username: 'admin' , Password: 'michael001' is the already created superuser for development purposes

Under MULTIMEDIA_APP, you'll find:

📷 Images

🎵 Audio Tracks

📹 Videos

Click "Add" to upload multimedia files with titles and optional descriptions.


📁 Static and Media Files
Static Files: Site assets (CSS, JS).
Tailwind CSS is loaded via CDN. The multimedia_app/static/ folder remains empty unless you add custom static assets.

Media Files: User-uploaded images, audio, and videos.
Stored in the /media/ directory and served automatically by Django during development.

🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you’d like to change.

📜 License
This project is licensed under the MIT License.

Built with 💙 using Django and Tailwind CSS.
