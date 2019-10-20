import turtle


def draw_square(brad):
    for i in range(1, 5):
        brad.forward(100)
        brad.right(90)


def draw_art():
    brad = turtle.Turtle()
    brad.color('yellow')
    brad.shape('turtle')
    brad.speed(2)

    window = turtle.Screen()
    window.setup(800, 600)
    window.bgcolor('red')

    for i in range(1, 37):
        draw_square(brad)
        brad.right(10)

    window.exitonclick()


draw_art()
