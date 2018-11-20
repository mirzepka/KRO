import numpy as np
import cv2
import matplotlib.pyplot as plt
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.resizeWindow('image', 800, 600)
#https://www.programcreek.com/python/example/89350/cv2.SimpleBlobDetector
img = cv2.imread('Data/water_coins.jpg',cv2.IMREAD_GRAYSCALE)

roi_size=(128, 128)
img = cv2.resize(img, roi_size)

blob_min_area=3
blob_min_int=.5
blob_max_int=.95
blob_th_step=10

params = cv2.SimpleBlobDetector_Params()
params.filterByArea = True
params.minArea = blob_min_area
params.maxArea = roi_size[0]*roi_size[1]
params.filterByCircularity = False
params.filterByColor = True
params.filterByConvexity = False
params.filterByInertia = False
# blob detection only works with "uint8" images.
params.minThreshold = int(blob_min_int*255)
params.maxThreshold = int(blob_max_int*255)
params.thresholdStep = blob_th_step
ver = (cv2.__version__).split('.')
    
if int(ver[0]) < 3:
    detector = cv2.SimpleBlobDetector(params)
else: 
    detector = cv2.SimpleBlobDetector_create(params)
     
# Detect blobs.
keypoints = detector.detect(img)
print(len(keypoints))
print(keypoints)
im_with_keypoints = cv2.drawKeypoints(img, keypoints, np.array([]),
            (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imwrite("blobs.jpg", im_with_keypoints); 
cv2.imshow('image',img)
cv2.waitKey(0)


cv2.destroyAllWindows()


