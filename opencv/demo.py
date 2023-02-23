import cv2 #导入包

img=cv2.imread('../images/img2.jpg')
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.imwrite('shifan.jpg',img)
cv2.destroyAllWindows()