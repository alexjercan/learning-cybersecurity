# speeds and feeds

[speeds and feeds](https://play.picoctf.org/practice/challenge/116)

## Description

There is something on my shop network running at nc mercury.picoctf.net 59953, but I can't tell what it is. Can you?

## Solution

Searching on google for the first line that we receive we can see that it looks like GCode, a language used by CNC machines to trace paths. This means that we have to somehow display how the final result would look IRL. I have tried some python libraries like gcody and mecode but thet are deprecated and do not work. I have however found an online tool [ncviewer.com/](https://ncviewer.com/) where we can paste the gcode and visualize the plot.