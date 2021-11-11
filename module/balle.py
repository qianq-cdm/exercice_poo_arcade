# Importer arcade
import arcade
import random


class Balle:

    def __init__(self, screen_width, screen_height, x, y):
        self.SCREEN_WIDTH = screen_width
        self.SCREEN_HEIGHT = screen_height
        self.x = x
        self.y = y
        self.change_x = random.randint(-10, 10)
        self.change_y = random.randint(-10, 10)
        self.rayon = random.randint(10, 30)
        self.color = arcade.csscolor.AZURE

    def update(self):
        self.x += self.change_x
        self.y += self.change_y

        if (self.x - self.rayon) < 0 or (self.x + self.rayon) > self.SCREEN_WIDTH:
            self.change_x = self.change_x * -1

        if (self.y - self.rayon) < 0 or (self.y + self.rayon) > self.SCREEN_HEIGHT:
            self.change_y = self.change_y * -1

    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, self.rayon, self.color)
