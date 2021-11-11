# Importer arcade
import arcade
import random


class Rectangle:

    def __init__(self, screen_width, screen_height, x, y):
        self.SCREEN_WIDTH = screen_width
        self.SCREEN_HEIGHT = screen_height
        self.x = x
        self.y = y
        self.width = random.randint(10, 30)
        self.height = random.randint(10, 30)
        self.change_x = random.randint(-10, 10)
        self.change_y = random.randint(-10, 10)
        self.color = arcade.csscolor.AZURE
        self.angle = random.randint(0, 360)

    def update(self):
        self.x += self.change_x
        self.y += self.change_y

        if (self.x - self.width) < 0 or (self.x + self.width) > self.SCREEN_WIDTH:
            self.change_x = self.change_x * -1

        if (self.y - self.height) < 0 or (self.y + self.height) > self.SCREEN_HEIGHT:
            self.change_y = self.change_y * -1

    def draw(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.width, self.height, self.color, self.angle)
