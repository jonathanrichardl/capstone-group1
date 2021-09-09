import cv2

vid = cv2.VideoCapture(0)
#ambil video dari webcam
while (True):

    # Capture the video frame
    # by frame
    ret, frame = vid.read()
    #read frame dari webcamnya, ret boolean, ke read atau engga, frame gambarnya.
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #konversi warna ke grayscale biar lebih gampang di detect.
    # Display the resulting frame
    clas = cv2.CascadeClassifier('face/FaceDetect-master/haarcascade_frontalface_default.xml')
    #buat cascade classifier pake classifier .xml yang sudah dibuat (parameter)
    faces = clas.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )#detect, caleFactor	Parameter specifying how much the image size is reduced at each image scale.
    #minSize	Minimum possible object size. Objects smaller than that are ignored.
    #flags	Parameter with the same meaning for an old cascade as in the function cvHaarDetectObjects. It is not used for a new cascade.
    #returns list of rectangles
    print("Found {0} faces!".format(len(faces)))
    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        #image, start value(x,y), end value(x,y), color.
    cv2.imshow("Faces found", frame)
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()
