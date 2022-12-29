import cv2
import imutils
import utils


image = cv2.imread("resources\\photomosaic1.JPG")
#
resized_image = utils.resizeImage(image, 0.1)
gray_image = utils.grayConvert(resized_image)
noise_reduced = utils.noiseRemoval(gray_image, 10, 40, 40)
utils.drawAndPauseImage(noise_reduced, "Noise Reduced")
canny_edge = utils.CannyEdge(noise_reduced, 30, 200)
utils.drawAndPauseImage(canny_edge, "Canny Edge")


contours = cv2.findContours(canny_edge.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(contours)
contours = sorted(contours, key=cv2.contourArea, reverse=True)[:50]
rectangleContour = None

countour_number = 0;    `
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

     print("contour ", countour_number, "is type ", type, " perim is ", perim, " area is ", area)
     if(type=='Rectangle' or type=='Pentagon'):
        temp_image = cv2.drawContours(resized_image.copy(), [approx], 0, (0, 255, 0), 3)
        utils.drawAndPauseImage(temp_image, "Temp Contour "+str(countour_number))


     countour_number = countour_number + 1
     if len(approx) == 4:
         rectangleContour = approx
         #break

# If we get here, hopefully we found a rectangle
if rectangleContour.any():
    cntrim = cv2.drawContours(resized_image.copy(), [rectangleContour], -1, (0, 255, 0), 3)
    utils.drawAndPauseImage(cntrim, "Final Rectangle")
else:
    print('Did not find any rectangle')


