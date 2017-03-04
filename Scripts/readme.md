
# Scripts

##### This directory contains all the python scripts used in this project. It contains three basic tracking scripts, one Cascade testing script and a video opencv inbuilt video script for Result video visualization.

### Tracking Script

#### 1.multi-tracker.py - 
It is implemented on Opencv-3.1 Multitracker module. It implements the idea of Dection using Opencv Haar/LBP Cascades in every `5th` frames and then Tracking the detected vehicles using Opencv Multi-tracker Module. Opencv provides 6 different trackers such as  BOOSTING, MIL, KCF, TLD, MEDIANFLOW, and GOTURN from which MIL and KCF are the most efficient one for out project.
###### The basic script is written for KCF tracker but you can change the argument in code for any of the six trackers.

###### Though it's the easiest and most efficient implementaion But it does not satisfy our purpose as IOS does not provide KCf inbuilt tracker.

#### Results -

[img2](https://cloud.githubusercontent.com/assets/16621282/23577791/73010068-00ee-11e7-9777-553b6f6df18a.png)



