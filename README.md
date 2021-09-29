# Calibrate-Huion-Pen
Tutorial on how to calibrate a Huion Pen that is wrongly calibrated over two displays

Finding the right way how to calibarte a huion pen has cost me much time and effort, and so I decided to make this tutorial

So, you're probably here because you plugged in your second tablet on hdmi or displayport or whatever and your computer successfully detected your device, 
but didn't manage to calibrate the pen correctly. This probably happened because two monitors were plugged in and now the tablet tries to span over the whole area 
of both displays.

Don't panic, there is an easy way to solve this. (Easy as in the linux kind of easy, meaning typing random commands in the shell)



Firstly, open a terminal and type in the command "xrandr".

This will probably look like this:

![](https://github.com/pycppdel/Calibrate-Huion-Pen/blob/master/ol.png)


There you can see the detected devices together with their shortened name to the port they're connected to. 

In this case HDMI-0(which is my standard monitor)
and DP-4(which is the huion tablet I connected via displayport)

Memorize the shortened name and type in the next command "xinput_calibrator --list"

![](https://github.com/pycppdel/Calibrate-Huion-Pen/blob/master/Calibrator.png)

There you can see the id your pen is connected with, in this case 15.

Now, what you need to do is tell your pen to only use the area of the drawing-tablet to move the mouse across.

The last step is now to do exactly that.

Type in the command "xinput map-to-output {PEN_ID} {DISPLAY_NAME}"

Since we have determined the displayname and the id of the pen, (DP-4 and 15), we can use them to pass as arguments
