import cv2
face_cascade = cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('cascades/haarcascade_eye.xml')
camera = cv2.VideoCapture(0)

while(True):
    ret, frame = camera.read()
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:#could be many faces
            img = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]#my eyes are in my face
            eyes = eye_cascade.detectMultiScale(roi_gray, 1.03, 5,0,(40,40))
            for (ex, ey, ew, eh) in eyes[:2]:#twice for two eyes normally
                cv2.rectangle(frame,(ex+x,ey+y),(x+ex+ew,y+ey+eh),(0,255,0),2)
        cv2.imshow('detected!',frame)
        if cv2.waitKey(100) & 0xff == ord('q') :
            break
camera.release()
cv2.destroyAllWindows()
