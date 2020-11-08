from turtle import *
import turtle as z
import math
from matplotlib import pyplot as plt

jupiter = Turtle()
saturn = Turtle()
spaceship = Turtle()
s2 = Turtle()

launch_angle = math.radians(90)

z.setup(width = 700, height = 700)
jupiter.shape("circle")
saturn.shape("circle")
spaceship.shape("circle")
jupiter.color("red")
saturn.color("brown")
spaceship.color("green")
s2.color("blue")

spaceship.shapesize(0.5,0.5)
s2.shapesize(0.5,0.5)

jupiter.penup()
spaceship.penup()
s2.penup()
saturn.penup()

saturn.hideturtle()
jupiter.hideturtle()
spaceship.hideturtle()
s2.hideturtle()

jupiter.goto(-150,0)
spaceship.goto(-170,-100)
s2.goto(-170,-100)
saturn.goto(-90,100)
saturn.showturtle()
jupiter.showturtle()
spaceship.showturtle()
spaceship.pendown()

G = 6.673e-11
v_x = 1 * math.cos(launch_angle)
v_y = 1 * math.sin(launch_angle)
v_x_2 = 1 * math.cos(launch_angle)
v_y_2 = 1 * math.sin(launch_angle)
v = 0
v_2 = 0
velocity = []
velocity_2 = []

while True:
    distance = math.sqrt((jupiter.xcor() - spaceship.xcor())**2 + (jupiter.ycor() - spaceship.ycor())**2)
    distance_saturn = math.sqrt((saturn.xcor() - spaceship.xcor())**2 + (saturn.ycor() - spaceship.ycor())**2)

    if((jupiter.xcor() - spaceship.xcor()) != 0):
        inclination = (jupiter.ycor() - spaceship.ycor()) / (jupiter.xcor() - spaceship.xcor())
    if((jupiter.xcor() - spaceship.xcor()) == 0):
        inclination = 0;

    if((saturn.xcor() - spaceship.xcor()) != 0):
        inclination_saturn = (jupiter.ycor() - spaceship.ycor()) / (jupiter.xcor() - spaceship.xcor())
    if((saturn.xcor() - spaceship.xcor()) == 0):
        inclination_saturn = 0;

    angle_saturn = math.atan(inclination_saturn)
    angle = math.atan(inclination)
    # gravity = G * ((1.898 * 10**27) * 5000) / (distance)**2
    gravity = 300 / (distance)**2
    gravity_saturn = 300 / (distance_saturn)**2
    #This gravity is not accurate figure

    if(spaceship.xcor() < jupiter.xcor() and spaceship.ycor() <= jupiter.ycor()):
        v_x = v_x + gravity * math.cos(angle)
        v_y = v_y + gravity * math.sin(angle)
        v_x_2 += gravity * math.cos(angle)
        v_y_2 += gravity * math.sin(angle)
    if(spaceship.xcor() <= jupiter.xcor() and spaceship.ycor() > jupiter.ycor()):
        v_x = v_x + gravity * math.cos(angle)
        v_y = v_y - gravity * math.sin(angle)
        v_x_2 += gravity * math.cos(angle)
        v_y_2 -= gravity * math.sin(angle)
    if(spaceship.xcor() > jupiter.xcor() and spaceship.ycor() >= jupiter.ycor()):
        v_x = v_x - gravity * math.cos(angle)
        v_y = v_y - gravity * math.sin(angle)
        v_x_2 -= gravity * math.cos(angle)
        v_y_2 -= gravity * math.sin(angle)
    if(spaceship.xcor() > jupiter.xcor() and spaceship.ycor() >= jupiter.ycor()):
        v_x = v_x - gravity * math.cos(angle)
        v_y = v_y + gravity * math.sin(angle)
        v_x_2 -= gravity * math.cos(angle)
        v_y_2 += gravity * math.sin(angle)

    if(spaceship.xcor() < saturn.xcor() and spaceship.ycor() < saturn.ycor()):
        v_x = v_x + gravity_saturn * math.sin(angle_saturn)
        v_y = v_y + gravity_saturn * math.sin(angle_saturn)
    if(spaceship.xcor() <= saturn.xcor() and spaceship.ycor() > saturn.ycor()):
        v_x = v_x + gravity_saturn * math.cos(angle_saturn)
        v_y = v_y - gravity_saturn * math.sin(angle_saturn)
    if(spaceship.xcor() > saturn.xcor() and spaceship.ycor() >= saturn.ycor()):
        v_x = v_x - gravity_saturn * math.cos(angle_saturn)
        v_y = v_y - gravity_saturn * math.sin(angle_saturn)
    if(spaceship.xcor() > jupiter.xcor() and spaceship.ycor() >= jupiter.ycor()):
        v_x = v_x - gravity_saturn * math.cos(angle_saturn)
        v_y = v_y + gravity_saturn * math.sin(angle_saturn)

    dx = spaceship.xcor() + v_x
    dy = spaceship.ycor() + v_y
    dx_2 = s2.xcor() + v_x_2
    dy_2 = s2.ycor() + v_y_2

    seta = math.atan(v_y / v_x)
    seta_2 = math.atan(v_y / v_x)

    v = abs(v_x / math.cos(seta))
    v_2 = abs(v_x_2 / math.cos(seta_2))

    velocity.append(v)
    velocity_2.append(v_2)
    jupiter.forward(1)
    saturn.forward(1)
    spaceship.goto(dx,dy)
    s2.goto(dx_2,dy_2)

    if(jupiter.xcor() == -50.0):
        break;

plt.title("Velocity of Space Ship")
plt.plot(velocity)
plt.show()
z.done()