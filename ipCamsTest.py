import cv2

def testCamOne():
    cap = cv2.VideoCapture('http://192.168.0.50:8081', cv2.CAP_FFMPEG)
    face_detector = cv2.CascadeClassifier('./haarcascades/haarcascade_frontalface_default.xml')
    
    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("No se pudo obtener el frame. Finalizando.")
                break

            print("CONEXION ESTABLECIDA - HTTP")
            
            # Procesa el frame
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_detector.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

            # Muestra el frame
            cv2.imshow('HTTP Frame', frame)

            # Sale del bucle si se presiona la tecla 'q'
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            
    except Exception as e:
        print(f"Error en la transmisión HTTP: {str(e)}")
    finally:
        cap.release()
        cv2.destroyAllWindows()

def testCamTwo():
    cap = cv2.VideoCapture('rtsp://192.168.0.50:554/user=admin&password=&channel=1&stream=0.sdp?', cv2.CAP_FFMPEG)
    face_detector = cv2.CascadeClassifier('./haarcascades/haarcascade_frontalface_default.xml')
    
    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("No se pudo obtener el frame. Finalizando.")
                break

            print("CONEXION ESTABLECIDA - RTSP")
            
            # Procesa el frame
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_detector.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

            # Muestra el frame
            cv2.imshow('RTSP Frame', frame)

            # Sale del bucle si se presiona la tecla 'q'
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            
    except Exception as e:
        print(f"Error en la transmisión RTSP: {str(e)}")
    finally:
        cap.release()
        cv2.destroyAllWindows()

def testCam():
    testCamOne()
    testCamTwo()

if __name__ == "__main__":
    testCam()