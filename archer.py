#Draius Disimone
#CMPT120

from graphics import *
import math

def location(pt1, circle):
    dx = pt1.getX() - circle.getCenter().getX()
    dy = pt1.getY() - circle.getCenter().getY()
    
    dist = math.sqrt(dx * dx + dy * dy)

    return dist <= circle.getRadius()
    
def main():
    win = GraphWin("Archer Table" , 1000 , 1000)
    yellow = Circle(Point(500 , 500) , 75)
    white = Circle(Point(500 , 500) , 375)
    black = Circle(Point(500 , 500) , 300)
    red = Circle(Point(500 , 500) , 150)
    blue = Circle(Point(500 , 500) , 225)
    
    yellow.setFill("yellow")
    white.setFill("white")
    black.setFill("black")
    red.setFill("red")
    blue.setFill("blue")
   
    yellow.draw(win)
    white.draw(win)
    black.draw(win)
    red.draw(win)
    blue.draw(win)
    
    score = 0
    total = 0

    for i in range(5):
        mouse = win.getMouse()
        if location(mouse , yellow):
            score = 90
        elif locationn(mouse , red):
            score = 70
        elif location(mouse , blue):
            score = 50
        elif locationn(mouse , black):
            score = 30
        elif location(mouse , white):
            score = 10
        print("Your click was worth " , score , " points")
        total += score
    print("Total Score = " , total)

main()
