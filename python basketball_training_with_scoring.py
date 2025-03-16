import cv2  # type: ignore
import mediapipe as mp  # type: ignore

# Initialize MediaPipe Pose model
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

cap = cv2.VideoCapture(1)  # Try 1 if this doesn't work

if not cap.isOpened():
    print("Error: Unable to access webcam.")
    exit()

print("Webcam accessed successfully. Press 's' to start Shooting mode, 'd' for Dribbling mode, or 'q' to quit.")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Error: Unable to grab frame.")
        break
    else:
        print("Frame captured successfully.")

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = pose.process(rgb_frame)

    if result.pose_landmarks:
        print("Pose landmarks detected.")

    cv2.imshow("Basketball Trainer", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        print("Exiting program.")
        break

cap.release()
cv2.destroyAllWindows()
