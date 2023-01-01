import cv2
import imutils
import utils
import numpy as np
import argparse

image = cv2.imread("resources\\plainbox2.jpg")
print(image.shape)

factor = 0.69
resized_image = utils.resizeImage(image, factor)
gray_image = utils.grayConvert(resized_image)
noise_reduced = utils.noiseRemoval(gray_image, 20,20,20)
utils.drawAndPauseImage(noise_reduced, "Noise Reduced")
canny_edge = utils.CannyEdge(noise_reduced, 100, 200)
utils.drawAndPauseImage(canny_edge, "Canny Edge")



contours = cv2.findContours(canny_edge.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(contours)
contours = sorted(contours, key=cv2.contourArea, reverse=True)[:50]
rectangleContourList = []

contour_number = 0;
for c in contours:
     perim = cv2.arcLength(c, True)
     #print("For contour ", countour_number, " perim is ", perim)

     area = cv2.contourArea(c)
     #print("For contour ", countour_number, " area is ", area)

     epsilon = 0.01*perim;

     approx = cv2.approxPolyDP(c, epsilon, True)
     #print("For contour ", countour_number, " approx is ", approx)

     type = "unknown"
     i, j = approx[0][0]
     if len(approx) == 3:
         type = 'Triangle'
     elif len(approx) == 4:
         type = 'Rectangle'
     elif len(approx) == 5:
         type = 'Pentagon'
     elif 6 < len(approx) < 15:
         type = 'Eclipse'
     else:
         type = 'Circle'

     print("contour ", contour_number, "is type ", type, " perim is ", perim, " area is ", area)
     if(type=='Rectangle' or type=='Pentagon'):
        temp_image = cv2.drawContours(resized_image.copy(), [approx], 0, (0, 255, 0), 3)
        #utils.drawAndPauseImage(temp_image, "Temp Contour "+str(contour_number))


     contour_number = contour_number + 1
     if len(approx) == 4:
         rectangleContourList.append(approx)
         print("Added contour ", contour_number, " to rectangularContourList")
         #break

# If we get here, hopefully we found a rectangle
if len(rectangleContourList) >= 3:
    print("Found ", len(rectangleContourList), " rectangles")
    for r in [0, 1, 2]:
        rectCoordinates = rectangleContourList[r]
        cntrim = cv2.drawContours(resized_image.copy(), [rectCoordinates], -1, (0, 255, 0), 3)
        utils.drawAndPauseImage(cntrim, "Rectangle " + str(r))
        print(rectCoordinates)
        print(rectCoordinates.reshape(4, 2))
        print(utils.order_points(rectCoordinates.reshape(4, 2)))
        transformedImage = utils.four_point_transform(image, rectCoordinates.reshape(4, 2) / factor)
        utils.drawAndPauseImage(transformedImage, "Transformed Rectangle " + str(r))
else:
    print('Did not find any rectangle')


