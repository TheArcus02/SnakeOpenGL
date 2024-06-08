from OpenGL.GL import *
import numpy as np
from PIL import Image
import pygame

def draw_cube(x, y, z, size=1.0):
    vertices = [
        (x-size/2, y-size/2, z-size/2),
        (x+size/2, y-size/2, z-size/2),
        (x+size/2, y+size/2, z-size/2),
        (x-size/2, y+size/2, z-size/2),
        (x-size/2, y-size/2, z+size/2),
        (x+size/2, y-size/2, z+size/2),
        (x+size/2, y+size/2, z+size/2),
        (x-size/2, y+size/2, z+size/2)
    ]

    faces = [
        (0, 1, 2, 3),
        (3, 2, 6, 7),
        (7, 6, 5, 4),
        (4, 5, 1, 0),
        (0, 3, 7, 4),
        (1, 5, 6, 2)
    ]

    tex_coords = [
        (0.0, 0.0),
        (1.0, 0.0),
        (1.0, 1.0),
        (0.0, 1.0)
    ]

    glBegin(GL_QUADS)
    for face in faces:
        for i, vertex in enumerate(face):
            glTexCoord2f(tex_coords[i][0], tex_coords[i][1])
            glVertex3fv(vertices[vertex])
    glEnd()

def load_png_texture(image_path):
    try:
        image = Image.open(image_path)
        image_data = np.array(image.convert("RGBA"))

        width, height = image.size

        # Generate texture ID
        texture_id = glGenTextures(1)

        # Define texture parameters
        glBindTexture(GL_TEXTURE_2D, texture_id)
        glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, image_data)

        return texture_id
    except Exception as e:
        print(f"Failed to load texture {image_path}: {e}")
        return None

def draw_text(text, position, font, color=(255, 255, 255)):
    text_surface = font.render(text, True, color)
    text_data = pygame.image.tostring(text_surface, "RGBA", True)
    glWindowPos2d(position[0], position[1])
    glDrawPixels(text_surface.get_width(), text_surface.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, text_data)

def draw_ground(texture_id):
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-20, -1, -15)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(20, -1, -15)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(19, -1, 15)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-19, -1, 15)
    glEnd()
    glDisable(GL_TEXTURE_2D)

def draw_sky(texture_id):
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-20, 20, -20)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(20, 20, -20)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(20, 5, 20)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-20, 5, 20)
    glEnd()
    glDisable(GL_TEXTURE_2D)


