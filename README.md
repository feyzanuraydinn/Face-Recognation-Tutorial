# Face Recognition Tutorial using OpenCV

## Introduction

Face recognition, a remarkable application of computer vision and machine learning, has gained significant attention in recent years. This technology enables computers to identify and verify individuals by analyzing their facial features. From unlocking smartphones to enhancing security systems, and even assisting law enforcement agencies, face recognition has a broad range of practical applications.

In this tutorial, we will delve into the world of face recognition using the power of Python and OpenCV. By the end of this tutorial, you will have a solid understanding of how to build a basic face recognition system that can detect and recognize faces in real-time video streams. 

## Installation

You'll need a working installation of Python to run the code examples and scripts. The code in this tutorial is written in Python 3.11.4.
Install required libraries using pip:
```
pip install -r requirements.txt
```
## Data Collection

In order to build a robust face recognition system, you'll need a dataset of faces to train and test your model. One way to create this dataset is by collecting images using your computer's camera. Let's walk through the process:

**1. Set Up a Data Collection Directory**

Create a directory named 'images' in the location where your project is located to store the images you will collect.


**2. Capture Images**

Write a Python script that captures images using your computer's camera. We will use the OpenCV library to access the camera feed and save images. The script will allow you to specify the person's name and the number of images to capture. 

To gather data using this method, execute the 'datacollect.py' script.

In summary, this code snippet prompts you to enter your name, captures 500 images using your computer's camera, and stores these images in a new directory named after the name you entered. Each captured image with a detected face will be saved within this directory. This dataset will be useful for training your face recognition model.

You can also add additional data by creating a folder with the person's name inside the "images" directory and placing their photos there.

**3. Train Your Model**

Write a script  that captures a dataset of facial images intended for training a face recognition model. It begins by importing the required libraries for image processing and recognition purposes. The code initializes the Local Binary Pattern (LBP) face recognition algorithm, a technique known for its effectiveness in capturing facial features. Images are systematically captured and systematically organized, each within dedicated folders named after the respective individuals' names. By establishing a mapping between names and unique identification numbers, the collected images and associated IDs are utilized to train the recognizer. The resultant trained model is then saved for later use, enhancing the system's capability to accurately identify individuals based on their distinctive facial characteristics. This comprehensive process substantially contributes to the reliability and precision of the facial recognition mechanism.

To train the model using this method, run 'train.py'.

## Testing The Trained Model

To put your trained model to the test, simply run 'test.py'. This code will enable your computer's camera to perform real-time face recognition using the trained model.

Running this code will open a window showing your computer's camera feed with real-time face recognition results overlaid on the video stream. Faces will be identified along with the probability of the predictions. To exit the program, press the 'q' key.

By executing this code, you'll witness your model in action, recognizing faces as you present them to the camera. This step is crucial to ensure your model's accuracy and readiness for practical applications.

## References
Key reference that contributed to the development of this tutorial is a YouTube video that provides valuable insights into face recognition using Python, OpenCV, and TensorFlow. I recommend checking out the following video:

URL: [Face Recognition Using Python, Keras, OpenCV & Tensorflow| Recognize Face in Real-time Video Streams](https://www.youtube.com/watch?v=lH01BgsIPuE)