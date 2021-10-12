from turtle import *
import time
import turtle
import random
from turtle import Turtle, Screen
from random import randint, choice
import turtle as t

wn = t.Screen()

screen = Screen()

print("\n********* Turtle Race **********")
def main():
    A = random.random()
    B = random.random()
    C = random.random()
    D = random.random()
    E = random.random()
    F = random.random()
    G = random.random()
    H = random.random()
    I = random.random()
    J = random.random()
    K = random.random()
    L = random.random()
    M = random.random()
    N = random.random()
    O = random.random()

    window = turtle.Screen()
    window.title("Turtle Race")
    turtle.bgcolor("white")
    turtle.color("black")
    turtle.speed(0)
    turtle.penup()
    turtle.setpos(-140, 200)
    turtle.write("Turtle Race", font=("Arial", 30, "bold"))
    turtle.penup()

    # dirt
    turtle.setpos(-400, -170)
    turtle.color("chocolate")
    turtle.begin_fill()
    turtle.pendown()
    turtle.forward(800)
    turtle.right(90)
    turtle.forward(300)
    turtle.right(90)
    turtle.forward(800)
    turtle.right(90)
    turtle.forward(300)
    turtle.end_fill()

    # startline
    turtle.color("black")
    turtle.shape("square")
    turtle.penup()

    for i in range(1):
        turtle.setpos(-250, -134)
        turtle.stamp()

    for i in range(1):
        turtle.setpos(-250, 146)
        turtle.stamp()

    # finish line
    stamp_size = 20
    square_size = 15
    finish_line = 200
    turtle.color("black")
    turtle.shape("square")
    turtle.shapesize(square_size / stamp_size)
    turtle.penup()

    for i in range(10):
        turtle.setpos(finish_line, (150 - (i * square_size * 2)))
        turtle.stamp()

    for j in range(10):
        turtle.setpos(finish_line + square_size, ((150 - square_size) - (j * square_size * 2)))
        turtle.stamp()

    turtle.hideturtle()

    # Turtle 1
    turtle1 = Turtle()
    turtle1.speed(0)
    turtle1.color(A, B, C)
    turtle1.shape("turtle")
    turtle1.penup()
    turtle1.goto(-250, 100)
    turtle1.pendown()

    # Turtle 2
    turtle2 = Turtle()
    turtle2.speed(0)
    turtle2.color(D, E, F)
    turtle2.shape("turtle")
    turtle2.penup()
    turtle2.goto(-250, 50)
    turtle2.pendown()

    # Turtle 3
    turtle3 = Turtle()
    turtle3.speed(0)
    turtle3.color(G, H, I)
    turtle3.shape("turtle")
    turtle3.penup()
    turtle3.goto(-250, 0)
    turtle3.pendown()

    # Turtle 4
    turtle4 = Turtle()
    turtle4.speed(0)
    turtle4.color(J, K, L)
    turtle4.shape("turtle")
    turtle4.penup()
    turtle4.goto(-250, -50)
    turtle4.pendown()

    # Turtle 5
    turtle5 = Turtle()
    turtle5.speed(0)
    turtle5.color(M, N, O)
    turtle5.shape("turtle")
    turtle5.penup()
    turtle5.goto(-250, -100)
    turtle5.pendown()

    time.sleep(1)  # paused the game for 1 second

    startin_it(turtle1, turtle2, turtle3, turtle4, turtle5)


def startin_it(turtle1, turtle2, turtle3, turtle4, turtle5):
    # screen.onscreenclick()
    for i in range(150):
        # to remove trailing lines
        turtle1.up()
        turtle2.up()
        turtle3.up()
        turtle4.up()
        turtle5.up()
        turtle1.forward(randint(1, 5))
        turtle2.forward(randint(1, 5))
        turtle3.forward(randint(1, 5))
        turtle4.forward(randint(1, 5))
        turtle5.forward(randint(1, 5))

    # stating which of the turtles won
    while True:
        zoom = choice([turtle1, turtle2, turtle3, turtle4, turtle5])
        if zoom.xcor() >= 200:
            zoom.forward(80)
            break
    screen.exitonclick()


if __name__ == "__main__":
    main()
