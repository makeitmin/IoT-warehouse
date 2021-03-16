# IoT_warehouse
This was conducted in Smart Factory Device Control class(Python+IoT). We use EV3 Mindstorm Education Core set and Python to make simple Smart IoT Warehouse. Two machines(Robot Arm & Color Sorter) publish and subscribe JSON data through IBM Cloud. When Color Sorter classify color blocks, its color sensor reads color data and publishes it to Cloud. Then Robot Arm which subscribes the cloud receives data. It counts the number of color blocks and makes different movements to bring box filled with color blocks.

## Prerequisites
- EV3 mindstorm education core set (2 sets for robot arm and color sorter)
- Python 3.8
- Visual Studio Code(+ ev3dev module)
- IBM Cloud Account

## Run Files
1. robot_arm.py : move robot arm
2. color_soter.py : move color sorter
