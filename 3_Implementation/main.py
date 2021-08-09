# import libraries
import cv2
# import classifier which is proposed by viola-Jones for Face Detection
classify = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
name = input()
# Webcam capture for Detecting the face
photo = cv2.VideoCapture(0)
i = 0
# window = Tk()
while photo.isOpened():
    ret, image = photo.read()
    # Convert a Image to GrayScale to detect faces easily in a grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    face = classify.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    # given the coordinates of which makes a rectangle box in the image/frame to show the location of face
    for (a, b, c, d) in face:
        cv2.rectangle(image, (a, b), (a + c, b + d), (0, 255, 0),
                      2)  # a,b are coordinates and c is height, d is width
    if ret == True:
        cv2.imshow("'Face Detection using Webcam'  - 'Press e to capture the image' ", image)
    for i in range(1):
        cv2.imwrite(name + '.jpg', image)
    if cv2.waitKey(20) & 0xff == ord('e'):
        break
if len(face) >= 1:
    print("Face Count = {0}".format(len(face)))
    print("Faces Found")
else:
    print("No face found")
photo.release()
cv2.destroyAllWindows()
