import sys

import pygame

width, height = 400, 400
caption = "Triple Triad: Console"
milliseconds_in_a_second = 1000.0

# Background color.
# blue = 166, 219, 255
# r, g, b = [float(value) / 255.0 for value in blue]


def init():
    pygame.init()
    pygame.display.set_mode((width, height), flags=pygame.OPENGL | pygame.DOUBLEBUF, vsync=True)
    pygame.display.set_caption(caption)


class Scene:
    @staticmethod
    def render():
        now = pygame.time.get_ticks() / milliseconds_in_a_second
        print(now)


class Game:
    def __init__(self, scene):
        self.scene = scene

    def tick(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        self.scene.render()
        pygame.display.flip()


def main():
    init()
    scene = Scene()
    game = Game(scene)

    while True:
        game.tick()
