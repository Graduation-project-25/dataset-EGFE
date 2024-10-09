import os
import shutil

# Define the path to the dataset folder
dataset_folder = './EGFE-dataset'  # Adjust the path if needed
image_output_folder = './EGFE-dataset/images'  # Folder for images
json_output_folder = './EGFE-dataset/jsons'  # Folder for JSON files

# Create output directories if they don't exist
if not os.path.exists(image_output_folder):
    os.makedirs(image_output_folder)
if not os.path.exists(json_output_folder):
    os.makedirs(json_output_folder)

# Iterate through files in the dataset folder
for filename in os.listdir(dataset_folder):
    file_path = os.path.join(dataset_folder, filename)
    
    # Check if it's a file and separate based on the file extension
    if os.path.isfile(file_path):
        if filename.endswith('.png') or filename.endswith('.jpg'):
            shutil.move(file_path, image_output_folder)
        elif filename.endswith('.json'):
            shutil.move(file_path, json_output_folder)

print("Files have been separated into 'images' and 'jsons' folders.")
