
# Scripts

##### This directory contains all the python scripts used in this project. It contains three basic tracking scripts, one Cascade testing script and a video opencv inbuilt video script for Result video visualization.

### Tracking Script

### 1.multi-tracker.py - 
It is implemented on Opencv-3.1 Multitracker module. It implements the idea of Dection using Opencv Haar/LBP Cascades in every `5th` frames and then Tracking the detected vehicles using Opencv Multi-tracker Module. Opencv provides 6 different trackers such as  BOOSTING, MIL, KCF, TLD, MEDIANFLOW, and GOTURN from which MIL and KCF are the most efficient one for our project.The green rectangle shows detection and red rectangle shows tracking in a frame. 
###### The basic script is written for KCF tracker but you can change the argument in code for any of the six trackers.

###### Though it's the easiest and most efficient implementaion But it does not satisfy our purpose as IOS does not provide KCf inbuilt tracker.

#### Results -
##### Detection
![img2](https://cloud.githubusercontent.com/assets/16621282/23577791/73010068-00ee-11e7-9777-553b6f6df18a.png)

#### Tracking
![img1](https://cloud.githubusercontent.com/assets/16621282/23577815/f424acb2-00ee-11e7-9c02-b6b16f71d116.png)

### 2.Neive Optical Flow -
It is the Neive Optical flow implementation of tracking problem.Here we are providing the whole frames as input and it produces Colour bolbs on analysis of moving pixels Particles.
#### To-do - 
- produce a K-Mean based rectangle on the moving detected bolbs.

#### Result -
![img4](https://cloud.githubusercontent.com/assets/16621282/23577941/9bb235e2-00f1-11e7-9c49-02114dce59bb.png)

### 3.Lucas Tracker - 
It is the the improved implementation of Neive optical flow on Opencv-3. It marks moving pixel particles as green dots and track the particles only.It is a very powerful algorithm and a faster one also. 

#### To-do - 
- Applying Lucas tracker on detected box only.
- Creating a Multi-tracker framework based on Lucas Kannade tracker
- Applying Back-ground substraction for this implementation

#### Results -
![img3](https://cloud.githubusercontent.com/assets/16621282/23577907/11b4de4e-00f1-11e7-95ff-615b0d983126.png)

### video.py - 
It is the Opencv inbulit video module that gives video visualization,Processing time and performance analysis.

### testpy
It is the basic python implementation for the Cascade reading and vehicle detection tasks.
