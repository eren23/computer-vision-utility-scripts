# Utility Scripts for Computer Vision Projects

In this repo I want to share scripts that I found myself writing over and over when I work on computer vision projects. Can be the code I found online, I can share directly or I can change them a bit, I'll also share some of my own.

### Image Collector From Video Feed

Use video recordings or your webcam to harvest images from video feed.
Inspired from [here](https://github.com/nicknochnack/TFODCourse), removed some parts because I needed faster image creation so I gave up on the automated process.


### Face Collector From Video Feed

Same logic from the image collector script, only addition is this time we use cvlib to first detect faces and then we crop our camera feed to save faces only.

