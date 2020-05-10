import cv2
import os
import pandas as pd
import numpy as np
from skimage.filters.rank import entropy
from skimage.morphology import disk
from skimage import data, io
from skimage.color import rgb2gray

def RMS_CONTRAST(imagefile):
    print(imagefile)
    img = cv2.imread(imagefile)
    oneD_pixels = np.concatenate(img, axis=0)

    brightness = 0
    ## average brightness
    for info in oneD_pixels:
        brightness += (0.2126 * info[0]) + (0.7152 * info[1]) + (0.0722 * info[2])
    average_brightness = brightness / len(oneD_pixels)  ## calculate average
    average_brightness /= 255  ## normalizing to 0 and 1

    rms = 0
    for info in oneD_pixels:
        brightness = (0.2126 * info[0]) + (0.7152 * info[1]) + (0.0722 * info[2])
        brightness /= 255  ## normalizing to 0 and 1
        rms += pow((brightness - average_brightness), 2);  ## calculate squared
    rms /= len(oneD_pixels)  ## calculate mean squared
    rms = pow(rms, 0.5)
    return rms

print('picasso rms start')
image_folder = os.path.join(os.pardir, 'data/picasso')
picasso_women_path = os.path.join(os.pardir, 'data/picasso_women.csv')
picasso_women = pd.read_csv(picasso_women_path)
print(image_folder)

picasso_women['RMS_contrast'] = picasso_women.apply(lambda x: RMS_CONTRAST(os.path.join(image_folder,x['Picturesource'])), axis = 1)

print('matisse rms start')
image_folder = os.path.join(os.pardir, 'data/henri-matisse')
matisse_women_path = os.path.join(os.pardir, 'data/matisse_women.csv')
matisse_women = pd.read_csv(matisse_women_path)
matisse_women['RMS_contrast'] = matisse_women.apply(lambda x: RMS_CONTRAST(os.path.join(image_folder,x['Picturesource'])), axis = 1)

def average_entropy(imagefile):
    print(imagefile)
    img = cv2.imread(imagefile)
    gray_img = rgb2gray(img)
    return entropy(gray_img, disk(5)).mean()

print('picasso entropy start')
image_folder = os.path.join(os.pardir, 'data/picasso')
picasso_women['AVG_entropy'] = picasso_women.apply(lambda x: average_entropy(os.path.join(image_folder,x['Picturesource'])), axis = 1)

print('matisse entropy start')
image_folder = os.path.join(os.pardir, 'data/henri-matisse')
matisse_women['AVG_entropy'] = matisse_women.apply(lambda x: average_entropy(os.path.join(image_folder,x['Picturesource'])), axis = 1)

print('updating csv....')
matisse_women.to_csv(matisse_women_path)
picasso_women.to_csv(picasso_women_path)
print('you are all set ;D')