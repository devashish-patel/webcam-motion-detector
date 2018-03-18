import cv2, pandas as pd
from datetime import datetime
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


# Start Video Capture
video = cv2.VideoCapture(0)

# initialize first frame
first_frame = None

status_list = [None, None]
time = []
df = pd.DataFrame(columns=["Start", "End"])

while True:

    # read the image
    capture, frame = video.read()

    # to identify status of the object
    status = 0

    # convert to Gray frame
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Convert a Gray frame into Gaussian Blur to reduce noise and improve accuracy
    gray_frame = cv2.GaussianBlur(gray_frame, (21, 21), 0)

    if first_frame is None:
        first_frame = gray_frame
        continue

    # delta frame - to compare current situation with initial situation
    delta_frame = abs(first_frame - gray_frame)

    # threshold frame - to identify object
    threshold_frame = cv2.threshold(delta_frame, 177, 255, cv2.THRESH_BINARY)[1]
    # make threshold frame smoother to remove black holes
    threshold_frame = cv2.dilate(threshold_frame, None, iterations=3)

    # find contours ( to detect the object)
    (_,cnts,_) = cv2.findContours(threshold_frame.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in cnts:
        if cv2.contourArea(contour) < 10000:
            continue
        status = 1
        (xc, yc, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (xc, yc), (xc + w, yc + h), (0, 230, 0), 3)

    # append the status after each iteration
    status_list.append(status)

    # check last two status and if it's a change then add timing
    if status_list[-1] == 1 and status_list[-2] == 0: # 0 -> 1
        time.append(datetime.now())
    elif status_list[-1] == 0 and status_list[-2] == 1: # 1 -> 0
        time.append(datetime.now())

    # show color frame (To show all objects)
    color_resize = cv2.resize(frame, (frame.shape[1] // 4, frame.shape[0] // 4))
    cv2.imshow("Color Frame", color_resize)

    # show threshold frame (To identify object)
    threshold_resize = cv2.resize(threshold_frame, (threshold_frame.shape[1] // 4, threshold_frame.shape[0] // 4))
    cv2.imshow("Throshold Frame", threshold_resize)

    # show delta frame video (to check difference)
    # Detect faces
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5)
    for (x, y, w, h) in faces:
        cv2.rectangle(gray_frame, (x, y), (x + w, y + h), (0, 230, 0), 3)
    # resize the video
    delta_resize = cv2.resize(delta_frame, (delta_frame.shape[1]//4, delta_frame.shape[0]//4))
    cv2.imshow("Delta Frame", delta_resize)

    # show current frame video ( For face detection)
    current_resize = cv2.resize(gray_frame, (gray_frame.shape[1] // 4, gray_frame.shape[0] // 4))
    cv2.imshow("Current Frame", current_resize)

    key = cv2.waitKey(1)
    # press 'q' to exit the window
    if key == ord('q'):
        if status == 1:
            time.append(datetime.now())
        break


for cur_time in (0, len(time), 2):
    df = df.append({"Start": time[cur_time], "End": time[cur_time+1]}, ignore_index=True)

df.to_csv("Time.csv")
# Stop Video Capture
video.release()
cv2.destroyAllWindows()
