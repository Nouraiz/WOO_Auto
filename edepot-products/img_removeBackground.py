import numpy as np
import cv2 as cv
import numpy as np

# Directory paths
root_dir = r"D:\Dropbox\eDEPOT\Current Working Directory\test\FWB-2004-(0).jpg"




img = cv.imread(root_dir)
imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret1, thresh = cv.threshold(imgray, 0, 255, cv.THRESH_BINARY_INV+cv.THRESH_OTSU)

# Removing Noise
kernel = np.ones((5, 5), np.uint8)
opening = cv.morphologyEx(thresh, cv.MORPH_OPEN, kernel, iterations=2)

# sure background area
sure_bg = cv.dilate(opening, kernel, iterations=3)

# Finding sure foreground area
dist_transform = cv.distanceTransform(opening,cv.DIST_L2,5)
ret, sure_fg = cv.threshold(dist_transform,0.7*dist_transform.max(),255,0)
# edges = cv.Canny(imgray, 180, 200, apertureSize=3)

#
# ret, thresh = cv.threshold(imgray, 200, 255, 0)
# contours, hierarchy = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
# img2 = cv.drawContours(img, contours, -1, (0,255,0), 3)
#
cv.namedWindow("cropped", cv.WINDOW_NORMAL)
cv.imshow("cropped", opening)
cv.resizeWindow("cropped", 600, 600)
cv.waitKey(0)






















# parser = argparse.ArgumentParser()
# parser.add_argument('file_in', help='Input file')
# parser.add_argument('file_out', help='Output file')
# args = parser.parse_args()

# #== Parameters =======================================================================
# BLUR = 19
# CANNY_THRESH_1 = 25
# CANNY_THRESH_2 = 255
# MASK_DILATE_ITER = 5
# MASK_ERODE_ITER = 13
# MASK_COLOR = (0.0,0.0,1.0)
#
# #-- Read image -----------------------------------------------------------------------
# img = cv2.imread(root_dir)
# gray = cv2.GaussianBlur(img, (5, 5), 1)
# gray = cv2.cvtColor(gray,cv2.COLOR_BGR2RGB)
# gray = cv2.cvtColor(gray,cv2.COLOR_BGR2GRAY)
#
# gray = 255 - cv2.threshold(gray, 0,255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1]
#
# edges = cv2.dilate(gray, kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (21,21)) , iterations = 1)
# edges = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3)))
# edges = cv2.GaussianBlur(edges, (1, 1), 0)
# gray = gray > 1
# hrc = []
# #-- Find contours in edges, sort by area ---------------------------------------------
# contour_info = []
# contours = cv2.findContours(gray, edges, hrc, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
#
# for c in contours:
#     contour_info.append((
#         c,
#         cv2.isContourConvex(c),
#         cv2.contourArea(c),
#     ))
# contour_info = sorted(contour_info, key=lambda c: c[2], reverse=True)
# max_contour = contour_info[0]
#
# #-- Create empty mask, draw filled polygon on it corresponding to largest contour ----
# # Mask is black, polygon is white
# mask = np.zeros(edges.shape)
# cv2.fillConvexPoly(mask, max_contour[0], (255))
#
# #-- Smooth mask, then blur it --------------------------------------------------------
# #mask = cv2.dilate(mask, None, iterations=MASK_DILATE_ITER)
# mask = cv2.GaussianBlur(mask, (BLUR, BLUR), 0)
# #mask = cv2.erode(mask, None, iterations=MASK_ERODE_ITER)
#
# #-- Blend masked img into MASK_COLOR background --------------------------------------
# img         = img.astype('float32') / 255.0                 #  for easy blending
# #cv2.imwrite('mask.png', mask)
#
# c_red, c_green, c_blue = cv2.split(img)
# img_a = cv2.merge((c_red, c_green, c_blue, mask.astype('float32') / 255.0))
#
# cv2.imwrite(root_dir+"-out.jpg", img_a*255)