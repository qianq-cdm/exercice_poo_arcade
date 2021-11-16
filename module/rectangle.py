"""
Fait par: Qian Qian
Groupe: 407
La classe de rectangle
"""

# Importer arcade
import arcade
import random


class Rectangle:

    def __init__(self, screen_width, screen_height, x, y):
        """
        Initializer le rectangle
        :param screen_width: largeur d'écran
        :param screen_height: hauteur d'écran
        :param x: la coordination x de rectangle
        :param y: la coordination x de rectangle
        """
        self.SCREEN_WIDTH = screen_width
        self.SCREEN_HEIGHT = screen_height
        self.x = x
        self.y = y
        # Largeur de rectangle
        self.width = random.randint(10, 30)
        # Hauteur de rectangle
        self.height = random.randint(10, 30)
        # Les directions de mouvement pour le rectangle
        self.change_x = random.randint(-10, 10)
        self.change_y = random.randint(-10, 10)
        # Le couleur de rectangle
        self.color = arcade.csscolor.AZURE
        # L'angle de rectangle
        self.angle = random.randint(0, 360)

    def update(self):
        """
        Réactualiser les données de rectangle
        :return: None
        """

        # Nouvelle coordination pour le rectangle
        self.x += self.change_x
        self.y += self.change_y

        # Si la rectangle atteint les côtés, change la direction de mouvement
        if (self.x - self.width) < 0 or (self.x + self.width) > self.SCREEN_WIDTH:
            self.change_x = self.change_x * -1

        if (self.y - self.height) < 0 or (self.y + self.height) > self.SCREEN_HEIGHT:
            self.change_y = self.change_y * -1

    def draw(self):
        """
        Dessiner le rectangles avec les nouvelles données
        :return: None
        """
        arcade.draw_rectangle_filled(self.x, self.y, self.width, self.height, self.color, self.angle)
