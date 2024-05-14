
from turtle import *

#effects
goto(-5, -5)
width(7)
color("purple")
#draw squar
begin_fill()
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
end_fill()
#draw roof
penup()
goto(200, 200)
left(120)
pendown()
color("red")
begin_fill()
forward(200)
left(120)
forward(200)
end_fill()
#draw door
penup()
goto(70, 0)
right(150)
color("yellow")
pendown()
begin_fill()
forward(100)
right(90)
forward(60)
right(90)
forward(100)
end_fill()
goto(75, 55)
color("brown")
forward(1)
#draw windows
color("green")
penup()
begin_fill()
goto(50, 180)
pendown()
forward(70)
right(90)
forward(40)
right(90)
forward(70)
right(90)
forward(40)
end_fill()

right(90)
penup()
begin_fill()
goto(150, 180)
pendown()
forward(70)
left(90)
forward(40)
left(90)
forward(70)
left(90)
forward(40)
end_fill()
exc







exitonclick()