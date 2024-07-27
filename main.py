from turtle import Turtle, Screen
import random

colors = ("red", "blue", "green", "brown", "yellow", "purple", "black", "cyan", "brown", "orange")
tim = Turtle()

tim.shape("turtle")

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

random_walk = [0, 90, 180, 270]
t_size = tim.pensize(12)
tim.speed("fast")

for i in range(0, 300, ):
    tim.forward(30)
    tim.color(random.choice(colors))
    tim.setheading(random.choice(random_walk))


screen = Screen()
screen.exitonclick()
