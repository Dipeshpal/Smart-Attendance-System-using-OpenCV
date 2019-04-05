from .Video_to_Image_Split import extraction, rotate
from .face_recognition import choice


def start_training():
    # create Dataset
    extraction.start_creating_dataset()

    # Create / Rotate images in image dataset
    rotate.rotate()

    # ML Training module call with choice 2
    choice(2)

    # Check Image
    choice(3)
