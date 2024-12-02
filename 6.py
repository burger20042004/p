# import cv2
# import numpy as np

# # Load an image
# image = cv2.imread('image.jpg')

# # Convert to grayscale
# gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# # Apply Canny edge detection
# edges = cv2.Canny(gray_image, 100, 200)

# # Display the original and processed images
# cv2.imshow('Original Image', image)
# cv2.imshow('Edge Detected Image', edges)

# # Wait for key press and close windows
# cv2.waitKey(0)
# cv2.destroyAllWindows()


import cv2


image = cv2.imread('image.jpg')

greyscale = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(greyscale, 100,200)
cv2.imshow("Original: " , image)
cv2.imshow("Edges: ", edges)

cv2.waitKey(0)

cv2.destroyAllWindows()



