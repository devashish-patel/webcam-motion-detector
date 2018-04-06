# Webcam Motion Detector
- Open Source Computer Vision based personal project to detect Human Faces and different objects coming in front of the webcam for a specific time frame.
- Programming Language: Python
- Libraries: OpenCV, Bokeh, Pandas
- For Human Face detection I've used HaarCascade Classifier XML file created by OpenCV.

###  Overview of Project:

------------
- Before you execute the project, please cover your webcam and remove the cover once your webcam starts and you can see some video recording windows on your desktop.
- You will see four different windows on your screen.
 - Color Frame: Which detects the different objects
 - Current Frame: Which detects the human face
 - Delta Frame*: Which compares the current situation the with the initial situation 
 - Threshold frame* - for identification of an object 
 - *not important for end-user
- Try Like this...

 - ![](https://thumbs.gfycat.com/AggravatingThisInsect-size_restricted.gif)
 
- At any moment if you want to stop, please press `q`
- A motion graph will be generated and automatically your default browser will pop-up where you can see it like this...
 - ![](https://thumbs.gfycat.com/SeriousVibrantAppaloosa-size_restricted.gif)



### How to run on your machine!! (Don't worry if you don't have Python installed, I've already taken care of it!)

------------


- Please download or clone this repo from here.
- Extract the folder and reach to the root of the project, by using the command line.
#### MAC Users:
- Write command `venv/bin/python plotting.py`
#### WINDOWS Users:
- Virtual Environment for Windows user will be available soon.

*Suggestions and Questions are always welcomed, please e-mail me at devashish2910@gmail.com or create an issue*
