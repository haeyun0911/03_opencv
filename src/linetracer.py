import cv2
import numpy as np
import matplotlib.pylab as plt

cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
if cap .isOpened():
    while True:
        ret, img = cap.read()
        if ret:
            key = cv2.waitKey(1)
            gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            equal_img = cv2.equalizeHist(gray_img)
            cv2.imshow('Original Camera Feed', img)
            cv2.imshow('Equalized Histogram Feed', equal_img)
            if key == ord('q') or key == ord('Q'):
                break
            elif key  == ord('s') or key == ord('S'):
                cv2.imwrite('C:/Users/405/projects/opencv_tutorial/03_opencv/img/capture.jpg', img)
                print('사진저장됨')
        else:
            print('no frame')
            break

else:
    print("can't open camera.")

cap.release()
cv2.destroyAllWindows()
    