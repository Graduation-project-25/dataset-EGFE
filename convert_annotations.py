import json
import os
from PIL import Image

# Define the paths for the image folder and annotations folder
image_folder = './EGFE-dataset/images'  # Adjust this path if needed
json_folder = './EGFE-dataset/jsons'  # Folder containing JSON annotations
output_annotation_folder = './EGFE-dataset/yolo_annotations'  # Output folder for YOLO formatted annotations

# Create the output annotation directory if it doesn't exist
if not os.path.exists(output_annotation_folder):
    os.makedirs(output_annotation_folder)

# Function to convert coordinates from (x, y, width, height) to YOLO format
def convert_to_yolo_format(x, y, width, height, image_width, image_height):
    x_center = (x + width / 2) / image_width
    y_center = (y + height / 2) / image_height
    yolo_width = width / image_width
    yolo_height = height / image_height
    
    return x_center, y_center, yolo_width, yolo_height

# Loop through the JSON files to extract annotations
for json_file in os.listdir(json_folder):
    if json_file.endswith('.json'):
        json_path = os.path.join(json_folder, json_file)
        
        # Load JSON file
        with open(json_path, 'r',encoding='utf-8') as f:
            data = json.load(f)
            print(f"Processing {json_file}: {data}")  # Check the loaded data
        
        # Assuming annotations are inside the 'layers' key now
        layers = data.get('layers', [])  # Safely get the 'layers' list, if available

        # Extract the image filename without the extension
        image_name = json_file.replace('.json', '.png')  # Adjust if your images have a different extension
        image_path = os.path.join(image_folder, image_name)
        
        # Check if the corresponding image exists
        if os.path.exists(image_path):
            # Open the image to get its dimensions
            with Image.open(image_path) as img:
                image_width, image_height = img.size
            
            # Prepare YOLO annotations
            yolo_annotations = []
            
            # Loop through the objects in the layers data
            for obj in layers:
                rect = obj['rect']
                x, y, width, height = rect['x'], rect['y'], rect['width'], rect['height']
                class_id = obj['label']  # Assuming the label is in 'label'
                
                # Convert the rectangle coordinates to YOLO format
                yolo_bbox = convert_to_yolo_format(x, y, width, height, image_width, image_height)
                yolo_annotations.append(f"{class_id} {' '.join(map(str, yolo_bbox))}")

            # Save YOLO formatted annotations to a text file
            output_file_path = os.path.join(output_annotation_folder, json_file.replace('.json', '.txt'))
            with open(output_file_path, 'w') as out_file:
                out_file.write('\n'.join(yolo_annotations))

print("All annotations have been converted to YOLO format.")
