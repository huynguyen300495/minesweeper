from PIL import Image

# The path to your image file
image_path = 'screenshot.png'

# Open the image file
img = Image.open(image_path)

# Display the image
# img.show()

# Given square size
square_size = 111

# Calculate the number of squares horizontally and vertically
num_squares_horizontal = img.width // square_size
num_squares_vertical = 8  # We have 8 rows as mentioned

# Initialize a list to store the file paths of the saved images
cropped_images = []

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
        
        # Save the cropped image to the environment path
        cropped_image_path = f'/Users/huynguyen/Desktop/Minesweeper/minesweeper/SquareImage/{y+1}_{x+1}.png'
        cropped_img.save(cropped_image_path)
        cropped_images.append(cropped_image_path)

# Return the list of cropped image paths
cropped_images




