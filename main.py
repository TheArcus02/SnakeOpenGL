import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from Snake import Snake
from Food import Food
from utils import draw_text, load_png_texture, draw_ground, draw_sky


def init_game():
    # Initialization
    pygame.init()

    # Display settings
    display = (1000, 1000)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL) 
    pygame.display.set_caption("Snake Game")

    # OpenGL settings
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glEnable(GL_DEPTH_TEST)

    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslatef(0.0, -5.0, -35)
    glRotatef(30, 1, 0, 0)

    # Set up OpenGL context
    pygame.display.gl_set_attribute(pygame.GL_MULTISAMPLEBUFFERS, 1)
    pygame.display.gl_set_attribute(pygame.GL_MULTISAMPLESAMPLES, 4)


def draw_grid():
    glColor3f(1.0, 1.0, 1.0)  # White grid lines
    glBegin(GL_LINES)


    for x in range(-19, 20):
        glVertex3f(x, 0, -15)
        glVertex3f(x, 0, 15)
    for z in range(-15, 16):
        glVertex3f(-19, 0, z)
        glVertex3f(19, 0, z)
    glEnd()


def setup_lighting():
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_POSITION, [0.0, 1.0, 1.0, 0.0])
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [1.0, 1.0, 1.0, 1.0])


# Change in the main loop
if __name__ == '__main__':
    init_game()

    pygame.font.init()
    font = pygame.font.SysFont("Arial", 24)

    running = True

    snake_head_texture = load_png_texture('snake_head_texture.png')
    snake_texture = load_png_texture('snake_body_texture.png')
    food_texture = load_png_texture('food_texture.png')
    ground_texture = load_png_texture('ground_texture.png')
    sky_texture = load_png_texture('sky_texture.png')

    snake = Snake()
    food = Food()

    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake.change_direction((-1, 0, 0))
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction((1, 0, 0))
                elif event.key == pygame.K_UP:
                    snake.change_direction((0, 0, -1))
                elif event.key == pygame.K_DOWN:
                    snake.change_direction((0, 0, 1))

        if snake.alive:
            snake.move()

            # Check collision with food
            if snake.positions[0] == food.position:
                snake.grow()
                food.respawn()

            # Render
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            setup_lighting()
            glDepthMask(False)  # Disable depth writes for sky
            draw_sky(sky_texture)
            glDepthMask(True)  # Re-enable depth writes
            draw_ground(ground_texture)
            snake.draw_head(snake_head_texture)
            snake.draw_body(snake_texture)
            food.draw(food_texture)
            pygame.display.flip()
            clock.tick(15)
        else:
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            draw_text('Game Over', (400, 500), font, (255, 255, 255))
            pygame.display.flip()
            pygame.time.wait(2000)
            running = False

    pygame.quit()
