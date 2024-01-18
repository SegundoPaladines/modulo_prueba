import cv2

def generateLocalVideo():
    cap = cv2.VideoCapture(0, cv2.CAP_V4L2)
    face_detector = cv2.CascadeClassifier('./haarcascades/haarcascade_frontalface_default.xml')
    try:
        while True:
            ret, frame = cap.read()
            if ret:
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = face_detector.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
                for (x, y, w, h) in faces:
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                    
                (flag, encoded_image) = cv2.imencode(".jpg", frame)
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + 
                       bytearray(encoded_image) + b'\r\n'
                )
                if not flag:
                    continue
                
            else:
                print("No se puede obteber el frame de la camara.")
                
    except Exception as e:
        print(f"error al obteber el frame: {str(e)}")
    finally:
        cap.release()