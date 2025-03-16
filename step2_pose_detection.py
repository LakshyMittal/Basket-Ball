import cv2  # type: ignore
import mediapipe as mp  # type: ignore
import os

# Setup MediaPipe Pose for detecting movements
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)

# Function to process frames for detecting basketball poses
def analyze_pose(frame):
    # Convert the frame to RGB (required by MediaPipe)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(rgb_frame)

    # Draw landmarks on the frame
    if results.pose_landmarks:
        mp.solutions.drawing_utils.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

    return frame

# Dictionary containing paths for different movements
video_folders = {
    'Dribbling': r'C:\Users\Acer\OneDrive\Desktop\basketball\dribbling\Frames',
    'Shooting': r'C:\Users\Acer\OneDrive\Desktop\basketball\shooting\Frames'
}

# Loop through the folders specified in the dictionary
for movement, folder_path in video_folders.items():
    # Check if the folder path exists
    if not os.path.exists(folder_path):
        print(f"Folder path '{folder_path}' does not exist. Skipping...")
        continue

    for video_folder in os.listdir(folder_path):
        video_folder_path = os.path.join(folder_path, video_folder)
        # Check if this is a directory
        if os.path.isdir(video_folder_path):
            for frame_file in os.listdir(video_folder_path):
                # Check if the file is a .jpg image
                if frame_file.endswith('.jpg'):
                    frame_path = os.path.join(video_folder_path, frame_file)
                    frame = cv2.imread(frame_path)
                    if frame is not None:
                        frame_with_pose = analyze_pose(frame)

                        # Save the frame with detected pose
                        output_path = os.path.join(video_folder_path, f'pose_{frame_file}')
                        cv2.imwrite(output_path, frame_with_pose)
                        print(f"Processed and saved frame: {output_path}")
                    else:
                        print(f"Could not read frame at {frame_path}")
        else:
            print(f"{video_folder_path} is not a directory. Skipping...")

# Release MediaPipe resources
pose.close() 