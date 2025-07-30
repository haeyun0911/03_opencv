import cv2
import numpy as np

def draw_histogram(image):
    hist = cv2.calcHist([image], [0], None, [256], [0,256])
    hist_img = np.full((300,256), 255, dtype=np.uint8)

    cv2.normalize(hist, hist, 0, 300, cv2.NORM_MINMAX)

    for x, y in enumerate(hist):
        cv2.line(hist_img, (x, 300), (x, 300-int(y)), 0)

    return hist_img

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
                cv2.imwrite('C:/Users/405/projects/opencv_tutorial/03_opencv/img/capture.jpg', gray_img)
                print('사진저장됨')

                hist_img = draw_histogram(gray_img)
                cv2.imshow('Histogram', hist_img)
        else:
            print('no frame')
            break

else:
    print("can't open camera.")

cap.release()
cv2.destroyAllWindows()
    