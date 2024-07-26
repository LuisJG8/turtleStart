from turtle import Turtle, Screen
import random

colors = ("red", "blue", "green", "brown", "yellow", "purple", "black", "cyan", "brown", "orange")

tim = Turtle()

tim.shape("turtle")

# Challenge 1

# for i in range(3, 11):
#     new_angle = 360 / i
#
# for sides in range(3, 11):
#     tim.forward(100)
#     tim.right(new_angle)

# Solution
# def draw_shape(number_of_sides):
#     new_angle = 360 / number_of_sides
#     for sides in range(number_of_sides):
#         tim.forward(100)
#         tim.right(new_angle)
#
#
# for i in range(3, 11):
#     colors = random.choice(ran_color)
#     tim.color(colors)
#     draw_shape(i)

# # Challenge 2
#
# random_move = [tim.right(10), tim.left(10)]
#
# def move_random(thing):

move_left = [tim.left(90), tim.forward(90), tim.right(90), tim.forward(90)]

randoms = random.choice(move_left)

for i in range(0, 100):
    random.choice(move_left)

screen = Screen()
screen.exitonclick()