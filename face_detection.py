import cv2
from constants import *

trained_face_data = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')


def detect_faces(source, content_path):
    if source == IMAGE:
        detect_faces_from_image(image_path=content_path)
    elif source == VIDEO:
        detect_faces_from_video(video_path=content_path)
    elif source == WEBCAM:
        detect_faces_from_webcam(stream_path=WEBCAM_PATH)
    else:
        raise NotImplemented


def detect_faces_from_image(image_path: str):
    image = cv2.imread(image_path)

    grayscaled_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    face_coordinates = trained_face_data.detectMultiScale(grayscaled_image)

    for x, y, w, h in face_coordinates:
        # print((x, y), (x+w, y+h))
        cv2.rectangle(image, (x, y), (x+w, y+h), STROKE_COLOR, STROKE_THICKNESS)

    cv2.imshow("Face Detector", image)

    DISPLAYING = True
    while DISPLAYING:
        key = cv2.waitKey(1)

        if key in (27, 81, 113):  # (Esc, Q, q) ascii codes
            cv2.destroyAllWindows()
            break


def detect_faces_from_video(video_path: str):
    video_capture = cv2.VideoCapture(video_path)

    while True:
        read, frame = video_capture.read()

        if read:
            grayscaled_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            face_coordinates = trained_face_data.detectMultiScale(grayscaled_frame)

            for x, y, w, h in face_coordinates:
                # print((x, y), (x+w, y+h))
                cv2.rectangle(frame, (x, y), (x+w, y+h), STROKE_COLOR, STROKE_THICKNESS)

            cv2.imshow("Face Detector", frame)
            key = cv2.waitKey(1)

            if key in (27, 81, 113):  # (Esc, Q, q) ascii codes
                cv2.destroyAllWindows()
                break


def detect_faces_from_webcam(stream_path=WEBCAM_PATH):
    return detect_faces_from_video(video_path=stream_path)  # 0 = default camera (built-in webcam)
