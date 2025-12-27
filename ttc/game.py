import sys

import pygame

width, height = 512, 512
caption = "Triple Triad: Console"
blue = 166, 219, 255

windows_size = width, height
r, g, b = [float(value) / 255.0 for value in blue]


def init():
    pygame.init()
    pygame.display.set_caption(caption)

    screen = pygame.display.set_mode(windows_size)

    return screen


class Scene:
    def __init__(self, screen):
        self.screen = screen

    def render(self):
        self.screen.fill(blue)


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
    screen = init()
    scene = Scene(screen)
    game = Game(scene)

    while True:
        game.tick()
