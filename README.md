# Image Day time detection

The script loads an image and converts it to grayscale. Then it applies a Gaussian blur to reduce noise, and calculates a threshold for the image. It counts the number of white pixels in the thresholded image and compares it to total number of pixels. If the ratio of white pixels is above the 0.5, it would print that the image was taken during the day, otherwise, it would print that the image was taken at night. Note that this is an example, and the values of the threshold can be adjusted according to the image characteristics.
