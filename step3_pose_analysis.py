import cv2  # type: ignore
import mediapipe as mp  # type: ignore
import os
import math

# Setup MediaPipe Pose for detecting movements
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)

# Function to calculate the angle between three points
def calculate_angle(a, b, c):
    angle = math.degrees(math.atan2(c[1] - b[1], c[0] - b[0]) - math.atan2(a[1] - b[1], a[0] - b[0]))
    angle = abs(angle)
    if angle > 180:
        angle = 360 - angle
    return angle

# Function to process frames and classify movements
def analyze_and_classify_pose(frame):
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(rgb_frame)

    if results.pose_landmarks:
        mp.solutions.drawing_utils.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        # Extracting landmarks for angle calculation
        landmarks = results.pose_landmarks.landmark

        # Define points for key joints for angle calculation (example: LEFT_ARM for dribbling)
        left_shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x, 
                         landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
        left_elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x, 
                      landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
        left_wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x, 
                      landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]

        # Calculate angles to classify the movement
        left_arm_angle = calculate_angle(left_shoulder, left_elbow, left_wrist)

        # Classification logic based on angles
        if 70 < left_arm_angle < 110:
            movement_type = "Dribbling"
        elif 150 < left_arm_angle < 180:
            movement_type = "Shooting"
        else:
            movement_type = "Unknown"

        # Annotate the frame with the movement type
        cv2.putText(frame, f'Movement: {movement_type}', (10, 30), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
    
    return frame

# Loop through frames in the "Frames" folder and process each one
video_folders = {
    'Dribbling': r'C:\Users\Acer\OneDrive\Desktop\basketball\dribbling\Frames',
    'Shooting': r'C:\Users\Acer\OneDrive\Desktop\basketball\shooting\Frames'
}

for movement, folder_path in video_folders.items():
    for video_folder in os.listdir(folder_path):
        video_folder_path = os.path.join(folder_path, video_folder)
        if os.path.isdir(video_folder_path):
            for frame_file in os.listdir(video_folder_path):
                if frame_file.endswith('.jpg'):
                    frame_path = os.path.join(video_folder_path, frame_file)
                    frame = cv2.imread(frame_path)
                    frame_with_classification = analyze_and_classify_pose(frame)

                    # Save the frame with classification
                    classified_frame_path = os.path.join(video_folder_path, f'classified_{frame_file}')
                    cv2.imwrite(classified_frame_path, frame_with_classification)

                    # Optionally display the frame (uncomment to use)
                    # cv2.imshow("Pose Detection and Classification", frame_with_classification)
                    # cv2.waitKey(1)

# Release MediaPipe resources
pose.close()