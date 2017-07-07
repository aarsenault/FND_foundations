import turtle
import random

guy = turtle.Turtle()
guy.speed(2)
guy.color("black")
guy.shape("turtle")


def randomwalks():
    window = turtle.Screen()
    window.bgcolor("blue")


    while True:

        x = random.random()
        z = random.random()
        y = random.randint(1,100)


        guy.forward(y*x)

        if x > 0.5:
            guy.left(360*x)
        else:
            guy.right(360*z)

randomwalks()



