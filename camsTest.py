import cv2

def print_camera_info():
    # para buscar las camaras
    for i in range(10):
        #cap = cv2.VideoCapture(i, cv2.CAP_DSHOW)
        #cap = cv2.VideoCapture(i, cv2.CAP_MSMF)
        cap = cv2.VideoCapture(i, cv2.CAP_V4L2)
        if not cap.isOpened():
            print(f"No se pudo abrir la cámara con índice {i}")
        else:
            width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            fps = cap.get(cv2.CAP_PROP_FPS)
            print(f"Cámara {i}: {width}x{height}, FPS: {fps}")
            cap.release()

if __name__ == "__main__":
    print_camera_info()
