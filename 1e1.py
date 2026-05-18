import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('1.jpg')



print(img.shape)

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        pixel = img[i][j]
        gray = int((int(pixel[0]) + int(pixel[1]) + int(pixel[2])) / 3)
        if gray > 255:
            gray = 255
        if gray < 0:
            gray = 0
        pixel[0] = gray
        pixel[1] = gray
        pixel[2] = gray



hist = [0] * 256

for i in range(img.shape[0]):
    for j in range(img.shape[1]):

        gray = img[i][j][0]

        hist[gray] += 1

cv2.imshow('gray', img)
plt.plot(hist)
plt.title("Histogram")
plt.xlabel("Gray Level")
plt.ylabel("Number of Pixels")

plt.show()

#cdf
cdf = [0] * 256
cdf[0] = hist[0]
for i in range(1, 256):
    cdf[i] = cdf[i - 1] + hist[i]

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        gray = img[i][j][0]
        equalized_gray = int(cdf[gray] * 255 / (img.shape[0] * img.shape[1]))
        if equalized_gray > 255:
            equalized_gray = 255
        if equalized_gray < 0:
            equalized_gray = 0
        img[i][j][0] = equalized_gray
        img[i][j][1] = equalized_gray
        img[i][j][2] = equalized_gray
#saveimg
cv2.imwrite('equalized.jpg', img)

#show img and histogram after equalization

cv2.imshow('equalized', img)
hist_equalized = [0] * 256
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        gray = img[i][j][0]
        hist_equalized[gray] += 1
plt.plot(hist_equalized)
plt.title("Equalized Histogram")
plt.xlabel("Gray Level")
plt.ylabel("Number of Pixels")
plt.show()
cv2.waitKey(0) 
cv2.destroyAllWindows()

old_h = img.shape[0]
old_w = img.shape[1]

new_h = int(old_h * 1.5)
new_w = int(old_w * 1.5)

new_img = np.zeros((new_h, new_w, 3), dtype=np.uint8)

scale_x = old_w / new_w
scale_y = old_h / new_h

for i in range(new_img.shape[0]):
    for j in range(new_img.shape[1]):
        x = int(j * scale_x)
        y = int(i * scale_y)
        new_img[i][j] = img[y][x]
cv2.imshow('resized', new_img) 
cv2.waitKey(0)
cv2.destroyAllWindows()

print("img size:", img.shape)
if len(img.shape) == 2:
    print("number of channels: 1")
else:
    print("number of channels:", img.shape[2])
print("data type:", img.dtype)
print("minimum pixel value:", img.min())
print("maximum pixel value:", img.max())