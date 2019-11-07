import turtle
import time
import math

def polypon(n): 
    for i in range(n):
        pen.fd(50)
        pen.left(360/n)
    
def arc(p,r,angle):
    L = 2 * math.pi * r *angle/360
    n = int(L / 3) + 1
    length = L / n

    
if __name__ == '__main__':
    pen = turtle.Turtle()
    

    turtle.exitonclick()
###############################################################################33

