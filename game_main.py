
from random import randint
import pygame
from pygame.constants import(
    K_u, QUIT, KEYDOWN, K_ESCAPE, K_SPACE, K_DOWN,  K_UP, K_LEFT, K_RIGHT
)

pygame.init()
screen_width = 800
screen_height = 600


class Player(pygame.sprite.Sprite):
    def __init__(self, width, height):
        pygame.sprite.Sprite.__init__(self)

        self.surf = pygame.Surface([width,height])
        self.surf.fill((200,200,200))
        self.rect = self.surf.get_rect(
            center=(
                screen_width/4,
                screen_height/1.3
            )
        )

    def update(self, pressed_keys):
        # if pressed_keys[K_UP]:
        #     self.rect.move_ip(0,-1)
        # if pressed_keys[K_DOWN]:
        #     self.rect.move_ip(0,1)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-3,0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(3,0)
        # keep "paddle" on sscreen
        if self.rect.left<0:
            self.rect.left=0
        if self.rect.right>screen_width:
            self.rect.right=screen_width

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.surf = pygame.Surface([15,15])
        self.surf.fill((0,0,0))
        self.rect = self.surf.get_rect(
            center=(
                screen_width/2,
                screen_height/2
            )
        )
        self.direction = randint(1,3),randint(1,3)
        self.speed = .5
        self.count = 0
    def bounceCount(self):
        dx, dy = ball.direction
        self.speed = .2
        if pygame.sprite.spritecollideany(player, ball_group_sprite):
            ball.direction = dx, -dy
            self.count += 1    
        if self.count == 0:
            self.speed = 1
        elif self.count >= 50:
            self.speed = .7
        else:
            self.speed = .5

        print("You hit the pattle:",self.count,"times")

            
    def update(self):
        
        dx, dy = ball.direction
        ball.rect.move_ip(ball.speed * dx, ball.speed * dy)
        if ball.rect.right >= screen_width or ball.rect.left <= 0:
            ball.direction = -dx-1, dy+1
        if ball.rect.top <= 0:
            ball.direction = dx+1, -dy -2
        if ball.rect.bottom >= screen_height:
            ball.direction = dx, -dy

        # collisioon with paddle
        if pygame.sprite.spritecollideany(player, ball_group_sprite):
            ball.bounceCount()
        

   
player = Player(75,5)
ball = Ball()



screen = pygame.display.set_mode((screen_width,screen_height))
game_is_running = True
while game_is_running:

    player_group_sprite = pygame.sprite.Group()
    player_group_sprite.add(player)
    ball_group_sprite = pygame.sprite.Group()
    ball_group_sprite.add(ball)
   
    screen.fill((123,123,123))
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                game_is_running = False
        elif event.type == QUIT:
            game_is_running = False

    # screen.blit(player.surf, player.rect)
    for entity in player_group_sprite:
        screen.blit(player.surf, player.rect)
        
    for entity in ball_group_sprite:
        screen.blit(ball.surf,ball.rect)
        ball.update()

    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)

    

    pygame.display.flip()