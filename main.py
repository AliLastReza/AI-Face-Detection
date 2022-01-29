import os
from time import sleep
from face_detection import *


def get_content_path(content_type: str):
    content_path = input(ASK_CONTENT_PATH_TEXT.format(content_type=content_type))

    if content_path == '':
        if content_type == IMAGE:
            content_path = IMAGE_SAMPLE_CONTENT
        elif content_type == VIDEO:
            content_path = VIDEO_SAMPLE_CONTENT
        else:
            raise NotImplemented
        return content_path

    abs_path_exists = os.path.exists(content_path)
    if not abs_path_exists:
        rel_path_exists = os.path.exists(os.path.join(BASE_DIR, content_path))
        if rel_path_exists:
            content_path = os.path.join(BASE_DIR, content_path)
        else:
            print("\nFile does not exists. Please enter a valid file path.")
            get_content_path(content_type)

    return content_path


def main():
    global FIRST_TIME_PREVIEWING

    print(WELCOME_MESSAGE)

    USING_THE_APP = True
    while USING_THE_APP:
        print(MENU_TEXT)

        source = input("source: ")
        if source not in SOURCES:
            print(f"""\n"{source}" is not in sources. Please select one of the sources (1, 2, 3).""")
            continue

        source_value = SOURCES[source]

        if source_value == EXIT:
            break

        if source_value in (IMAGE, VIDEO):
            content_path = get_content_path(source_value)
        elif source_value == WEBCAM:
            content_path = 0
        else:
            raise NotImplemented

        print(BEFORE_PREVIEW_TEXT)
        if FIRST_TIME_PREVIEWING:
            sleep(4)
            FIRST_TIME_PREVIEWING = False

        detect_faces(source=source_value, content_path=content_path)


if __name__ == "__main__":
    main()
