import pygame
import os

WIN_WIDTH = 600
WIN_HEIGHT = 800


BIRD_IMAGES = [pygame.transform.scale2x(pygame.image.load(os.path.join("images", "bird1.png"))), pygame.transform.scale2x(
    pygame.image.load(os.path.join("images", "bird2.png"))), pygame.transform.scale2x(pygame.image.load(os.path.join("images", "bird3.png")))]

PIPE_IMAGE = pygame.transform.scale2x(pygame.image.load(os.path.join("images", "pipe.png")))

BASE_IMAGE = pygame.transform.scale2x(pygame.image.load(os.path.join("images", "base.png")))

BG_IMAGE = pygame.transform.scale2x(pygame.image.load(os.path.join("images", "bg.png")))

class Bird:
    IMG = BIRD_IMAGES
    MAX_ROTATION = 25
    ROTATION_VELOCITY = 20
    ANIMATION_TIME = 5

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tilt = 0
        self.tick_count = 0
        self.vel = 0
        self.height = self.y
        self.img_count = 0
        self.img = self.IMG[0]

    def jump(self):
        self.vel = -10.5
        self.tick_count = 0
        self.height = self.y

    def move(self):
        self.tick_count += 1

        d = self.vel*self.tick_count + 1.5*self.tick_count**2

        if d >= 16:
            d = 16

        if d < 0:
            d -= 2

        self.y = self.y + d

        if d < 0 or self.y < self.height + 50:
            if self.tilt < self.MAX_ROTATION:
                self.tilt = self.MAX_ROTATION
        else:
            if self.tilt > -90:
                self.tilt -= self.ROTATION_VELOCITY
