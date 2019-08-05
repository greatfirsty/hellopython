import cv2
cv2.namedWindow('Image')

aa = cv2.VideoCapture(0)
while (aa.isOpened):
    ret, img = aa.read()
    if ret == True:
        cv2.imshow('Image',img)
        k = cv2.waitKey(100)
        if k == ord('a') or k ==ord('A'):
            cv2.imwrite('test.jpg',img)
            break
aa.close()
cv2.waitKey(0)
cv2.destryAllWindow()

