import cv2
import os

def generateIpCameraVideo():
    ## parametros para acceso al streaming
    USR = 'admin'
    PASSWD = 'admin'
    IPADD = 'http://220.254.72.200'
    PORT = '554'

    os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"] = "rtsp_transport;udp"

    URL = 'rtsp://{}:{}@{}:{}/onvif1'.format(USR, PASSWD, IPADD, PORT)
    
    cap = cv2.VideoCapture(URL, cv2.CAP_FFMPEG)
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
                print("no se puede obtener conexion con la camara.")
                
    except Exception as e:
        print(f"error al obtener el frame: {str(e)}")
    finally:
        cap.release()
