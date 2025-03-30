# Tortoisebot ROS2 Humble Release

![TortoiseBot Banner](https://github.com/rigbetellabs/tortoisebot_docs/raw/master/imgs/packaging/pack_front.png)

<div align="center">

![stars](https://img.shields.io/github/stars/rigbetellabs/tortoisebot?style=for-the-badge)
![forks](https://img.shields.io/github/forks/rigbetellabs/tortoisebot?style=for-the-badge)
![watchers](https://img.shields.io/github/watchers/rigbetellabs/tortoisebot?style=for-the-badge)
![repo-size](https://img.shields.io/github/repo-size/rigbetellabs/tortoisebot?style=for-the-badge)
![contributors](https://img.shields.io/github/contributors/rigbetellabs/tortoisebot?style=for-the-badge)

</div>

<p align="center">
<a href="#connect-with-us">Connect with Us</a> • 
<a href="#about-tortoisebot">About</a> • 
<a href="#installation">Installation</a> • 
<a href="#setup">Setup</a> • 
<a href="#demos">Demos</a> • 
<a href="#troubleshooting">Troubleshooting</a>
</p>

## About TortoiseBot 🐢🤖

The TortoiseBot is a versatile robotic platform for ROS2 development, created and maintained by the team at RigBetel Labs LLP. This repository contains all the necessary software to set up and run your TortoiseBot with ROS2 Humble.

For comprehensive documentation, visit our [Wiki](https://github.com/rigbetellabs/tortoisebot/wiki/1.-Getting-Started).

## Connect with Us

<div>

[![Website](https://img.shields.io/website?down_color=lightgrey&down_message=offline&label=Rigbetellabs%20Website&style=for-the-badge&up_color=green&up_message=online&url=https%3A%2F%2Frigbetellabs.com%2F)](https://rigbetellabs.com/)
[![Discord](https://img.shields.io/discord/890669104330063903?logo=Discord&style=for-the-badge)](https://rigbetellabs.com/discord)
[![Youtube](https://img.shields.io/youtube/channel/subscribers/UCfIX89y8OvDIbEFZAAciHEA?label=YT%20Subscribers&style=for-the-badge)](https://www.youtube.com/channel/UCfIX89y8OvDIbEFZAAciHEA)

</div>

## Installation

### 1. Install Required Dependencies

```bash
# Set build optimization (optional but recommended)
export WORKERS_BUILD_DEPS=$(nproc)

# Install ROS2 packages and basic dependencies
sudo apt-get update
sudo apt-get install -y wget unzip
sudo apt-get install -y ros-humble-vision-opencv ros-humble-cv-bridge ros-humble-image-transport
sudo apt-get install -y ros-humble-imu-tools ros-humble-imu-complementary-filter ros-humble-robot-localization
sudo apt-get install -y cmake libgoogle-glog-dev libatlas-base-dev libsuitesparse-dev libboost-python-dev libboost-dev libboost-filesystem-dev libboost-program-options-dev
```

### 2. Create ROS2 Workspace and Build

```bash
# Create and navigate to workspace
mkdir -p ~/ROS_WS/src
cd ~/ROS_WS

# Clone repository
git clone -b ros2-humble https://github.com/rigbetellabs/tortoisebot.git src

# Build workspace
colcon build
```

If you encounter YDLidar-related build issues:

```bash
# Build YDLidar SDK manually
cd ~/ROS_WS/src/YDLidar-SDK
mkdir -p build && cd build
cmake ..
make -j$(nproc) 
sudo make install

# Return to workspace and build again
cd ~/ROS_WS
colcon build
```

### 3. Install Advanced Dependencies (if needed)

#### OpenCV Installation

```bash
# Clone OpenCV repositories
git clone https://github.com/opencv/opencv.git -b 4.8.0 --depth 1
git clone https://github.com/opencv/opencv_contrib.git -b 4.8.0 --depth 1

# Build OpenCV
cd opencv
mkdir build && cd build
cmake -D CMAKE_BUILD_TYPE=RELEASE -D INSTALL_C_EXAMPLES=OFF -D INSTALL_PYTHON_EXAMPLES=OFF -D OPENCV_GENERATE_PKGCONFIG=ON -D BUILD_EXAMPLES=OFF -D OPENCV_ENABLE_NONFREE=ON -D WITH_IPP=OFF -D BUILD_TESTS=OFF -D BUILD_PERF_TESTS=OFF -D BUILD_opencv_adas=OFF -D BUILD_opencv_bgsegm=OFF -D BUILD_opencv_bioinspired=OFF -D BUILD_opencv_ccalib=OFF -D BUILD_opencv_datasets=ON -D BUILD_opencv_datasettools=OFF -D BUILD_opencv_face=OFF -D BUILD_opencv_latentsvm=OFF -D BUILD_opencv_line_descriptor=OFF -D BUILD_opencv_matlab=OFF -D BUILD_opencv_optflow=ON -D BUILD_opencv_reg=OFF -D BUILD_opencv_saliency=OFF -D BUILD_opencv_surface_matching=OFF -D BUILD_opencv_text=OFF -D BUILD_opencv_tracking=ON -D BUILD_opencv_xobjdetect=OFF -D BUILD_opencv_xphoto=OFF -D BUILD_opencv_stereo=OFF -D BUILD_opencv_hdf=OFF -D BUILD_opencv_cvv=OFF -D BUILD_opencv_fuzzy=OFF -D BUILD_opencv_dnn=OFF -D BUILD_opencv_dnn_objdetect=OFF -D BUILD_opencv_dnn_superres=OFF -D BUILD_opencv_dpm=OFF -D BUILD_opencv_quality=OFF -D BUILD_opencv_rapid=OFF -D BUILD_opencv_rgbd=OFF -D BUILD_opencv_sfm=OFF -D BUILD_opencv_shape=ON -D BUILD_opencv_stitching=OFF -D BUILD_opencv_structured_light=OFF -D BUILD_opencv_alphamat=OFF -D BUILD_opencv_aruco=OFF -D BUILD_opencv_phase_unwrapping=OFF -D BUILD_opencv_photo=OFF -D BUILD_opencv_gapi=OFF -D BUILD_opencv_video=ON -D BUILD_opencv_ml=OFF -D BUILD_opencv_python2=OFF -D WITH_GSTREAMER=OFF -D ENABLE_PRECOMPILED_HEADERS=OFF -D CMAKE_INSTALL_PREFIX=/usr/local -D OPENCV_EXTRA_MODULES_PATH=../../opencv_contrib/modules/ ../

make -j $WORKERS_BUILD_DEPS
sudo make install
sudo ldconfig
```

#### Eigen and Ceres Solver (for VINS-Fusion)

```bash
# Install Eigen
wget -O eigen-3.4.0.zip https://gitlab.com/libeigen/eigen/-/archive/3.4.0/eigen-3.4.0.zip 
unzip eigen-3.4.0.zip 
cd eigen-3.4.0 && mkdir build && cd build
cmake ../ && sudo make install -j $WORKERS_BUILD_DEPS
cd ../../

# Install Ceres Solver
wget http://ceres-solver.org/ceres-solver-2.1.0.tar.gz
tar zxf ceres-solver-2.1.0.tar.gz
cd ceres-solver-2.1.0
mkdir build && cd build
cmake -DEXPORT_BUILD_DIR=ON \
      -DCMAKE_INSTALL_PREFIX=/usr/local \
      ../
make -j $WORKERS_BUILD_DEPS
sudo make install -j $WORKERS_BUILD_DEPS

# Clean up environment variable
unset WORKERS_BUILD_DEPS
```

## Setup

### Robot Setup

- For basic operation, launch the bringup file:
  ```bash
  ros2 launch tortoisebot_bringup bringup.launch.py
  ```

- For complete operation with navigation and SLAM/localization:
  ```bash
  ros2 launch tortoisebot_bringup autobringup.launch.py use_sim_time:=True exploration:=True
  ```
  - Use `exploration:=False` when using a saved map for navigation
  - Use `use_sim_time:=False` when working with a physical robot

### Launch Files Reference

- **SLAM**: `cartographer.launch.py`
- **Navigation**: `navigation.launch.py`
- **Rviz**: `rviz.launch.py`
- **Gazebo**: `gazebo.launch.py`

### Remote PC Setup

When building on a remote PC, ignore packages that require hardware connection:

```bash
colcon build --packages-ignore ydlidar_sdk ydlidar_ros2_driver v4l2_camera
```

### Visual-Inertial Navigation with VINS-Fusion

To run VINS-Fusion visual-inertial odometry:

```bash
ros2 run vins vins_node src/tortoisebot_description/raspicam/raspicam_mono_imu.yaml --ros-args --log-level info
```

For pose graph optimization (loop closure):

```bash
ros2 run loop_fusion loop_fusion_node src/tortoisebot_description/raspicam/raspicam_mono_imu.yaml --ros-args --log-level info
```

### EKF and Robot Localization

To run ekf node
```bash
ros2 launch tortoisebot_bringup ekf.launch.py
```

## Demos

The TortoiseBot supports multiple demo applications including:
- Teleoperation
- Mapping
- Autonomous Navigation
- Sensor Visualization (Lidar, Odometry, Camera)

# **Fusion of VINS-Fusion, AMCL, and IMU for Robot Localization**

## **1. Introduction**
This document presents an approach to combining **Visual-Inertial Odometry (VINS-Fusion)**, **Adaptive Monte Carlo Localization (AMCL)**, and **IMU-based filtering (EKF/UKF)** for robust localization of **TortoiseBot** in **ROS 2 Humble**. The approach is based on theoretical foundations and initial experimental validation.

## **2. Methodology**
The localization system consists of the following components:

- **VINS-Fusion**: Provides **relative** pose estimation using camera and IMU data.
- **AMCL**: Corrects **global** localization by comparing laser scan data with a known map.
- **IMU + EKF/UKF**: Fuses acceleration and gyroscope data for short-term stability.
- **Fusion Strategy**: The `robot_localization` package (EKF/UKF) is used to merge multiple odometry sources.

### **Data Flow**
```plaintext
[Camera + IMU] --(VINS-Fusion)--> /odometry
[Lidar] --(AMCL)--> /amcl_pose
[IMU] --> /imu_plugin/out
[Wheel Odometry] --> /odom
All Inputs --> (EKF/UKF) --> /filtered_odom
```

## **3. Implementation**

### **VINS-Fusion Setup**
- Camera-IMU calibration using `kalibr` [in our case malually calculated]
- Feature extraction and tracking for visual odometry
- Loop closure for drift correction [Optional]

### **AMCL Configuration**
- Particle filter for global localization
- Scan matching using laser data (`/scan` topic)
- Dynamic re-sampling based on motion model

### **EKF Node (robot_localization)**
- Subscribes to `/odometry`, `/odom`, and `/imu_plugin/out`
- Provides **drift-compensated** pose estimation on `/filtered_odom`

## **4. Experimental Results**

### **VINS-Fusion Output**
Expected: `/vins_odom` should match ground truth.
Actual: Observed drift due to poor feature tracking.

### **AMCL Pose Estimates**
Expected: `/amcl_pose` should stabilize quickly.
Actual: Inconsistent pose estimation, likely due to poor lidar scan matching.

### **IMU Drift Correction**
Expected: EKF should compensate for drift.
Actual: IMU noise causing fluctuations in `/filtered_odom`.

## **5. Conclusion**
The proposed approach is theoretically sound but currently has implementation challenges. Further debugging and tuning are needed to achieve accurate localization. The next steps include refining sensor calibration, parameter tuning, and debugging data fusion inconsistencies.

[![Watch the video](https://img.youtube.com/vi/4MctUURRlWI/0.jpg)](https://youtu.be/4MctUURRlWI)

## Troubleshooting

### Build Issues

If you encounter build errors, try these steps in order:

1. Rebuild workspace:
   ```bash
   colcon build
   ```

2. Clean and rebuild:
   ```bash
   rm -rf build/ install/ log/
   colcon build
   ```

### Navigation and Localization Issues

If you encounter problems with navigation components:

1. Check if AMCL or map_server nodes are in error state:
   ```bash
   ros2 lifecycle list
   ```

2. Manually configure and activate the nodes:
   ```bash
   # For AMCL issues
   ros2 lifecycle set /amcl configure
   ros2 lifecycle set /amcl activate
   
   # For map server issues
   ros2 lifecycle set /map_server configure
   ros2 lifecycle set /map_server activate
   ```

3. Verify node status:
   ```bash
   ros2 lifecycle list
   ```

## Documentation

For detailed documentation, please visit our Wiki:

1. [Getting Started](https://github.com/rigbetellabs/tortoisebot/wiki/1.-Getting-Started)
2. [Hardware Assembly](https://github.com/rigbetellabs/tortoisebot/wiki/2.-Hardware-Assembly)
3. [TortoiseBot Setup](https://github.com/rigbetellabs/tortoisebot/wiki/3.-TortoiseBot-Setup)
4. [Server PC Setup](https://github.com/rigbetellabs/tortoisebot/wiki/4.-Server-PC-Setup)
5. [Running Demos](https://github.com/rigbetellabs/tortoisebot/wiki/5.-Running-Demos)

[Join](https://discord.gg/qDuCSMTjvN) our community for free support. Post your projects or ask questions if you need any help.

## About Us

TortoiseBot is sourced, assembled, made & maintained by our team at:

RigBetel Labs LLP®, Charholi Bk., via. Loheagaon, Pune - 412105, MH, India 🇮🇳  
🌐 [RigBetelLabs.com](https://rigbetellabs.com)  
📞 [+91-8432152998](https://wa.me/918432152998)  
📨 getintouch.rbl@gmail.com, info@rigbetellabs.com  

[LinkedIn](http://linkedin.com/company/rigbetellabs/) | 
[Instagram](http://instagram.com/rigbetellabs/) | 
[Facebook](http://facebook.com/rigbetellabs) | 
[Twitter](http://twitter.com/rigbetellabs) | 
[YouTube](https://www.youtube.com/channel/UCfIX89y8OvDIbEFZAAciHEA) | 
[Discord Community](https://discord.gg/qDuCSMTjvN)
