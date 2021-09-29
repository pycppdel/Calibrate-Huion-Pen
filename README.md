# Calibrate-Huion-Pen
Tutorial on how to calibrate a Huion Pen

Finding the right way how to calibarte a huion pen has cost me much time and effort, and so I decided to make this tutorial

So, you're probably here because you plugged in your second tablet on hdmi or displayport or whatever and your computer successfully detected your device, 
but didn't manage to calibrate the pen correctly. This probably happened because two monitors were plugged in and now the tablet tries to span over the whole area 
of both displays.

Don't panic, there is an easy way to solve this. (Easy as in the linux kind of easy, meaning typing random commands in the shell)



Firstly, open a terminal and type in the command "xrandr".

This will probably look like this:

![](https://github.com/pycppdel/Calibrate-Huion-Pen/blob/master/ol.png)


There you can see the detected devices together with their shortened name to the port they're connected to, in this case HDMI-0(which is my standard monitor)
and DP-4(which is the huion tablet I connected via displayport)
