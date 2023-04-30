# Camera Calibration with AR

This repository provides tools and resources for calibrating a camera and applying simple Augmented Reality (AR) techniques using OpenCV. 

## Tech Stack

- Python 3.7 or later
- OpenCV 4.5 or later
- NumPy
- SciPy

## Screenshots

<p align="center">
  <a href="https://github.com/behzod1996/opencv-samples"><img width="300px" alt="Camera Calibration" src="https://github.com/behzodhalil/opencv-samples/blob/main/docs/images/camera_calibration_screenshot.png?raw=true"/></a> <br>
</p>

## Usage

`camera_calibration.py`: A script for calibrating your camera using a chessboard pattern. This script estimates the camera's intrinsic parameters and lens distortion coefficients, which are essential for accurate AR rendering.

`pose_estimation.py`: A script for detecting a planar pattern (e.g., a chessboard) in real-time from a video feed, estimating the camera pose relative to the pattern, and overlaying a 3D object onto the pattern.
