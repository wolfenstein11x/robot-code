#!/usr/bin/python3

import argparse
import cv2

# fetching the arguments and save in dictionary
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Enter path to the image")
args = vars(ap.parse_args())

# load and convert image into numpy array
image = cv2.imread(args["image"])

# come up with a way for it to test if it is a tennis ball 
# maybe look for a bunch of yellow pixels in the middle or something

if True:
	print("That is a tennis ball")
else:
	print("That is not a tennis ball")

# load image into cv2 window
cv2.imshow("Image Title", image)

# wait for key press
cv2.waitKey(0)