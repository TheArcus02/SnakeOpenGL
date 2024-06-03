import random
from OpenGL.GL import *
from utils import draw_squere
class Food:
    def __init__(self):
        self.position = (random.randint(-9, 9), random.randint(-9, 9))

    def respawn(self):
        self.position = (random.randint(-9, 9), random.randint(-9, 9))

    def draw(self, food_texture):
        glColor3f(1.0, 1.0, 1.0)
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, food_texture)
        glBegin(GL_QUADS)
        draw_squere(self.position[0], self.position[1])
        glEnd()
        glDisable(GL_TEXTURE_2D)