import turtle

def draw_shape():
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(2)
    
    for i in range (1,37):
       x = 1
       while x <= 4:
             brad.forward(100)
             brad.right(90)
             x += 1
       brad.right(10)
    window.exitonclick()

draw_shape()
