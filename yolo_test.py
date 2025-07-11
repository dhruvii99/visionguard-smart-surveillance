from ultralytics import YOLO

# Load YOLOv8 nano model (lightweight)
model = YOLO('yolov8n.pt')

# Run detection on Zidane image
results = model.predict('https://ultralytics.com/images/zidane.jpg')

# Show results
results[0].show()
