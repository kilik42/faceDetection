import cv2

# trainedFaceData = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#choose an image
#img = cv2.imread('Robert_Downey_Jr..jpg')
webcam = cv2.VideoCapture(0)

#iterate over frames
while True:

    #read the current frame
    successful_frame_read, frame = webcam.read()

# make it black and white or greyscale
    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    trainedFaceData = cv2.CascadeClassifier(grayscaled_img)

    cv2.imshow("first one", grayscaled_img)
    cv2.waitKey(1)
    
#detect faces
# face_coordinates = trainedFaceData.detectMultiScale(grayscaled_img)
#print(face_coordinates)

#draw rectangles around the faces
# (x,y,w,h) = face_coordinates[0]
# cv2.rectangle(img, (x, y), (x+w,y+h), (0,255,0), 2)


# cv2.imshow("first one", grayscaled_img)
# cv2.waitKey()