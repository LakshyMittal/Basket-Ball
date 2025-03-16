import os

# Define the path where results should be saved
results_file_path = r"C:\Users\Acer\OneDrive\Desktop\basketball\pose_evaluation.txt"

# Sample data to write to the file (replace this with your actual evaluation logic)
pose_evaluation_data = {
    'Dribbling': 5,   # Example count for Dribbling
    'Shooting': 3     # Example count for Shooting
}

# Function to evaluate poses and save results
def evaluate_and_save_pose_results():
    try:
        # Open the file in write mode
        with open(results_file_path, 'w') as file:
            # Write evaluation data to file
            for movement, count in pose_evaluation_data.items():
                file.write(f"{movement}: {count}\n")
        
        # Confirm that the file has been created successfully
        print(f"pose_evaluation.txt created successfully at {results_file_path}.")
    
    except Exception as e:
        print(f"Error while saving pose evaluation data: {e}")

# Execute the evaluation and saving function
evaluate_and_save_pose_results()
