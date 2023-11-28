import turtle
import random


t = turtle.Turtle()
w = turtle.Screen()
t.speed(0)
w.bgcolor("black")
t.color("white")
w.title("Sky")


def stars():
    for i in range(5):
        t.fd(10)
        t.right(144)


for i in range(100):

    x = random.randint(-640, 640)
    y = random.randint(-330, 330)
    stars()


    t.up()
    t.goto(x, y)
    t.down()



t.hideturtle()


# import turtle

# screen = turtle.Screen()

# screen.bgcolor("gray")
# pen = turtle.Turtle()

# pen.pencolor("black")
# pen.pensize(2)  

# pixels_per_inch = 10  
# pen.penup()
# pen.goto(-350, -48)
# pen.pendown()

# pen_length = 700
# pen.forward(pen_length)

"""Hi Alice, unfortunately, the above commented codes did not finish as i tried to. if you uncomment these codes, you will see that I tried define a line where it splits the sky and the road in two different colors but it did not go as I planned, However, I left those codes there if you would like to go through"""
import turtle 

def draw_car():
    screen= turtle.Screen()

    car= turtle.Turtle()

    car.pencolor("black")
    car.pensize(2)


    car.fillcolor("pink")
    car.begin_fill()
    car.goto(-200,-280)
    car.forward(370)
    car.left(90)
    car.forward(100)
    car.left(90)
    car.forward(370)
    car.left(90)
    car.forward(100)
    car.end_fill()


    car.fillcolor("deeppink1")
    car.begin_fill()
    car.penup()
    car.goto(-100, -200)
    car.pendown() 
    car.left(90)
    car.forward(150) 
    car.left(90)
    car.forward(80) 
    car.left(90)
    car.forward(150)
    car.left(90)
    car.forward(80)
    car.end_fill()


    car.penup()
    car.goto(-150,-290)
    car.pendown()
    car.fillcolor("white")
    car.begin_fill()
    car.circle(30)
    car.end_fill()

    car.penup()
    car.goto(20, -290)
    car.pendown()
    car.fillcolor("white")
    car.begin_fill()
    car.circle(30)
    car.end_fill()
    # #draw the window 
    car.penup()
    car.goto(-80,-180)
    car.pendown()
    car.fillcolor("white")
    car.left(90)
    car.forward(40)
    car.left(90)
    car.forward(40)
    car.left(90)
    car.forward(40)
    car.left(90)
    car.forward(40)
    car.end_fill() 

    car.penup()
    car.goto(-10,-180)
    car.pendown()
    car.fillcolor("white")
    car.left(90)
    car.forward(40)
    car.left(90)
    car.forward(40)
    car.left(90)
    car.forward(40)
    car.left(90)
    car.forward(40)
    car.end_fill() 
    screen.exitonclick()
    w.exitonclick()

draw_car()