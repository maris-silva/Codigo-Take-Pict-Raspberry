from time import time
import requests
import cv2
import base64
import datetime

# Create a new VideoCapture object
cam = cv2.VideoCapture(0)

# Initialise variables to store current time difference as well as previous time call value
previous = time()
delta = 0

while True:
# Get the current time, increase delta and update the previous variable
    current = time()
    delta += current - previous
    previous = current
    if delta > 1:
        # Reset the time counter
        delta = 0

        _, img = cam.read()
        _, jpeg = cv2.imencode(".jpeg", img)
        image_data = jpeg.tobytes()
        image_b64 = base64.b64encode(image_data).decode("utf-8")
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        filename = "image_{}.jpg".format(timestamp)

        response = requests.post("https://dedoduro.com.br/api/upload/1", data={"image": image_b64, "name": filename})
        print(response)
        cv2.waitKey(1)
