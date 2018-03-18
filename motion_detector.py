import cv2
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


# Start Video Capture
video = cv2.VideoCapture(0)

# initialize first frame
first_frame = None

while True:

    # read the image
    capture, frame = video.read()

    # convert to Gray frame
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Convert a Gray frame into Gaussian Blur to reduce noise and improve accuracy
    gray_frame = cv2.GaussianBlur(gray_frame, (21, 21), 0)

    if first_frame is None:
        first_frame = gray_frame
        continue

    # delta frame - to compare current situation with initial situation
    delta_frame = abs(first_frame - gray_frame)
    print(delta_frame)

    # show current frame video
     # Detect faces
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5)

    for (x, y, w, h) in faces:
        cv2.rectangle(gray_frame, (x, y), (x + w, y + h), (0, 230, 0), 3)

    current_resize = cv2.resize(gray_frame, (gray_frame.shape[1]//2, gray_frame.shape[0]//2))
    cv2.imshow("Current Frame", current_resize)

    # show delta frame video
    # resize the video
    delta_resize = cv2.resize(delta_frame, (delta_frame.shape[1]//3, delta_frame.shape[0]//3))
    cv2.imshow("Delta Frame", delta_resize)

    key = cv2.waitKey(1)

    # press 'q' to exit the window
    if key == ord('q'):
        break


# Stop Video Capture
video.release()
cv2.destroyAllWindows()
