# Face-Recognition

Face Recognition using OpenCV and Machine Learining

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

I am using [miniconda](https://conda.io/en/latest/miniconda.html) and [Python 3.6.6](https://www.python.org/). Make sure you have miniconda /  anaconda or Python installed.
Recommended Prerequisites- 
* Miniconda or
* Python 3.x

I have following Python library  installed on miniconda-

* matplotlib==3.0.2
* numpy==1.14.5
* opencv-contrib-python==4.0.0.21
* opencv-python==3.4.0.14
* scikit-learn==0.20.2
* scipy==1.1.0
* tensorboard==1.10.0
* tensorflow==1.10.0

You can install all these with "requirements.txt" file.
Just Run following command in terminal-

```
pip install -r requirements.txt
```

### How to use all these file and what these files are?
Project contain following folders and files-
```
Face_Recognition
  cascades-|
           |-haarcascade_frontalface_default.xml
  dataset-|
          |- Training dataset will automatically genrate here
  image_dataset-|
                |- Here you need create some folder and put related images to that folder.
  model-|
        |- Your model will genrated once you trained your model
  venv-|
       |- Files related to your virtual environment
  Video-to-Image-Split-|
                              |- Instruction.txt (Read this to genrate image dataset)
                              |- split.py
    check_face.py
    create_dataset.py
    face_recognition.py
    requirements.txt
    test.py
    train.py
```
#### Explaination

01. cascades: It is the folder which contain ["haarcascade_frontalface_default.xml"](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml)

02. dataset: Training dataset will automatically genrate here. You will have following files-
    ```
    * features_dataset.npy: Features of all images
    * label_dataset.npy: Labels of all images
    * features_dataset_train.npy: Features of training dataset (After training)
    * label_dataset_train.npy: Labels of training dataset (After training)
    * x_train: Features of training dataset (After Dataset Spliting)
    * y_train: Labels of training dataset (After Dataset Spliting)
    * x_test: Features of testing dataset (After Dataset Spliting)
    * y_test: Labels of testing dataset (After Dataset Spliting)
    ```
            
03. image_dataset: Here you need create some folder and put related images to that folder.
 
04. model: Your model will genrated once you trained your model
 
05. venv: Files related to your virtual environment
 
06. Video-to-Image-Split-master: You can create dataset for training with this module. Read instruction to use it.
 
07. check_face.py: It will check "capture_image.jpg" (If face is found and belongs to trained image dataset then it will show result". You need to put "capture_image.jpg" in "Face_Recognition" folder ti check model.
 
08. create_dataset.py: It will create dataset for all images and split whole dataset into training and testing set.
 
09. face_recognition.py: This is the main file which run other files and function. It will create dataset, train model, test model and also check image.
 
 10. test.py: It will test the test dataset and find accuracy after testing.
 
 11. train.py: It will train model with train dataset.
 
 12. requirements.txt: Requirements for this projects.
 
 
## How to use-
1. First download this [repository](https://github.com/Dipeshpal/OpenCV-Face-Recognition).

2. Now you need to create dataset, you can create dataset very easily. Read and follow following instruction-
   - Create a video of your face upto 30-60 seconds long.
   - Put that video file in "Video-to-Image-Split-master" folder.
   - Run "split.py"
   ```
   python split.py
   ```
     - Enter folder name you want to create
     - Enter your video file name
    It will now create Folder in "Video-to-Image-Split-master" directory containing images. This script will capture frames from video and save those frames in Folder.

3. Now copy these folder and paste it on 'images_dataset" directory in "Face_Recognition" project.

4. Activate virtual environment for this project. Open command prompt in "Face_Recogintiion" folder (project root directory) and type followning in command prompt.
   ```
   venv\Scripts\activate
   ```

5. Then Run following command to install all python library.
   ```
   pip install -r requirements.txt
   ```

6. Now run "face_recognition.py". Type following command
   ```
   python face_recognition.py
   ```
This will do all the things for you. It will use images in "images_dataset" directory to create dataset (dataset of image with features and labels, train and test dataset with features and labels). Then it will now train the model with train dataset and create model then test the model with test dataset also find accuracy and check "capture_image.jpg" with trained model.
