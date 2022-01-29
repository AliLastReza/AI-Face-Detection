import os


WELCOME_MESSAGE = """Hey, Welcome to Face Detection App 1.0"""

MENU_TEXT = """\nSelect SOURCE of face detection from menu:
1. Image
2. Video
3. Webcam
0. Exit
"""

IMAGE = 'image'
VIDEO = 'video'
WEBCAM = 'webcame'
EXIT = 'Exit'

SOURCES = {
    '1': IMAGE,
    '2': VIDEO,
    '3': WEBCAM,
    '0': EXIT
}

WEBCAM_PATH = 0

ASK_CONTENT_PATH_TEXT = """\nPlease enter relative or absolute path of {content_type}, or press
Enter to use sample data.
{content_type} path (press Enter to use sample data): """

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

IMAGE_SAMPLE_CONTENT = 'sample_data/image1.png'
VIDEO_SAMPLE_CONTENT = 'sample_data/video1.mp4'

BEFORE_PREVIEW_TEXT = """\nIn few seconds you will see the preview.
Press Esc to exit."""

FIRST_TIME_PREVIEWING = True

STROKE_THICKNESS = 3
STROKE_COLOR = (255, 0, 0)  # Blue
