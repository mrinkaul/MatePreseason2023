import cv2
import numpy as np

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

def orderPoint(pts):
    rect = np.zeros((4,2), dtype= "float32")
    s = pts.sum(axis = 1)

    rect[0] = pts[np.argmax(s)]
    rect[2] = pts[np.argmin(s)]

    diff = np.diff(pts,axis = 1)

    rect[1] = pts[np.argmin(diff)]
    rect[3] = pts[np.argmax(diff)]
    return rect



def fourPointTransf(img, pts):
    rect = orderPoint(pts)
    (tl, tr, br, bl) = rect
    widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
    widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
    maxWidth = max(int(widthA), int(widthB))

    heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
    heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
    maxHeight = max(int(heightA), int(heightB))

    dst = np.array([
        [0, 0],
        [maxWidth - 1, 0],
        [maxWidth - 1, maxHeight - 1],
        [0, maxHeight - 1]], dtype="float32")

    M = cv2.getPerspectiveTransform(rect, dst)
    warped = cv2.warpPerspective(img, M, (maxWidth, maxHeight))
    return warped





















