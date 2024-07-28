import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.speed("fastest")
# for i in range(3, 11):
#     new_angle = 360 / i
#
# for sides in range(3, 11):
#     tim.forward(100)
#     tim.right(new_angle)

# def draw_shape(number_of_sides):
#     new_angle = 360 / number_of_sides
#     for sides in range(number_of_sides):
#         tim.forward(100)
#         tim.right(new_angle)
#
# for i in range(3, 11):
#     colors_ran = random.choice(colors)
#     tim.color(colors_ran)
#     draw_shape(i)

# random_walk = [0, 90, 180, 270]
# t_size = tim.pensize(12)
# tim.speed("fast")
turtle.colormode(255)
#
def random_colors():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color
#
# for i in range(0, 300):
#     tim.forward(30)
#     tim.color(random_colors())
#     tim.setheading(random.choice(random_walk))

# it makes a donut
# for _ in range(0, 40):
#     tim.circle(100)
#     tim.tilt(3)
#     tim.circle(50, 50, 50)

tim.setposition(0, 0)

for _ in range(0, 75):
    tim.color(random_colors())
    current_h = tim.heading()
    tim.setheading(current_h + 5)
    tim.circle(100)

screen = Screen()
screen.exitonclick()
