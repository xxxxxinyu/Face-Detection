import os
import cv2

def loadImages(dataPath):
    """
    load all Images in the folder and transfer a list of tuples. The first 
    element is the numpy array of shape (m, n) representing the image. 
    The second element is its classification (1 or 0)
      Parameters:
        dataPath: The folder path.
      Returns:
        dataset: The list of tuples.
    """
    # Begin your code (Part 1)
    """
    dataset: A list stores tuples 
    Use os.listdir to list the files under dataPath. And then, use 
    if-statement to find non-face folder and face folder respectively 
    and list it. When use imread, cv2.IMREAD_UNCHANGED makes sure the
    image stil be grayscale. Then, create a tuple to store image and 
    classification (0 represents non-face, and 1 represents face). 
    Finally, put tuples into the list dataset.
    """
    dataset = []
    L1 = os.listdir(dataPath)
    for L2 in L1:
      if L2 == 'non-face':
        Nonface = os.listdir(dataPath + '/non-face')
        for i in Nonface:
          img = cv2.imread(dataPath + '/non-face/' + i, cv2.IMREAD_UNCHANGED)
          t = (img, 0)
          dataset.append(t)
      elif L2 == 'face':
        Face = os.listdir(dataPath + '/face')
        for i in Face:
          img = cv2.imread(dataPath + '/face/' + i, cv2.IMREAD_UNCHANGED)
          t = (img, 1)
          dataset.append(t)
      

    # raise NotImplementedError("To be implemented")
    # End your code (Part 1)
    return dataset
