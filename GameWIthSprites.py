import pygame
import random

SCREEN_WIDTH, SCREEN_HEIGHT = 500, 400
MOEMENT_SPEED = 5
FONT_SIZE = 72

pygame.init()

backround_image = pygame.transform.scale(pygame.image.load("bg.jpg"),
                                         (SCREEN_WIDTH, SCREEN_HEIGHT))

font = pygame.font.SysFont("Times New roman", FONT_SIZE)

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(
            pygame.Color('dogerblue'))
        pygame.draw.rect(self.image, color, pygame.Rect(0, 0, width, height))
        self.rect = self.image.get_rect()

    def move(self, x_change, y_change):
        self.rect.x = max(
            min(self.rect.x + x_change, SCREEN_WIDTH - self.rect.width), 0)
        self.rect.y = max(
            min(self.rect.y + y_change, SCREEN_HEIGHT - self.rect.height), 0)
        
screen = pygame.displa.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("sprite Collison")
all_sprites = pygame.spriteGroup()

sprite1 = Sprite(pygame.Color('black'), 20, 30 )
sprite1.rect.x, sprite1.rect.y = random.randint(
    0, SCREEN_WIDTH - sprite1.rect.height)
all_sprites.add(sprite1)


sprite2 = Sprite(pygame.Color('red'), 20, 30 )
sprite2.rect.x, sprite2.rect.y = random.randint(
    0, SCREEN_WIDTH - sprite2.rect.height)
all_sprites.add(sprite2)

running, won = True, False
clock = pygame.time.Clock()

while running:
    for event