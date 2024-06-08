from OpenGL.GL import *
from utils import draw_cube

class Snake:
    def __init__(self):
        self.positions = [(0, 0, 0)]
        self.direction = (1, 0, 0)
        self.alive = True

    def move(self):
        head_x, head_y, head_z = self.positions[0]
        dir_x, dir_y, dir_z = self.direction
        new_head = (head_x + dir_x, head_y + dir_y, head_z + dir_z)


        board_width = 19
        board_depth = 15

        # Wrap around for x and z coordinates
        if new_head[0] > board_width:
            new_head = (-board_width + (abs(new_head[0]) - board_width) % (2 * board_width), new_head[1], new_head[2])
        elif new_head[0] < -board_width:
            new_head = (board_width + (abs(new_head[0]) + board_width) % (2 * board_width), new_head[1], new_head[2])

        if new_head[2] > board_depth:
            new_head = (new_head[0], new_head[1], -board_depth)
        elif new_head[2] < -board_depth:
            new_head = (new_head[0], new_head[1], board_depth)

        if new_head in self.positions:
            self.alive = False
            return

        self.positions = [new_head] + self.positions[:-1]

    def grow(self):
        tail = self.positions[-1]
        self.positions.append(tail)

    def change_direction(self, direction):
        opposite_direction = (-self.direction[0], -self.direction[1], -self.direction[2])
        if direction != opposite_direction:
            self.direction = direction

    def draw_head(self, head_texture):
        glColor3f(1.0, 1.0, 1.0)
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, head_texture)
        draw_cube(*self.positions[0])
        glDisable(GL_TEXTURE_2D)

    def draw_body(self, body_texture):
        glColor3f(1.0, 1.0, 1.0)
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, body_texture)
        for pos in self.positions[1:]:
            draw_cube(*pos)
        glDisable(GL_TEXTURE_2D)
