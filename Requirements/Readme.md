# Requirements

## Introduction

-   Biometrics are a way to measure a person’s physical characteristics to verify their identity.
-   Face detection is used to detect the faces in the images or live video.
-   It is a part of Object Detection.
-   It is used to detect the faces in real time for surveillance and tracking of a person or objects.

## Research

-   In the past few years face recognition, appreciated as one of the most promising applications in the field of image analysis. 
-   Object detection is one of the computer technologies, which connected to the image processing and computer vision and it interacts with detecting instances of an object such     as human faces, building, tree, car, etc. 
-   The primary aim of face detection is to determine whether there is any face in an image or not.
-   Face Detection is the first and essential step for face recognition, and it is used to detect faces in the images.
-   Facebook is also using face detection algorithm to detect faces in the images and recognise them.

## Cost and Features

**Cost**

-   If there is an internal enabled webcam attached to your laptop / PC, then it’s free of cost.
-   But, if there is no internal enabled webcam, we have to buy an external device to access it. It is not cost-effective.

**Features**

  The features of Face detection are:

  1.Quick to compute.
     - Classification of a face does not require a lot of offline processing.
  2.Accurate.
     - Most of the images can provide accuracy above the 90%

## Defining the System

![](Block.png)

## SWOT Analysis

![](SWOT.png)

## 4W's and 1'H

  **Who**

    It is helpful for the detecting the faces in real-time for tracking of a person or objects through surveillance or Webcam.

  **What**

    The primary aim of face detection is to determine whether there is any face in an image or not.

  **When**

    When any uncertain thing happens or performing it for attendance management.

  **Where**

    Can be put in schools, colleges, offices or any public places.

  **How**

    Face Detection works as to detect multiple faces in an image. 

    Steps that works how face detection operates:

      1. Image is imported by providing the location of the image.
      2. Then, the picture is transformed from RGB to grayscale because it is easy to detect faces in grayscale.
      3. Image Segmentation, which is used for detecting of multiple objects in a single image so that the classifier can easily detect the objects and faces in the picture.
      4. The next step is to use haar-like features algorithm which is proposed by viola-jones for face detection.
      5. This algorithm used for finding the location of human faces in frame or image.
      6. The next step is to give the coordinates which makes a rectangle box in the image/frame to show the location of face.
      7. After this, It can make a rectangle box in the area of interest where it detects the face.
