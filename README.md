# Computer Vision Sorting Robotic Arm: Mechanical CAMden

### Project Overview: 
The goal of this project is to mimic the behavior of our close friend, Camden James Droz. Not only is he an inspiration to us all, but more importantly, he is excellent at sorting objects by color. For our final project, we used computer vision and inverse kinematics to sort cubes of various colors into different locations. This is done by using an ArUco board to translate image coordinates to camera coordinates to world coordinates, and then transfrom from the board frame, to the camera frame, to the robotic frame. Lastly, use our IK algorithm to move our robotic arm to the desired end effector position and pick up the object. Mechanical CAMden is shown in action below: 

<img src="media/gif_video.gif" height="275">  <img src="media/gif_video2.gif" height="275">

### Repository Information: 
This repository provides the python libraries for interfacing with the Hiwonder 5-DOF mobile manipulator. We have modified the original reporsitory to add additional functionality to the Hiwonder 5-DOF mobile manipulator; we have added a sorter.py function as the final project of our Fundamentals of Robotics final. Our final report for the project can be found in this repo here: [Final Project Report.](https://github.com/swisnoski/hiwonder-armpi-pro/blob/v2025/Mechanical_CAMden_Technical_Report.pdf)

### Robot Information:
The robot platform has an onboard **Raspberry Pi 4B** which serves as the main compute unit of the system. The 5-DOF arm are driven by serial bus servos controlled over serial while the mobile base is driven by DC motors controlled by a custom driver board with communication over I2C. Our project development was completed onboard the Raspberry Pi over **SSH protocol**.


## Setting up the onboard Raspberry Pi

#### Step 0: Connect to Raspberry Pi over SSH
- Run `ssh funrobot@funrobot#.local` in terminal, replacing `#` with the number of your SD card.
  [Find your SD card number](https://docs.google.com/spreadsheets/d/1oiZmZgGmFAW9nbCus0FoESnCpqEN_4TZb9X0I5U4Vjc/).
  **The password is `FunR0b0!`** 
- SSH troubleshooting:
  - Make sure you are connected to the Olin Robotics network (It should work on Olin, but Olin Robotics may be faster/more stable).
  - Make sure OpenSSH Client and OpenSSH Server are installed (should be installed by default on Mac/Linux, may need to be installed under `Settings > System > Optional Features` in Windows).
  - Make sure the OpenSSH folder is added to your path. Should be `C:\Windows\System32\OpenSSH` in Windows.
  - Check the SD card to make sure the number physically written on it matches what you expect.

#### Step 1: Create a virtual environment
- We strongly recommend that you create a new python virtual environment for all your work on the platform.
- Follow this [tutorial here](https://docs.python.org/3/tutorial/venv.html).


#### Step 2: Get this repository from Github
- I recommend you fork this repository to the account of one of your teammates and then you all can clone from the forked version.
- Follow [this tutorial](https://ftc-docs.firstinspires.org/en/latest/programming_resources/tutorial_specific/android_studio/fork_and_clone_github_repository/Fork-and-Clone-From-GitHub.html) to understand how to fork and clone repositories


#### Step 3: Install all required Python packages
```bash
# first: make sure you have activated the virtual environment. See step 1 tutorial

# cd to the project folder
$ cd hiwonder-armpi-pro

# install all required packages from requirements.txt
$ pip install -r requirements.txt
```


### How to Run

- Before you run any script, please initialize the **pigpiod module**
``` bash
$ sudo pigpiod
```

- If setup worked well, you should be able to run the main script with the command below:
``` bash
$ sudo venv/bin/python main.py 
# this runs the main script using admin privileges and the virtual environment's python interpreter.
# N.B.: Please make sure you set the right path for your virtual environment's python interpreter above
```

### Usage Guide

<img src = "media/jstick-manual-1.png" height="300"> 
<img src = "media/jstick-manual-2.png" height="330">


