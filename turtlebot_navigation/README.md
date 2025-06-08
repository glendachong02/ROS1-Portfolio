# 🤖 TurtleBot3 Navigation Project

This subproject showcases the use of **TurtleBot3** for autonomous navigation and mapping using the ROS 1 framework. It is presented in a format understandable to:

- 🧑‍💼 Non-Technical Managers
- 🧑‍💻 Technical Managers & Developers
- 🤖 Bots / Automated Readers

---

## 🧑‍💼 Non-Technical Summary

TurtleBot3 is a low-cost, open-source robot designed for learning and testing robotics software. It enables:
- Indoor autonomous navigation
- Real-time obstacle detection and avoidance
- Smart team training in automation and AI
- Educational demonstrations in R&D and innovation

This project uses it to:
- Build maps using sensors (SLAM)
- Navigate indoor spaces autonomously
- Visualize real-time robot data (RViz)

---

## 🧑‍💻 Technical Overview

### ✅ Technologies Used
- **ROS 1** (Melodic or Noetic)
- TurtleBot3 (Burger model)
- Packages:
  - `turtlebot3_bringup`
  - `turtlebot3_teleop`
  - `turtlebot3_slam`
  - `turtlebot3_navigation`
  - `map_server`
  - `rviz`

### 📁 Key Components

| File/Folder            | Description |
|------------------------|-------------|
| `launch/`              | Bringup, teleop, SLAM, and navigation launch files |
| `maps/`                | Saved map files for localization |
| `rviz/navigation.rviz` | RViz config showing map, laser, robot, goals |

### 🧪 Demo Steps

1. **Bring up the robot:**
   ```bash
   roslaunch turtlebot3_bringup turtlebot3_robot.launch
