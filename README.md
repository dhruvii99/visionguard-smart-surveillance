# visionguard-smart-surveillance
An AI-powered smart surveillance &amp; incident reporting system using YOLOv5, Flask, NLP and Twilio alerts

## 🚀 Features

- 📹 Live CCTV video feed processing
- 🎯 Object detection with YOLOv8
- 📝 Automatic detection logs saved in CSV
- 🌐 Web dashboard built with Flask
- 🔔 Instant alert system (Twilio integration - planned)
- 📊 NLP module for smart event reporting (planned)

---

## 📂 Project Structure

visionguard-smart-surveillance/
├── app.py # Flask app
├── yolo_test.py # YOLO standalone test
├── yolov8n.pt # YOLOv8 model weights
├── videos/ # Input CCTV/sample videos
├── logs/ # Detection logs (CSV)
├── templates/index.html # Web dashboard template
├── requirements.txt # Python dependencies
├── README.md # Project info
├── .gitignore # Ignore venv, logs etc.


---

## ⚙️ Setup

1️⃣ **Clone the repo**
```bash
git clone https://github.com/YOUR_USERNAME/visionguard-smart-surveillance.git
cd visionguard-smart-surveillance
python -m venv venv
source venv/Scripts/activate  # Windows
# or
source venv/bin/activate      # Mac/Linux

pip install -r requirements.txt
4️⃣ Add your video file

Place your CCTV or sample video inside the videos/ folder.

5️⃣ Run the app

bash
Copy
Edit
python app.py
Visit http://127.0.0.1:5000 to see the live feed!


---

## ✅ **How to use it**
1️⃣ **Copy this markdown text.**  
2️⃣ Replace `YOUR_USERNAME` with your GitHub username in the clone link.  
3️⃣ Add your name at the end.  
4️⃣ Paste into your `README.md` file → `git add README.md` → `git commit -m "Updated README"` → `git push`.

---

If you want, I can generate a final version for you with **your name + repo link**.  
Want it? 🚀
