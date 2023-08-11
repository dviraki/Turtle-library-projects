from turtle import Turtle
import random

FOOD_POSSIBLE_POSITION_X = -200
FOOD_POSSIBLE_POSITION_Y = 200


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.generate_food()

    def generate_food(self):
        random_x = random.randint(FOOD_POSSIBLE_POSITION_X, FOOD_POSSIBLE_POSITION_Y)
        random_y = random.randint(FOOD_POSSIBLE_POSITION_X, FOOD_POSSIBLE_POSITION_Y)
        self.goto(random_x, random_y)
