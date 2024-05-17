"""
matching.py

Author: Héctor Camacho Zamora
Organization: UDEM
Date: 17-05-2024

This python program is used to extract keypoints of an image.
example of use: 
python3 matching.py --referenced_image panda.jpeg --matched_image panda-and-truck.jpeg 

"""
#LE CAMBIE EL NOMBRE AL ARCHIVO POR QUE NO SE ENCONTRABA EN MI COMPUTADORA CON EL NOMBRE PASADO
import argparse
import cv2
import numpy as np

def user_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("--referenced_image", required=True, help="path to input image")
    parser.add_argument("--matched_image", required=True, help="path to input image")
    return parser.parse_args()
def load_image(args):  
    image = cv2.imread(args)
    return image
def feature_detect(image):

    orb = cv2.ORB_create(nfeatures=1000) 
    kp, dp = orb.detectAndCompute(image, None) 
    return kp, dp

def match_feature(dp1, dp2):
    bf = cv2.BFMatcher() 
    matches = bf.knnMatch(dp1, dp2, k=2)
    good_matches = [] 
    for m, n in matches:
        if m.distance < 0.7 * n.distance:
            good_matches.append([m])
    return good_matches

def run_pipeline():
    

    args = user_parse()
    image1 = load_image(args.referenced_image)
    image2 = load_image(args.matched_image)
    kp1, dp1 = feature_detect(image1)
    kp2, dp2 = feature_detect(image2)
    good_matches = match_feature(dp1, dp2)
    img = cv2.drawMatchesKnn(image1, kp1, image2, kp2, good_matches, None, flags = 2)

    cv2.imshow("matches", img)
    if cv2.waitKey(0) & 0xff == 27:
        cv2.destroyAllWindows()
   

if __name__ == "__main__":
    run_pipeline()