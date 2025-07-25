#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

# globals for mouse callback
refPt = []
cropping = False

def click_and_crop(event, x, y, flags, param):
    global refPt, cropping
    image = param
    if event == cv2.EVENT_LBUTTONDOWN:
        refPt = [(x, y)]
        cropping = True
    elif event == cv2.EVENT_MOUSEMOVE and cropping:
        temp = image.copy()
        cv2.rectangle(temp, refPt[0], (x, y), (0,255,0), 2)
        cv2.imshow("ROI", temp)
    elif event == cv2.EVENT_LBUTTONUP:
        refPt.append((x, y))
        cropping = False
        cv2.rectangle(image, refPt[0], refPt[1], (0,255,0), 2)
        cv2.imshow("ROI", image)

def select_roi(image):
    """Display image, let user drag out a box, press 'c' to confirm or 'r' to reset."""
    global refPt, cropping
    clone = image.copy()
    cv2.namedWindow("ROI")
    cv2.setMouseCallback("ROI", click_and_crop, clone)

    while True:
        cv2.imshow("ROI", clone)
        key = cv2.waitKey(1) & 0xFF
        if key == ord("r"):       # reset selection
            clone = image.copy()
            refPt = []
        elif key == ord("c"):     # confirm selection
            break

    cv2.destroyWindow("ROI")

    if len(refPt) == 2:
        (x1, y1), (x2, y2) = refPt
        x, y = min(x1,x2), min(y1,y2)
        w, h = abs(x2-x1), abs(y2-y1)
        return x, y, w, h
    return 0, 0, 0, 0

class ROISaver(object):
    def __init__(self):
        rospy.init_node("roi_saver", anonymous=True)
        self.bridge = CvBridge()
        rospy.Subscriber("/camera/rgb/image_raw",
                         Image,
                         self.callback,
                         queue_size=1)
        rospy.spin()

    def callback(self, msg):
        # Convert ROS Image to OpenCV Mat
        try:
            cv_img = self.bridge.imgmsg_to_cv2(msg, "bgr8")
        except CvBridgeError as e:
            rospy.logerr("CvBridge error: %s", e)
            return

        # Let user select ROI
        x, y, w, h = select_roi(cv_img)

        # Log the raw pixel coordinates
        rospy.loginfo("ROI coords (pixels): x=%d, y=%d, w=%d, h=%d", x, y, w, h)

        # Crop and save if valid
        if w > 0 and h > 0:
            roi = cv_img[y:y+h, x:x+w]
            filename = "roi.jpg"
            if cv2.imwrite(filename, roi):
                rospy.loginfo("Saved ROI to %s", filename)
            else:
                rospy.logerr("Failed to save ROI to %s", filename)
        else:
            rospy.loginfo("No ROI selected, exiting without saving.")

        # Exit after one capture
        rospy.signal_shutdown("ROI saved, node exiting.")

if __name__ == "__main__":
    try:
        ROISaver()
    except rospy.ROSInterruptException:
        pass

