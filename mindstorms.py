import turtle

def draw_shape():
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(2)
    x = 1
    for i in range (1,37):
       while x <= 4:
             brad.forward(100)
             brad.right(90)
             x += 1
       brad.right(10)
    
    angie = turtle.Turtle()
    angie.circle(50)
    angie.shape("turtle")
    angie.color("blue")
    angie.speed(1)

    olive = turtle.Turtle()
    olive.shape("turtle")
    olive.color("gray")
    x = 1
    while x <= 2:
        olive.right(60)
        olive.forward(100)
        x+=1
    olive.right(150)
    
    olive.forward(155)

    window.exitonclick()

draw_shape()
