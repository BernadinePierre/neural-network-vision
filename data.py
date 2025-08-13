import numpy as np

#generate_blank() always returns an 8x8 NumPy array where every pixel is set to 0.
def generate_blank():
    return np.zeros((8, 8), dtype=int) 

#generate_horizontal_line() returns an 8x8 NumPy array where a random single row is set to 1.
#This row should be randomly selected when you call the function.
def generate_horizontal_line():
    blank_img = generate_blank()
    random_single_row = np.random.randint(0, 8)
    blank_img[random_single_row, :] = 1
    horizontal_line_img = blank_img
    return horizontal_line_img

print("Here's a blank image:\n", generate_blank())
print("Here's a horizontal line image:\n", generate_horizontal_line())