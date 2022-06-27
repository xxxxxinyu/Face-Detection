import os
import cv2
import matplotlib.pyplot as plt
from google.colab.patches import cv2_imshow

def detect(dataPath, clf):
    """
    Please read detectData.txt to understand the format. Load the image and get
    the face images. Transfer the face images to 19 x 19 and grayscale images.
    Use clf.classify() function to detect faces. Show face detection results.
    If the result is True, draw the green box on the image. Otherwise, draw
    the red box on the image.
      Parameters:
        dataPath: the path of detectData.txt
      Returns:
        No returns.
    """
    # Begin your code (Part 4)
    """
    Read txt and raed image.
    clip: cut image by given x, y, width and height
    Use resize function to transer images to 19*19.
    Use cvtColor function ti transer images from BGR to grayscale
    """
    f = open(dataPath)
    
    for _ in range (2):
      line = f.readline()
      t = line.split()
      pos = int(t[1])
      pic = t[0]
      img = cv2.imread('data/detect/' + pic, cv2.IMREAD_UNCHANGED)

      for i in range(pos):
        
        coordinate = f.readline()
        tmp = coordinate.split()
        x_pos = int(tmp[0])
        y_pos = int(tmp[1])
        length = int(tmp[2])

        clip = img[y_pos:(y_pos+length), x_pos:(x_pos+length)]
        clip = cv2.resize(clip, (19,19), interpolation=cv2.INTER_LINEAR)
        clip = cv2.cvtColor(clip, cv2.COLOR_BGR2GRAY)

        if(clf.classify(clip)):
          cv2.rectangle(img, (x_pos, y_pos), (x_pos+length, y_pos+length), (0,225,0), 3)
        else:
          cv2.rectangle(img, (x_pos, y_pos), (x_pos+length, y_pos+length), (0,0,255), 3)

      
      cv2_imshow(img)
    f.close()
    # raise NotImplementedError("To be implemented")
    # End your code (Part 4)
