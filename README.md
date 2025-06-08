# 🤖 ROS 1 Digital Portfolio

Welcome to the ROS 1 Digital Portfolio — a structured showcase of Robot Operating System (ROS) 1 concepts, use cases, and demonstrations, tailored for three different audiences:

- 🧑‍💼 **Non-Technical**: Understand how ROS fits into workforce needs and tech roles
- 🧑‍💻 **Technical**: Dive into technical systems, architecture, and tooling
- 🤖 **Bots/Docs Readers**: Access machine-readable metadata for automation and indexing

---

## 🔍 Overview

ROS 1 (Robot Operating System) is an open-source middleware for developing modular robotic systems. It allows developers to build, simulate, and control robots using a publish-subscribe architecture.

This repository includes:

- 🔧 Our code projects (TurtleBot navigation, Gazebo simulation)
- 📄 Audience-specific breakdowns
- 📊 Visuals and architecture diagrams
- 📚 Learning and migration resources

---

## 🧑‍💼 For Non-Technical

📄 [overview/Non-Technical.md](overview/Non-Technical.md)

- What is ROS 1?
- Why it's important in modern robotics hiring
- How it supports innovation and teamwork
- Hiring tips: what to look for in a ROS-ready candidate

---

## 🧑‍💻 For Technical

📄 [overview/Technical.md](overview/Technical.md)

- ROS 1 architecture (nodes, topics, services)
- System integration: sensors, SLAM, navigation, simulation
- Development tools and packages
- Tips for infrastructure setup and long-term maintainability

---

## 🤖 For Bots / Automation Systems

🧾 [overview/bots.json](overview/bots.json)

Includes structured data:
- Core ROS concepts
- Supported languages
- System requirements
- Package structure and API keywords

---

## 🚀 Projects

📂 `projects/` contains real-world and simulated ROS 1 applications:

- [TurtleBot Navigation](projects/turtlebot_navigation/)
  - Bringup, teleoperation, SLAM, AMCL
- [Gazebo Simulation](projects/gazebo_simulation/)
  - Simulated environments for testing navigation and mapping

---

## 🖼️ Visuals

📂 `visuals/` contains:
- ROS node architecture diagrams
- RViz screenshots of SLAM/mapping
- TF (transform) tree examples

---

## 📚 Resources

📂 `resources/` includes:
- [ROS wiki & tutorials](resources/ROS_wiki_links.md)
- [Learning paths](resources/learning_paths.md)
- [ROS 1 → ROS 2 migration tips](resources/transition_to_ros2.md)

---

## ⚙️ Run Instructions

### 1. Manual Bringup (development)
```bash
roscore  # Start ROS master (manual mode)

# In a new terminal
roslaunch turtlebot_bringup minimal.launch
# In a new terminal
roslaunch turtlebot_teleop keyboard_teleop.launch
# In a new terminal
roslaunch turtlebot_navigation gmapping_demo.launch
