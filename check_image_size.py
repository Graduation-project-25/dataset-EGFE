from PIL import Image
import os

# Specify the path to the image you want to check
image_path = './EGFE-dataset/preprocessed_images/0.png'  # Change this to the path of your specific image

# Check if the file exists
if os.path.exists(image_path):
    # Open the image
    img = Image.open(image_path)
    
    # Get the size of the image
    width, height = img.size
    
    # Print the dimensions
    print(f"The size of the image '{os.path.basename(image_path)}' is: {width} x {height}")
else:
    print(f"The image '{os.path.basename(image_path)}' does not exist.")

