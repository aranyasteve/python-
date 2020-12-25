import turtle
import time
import random

delay = 0.1

score = 0
high_score = 0

top = turtle.Screen()
top.title("Snake Game")
top.bgcolor("yellow")
top.setup(width=600, height=600)
top.tracer(0)

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color('black')
head.penup()
head.goto(0, 0)
head.direction = "stop"

food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

sc = turtle.Turtle()
sc.speed(0)
sc.shape("square")
sc.color("black")
sc.penup()
sc.hideturtle()
sc.goto(0, 260)
sc.write("Score:0 High Score:0", align="center", font=("ds-digital", 24, "normal"))


def go_up():
    if head.direction != "down":
        head.direction = 'up'


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def go_right():
    if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)


top.listen()
top.onkeypress(go_up, "w")
top.onkeypress(go_down, "s")
top.onkeypress(go_left, "a")
top.onkeypress(go_right, "d")

top.onkeypress(go_up, "Up")
top.onkeypress(go_down, "Down")
top.onkeypress(go_left, "Left")
top.onkeypress(go_right, "Right")

n = ""

while n != ";":
    try:
        top.update()

        if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
            time.sleep(1)
            head.goto(0, 0)
            food.goto(0, 100)
            head.direction = "stop"

            for segment in segments:
                segment.goto(1000, 1000)

            segments.clear()

            score = 0

            delay = 0.1

            sc.clear()
            sc.write("Score {} High Score {}".format(score, high_score), align="center", font=("ds-digital", 24, "normal"))

        if head.distance(food) < 20:
            x = random.randint(-280, 280)
            y = random.randint(-280, 260)
            food.goto(x, y)
            new_segment = turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape("square")
            new_segment.color("red")
            new_segment.penup()
            segments.append(new_segment)

            delay = delay-0.001
            score = score+10

            if score > high_score:
                high_score = score
            sc.clear()
            sc.write("Score {} High Score {}".format(score, high_score), align="center", font=("ds-digital", 24, "normal"))

        for index in range(len(segments)-1, 0, -1):
            x = segments[index-1].xcor()
            y = segments[index-1].ycor()
            segments[index].goto(x, y)

        if len(segments) > 0:
            x = head.xcor()
            y = head.ycor()
            segments[0].goto(x, y)

        move()

        for segment in segments:
            if segment.distance(head) < 20:
                time.sleep(1)
                head.goto(0, 0)
                food.goto(0, 100)
                head.direction = "stop"

                for segment in segments:
                    segment.goto(1000, 1000)
                segments.clear()
                score = 0
                delay = 0.1
                sc.clear()
                sc.write("Score {} High Score {}".format(score, high_score), align="center",
                         font=("ds-digital", 24, "normal"))

        time.sleep(delay)

    except:
        n = ";"
        exit(0)

top.mainloop()

















