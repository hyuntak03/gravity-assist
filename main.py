from turtle import *
import turtle as z
import math
from matplotlib import pyplot as plt

planet = Turtle()
spaceship = Turtle()

launch_angle = math.radians(90)

z.setup(width = 700, height = 700)
planet.shape("circle")
spaceship.shape("circle")
planet.color("red")
spaceship.color("green")

spaceship.shapesize(0.5,0.5)

spaceship.left(90)
planet.penup()
spaceship.penup()
planet.hideturtle()
spaceship.hideturtle()
planet.goto(-150,0)
spaceship.goto(-200,-100)
planet.showturtle()
spaceship.showturtle()
spaceship.pendown()

G = 6.673e-11
v_x = 1 * math.cos(launch_angle)
v_y = 1 * math.sin(launch_angle)
v = 0
velocity = []

while True:
    distance = math.sqrt((planet.xcor() - spaceship.xcor())**2 + (planet.ycor() - spaceship.ycor())**2)
    if((planet.xcor() - spaceship.xcor()) != 0):
        inclination = (planet.ycor() - spaceship.ycor()) / (planet.xcor() - spaceship.xcor())
    if((planet.xcor() - spaceship.xcor()) == 0):
        inclination = 0;

    angle = math.atan(inclination)
    # gravity = G * ((1.898 * 10**27) * 5000) / (distance)**2
    gravity = 300 / (distance)**2
    #This gravity is not accurate figure

    if(spaceship.xcor() < planet.xcor() and spaceship.ycor() <= planet.ycor()):
        v_x = v_x + gravity * math.cos(angle)
        v_y = v_y + gravity * math.sin(angle)
    if(spaceship.xcor() <= planet.xcor() and spaceship.ycor() > planet.ycor()):
        v_x = v_x + gravity * math.cos(angle)
        v_y = v_y - gravity * math.sin(angle)
    if(spaceship.xcor() > planet.xcor() and spaceship.ycor() >= planet.ycor()):
        v_x = v_x - gravity * math.cos(angle)
        v_y = v_y - gravity * math.sin(angle)
    if(spaceship.xcor() > planet.xcor() and spaceship.ycor() >= planet.ycor()):
        v_x = v_x - gravity * math.cos(angle)
        v_y = v_y + gravity * math.sin(angle)

    dx = spaceship.xcor() + v_x
    dy = spaceship.ycor() + v_y
    seta = math.atan(v_y / v_x)
    v = abs(v_x / math.cos(seta))
    velocity.append(v)
    planet.forward(1)
    spaceship.goto(dx,dy)
    if(planet.xcor() == 350.0):
        break;

plt.plot(velocity)
plt.show()
z.done()