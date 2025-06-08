# 🤖 TurtleBot3 Navigation Demo

This project contains example launch files and configurations for running TurtleBot3 with:

- 🕹️ Keyboard Teleoperation
- 🧭 SLAM (Mapping)
- 🌍 AMCL (Autonomous Navigation using a saved map)
- 👁️ RViz visualization

---

## 🧰 Requirements

- Ubuntu 18.04 (ROS Melodic) or 20.04 (ROS Noetic)
- TurtleBot3 packages:
  ```bash
  sudo apt install ros-${ROS_DISTRO}-turtlebot3*
  ```
- Set your model:
  ```bash
  export TURTLEBOT3_MODEL=burger
  ```

---

## 🚀 How to Use

### 1️⃣ Bringup (real or simulated)
```bash
roslaunch turtlebot3_bringup turtlebot3_robot.launch
```

### 2️⃣ Teleoperate with Keyboard
```bash
roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch
```

### 3️⃣ SLAM (Mapping)
```bash
roslaunch turtlebot3_slam turtlebot3_slam.launch slam_methods:=gmapping
```

### 4️⃣ Save the Map
```bash
rosrun map_server map_saver -f ~/my_map
```

Copy `my_map.yaml` and `my_map.pgm` into the `maps/` folder in this repo.

### 5️⃣ Navigation
```bash
roslaunch turtlebot3_navigation turtlebot3_navigation.launch map_file:=$(rospack find YOUR_PACKAGE_NAME)/maps/my_map.yaml
```

---

## 🖼️ RViz Configuration
A custom `rviz/navigation.rviz` file is included for a clear layout of robot position, map, and laser scan.

