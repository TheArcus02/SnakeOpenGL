import random
from OpenGL.GL import *
from utils import draw_cube

class Food:
    def __init__(self):
        self.position = (random.randint(-9, 9), 0, random.randint(-9, 9))

    def respawn(self):
        self.position = (random.randint(-9, 9), 0, random.randint(-9, 9))

    def draw(self, food_texture):
        glColor3f(1.0, 1.0, 1.0)
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, food_texture)
        draw_cube(*self.position)
        glDisable(GL_TEXTURE_2D)
