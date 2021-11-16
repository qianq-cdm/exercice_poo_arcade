"""
Fait par: Qian Qian
Groupe: 407
La classe de balle
"""

# Importer arcade
import arcade
import random


class Balle:

    def __init__(self, screen_width, screen_height, x, y):
        """
        Initializer la balle
        :param screen_width: largeur d'écran
        :param screen_height: hauteur d'écran
        :param x: la coordination x de la balle
        :param y: la coordination x de la balle
        """
        self.SCREEN_WIDTH = screen_width
        self.SCREEN_HEIGHT = screen_height
        self.x = x
        self.y = y
        # Les directions de mouvement de la balle
        self.change_x = random.randint(-10, 10)
        self.change_y = random.randint(-10, 10)
        # La grandeur de la balle
        self.rayon = random.randint(10, 30)
        # La couleur de la balle
        self.color = arcade.csscolor.AZURE

    def update(self):
        """
        Réactualiser les données de la balles
        :return: None
        """

        # Nouvelle coordination pour la balle
        self.x += self.change_x
        self.y += self.change_y

        # Si la balle atteint les côtés, change la direction de mouvement
        if (self.x - self.rayon) < 0 or (self.x + self.rayon) > self.SCREEN_WIDTH:
            self.change_x = self.change_x * -1

        if (self.y - self.rayon) < 0 or (self.y + self.rayon) > self.SCREEN_HEIGHT:
            self.change_y = self.change_y * -1

    def draw(self):
        """
        Dessiner la balle avec les nouvelles données
        :return: None
        """
        arcade.draw_circle_filled(self.x, self.y, self.rayon, self.color)
