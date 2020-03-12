import cv2
import numpy as np

    #カメラの指定
URL = "http://192.168.0.121:8080/?action=stream" 

#カメラから画像を取得
cap = cv2.VideoCapture(URL)

#画像を動画として処理
while 1:
    #取得した画像を読み込む
    ret,frame = cap.read()
    
    #HSV色空間に変換
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    #色の閾値の設定
    lo_color = np.array([40,50,50])
    hi_color = np.array([70,200,200])

    #特定の色だけを認識
    mask = cv2.inRange(hsv,lo_color,hi_color)
   
    #輪郭の検出
    contours,hierarchy = cv2.findContours(mask,1,2)

    if len(contours) == 0:
        continue


    #エリアの面積を取得
    area_list = [cv2.contourArea(cnt) for cnt in contours]

    #エリアの中で最も大きい面積を選択
    big_index = np.argmax(area_list)

    #
    big_area = contours[big_index]    

    #
    M = cv2.moments(big_area)

    #領域の重心を求める
    try:
        cx = int(M['m10'] / M['m00'])
        cy = int(M['m01'] / M['m00'])
    except ZeroDivisionError:
        continue

    
    R = 50
    L = 550

    if cx >= R & cx <= L :
        print("中心")
        print(cx)
    if cx < R :
        print("左")
        print(cx)
    if cx > L :
        print("右")
        print(cx)

     #重心を画像にプロットする
    cv2.circle(frame,(cx,cy),5,(0,0,255),-1)

    #画像を表示
 #   cv2.imshow("show frame",frame)
 #   cv2.imshow("show mask",mask)

    #終了するためのキーを設定
    k = cv2.waitKey(1)
    if k == ord('q'):
        break

#すべてのウィンドウを閉じる
#cv2.destroyAllWindows

