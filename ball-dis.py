import cv2
import numpy as np

#URL = "http://192.168.0.121:8080/?action=stream"

cap = cv2.VideoCapture(0)

while True:
        ret, frame = cap.read()

            
                blur1 = cv2.bilateralFilter(frame,20,75,75)
                    blur2 = cv2.bilateralFilter(blur1,15,75,75)
                        #blur3 = cv2.bilateralFilter(blur2,10,75,75)
                            #blur4 = cv2.bilateralFilter(blur3,9,75,75)
                                
                                    hsv = cv2.cvtColor(blur2, cv2.COLOR_BGR2HSV)

                                        lo_color = np.array([20, 20, 20])
                                            hi_color = np.array([40, 240, 240])
                                                mask = cv2.inRange(hsv,lo_color,hi_color)

                                                    median = cv2.medianBlur(mask,21)


                                                        #mask_color = cv2.cvtColor(median, cv2.COLOR_THRESHBINARY2GRAY)


                                                            blur = cv2.bilateralFilter(frame,10,75,75)

                                                                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                                                                    circles = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,100,param1=50,param2=50,minRadius=0,maxRadius=0)
                                                                        
                                                                            if len(circles) == None:
                                                                                        continue


                                                                                            circles = np.uint16(np.around(circles))
                                                                                                for i in circles[0,:]:
                                                                                                            # draw the outer circle
                                                                                                                    cv2.circle(frame,(i[0],i[1]),i[2],(0,255,0),2)
                                                                                                                            # draw the center of the circle
                                                                                                                                    cv2.circle(frame,(i[0],i[1]),2,(0,0,255),3)




                                                                                                                                        cv2.imshow("show frame!",frame)
                                                                                                                                            cv2.imshow("show blur!",blur2)
                                                                                                                                                cv2.imshow("show blur2!",median)
                                                                                                                                                    cv2.imshow("show mask!",mask)
                                                                                                                                                        #cv2.imshow("show gray!",gray)

                                                                                                                                                            k = cv2.waitKey(10)
                                                                                                                                                                if k == ord('q'):
                                                                                                                                                                            break

                                                                                                                                                                            cv2.destroyAllWindows()
                                                                                                                                                                            
