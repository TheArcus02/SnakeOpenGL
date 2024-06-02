import random
from OpenGL.GL import *

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
        x_center = self.position[0] + 0.5  # Przesuń do środka kwadratu planszy
        y_center = self.position[1] + 0.5
        glTexCoord2f(0.0, 0.0);
        glVertex3f(x_center - 0.5, y_center - 0.5, 0)
        glTexCoord2f(1.0, 0.0);
        glVertex3f(x_center + 0.5, y_center - 0.5, 0)
        glTexCoord2f(1.0, 1.0);
        glVertex3f(x_center + 0.5, y_center + 0.5, 0)
        glTexCoord2f(0.0, 1.0);
        glVertex3f(x_center - 0.5, y_center + 0.5, 0)
        glEnd()
        glDisable(GL_TEXTURE_2D)