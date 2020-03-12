import cv2

#URL = "http://62.30.204.115:1024/mjpg/video.mjpg?timestamp=1546777112630"
#URL = "http://192.168.0.113:8080/?action=stream"
#URL = "http://192.168.11.3:8080/?action=stream"
#URL = "http://2.2.2.1:81/stream"

URL = "rtsp://admin:123456@192.168.0.123/0/video1"
#URL = "rtsp://192.168.0.123/0/video1"

cap = cv2.VideoCapture(URL)

while True:
    ret, frame = cap.read()
    #frame = cv2.flip(frame,-1)
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #cany = cv2.Canny(gray, 100, 200)

    cv2.imshow("show image!", frame)
    #cv2.imshow("show gray!", gray)
    #cv2.imshow("show cany!", cany)

    k = cv2.waitKey(1)
    if k == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
