# Border Sentry Tower
  
This project uses a **phone (IP Webcam app)** as the camera and a **laptop** running Python with **YOLOv8 + OpenCV** to detect objects crossing a **virtual boundary line**.  

---

## Demo
- Live video feed from phone → streamed to laptop  
- Objects (people/vehicles) detected with bounding boxes  
- Red line = **virtual border**  
- When an object crosses → **ALERT shown on screen + console**

---

## Features
-  Connect phone camera feed via IP Webcam  
-  Real-time object detection using **YOLOv8**  
-  Virtual boundary line crossing detection  
-  Alerts when line is crossed (visual + console log)  
-  (Optional) Add sound siren or cloud logging dashboard

---

##  Requirements
- Python **3.9+**
- Phone + IP Webcam app (Android: *IP Webcam*, iOS: *DroidCam/Iriun*)
- Laptop on the **same Wi-Fi** network

---

##  Installation

1. Clone this repo:
   ```bash
   git clone https://github.com/your-username/ai-sentry-tower.git
   cd ai-sentry-tower
