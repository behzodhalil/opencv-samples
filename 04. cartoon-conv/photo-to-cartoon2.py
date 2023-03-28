import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread("/Users/a1234/Documents/opencv-samples/docs/images/seoul.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gray = cv2.medianBlur(gray, 5)
edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

plt.figure(figsize=(10,10))
plt.imshow(edges,cmap="gray")

plt.axis("off")
plt.title("Edged Image")

plt.show()