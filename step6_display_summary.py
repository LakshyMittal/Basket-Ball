import cv2  # type: ignore # Import OpenCV
import matplotlib.pyplot as plt  # type: ignore # Import Matplotlib
import numpy as np  # type: ignore # Import NumPy

# Initialize external webcam
cap = cv2.VideoCapture(1)  # Use 1 for the external webcam
if not cap.isOpened():
    print("Error: Unable to access the external camera.")
    exit()

# Initialize heatmap storage
heatmap = np.zeros((480, 640))  # Assuming frame size is 640x480

# Main loop
while True:
    ret, frame = cap.read()  # Read a frame from the webcam
    if not ret:
        print("Error: Frame not captured.")
        break

    # Simulate keypoint detection (Replace with your function)
    keypoints = [[320, 240], [300, 200], [400, 300]]  # Example keypoints (Replace with your detection function)
    if keypoints:
        for kp in keypoints:
            x, y = int(kp[0]), int(kp[1])
            if 0 <= x < 640 and 0 <= y < 480:
                heatmap[y, x] += 1

    # Display heatmap periodically (every 100 frames)
    if cv2.waitKey(1) % 100 == 0:
        plt.imshow(heatmap, cmap='hot', interpolation='nearest')
        plt.title("Movement Heatmap")
        plt.show()

    # Exit loop on 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
