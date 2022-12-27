import cv2
import matplotlib.pyplot as plt

import utils

image = cv2.imread("resources\\photomosaic1.jpg")
resized_image = utils.resizeImage(image, 0.1)
cv2.imshow("Resized image", resized_image)

gray_image = utils.grayConvert(resized_image)
cv2.imshow("gray image", gray_image)

noise_reduced = utils.noiseRemoval(gray_image)
cv2.imshow("noise down img", noise_reduced)

canny_edge = utils.CannyEdge(noise_reduced)
cv2.imshow("edge sharpen", noise_reduced)

cv2.waitKey(0)

