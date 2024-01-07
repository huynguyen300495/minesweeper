from PIL import Image
from screen import analyze_square
import numpy as np


matrix = [['-' for _ in range(10)] for _ in range(8)]
# The path to your image file

def get_matrix(img):
    
    # Given square size
    square_size = img.width // 10

    # Calculate the number of squares horizontally and vertically
    num_squares_horizontal = img.width // square_size
    num_squares_vertical = 8  # We have 8 rows as mentioned

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
            
            result = analyze_square(cropped_img)

            matrix[y][x] = result
          
            # cropped_image_path = f'SquareImage/{y+1}_{x+1}.png'
            
            # # Save the cropped image
            # cropped_img.save(cropped_image_path)
            
            # # Append the relative path to the list
            # cropped_images.append(cropped_image_path)


    return matrix


# image_path = 'screenshot.png'
# matrix = get_matrix(image_path)

# print(matrix)

# for row in matrix:
#     print(' '.join([str(x) for x in row]))
