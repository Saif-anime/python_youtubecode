import cv2

def detect_eyes(image):
    eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    eyes = eye_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    for (x, y, w, h) in eyes:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    return image

image = cv2.imread('example_image.jpg')
detected_eyes_image = detect_eyes(image)
cv2.imshow('Detected eyes', detected_eyes_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
