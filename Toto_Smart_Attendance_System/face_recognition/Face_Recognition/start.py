from .Video_to_Image_Split import extraction
from .face_recognition import choice


def start_training():
    extraction.start_training()
    # ML Training module call with choice 2
    choice(2)
    choice(3)
