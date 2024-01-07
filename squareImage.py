from PIL import Image
import os

# The path to your image file
image_path = 'screenshot.png'

# Open the image file
img = Image.open(image_path)

# Given square size
square_size = img.width // EASY_X

# Calculate the number of squares horizontally and vertically
num_squares_horizontal = img.width // square_size
num_squares_vertical = 8  # We have 8 rows as mentioned

# Initialize a list to store the file paths of the saved images
cropped_images = []

# Ensure the 'SquareImage' directory exists
os.makedirs('SquareImage', exist_ok=True)

# Crop and save the squares
for y in range(num_squares_vertical):
    for x in range(num_squares_horizontal):
        # Define the box to crop
        left = x * square_size
        upper = y * square_size
        right = left + square_size
        lower = upper + square_size
        box = (left, upper, right, lower)
        
        # Crop the image to the box
        cropped_img = img.crop(box)
        
        # Define the relative path for the cropped image
        cropped_image_path = f'SquareImage/{y+1}_{x+1}.png'
        
        # Save the cropped image
        cropped_img.save(cropped_image_path)
        
        # Append the relative path to the list
        cropped_images.append(cropped_image_path)

# Return the list of cropped image paths
cropped_images
