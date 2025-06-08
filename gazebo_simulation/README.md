## Overview
Gazebo is a powerful open-source 3D robotics simulator integrated tightly with ROS 1. It allows developers to test and validate robot models, sensors, and algorithms in realistic virtual environments without physical hardware.

## Key Features
- Physics engine for realistic simulation (ODE, Bullet, DART)
- Sensor simulation (cameras, LIDAR, IMU, GPS, etc.)
- Environment modeling with lights, textures, and objects
- Robot model support via URDF and SDF
- Plugins for custom robot behavior and sensor data generation
- Integration with ROS topics, services, and actions

## How It Works with ROS 1
- Uses `roslaunch` to start Gazebo alongside ROS nodes
- ROS topics relay sensor data and robot state
- Actuator commands sent as ROS messages control simulated robots
- Simulation time synced with ROS time for consistency
