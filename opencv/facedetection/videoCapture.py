import cv2, time
video = cv2.VideoCapture(0)#accessing first web cam
numOfFrames=0
while True:
    numOfFrames=numOfFrames+1
    check, frame = video.read()
    print(check)
    print(frame)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #time.sleep(3)
    cv2.imshow("Capturing",gray)
    key = cv2.waitKey(1)
    if key==ord('q'):
       break

print("Num of frames captured " ,numOfFrames)
video.release()
cv2.destroyAllWindows()
