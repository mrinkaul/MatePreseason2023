import cv2

def resizeImage(img, factor):
    return cv2.resize(img, (0, 0), fx=factor, fy=factor)

def grayConvert(img):
    return cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

def noiseRemoval(img):
    return cv2.bilateralFilter(img, 9, 75, 75)

def CannyEdge (img):
    return cv2.Canny(img, 250, 255)
