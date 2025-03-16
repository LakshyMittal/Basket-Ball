import os

# Paths to the folders where the frames are saved
movement_folders = {
    'Dribbling': r'C:\Users\Acer\OneDrive\Desktop\basketball\dribbling\Frames',
    'Shooting': r'C:\Users\Acer\OneDrive\Desktop\basketball\shooting\Frames'
}

# Dictionary to store the results of pose matching for each movement
pose_summary = {
    'Dribbling': 0,
    'Shooting': 0
}

# File where results from Step 4 are stored
results_file_path = r"C:\Users\Acer\OneDrive\Desktop\basketball\pose_evaluation.txt"

# Function to read results from the file and count matches
def summarize_pose_matches():
    if not os.path.exists(results_file_path):
        print(f"No results found from Step 4 at {results_file_path}. Please make sure Step 4 completed successfully.")
        return
    
    try:
        with open(results_file_path, "r") as results_file:
            for line in results_file:
                # Check each line to see if it indicates a pose match
                if "matches the criteria" in line:
                    if "Dribbling" in line:
                        pose_summary['Dribbling'] += 1
                    elif "Shooting" in line:
                        pose_summary['Shooting'] += 1
    except Exception as e:
        print(f"An error occurred while reading the results file: {e}")
        return
    
    # Print the summary
    print("Pose Evaluation Summary:")
    for movement, count in pose_summary.items():
        print(f"{movement} frames matching criteria: {count}")
    
    # Save summary to a file
    try:
        summary_file_path = r"C:\Users\Acer\OneDrive\Desktop\basketball\pose_summary_report.txt"
        with open(summary_file_path, "w") as summary_file:
            summary_file.write("Pose Evaluation Summary:\n")
            for movement, count in pose_summary.items():
                summary_file.write(f"{movement} frames matching criteria: {count}\n")
        print(f"Summary saved to '{summary_file_path}'")
    except Exception as e:
        print(f"An error occurred while saving the summary file: {e}")

# Run the summary function
summarize_pose_matches()
