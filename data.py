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

# Example Labels:
# 0 = blank
# 1 = horizontal_line
# ...etc... (when you add more types, you can add more labels)

#Create a function which returns a number of samples of every type, each flattened, along with labels for which type each image is.
def generate_image_dataset(samples_per_class=100):
# This function should return two NumPy arrays:
#   X: the flattened input data, which has shape (num_samples, 64)
#   y: the labels for the input data, which has shape (num_samples,)
    X = []
    y = []

    #blank img (label 0)
    for _ in range(samples_per_class):
        img = generate_blank()
        X.append(img.flatten())
        y.append(0)

    #horizontal_line img (label 1)
    for _ in range(samples_per_class):
        img = generate_horizontal_line()
        X.append(img.flatten())
        y.append(1)

    X = np.array(X)
    y = np.array(y)

    return X, y

# print("Here's a blank image:\n", generate_blank())

# print("Here's a horizontal line image:\n", generate_horizontal_line())

X, y = generate_image_dataset(samples_per_class=2)
print("Here's the X dataset shape when num_samples = 4:\n", X.shape)
print("Here's the y dataset shape num_samples = 4:\n", y.shape)
print("Sample img 1:\n", X[0].reshape(8, 8), "\nSample img 2:\n", X[1].reshape(8, 8))
print("Sample label 1:", y[0], "\nSample label 2:", y[1])
print("Sample img 3:\n", X[2].reshape(8, 8), "\nSample img 4:\n", X[3].reshape(8, 8))
print("Sample label 3:", y[2], "\nSample label 4:", y[3])