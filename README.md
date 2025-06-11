# ROS 1 Digital Portfolio – Team 3

A structured, multi-audience portfolio showcasing Robot Operating System (ROS 1) projects with real-world and simulated applications. Designed to inform non-technical stakeholders, support technical understanding, and enable machine-readable indexing.

![ROS Version](https://img.shields.io/badge/ROS-1-brightgreen)
![Language](https://img.shields.io/badge/language-Python-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Platform](https://img.shields.io/badge/platform-Gazebo%20%7C%20Ubuntu-important)

---

## Overview

ROS 1 (Robot Operating System) is a modular open-source middleware used to develop, simulate, and control robotic systems. This repository demonstrates ROS capabilities through projects like TurtleBot navigation and Gazebo simulations.

### Contents

- Source code for ROS 1 projects
- Audience-specific breakdowns
- Visuals and architecture diagrams
- Learning resources and migration support
- Structured metadata for bots and indexing systems

---

## Audience Sections

### Non-Technical Guide: ROS in Industry and Hiring

Refer to `Non-Technical.md` for:

- What is ROS 1 and why it matters
- Workforce relevance: where ROS is used
- How robotics supports innovation and collaboration
- Tips for hiring or evaluating a ROS-ready candidate

### Technical Overview: ROS Architecture and Tools

Refer to `Technical.md` for:

- Core ROS concepts: nodes, topics, services, actions
- System integration: sensors, SLAM, navigation
- Tools: Gazebo, RViz, TF, launch files
- Development workflows and maintenance strategies

### Automation-Ready Metadata for Bots

Refer to `bots.json` for machine-readable structure, including:

- Supported languages and environments
- Core ROS 1 concepts and terminology
- System requirements and package structure
- API-relevant keywords

---

## Project Portfolio

| Project | Description | Skills Demonstrated | Tools Used |
|--------|-------------|---------------------|------------|
| TurtleBot Navigation | SLAM and autonomous navigation with real-time localization | Teleoperation, GMapping, AMCL | TurtleBot3, ROS 1, RViz |
| Gazebo Simulation | Simulated 3D test environments for ROS application testing | Simulation, TF trees, URDF | Gazebo, ROS 1 |

Source code located in the `projects/` directory.

---

## Visual Assets

Located in the `visuals/` folder:

- Node architecture diagrams
- SLAM and map outputs in RViz
- TF tree examples for transform visualization

Example:

```markdown
![GMapping SLAM Output](visuals/slam_output_map1_rviz.png)
*Figure: SLAM map generated using GMapping in RViz.*
