import cv2  # type: ignore
import os

video_folders = {
    'Dribbling': r'C:\Users\Acer\OneDrive\Desktop\basketball\dribbling',  
    'Shooting': r'C:\Users\Acer\OneDrive\Desktop\basketball\shooting'      
}

frame_rate = 1


for movement, folder_path in video_folders.items():
    output_folder = os.path.join(folder_path, 'Frames')
    os.makedirs(output_folder, exist_ok=True)
           
    for video_file in os.listdir(folder_path):
        if video_file.endswith('.mp4'):
            video_path = os.path.join(folder_path, video_file)
            
            video_name = os.path.splitext(video_file)[0]
            video_output_folder = os.path.join(output_folder, video_name)
            os.makedirs(video_output_folder, exist_ok=True)

            cap = cv2.VideoCapture(video_path)
            count = 0
            while cap.isOpened():
                cap.set(cv2.CAP_PROP_POS_MSEC, count * 1000 * frame_rate)
                success, image = cap.read()
                if not success:
                     break

                cv2.imwrite(os.path.join(video_output_folder, f"frame{count}.jpg"), image)
                count += 1

            cap.release() 
            print(f"Frame extraction completed for {movement} - {video_name}") 