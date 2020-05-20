import cv2
img = cv2.imread("b.jpg")
grey_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#changing to gray img
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
faces=face_cascade.detectMultiScale(grey_img,
scaleFactor = 1.05,
minNeighbors = 5)
print(type(faces))
print(faces)
for x,y,w,h in faces:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)#rbg for 0,255,0 3 = width
resized = cv2.resize(img,(int(img.shape[1]/3),int(img.shape[0]/2)))
cv2.imshow("photo",resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
