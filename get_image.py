#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import sys
import os

def main():
    # Allow passing the image filename as the first argument
    if len(sys.argv) > 1:
        img_path = sys.argv[1]
    else:
        img_path = "human.jpg"    # default if you run without args

    if not os.path.exists(img_path):
        sys.stderr.write("Error: file not found: {}\n".format(img_path))
        sys.exit(1)

    img = cv2.imread(img_path)
    if img is None:
        sys.stderr.write("Error: failed to load image {}\n".format(img_path))
        sys.exit(1)

    height, width = img.shape[:2]
    # Print out width and height
    print "Width =", width
    print "Height =", height

if __name__ == "__main__":
    main()
#!/usr/bin/env python3
import cv2

# replace with your actual image name/path if needed
img = cv2.imread("human.jpg")  
if img is None:
    raise RuntimeError("Failed to load image—check the filename!")
H, W = img.shape[:2]
print("Width =", W, " Height =", H)

