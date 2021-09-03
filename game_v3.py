import random
import pygame
from pygame.constants import(
KEYDOWN, K_DOWN, K_ESCAPE, K_LEFT, K_RIGHT, K_UP, QUIT
)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.Surface((20,10))
        self.surf.fill((225,225,225))
        self.rect = self.surf.get_rect(
            center=(
                random.randint(screen_width + 20, screen_width + 100),
                random.randint(0,screen_height)
            )
        )
        self.speed = random.randint(5,25)
    
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75,25))
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect()

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0,-1)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0,1)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-1,0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(1,0)

        # keep plauer on screem
        if self.rect.left<0:
            self.rect.left = 0
        if self.rect.right > screen_width:
            self.rect.right = screen_width
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= screen_height:
            self.rect.bottom = screen_height 

pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height))

player_one = Player()

enemies = pygame.sprite.Group()
all_sprie = pygame.sprite.Group()
all_sprie.add(player_one)
# pygame.display.flip()
# screen.fill((0,0,0))
# for entity in all_sprie:
#     screen.blit(entity.surf, entity.rect)
running = True
while running:

    # event handler taking place inside event.get()
    for event in pygame.event.get():
    
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running=False       
        elif event.type == QUIT:
            running =False
    pressed_keys = pygame.key.get_pressed()
    player_one.update(pressed_keys)
    screen.fill((0,0,0))
    
    for entity in all_sprie:
        screen.blit(entity.surf, entity.rect)
    
    # cant use below to move player
    # screen.blit(player_one.surf, (screen_width/2,screen_height/2))
    
    screen.blit(player_one.surf, player_one.rect)
    pygame.display.flip()



