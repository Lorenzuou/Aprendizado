import cv2
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

image = plt.imread('People-is-or-are.jpg')


Width = image.shape[1]
Height = image.shape[0]


net = cv2.dnn.readNet('yolov3.weights', 'yolov3.cfg')


image.imgshow()