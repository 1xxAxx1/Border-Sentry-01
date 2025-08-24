import cv2
import numpy as np
from ultralytics import YOLO

STREAM_URL = "http:// (PASTE IP ADDRESS HERE) /video"   # Video feed from IP cam
MODEL = YOLO("yolov8n.pt")  # YOLO
CONF_THRESH = 0.5

# Boundary line
LINE_START = (0, 400)  # (x1, y1)
LINE_END   = (5000, 400)  # (x2, y2)

# Check if bbox crosses line
def crossed_line(x1, y1, x2, y2):
    cx = int((x1 + x2) / 2)
    cy = int((y1 + y2) / 2)
    # Line equation
    line_y = int(np.interp(cx, [LINE_START[0], LINE_END[0]], [LINE_START[1], LINE_END[1]]))
    return cy > line_y  # object center below line → crossing


cap = cv2.VideoCapture(STREAM_URL)

if not cap.isOpened():
    print("Could not open stream.")
    exit()

print("Connected. Press Q to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Frame not received.")
        break

    results = MODEL(frame)[0]  # Run YOLO
    for box in results.boxes:
        cls = int(box.cls[0])
        conf = float(box.conf[0])
        if conf < CONF_THRESH:
            continue

        # Get object info
        x1, y1, x2, y2 = box.xyxy[0].cpu().numpy().astype(int)
        label = MODEL.names[cls]

        # Draw box
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, f"{label} {conf:.2f}", (x1, y1 - 5),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

        # Check crossing
        if crossed_line(x1, y1, x2, y2):
            cv2.putText(frame, f"ALERT: {label} crossed!", (50, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
            print(f"ALERT: {label} crossed boundary")

    # Draw boundary line
    cv2.line(frame, LINE_START, LINE_END, (0, 0, 255), 3)

    cv2.imshow("AI Sentry Tower", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
