from flask import Flask, render_template, Response
from camStreaming import generateLocalVideo
from IPCamera import generateIpCameraVideo

import cv2

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('home/index.html')

@app.route("/video_local_stream")
def video_local_stream():
    return Response(generateLocalVideo(), mimetype="multipart/x-mixed-replace; boundary=frame")

@app.route("/video_ip_camera_stream")
def video_ip_camera_stream():
    return Response(generateIpCameraVideo(), mimetype="multipart/x-mixed-replace; boundary=frame")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')

