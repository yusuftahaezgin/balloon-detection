Real-Time Red Balloon Detection with YOLOv8
This project uses a custom-trained YOLOv8 model to detect red balloons in real-time via a webcam. The application draws a box around each detected balloon and indicates its position relative to the screen center (e.g., top-left).

Features
  - Detects red balloons in real-time from a webcam feed.
  - Displays the balloon's position relative to the screen center.
  - Powered by a custom-trained YOLOv8 model for high accuracy.
    
Tech Stack
  - Python
  - OpenCV
  - Ultralytics YOLOv8

Getting Started
1. Clone the repository:
git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name

2. Install dependencies:
pip install opencv-python ultralytics

3. Run the application:
Place the trained model file (best.pt) in the root directory and run the script:
python your_script_name.py

A window will open showing your webcam feed. When a red balloon is shown to the camera, it will be highlighted with a red box and its positional information will be displayed.

Press the 'q' key to close the window and stop the program.

Dataset and Training
The model was trained on the https://universe.roboflow.com/ravad/finalv6-nagig/dataset/2, which contains annotated images of red balloon and blue balloon classes.

  - Model Architecture: YOLOv8n (nano version) was used as the base model.
  - Training Environment: The model was trained for 50 epochs in a Google Colab notebook using a T4 GPU.
  - Performance: The final trained model achieved a mAP50-95 of 0.856 for the red balloon class, indicating high accuracy in both detection and localization. The code is filtered to        only display detections for the red balloon class.

