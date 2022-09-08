import cv2

frame = cv2.imread("x1.jpeg")

#convert image to grayscale
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#get image to binary and remove noise
ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)
#find contours
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#save image with the first contour
cv2.drawContours(frame, contours, 0, (0, 255, 0), 3)
cv2.imwrite("x3.jpeg", frame)
#draw contours
cv2.drawContours(frame, contours, -1, (0, 255, 0), 2)
# #save image

cv2.imwrite("x.jpeg", frame)
cv2.imshow("frame", frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)
#closes window when any key is pressed
print("ASd")

