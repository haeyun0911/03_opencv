import cv2
import numpy as np
img = cv2.imread('../img/hand.jpg')
img2 = img.copy()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, th= cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

contours, hierarchy = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cntr = contours[0]
cv2.drawContours(img, [cntr], -1, (0,255,0), 1)
#print(len(contour), hierarchy)
#epsilon = 0.05*cv2.arcLength(contour, True)
#approx = cv2.approxPolyDP(contour, epsilon, True)
#contour2, hierarchy = cv2.findContours(imthres, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#print(len(contour2),hierarchy)
hull = cv2.convexHull(cntr)

#print('도형의 갯수: %d(%d)'% (len(contour), len(contour2)))

cv2.drawContours(img2, [hull], -1, (0,255,0), 1)
print(cv2.isContourConvex(cntr), cv2.isContourConvex(hull))

hull2 = cv2.convexHull(cntr, returnPoints=False)
defects = cv2.convexityDefects(cntr, hull2)

for i in range(defects.shape[0]):
    startP, endP, farthestP, distance = defects[i,0]
    farthest = tuple(cntr[farthestP][0])
    dist = distance/256.0
    if dist > 1:
        cv2.circle(img2,farthest, 3, (0,0,255), -1)

'''
for idx, cont in enumerate(contour2):
    color = [int(i) for i in np.random.randint(0,255,3)]
    cv2.drawContours(img2,contour2, idx, color, 3)
    cv2.putText(img2,str(idx), tuple(cont[0][0]),cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255))
'''
'''
for i in contour:
    for j in i:
        cv2.circle(img, tuple(j[0]), 1, (255,0,0), -1)

for i in contour2:
    for j in i:
        cv2.circle(img2, tuple(j[0]), 1, (255,0,0), -1)
'''
cv2.imshow('contour', img)
cv2.imshow('convex hull', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()