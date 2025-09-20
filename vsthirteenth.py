#Snake Game

import turtle
import random
import time

delay=0.1
sc=0
hs=0

s=turtle.Screen()
s.title("Snake Game")
s.bgcolor("light blue")
s.setup(width=600,height=600)

head=turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("blue")
head.fillcolor("red")
head.penup()
head.goto(0,0)
head.direction="stop"

head=turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("red")
head.fillcolor("blue")
head.penup()
head.ht()
head.goto(150,200)
head.st()

sb=turtle.Turtle()
sb.penup()
sb.ht()
sb.goto(-250,250)
sb.st()

sb.write("Score:0   |   Highest Score:0")

def moveUp():
    if head.direction!="down":
        head.direction="up"
def moveDown():
    if head.direction!="up":
        head.direction="down"
def moveLeft():
    if head.direction!="right":
        head.direction!="left"
def moveRight():
    if head.direction!="left":
        head.direction!="right"
def moveStop():
    head.direction="stop"

def move():
    if head.direction=="up":
        y=head.ycor()
        head.sety(y+20)
    if head.direction=="left":
        x=head.xcor()
        head.setx(x-20)
    if head.direction=="down":
        y=head.ycor()
        head.sety(y-20)
    if head.direction=="right":
        x=head.xcor()
        head.setx(x+20)