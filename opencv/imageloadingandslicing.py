import cv2 as cv
img = cv.imread("galaxy.jpg")
print(img)
print(img.ndim)
print(img.shape)
print(type(img))


resized_img = cv.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
cv.imshow("Galaxy",resized_img)
cv.imwrite("Resized_img.jpg",resized_img)
cv.waitKey(0)
cv.destroyAllWindows()
