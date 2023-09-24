import turtle

import time

BC = 'DodgerBlue4'

def draw_moon():

    turtle.pencolor(BC)

    turtle.fillcolor( 'Gold')

    turtle.penup()

    turtle.goto( -150, 0)

    turtle.pendown()

    turtle.begin_fill()

    turtle.circle( 110)

    turtle.end_fill()

def draw_mountain():

    turtle.fillcolor( 'grey21')

    turtle.pencolor( 'grey31')

    turtle.pensize( 4)

    turtle.penup()

    turtle.goto( -500, -250)

    turtle.begin_fill()

    turtle.pendown()

    turtle.left(15)

    turtle.forward( 400)

    turtle.right( 30)

    turtle.forward( 200)

    turtle.left( 40)

    turtle.forward( 300)

    turtle.right( 50)

    turtle.forward( 300)

    turtle.goto( 500, -300)

    turtle.goto( -500, -300)

    turtle.end_fill()

def draw_cloud():

    step = 1.5

    angle = 3

    disize = 0.6

    psize = 5

    turtle.pencolor('WhiteSmoke')

    turtle.pencolor('Gainsboro')

    turtle.pensize(psize)

    turtle.penup()

    turtle.goto( -500, 200)
    
    turtle.pendown()
    
    turtle.forward( 250)

    for i in range( 30):

        psize += disize

        turtle.pensize(psize)

        turtle.right(angle)

        turtle.forward(step)

        for i in range( 30):

                psize -= disize

                turtle.pensize(psize)

                turtle.right(angle)

                turtle.forward(step)

                turtle.forward( 100)

                for i in range( 30):

                    psize += disize

                    turtle.pensize(psize)

                    turtle.left(angle)

                    turtle.forward(step)

                    for i in range( 30):

                        psize -= disize

                        turtle.pensize(psize)

                        turtle.left(angle)

                        turtle.forward(step)

                        turtle.forward( 600)

def draw_init():

    turtle.setup( 1000, 600)
    
    turtle.bgcolor(BC)
    
    turtle.speed( 8) 

def main():

    draw_init()

    draw_moon()

    draw_cloud()

    draw_mountain()

    turtle.exitonclick() 

main()