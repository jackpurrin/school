# i CANNOT code very well in python! but, https://docs.python.org/3/library/tkinter.html was a life saver when writing this project!
# hopefully by the end of the school year, i can write better python code!

# importing stuff to actually draw the window and traffic lights!
from tkinter import ttk
from turtle import *
import time

def init():
    tracer(False) # helped me remove the turtle animation! https://stackoverflow.com/questions/59119036/how-do-i-make-a-turtle-run-faster#59119526 

def circle(total_degrees, x, y, t_color):
    color(t_color)
    teleport(x,y) # sets the x and y of where the bottom of the circle should be, useful for setting the position so i can have 3 circles. one for each light of a traffic light!
    begin_fill()
    while total_degrees != 0: # i forgot how loops work in python, w3 schools is a great resource!
        forward(1) # moves the turtle by one pixel
        left(1) # turns it left by one pixel
        total_degrees -= 1 # removes one degree, so it doesn't loop forever. you shouldn't usually need to use more than 365 tho.
    end_fill()

init()
circle(365, 0, 120, 0, "red")
