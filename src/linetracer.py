import cv2
import numpy as np

def draw_histogram(image):
    hist = cv2.calcHist([image], [0], None, [256], [0,256])
    hist_img = np.full((300,256), 255, dtype=np.uint8)

    cv2.normalize(hist, hist, 0, 300, cv2.NORM_MINMAX)

    for a, b in enumerate(hist):
        cv2.line(hist_img, (a, 300), (a, 300-int(b)), 0)

    return hist_img

cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
x=0; y= 0; w=640; h = 320
if cap .isOpened():
    while True:
        ret, img = cap.read()

        if ret:
            key = cv2.waitKey(1)
            img2 = img.copy()
            gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            thresh_val, th=cv2.threshold(gray_img, 127, 255, cv2.THRESH_BINARY)
            equal_img = cv2.equalizeHist(gray_img)

            contours, hierarchy = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            if contours:
                contour = contours[0]
                epsilon = 0.05*cv2.arcLength(contour, True)
                approx = cv2.approxPolyDP(contour, epsilon, True)

                cv2.drawContours(img2, [approx], -1, (0,0,255), 2)


            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

            cv2.imshow('Original Camera Feed', img)
            cv2.imshow('Equalized Histogram Feed', equal_img)
            cv2.imshow('Approximation', img2)
            if key == ord('q') or key == ord('Q'):
                break
            elif key  == ord('s') or key == ord('S'):
                roi_gray=gray_img[y:y+h, x:x+w]
                cv2.imwrite('C:/Users/405/projects/opencv_tutorial/03_opencv/img/capture.jpg', roi_gray)
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
    