# [Script Name]
# Author: [Obaid ur Rahman]
# Date: [29/09/2026]
# Description: [a square with side length 100, an equilateral triangle with side length 100, and a rectangle with width 150 and height 75 using a different color for each shape and use penup() and pendown() between shapes.]

import turtle

t = turtle.Turtle()
t.speed(3)

#Draw square
t.color("blue")
for i in range(4):
    t.forward(100)
    t.right(90)

#Move to new location
t.penup()
t.goto(150, 0)
t.pendown()

#Draw triangle
t.color("red")
for i in range(3):
    t.forward(100)
    t.left(120)

#Move to new location
t.penup()
t.goto(-200, 0)
t.pendown()

#Draw rectangle
t.color("green")
for i in range(2):
    t.forward(150)
    t.right(90)
    t.forward(75)
    t.right(90)

turtle.done()