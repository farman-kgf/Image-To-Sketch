import cv2

# Prompt the user to input the image file path
image_path = input("Enter the path to the image file: ")

# Read the input image
img = cv2.imread(image_path)

if img is None:
    print("Error: Image not found or unable to read the image.")
    exit()

# Convert to grayscale
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Invert the grayscale image
invert = cv2.bitwise_not(gray_image)

# Apply Gaussian blur
blur = cv2.GaussianBlur(invert, (21, 21), 0)

# Invert the blurred image
invert_blur = cv2.bitwise_not(blur)

# Create the sketch effect by dividing the grayscale image by the inverted blurred image
sketch = cv2.divide(gray_image, invert_blur, scale=250.0)

# Save the sketch image

sketchpng = input("what the name youwant to save as : ")

cv2.imwrite("sketch.png", sketch)

print("Sketch image saved as 'sketch.png'.")

exit()