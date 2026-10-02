
# [creative.py]
# Author: [Obaid ur Rahman]
# Date: [02/10/2026]
# Description: [This script draws a simple house using different shapes and colors.]

import turtle

t = turtle.Turtle()
t.speed(5)

# move location
t.penup()
t.goto(-200,0)
t.pendown()


#Draw Rectangle
t.color("Red")
for i in range(2):
    t.forward(400)
    t.right(90)
    t.forward(200)
    t.right(90)



# move to new location
t.penup()
t.goto(-200,0)
t.pendown()

# Draw Triangle
t.color("Green")
for i in range(3):
    t.forward(200)
    t.left(120)

# new location
t.penup()
t.goto(0,0)
t.pendown()

# new shape
t.color("Blue")
for i in range(1):
    t.left(120)
    t.forward(200)
    t.right(120)
    t.forward(300)
    t.right(90)
    t.forward(180)

# new location
t.penup()
t.goto(0,0)
t.pendown()

# new square
t.color("Purple")
for i in range(4):
    t.forward(200)
    t.right(90)

# new location
t.penup()
t.goto(-50,-100)
t.pendown()

# new rectangle(door)
t.color("Brown")
for i in range(2):
    t.forward(100)
    t.right(90)
    t.forward(75)
    t.right(90)

# new location
t.penup()
t.goto(-115,-150)
t.pendown()

# door handle
t.color("Yellow")
t.circle(5)
t.fillcolor("Yellow")

#new location
t.penup()
t.goto(150,100)
t.pendown()

# new rectangle(window)
t.color("Light Blue")
for i in range(2):
    t.forward(50)
    t.right(90)
    t.forward(100)
    t.right(90)


turtle.done()
