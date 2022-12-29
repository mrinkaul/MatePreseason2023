import cv2

def resizeImage(img, factor):
    return cv2.resize(img, (0, 0), fx=factor, fy=factor)

def grayConvert(img):
    return cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

def noiseRemoval(img):
    return cv2.bilateralFilter(img, 11, 17, 17)

def noiseRemoval(img, d, sigmaColor, sigmaSpace):
    return cv2.bilateralFilter(img, d, sigmaColor, sigmaSpace)

def CannyEdge (img):
    return cv2.Canny(img, 30, 200)

def CannyEdge (img, lower_t, higher_t):
    return cv2.Canny(img, lower_t, higher_t)

def drawAndPauseImage(img, title):
    cv2.imshow(title, img)
    cv2.waitKey(0)