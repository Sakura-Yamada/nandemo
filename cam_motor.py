import cv2
import numpy as np

URL = "http://192.168.0.121:8080/?action=stream" 
#URL = "http://192.168.0.121:8080/?action=stream"
#URL = 0
cap = cv2.VideoCapture(URL)

while True:
    #画像読み込み
    ret,frame = cap.read()
    
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lo_color = np.array([40,50,50])
    hi_color = np.array([70,200,200])
    
    mask = cv2.inRange(hsv,lo_color,hi_color)
    
    contours, hierarchy = cv2.findContours(mask,1,2)

    if len(contours) == 0:
        continue

    area_list = [cv2.contourArea(cnt) for cnt in contours]
    big_index = np.argmax(area_list)
    big_area = contours[big_index]

    M = cv2.moments(big_area)

    try:
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
    except ZeroDivisionError:
        continue

    if cx >= 213 & cx <= 426 :
        print("中心")
        print(cx)
    if cx < 213 :
        print("左")
        print(cx)
    if cx > 426 :
        print("右")
        print(cx)

    cv2.circle(frame,(cx,cy),5,(255,0,0),-1)


    only_color = cv2.bitwise_and(frame,frame,mask=mask)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    canny = cv2.Canny(gray,100,200)

    ret,binary = cv2.threshold(gray,100,255,cv2.THRESH_BINARY)

    cv2.imshow("show image",frame)
#    cv2.imshow("show gray",gray)
#    cv2.imshow("show binary",binary)
    cv2.imshow("show mask",mask)
#    cv2.imshow("show only_color",only_color)
#    cv2.imshow("show cany",canny)


    k = cv2.waitKey(1)
    if k == ord('q'):
        break

cv2.destroyAllWindows















