import cv2 # type: ignore
import numpy as np # type: ignore
import tensorflow as tf # type: ignore
from mediapipe import solutions as mp_solutions # type: ignore

# Initialize pose detection
mp_pose = mp_solutions.pose
pose = mp_pose.Pose()
mp_drawing = mp_solutions.drawing_utils

# Initialize webcam
cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture frame.")
        break
 
    # Flip the frame for a mirror effect
    frame = cv2.flip(frame, 1)

    # Convert the frame to RGB for Mediapipe
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Perform pose detection
    results = pose.process(rgb_frame)
    
    # Draw the pose landmarks on the frame
    mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

    # Check if landmarks are detected
    if results.pose_landmarks:
        landmarks = results.pose_landmarks.landmark

        # Extract key landmarks
        left_wrist = landmarks[mp_pose.PoseLandmark.LEFT_WRIST]
        left_elbow = landmarks[mp_pose.PoseLandmark.LEFT_ELBOW]
        left_shoulder = landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER]
        right_wrist = landmarks[mp_pose.PoseLandmark.RIGHT_WRIST]
        right_elbow = landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW]
        right_shoulder = landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER]

        # Example logic: Check for shooting motion (right arm movement)
        if right_wrist.y < right_shoulder.y and right_elbow.y < right_shoulder.y:
            cv2.putText(frame, "Shooting Detected!", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # Example logic: Check for dribbling motion (right wrist repetitive movement)
        if abs(right_wrist.y - right_elbow.y) > 0.05:  # Adjust threshold for sensitivity
            cv2.putText(frame, "Dribbling Detected!", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    # Display the frame
    cv2.imshow("Basketball Detection", frame)

    # Quit the application
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Releavvvs
cap.release()
cv2.destroyAllWindows()


