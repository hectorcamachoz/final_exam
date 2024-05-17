"""
final_exam_vc.py

Author: Héctor Camacho Zamora
Organization: UDEM
Date: 17-05-2024

This python program is used to extract keypoints of an image.
"""
import argparse
import cv2
import numpy as np

def user_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input_image", required=True, help="path to input image")
    args = vars(parser.parse_args())
    return args
def load_image(args):  
    image = cv2.imread(args.input_image)
    return image
def feature_detect(image):

    orb = orb.create()
    kp = orb.detect(image, None)
    kp, des = orb.compute(image, kp)
    img = cv2.drawKeypoints(image, kp, image, color=(0, 255, 0), flags=0)
    return img

def run_pipeline():
    

    args = user_parse()
    image = load_image(args)
    image = feature_detect(image)
    cv2.show("Keypoints", image)

   

if __name__ == "__main__":
    run_pipeline()