import cv2
import numpy as np

#opencv로 히스토그램 출력 코드
def draw_histogram(image):
    hist = cv2.calcHist([image], [0], None, [256], [0,256])
    hist_img = np.full((300,256), 255, dtype=np.uint8)

    cv2.normalize(hist, hist, 0, 300, cv2.NORM_MINMAX)

    for a, b in enumerate(hist):
        cv2.line(hist_img, (a, 300), (a, 300-int(b)), 0)

    return hist_img

cap = cv2.VideoCapture(0)
# 캠 창 크기 
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
#ROI 좌표 설정
x, y, w, h = 0, 0, 640, 320

if cap.isOpened():
    while True:
        ret, img = cap.read()
        if not ret:
            print('no frame')
            break

        key = cv2.waitKey(1)

        # 평탄화된 영상
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        equal_img = cv2.equalizeHist(gray_img)
        equal_color = cv2.cvtColor(equal_img, cv2.COLOR_GRAY2BGR)

        # ROI 설정
        roi = equal_img[y:y+h, x:x+w]

        # 컨투어 검출
        _, th = cv2.threshold(roi, 127, 255, cv2.THRESH_BINARY_INV)
        contours, _ = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if contours:
            contour = max(contours, key=cv2.contourArea)  # 가장 큰 컨투어 사용
            epsilon = 0.05 * cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, epsilon, True)
            approx += np.array([[x, y]])  # ROI 기준 → 전체 이미지 기준으로 보정

            # 컨투어 그리기 (equal_color에)
            cv2.drawContours(equal_color, [approx], -1, (0, 255, 0), 2)

        # ROI 사각형 그리기
        cv2.rectangle(equal_color, (x, y), (x + w, y + h), (0, 0, 255), 2)

        # 최종 출력
        cv2.imshow('Equalized with ROI and Contour', equal_color)
        
        # q키 입력시 종료
        if key == ord('q') or key == ord('Q'):
            break
        
        # s키 입력시 캡쳐
        elif key == ord('s') or key == ord('S'):
            roi_gray = gray_img[y:y+h, x:x+w]
            cv2.imwrite('C:/Users/405/projects/opencv_tutorial/03_opencv/img/capture.jpg', roi_gray)
            print('사진저장됨')

            hist_img = draw_histogram(roi_gray)
            cv2.imshow('Histogram', hist_img)

else:
    print("can't open camera.")

cap.release()
cv2.destroyAllWindows()
