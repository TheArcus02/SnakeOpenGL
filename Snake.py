from OpenGL.GL import *

class Snake:
    def __init__(self):
        self.positions = [(0, 0)]
        self.direction = (1, 0)

    def move(self):
        head_x, head_y = self.positions[0]
        dir_x, dir_y = self.direction
        new_head = (head_x + dir_x, head_y + dir_y)
        self.positions = [new_head] + self.positions[:-1]

    def grow(self):
        tail = self.positions[-1]
        self.positions.append(tail)

    def change_direction(self, direction):
        self.direction = direction

    def draw_head(self, head_texture):
        glColor3f(1.0, 1.0, 1.0)
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, head_texture)
        glBegin(GL_QUADS)
        x, y = self.positions[0]
        x_center = x + 0.5  # Przesuń do środka kwadratu planszy
        y_center = y + 0.5
        glTexCoord2f(0.0, 0.0); glVertex3f(x_center - 0.5, y_center - 0.5, 0)
        glTexCoord2f(1.0, 0.0); glVertex3f(x_center + 0.5, y_center - 0.5, 0)
        glTexCoord2f(1.0, 1.0); glVertex3f(x_center + 0.5, y_center + 0.5, 0)
        glTexCoord2f(0.0, 1.0); glVertex3f(x_center - 0.5, y_center + 0.5, 0)
        glEnd()
        glDisable(GL_TEXTURE_2D)

    def draw_body(self, body_texture):
        glColor3f(1.0, 1.0, 1.0)
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, body_texture)
        glBegin(GL_QUADS)
        for (x, y) in self.positions[1:]:
            x_center = x + 0.5  # Przesuń do środka kwadratu planszy
            y_center = y + 0.5
            glTexCoord2f(0.0, 0.0); glVertex3f(x_center - 0.5, y_center - 0.5, 0)
            glTexCoord2f(1.0, 0.0); glVertex3f(x_center + 0.5, y_center - 0.5, 0)
            glTexCoord2f(1.0, 1.0); glVertex3f(x_center + 0.5, y_center + 0.5, 0)
            glTexCoord2f(0.0, 1.0); glVertex3f(x_center - 0.5, y_center + 0.5, 0)
        glEnd()
        glDisable(GL_TEXTURE_2D)