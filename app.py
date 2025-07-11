from flask import Flask, render_template, Response
from ultralytics import YOLO
import cv2
import pandas as pd
from datetime import datetime

# 1️⃣ Setup Flask
app = Flask(__name__)

# 2️⃣ Load YOLOv8 model
model = YOLO('yolov8n.pt')

# 3️⃣ Setup video capture (use a sample video for now)
cap = cv2.VideoCapture('videos/sample.mp4')  # Put your CCTV sample video in /videos

# 4️⃣ CSV log file setup
log_file = 'logs/detection_log.csv'

# Make empty log if not exists
try:
    pd.read_csv(log_file)
except:
    pd.DataFrame(columns=['timestamp', 'object']).to_csv(log_file, index=False)

def gen_frames():
    while True:
        success, frame = cap.read()
        if not success:
            break

        # Run YOLOv8 detection
        results = model.predict(frame, verbose=False)

        # Draw boxes
        annotated_frame = results[0].plot()

        # Log detections
        labels = results[0].names
        for box in results[0].boxes:
            cls_id = int(box.cls[0])
            obj_name = labels[cls_id]
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            log_entry = pd.DataFrame([[timestamp, obj_name]])
            log_entry.to_csv(log_file, mode='a', header=False, index=False)

        # Encode frame for streaming
        ret, buffer = cv2.imencode('.jpg', annotated_frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)
   
cap = cv2.VideoCapture('videos/sample.mp4')
if not cap.isOpened():
    print("❌ Video failed to open")
else:
    print("✅ Video opened successfully")

