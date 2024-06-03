from OpenGL.GL import *
import numpy as np
from PIL import Image
import pygame

def draw_squere(x, y):
    x_center = x + 0.5
    y_center = y + 0.5
    glTexCoord2f(0.0, 0.0)
    glVertex3f(x_center - 0.5, y_center - 0.5, 0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(x_center + 0.5, y_center - 0.5, 0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(x_center + 0.5, y_center + 0.5, 0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(x_center - 0.5, y_center + 0.5, 0)


def load_png_texture(image_path):
    try:
        image = Image.open(image_path)
        image_data = np.array(image.convert("RGBA"))

        width, height = image.size

        # Wygeneruj identyfikator tekstury
        texture_id = glGenTextures(1)

        # Zdefiniuj parametry tekstury
        glBindTexture(GL_TEXTURE_2D, texture_id)
        glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, image_data)

        return texture_id

    except Exception as e:
        print("Wystąpił błąd podczas wczytywania tekstury:", e)
        return None

def draw_text(text, position, font, color=(1.0, 1.0, 1.0)):
    text_surface = font.render(text, True, color)
    text_data = pygame.image.tostring(text_surface, "RGBA", True)

    glRasterPos2d(*position)
    glDrawPixels(text_surface.get_width(), text_surface.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, text_data)
