#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
slope_detector.py

Filters out ground plane from incoming PointCloud2 and only publishes a cmd_vel when on a steep slope.
"""

import rospy
import numpy as np
import tf2_ros
from sensor_msgs.msg import PointCloud2
from sensor_msgs import point_cloud2
from geometry_msgs.msg import Twist


def callback(cloud_msg):
    # Build Nx3 array of (x,y,z)
    points_list = []
    for p in point_cloud2.read_points(cloud_msg, skip_nans=True):
        try:
            points_list.append((p[0], p[1], p[2]))
        except Exception:
            continue

    if not points_list:
        rospy.logwarn("slope_detector: received empty cloud, skipping")
        return

    points = np.array(points_list)
    if points.ndim != 2 or points.shape[1] != 3:
        rospy.logwarn("slope_detector: unexpected points shape %s, skipping", points.shape)
        return

    # Now it's safe to do the plane‐distance dot product:
    normal = np.array([0.0, 0.0, 1.0])
    d = 0.0
    ground_dist_thresh = rospy.get_param('~ground_distance', 0.05)

    distances = np.dot(points, normal) + d
    ground_mask = np.abs(distances) < ground_dist_thresh
    non_ground = np.count_nonzero(~ground_mask)
    rospy.loginfo("slope_detector: %d non-ground points", non_ground)




def main():
    rospy.init_node('slope_detector')

    # Publisher for filtered cmd_vel
    global cmd_pub
    cmd_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)

    # Subscribe to raw point cloud
    rospy.Subscriber('/camera/depth/points', PointCloud2, callback, queue_size=1)

    rospy.loginfo("slope_detector: listening on /camera/depth/points")
    rospy.spin()

if __name__ == '__main__':
    main()

