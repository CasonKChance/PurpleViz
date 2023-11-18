import cv2
import numpy as np

cap = cv2.VideoCapture(0)
morph = 2
font = cv2.FONT_HERSHEY_SIMPLEX
x1,y1, x2,y2 = 100,100, 400,400
h,w = y2-y1, x2-x1
xy1, xy2 = (x1,y1), (x2,y2)
while True:
    _,img = cap.read()
    cv2.rectangle(img, xy1, xy2, (123,234,123), 5)
    roi = img[y1:y2, x1:x2]
    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    gray = gray+gray
    _, thresh = cv2.threshold(gray, 65, 255, cv2.THRESH_BINARY)
    kernel = np.ones((morph, morph),np.uint8)
    thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.RETR_TREE) #change this to 'contours,_' for opencv2
    text = '# of particles: ' + str(len(contours))
    bg = np.zeros_like(img)
    cv2.putText(bg, text, (50,200), font, 1.72, (0,255,244), 3, cv2.LINE_AA)
    cv2.imshow('thresh', thresh)
    cv2.imshow('bg', bg)
    k = cv2.waitKey(1)
    if k ==27: break
cv2.destroyAllWindows()