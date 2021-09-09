import cv2

# Reading the Image
image = cv2.imread('pedestrian1.jpg')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)    

Haar = cv2.CascadeClassifier('haarcascade_fullbody.xml')
bodies = Haar.detectMultiScale(
        gray,
        scaleFactor=1.02,
        minNeighbors=3,
        minSize=(25, 25),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
   
         
   
#padding=(4, 4),   
# Drawing the regions in the Image
for (x, y, w, h) in bodies:
    cv2.rectangle(image, (x, y), 
                  (x + w, y + h), 
                  (0, 0, 255), 2)
  
# Showing the output Image
cv2.imshow("Image", image)
cv2.waitKey(0)
   
cv2.destroyAllWindows()