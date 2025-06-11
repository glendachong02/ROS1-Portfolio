# TurtleBot3 Navigation Project

This subproject demonstrates autonomous indoor navigation and mapping using TurtleBot3 with the ROS 1 framework. It is structured to support both non-technical and technical audiences, while remaining machine-readable for automated indexing systems.

---

## Project Summary

TurtleBot3 is a compact, affordable, open-source robot platform used in robotics research, education, and prototyping. This project uses TurtleBot3 to:

- Build 2D maps of indoor environments using sensor data (SLAM)
- Navigate autonomously with obstacle detection and path planning
- Visualize robot state and mapping progress in RViz

---

## Audience Sections

### Non-Technical Overview

This project is useful for robotics education, innovation planning, and AI training programs. Key features include:

- Autonomous indoor navigation with real-time obstacle avoidance
- Smart team training in AI, automation, and robotics
- Demonstrations for innovation labs, R&D teams, or educational settings
- Clear insight into robotics workflows and how AI systems "see" and act

### Technical Overview

This section outlines the core architecture, packages, and files used in the ROS 1-based implementation.

#### Technologies Used

- **Operating System**: Ubuntu 18.04 or 20.04
- **ROS Distribution**: Melodic or Noetic
- **Robot Platform**: TurtleBot3 (Burger model)

#### ROS Packages

- `turtlebot3_bringup`: Robot initialization
- `turtlebot3_teleop`: Keyboard teleoperation
- `turtlebot3_slam`: SLAM implementation using GMapping
- `turtlebot3_navigation`: Autonomous path planning and navigation
- `map_server`: Map saving and loading
- `rviz`: Visualization of real-time robot data

---

## SLAM and Navigation Workflow

- Navigate the robot in a simulated or real-world space
- Use SLAM to scan and build a map dynamically
- Save map data for future autonomous navigation
- Load map and localize robot position for efficient pathfinding

---

## Project Directory Structure

| Path | Description |
|------|-------------|
| `launch/` | Launch files for bringup, SLAM, teleop, and navigation |
| `maps/` | Contains generated maps used for localization |
| `rviz/navigation.rviz` | Preconfigured RViz visualization layout |

---

## Demo: Bring Up the Robot

### 1. Start ROS Master

```bash
roscore
#new terminal
roslaunch turtlebot3_bringup turtlebot3_robot.launch
#new terminal
roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch
#new terminal
roslaunch turtlebot3_slam turtlebot3_slam.launch slam_methods:=gmapping
#new terminal
rosrun map_server map_saver -f ~/maps/my_map
roslaunch turtlebot3_navigation turtlebot3_navigation.launch map_file:=~/maps/my_map.yaml

