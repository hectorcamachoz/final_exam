"""
extract.py

Author: Héctor Camacho Zamora
Organization: UDEM
Date: 17-05-2024

This python program is used to extract keypoints of an image.
"""
#LE CAMBIE EL NOMBRE AL ARCHIVO POR QUE NO SE ENCONTRABA EN MI COMPUTADORA CON EL NOMBRE PASADO
import argparse
import cv2
import numpy as np

def user_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_image", required=True, help="path to input image")
    args = vars(parser.parse_args())
    return parser.parse_args()
def load_image(args):  
    image = cv2.imread(args)
    return image
def feature_detect(image):

    orb = cv2.ORB_create(nfeatures=1000) 
    kp, dp = orb.detectAndCompute(image, None) 
    img = cv2.drawKeypoints(image, kp, image, color=(0, 255, 0), flags=0)
    return kp, dp, img


def run_pipeline():
    

    args = user_parse()
    image = load_image(args.input_image)
    kp, dp, img = feature_detect(image)
    cv2.imshow("Keypoints", img)
    if cv2.waitKey(0) & 0xff == 27:
        cv2.destroyAllWindows()
   

if __name__ == "__main__":
    run_pipeline()