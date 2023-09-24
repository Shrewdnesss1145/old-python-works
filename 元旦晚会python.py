import turtle
import random 
turtle.setup(600, 700) 
turtle.colormode(255) 
turtle.bgcolor((255, 182, 193)) 
turtle.tracer(False) 
turtle.hideturtle() 


turtle.penup() 
turtle.goto(-260, -320)
turtle.pendown() 


turtle.color((219, 112, 147))
turtle.begin_fill()
for i in range(2):
    turtle.forward(520)
    turtle.left(90) 
    turtle.forward(640)
    turtle.left(90)
turtle.end_fill()


turtle.penup() 
turtle.goto(0, -280)
turtle.pendown()

turtle.color((255,250,250))
turtle.begin_fill()
turtle.circle(200)
turtle.end_fill()


turtle.color((245, 245, 245))
turtle.setheading(0)


turtle.penup()
turtle.goto(-150, 230)
turtle.pendown() 
turtle.write('希望同学和老师们', font = ('space mono', 30,'bold'))


turtle.penup()
turtle.goto(-110, 180)
turtle.pendown()
turtle.write('身体健康，万事如意', font = ('space mono', 30, 'bold'))


turtle.penup()
turtle.goto(-200, 120)
turtle.pendown()
turtle.write('学习积极向上，奋发直追!', font = ('space mono', 30, 'bold'))


turtle.penup()
turtle.goto(140, -250)
turtle.pendown()
turtle.write('杨嘉诚', font = ('space mono', 20, 'bold'))


def draw_tree(length):    
    if length > 20:
        turtle.color((128, 128, 128))
        turtle.pensize(length / 10)
        turtle.forward(length)
        angle = random.randint(10, 30)
        number = random.randint(5, 15)
        turtle.right(angle)
        draw_tree(length - number)
        turtle.left(angle*2)
        draw_tree(length - number)
        turtle.right(angle)
        turtle.backward(length)
    else:
        turtle.color((50, 205, 50))
        turtle.begin_fill()
        turtle.circle(8, 90)
        turtle.left(90)
        turtle.circle(8, 90)
        turtle.left(90)
        turtle.end_fill()
        turtle.color((0, 100, 0))

       
def draw_mill():
    colors = [(193, 203, 215), (234, 208, 209), (134, 150, 167), (150, 140, 139)]
    turtle.pensize(5)
    turtle.pencolor((105, 105, 105))
    turtle.penup()
    turtle.goto(0, -280)
    turtle.pendown()
    turtle.goto(0, -50)
    for i in range(4):
        turtle.fillcolor(colors[i])
        turtle.begin_fill()
        turtle.setheading(i * 90)
        turtle.forward(150)
        turtle.left(150)
        turtle.forward(100)
        turtle.goto(0, -50)
        turtle.end_fill()


turtle.setheading(90)
turtle.penup() 
turtle.goto(0, -280)
turtle.pendown()

#调用draw_tree(参数) draw_mill()
draw_tree(75)
































