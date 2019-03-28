import os
import numpy as np
from sklearn import tree, model_selection
from sklearn.metrics import accuracy_score
import test
import check_face
import train
import create_dataset
from sklearn.externals import joblib


# Find current face_train.py directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# From base directory find images_data-set directory
image_dir = os.path.join(BASE_DIR, "images_dataset")


def create_numpy_dataset():
    """
    It will create numpy data-set
    It will scan all images and convert into numpy array and
    split into training and testing data-set
    :return: x_train, x_test, y_train, y_test
    """
    print("Creating Data-set")
    features_dataset, label_dataset = create_dataset.create_dataset()

    np.save("dataset/features_dataset.npy", features_dataset)
    np.save("dataset/label_dataset.npy", label_dataset)

    # loaded_features_dataset = np.load('features_dataset.npy')
    # loaded_label_dataset = np.load('label_dataset.npy')

    print("Data Splitting-")
    x_train, x_test, y_train, y_test =  model_selection.train_test_split(features_dataset, label_dataset, test_size = 0.5)
    np.save("dataset/x_train.npy", x_train)
    np.save("dataset/x_test.npy", x_test)
    np.save("dataset/y_train.npy", y_train)
    np.save("dataset/y_test.npy", y_test)
    print("Data-set split into: x_train, x_test, y_train, y_test")
    return x_train, x_test, y_train, y_test


def training_dataset():
    """
    It will use x_train and y_labels to train network
    :return: It will create features_dataset_train.npy and label_dataset_train.npy
    """
    x_train = np.load('dataset/x_train.npy')
    y_train = np.load('dataset/y_train.npy')
    print("Training")
    features_dataset_train, label_dataset_train = train.training(x_train, y_train)

    # saving training data-set
    print("Saving training data-set")
    np.save("dataset/features_dataset_train.npy", features_dataset_train)
    np.save("dataset/label_dataset_train.npy", label_dataset_train)
    print("#### Training data-set saved ####")


def testing_dataset(clf):
    """
    It will use testing data-set (x_test, y_test) and clf (classifire)
    :param clf:
    :return: accuracy
    """
    x_test = np.load('dataset/x_test.npy')
    y_test = np.load('dataset/y_test.npy')
    print("Testing")
    features_dataset_test, label_dataset_test = test.testing(x_test, y_test)
    predictions = clf.predict(features_dataset_test)
    acc = accuracy_score(label_dataset_test, predictions)
    print("Accuracy in testing: ", acc)


def fit_classifire():
    """
    It will create classifire with the help of "features_dataset_train.npy", "labels_dataset_train.npy"
    :return: clf (classifire)
    """
    # loading training data-set
    print("Loading training dataset")
    features_dataset_train = np.load('dataset/features_dataset_train.npy')
    label_dataset_train = np.load('dataset/label_dataset_train.npy')

    # using Classifire on training data-set
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(features_dataset_train, label_dataset_train)
    filename = 'model/finalized_model.sav'
    joblib.dump(clf, filename)
    return clf


print("Press 1 for RUN model (automatically detect if previous model present)")
print("Press 2 for create new model (overwrite existing model)")
print("Press 3 for check your image")
choice = int(input("Enter your choice: "))

flag = 0

try:
    if choice == 1:
        try:
            read_model = 'model/finalized_model.sav'
            clf = joblib.load(read_model)
            flag = 1
        except:
            print("No previous training model found, Let's create new model")


        if flag == 1:
            print("Checking Capture Image")
            check_face.check(clf)
        else:
            x_train, x_test, y_train, y_test = create_numpy_dataset()

            training_dataset()

            clf = fit_classifire()

            testing_dataset(clf)
    elif choice == 2:
        x_train, x_test, y_train, y_test = create_numpy_dataset()

        training_dataset()

        clf = fit_classifire()

        testing_dataset(clf)
        print("New model created successfully, now check your image (choose choice=3)")
    elif choice == 3:
        try:
            read_model = 'model/finalized_model.sav'
            clf = joblib.load(read_model)
            flag = 1
        except:
            print("No previous training model found, Let's create new model")

            x_train, x_test, y_train, y_test = create_numpy_dataset()

            training_dataset()

            clf = fit_classifire()

            testing_dataset(clf)
            print("New model created successfully, now check your image (choose choice=3)")
        else:
            read_model = 'model/finalized_model.sav'
            clf = joblib.load(read_model)
            print("Checking Capture Image")
            check_face.check(clf)
except:
    print("Invalid input try again")
