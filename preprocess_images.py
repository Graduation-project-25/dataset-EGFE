from PIL import Image
import os

# Define the path to the image folder
image_folder = './EGFE-dataset/images'
output_folder = './EGFE-dataset/preprocessed_images'

# Set the desired image size
target_size = (224, 224)  # Example size, adjust as needed

# Create output directory if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Loop through images and resize
for filename in os.listdir(image_folder):
    if filename.endswith('.png') or filename.endswith('.jpg'):
        img_path = os.path.join(image_folder, filename)
        img = Image.open(img_path)
        img_resized = img.resize(target_size)
        
        # Save the resized image to the output folder
        img_resized.save(os.path.join(output_folder, filename))

print("All images have been resized.")
