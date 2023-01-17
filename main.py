import cv2

def detect_day_or_night(image_path):
    # Load image
    image = cv2.imread(image_path)

    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Calculate threshold for image
    thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]

    # Count white pixels
    white_pixels = cv2.countNonZero(thresh)

    # Determine if image is day or night based on number of white pixels
    if white_pixels > (gray.shape[0] * gray.shape[1]) * 0.5:
        print("This image was taken during the day.")
    else:
        print("This image was taken at night.")

# Test the function with an example image
detect_day_or_night("example_image.jpg")
