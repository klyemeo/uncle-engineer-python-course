import time
from turtle import *
import random


bgcolor('black')
time.sleep(2)
speed(10000)

def Donut():
    for i in range(120):
        pencolor("blue")
        circle(50)
        right(180)
        pencolor("light blue")
        circle(100)
        right(180)


        penup()
        forward(3)
        pendown()

        left(3)
       

Donut()




