import pygame
import os

WIDTH,HEIGHT=900,500
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("SPACEWAR")

FPS = 60
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55,40
VEL=5
BULLET_VEL = 7
MAX_BULLETS = 5

YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2

MIDDLELINE = pygame.Rect(WIDTH//2 - 5,0,10,HEIGHT)

# IMAGES
YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join("spaceship","Assets","spaceship_yellow.png"))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE,(SPACESHIP_WIDTH, SPACESHIP_HEIGHT)),90)
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join("spaceship","Assets","spaceship_red.png"))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE,(SPACESHIP_WIDTH, SPACESHIP_HEIGHT)),270)
SPACEBG = pygame.image.load(os.path.join("spaceship","Assets","spacebg.png"))
BG = pygame.transform.scale(SPACEBG,(WIDTH,HEIGHT))

def draw_window(yellow,red,yellow_bullets,red_bullets):
    # WIN.fill(WHITE)
    WIN.blit(BG,(0,0))
    pygame.draw.rect(WIN,BLACK,MIDDLELINE)
    WIN.blit(YELLOW_SPACESHIP,(yellow.x,yellow.y))
    WIN.blit(RED_SPACESHIP,(red.x,red.y))

    for bullet in red_bullets:
        pygame.draw.rect(WIN,RED, bullet)
    for bullet in yellow_bullets:
        pygame.draw.rect(WIN,YELLOW, bullet)
    

    pygame.display.update()

def yellow_movement(key,yellow):
    if key[pygame.K_w] and yellow.x + VEL + yellow.height < MIDDLELINE.x:
        yellow.x += VEL
    if key[pygame.K_s] and yellow.x - VEL > 0:
        yellow.x -= VEL
    if key[pygame.K_a] and yellow.y - VEL > 0:
        yellow.y -= VEL
    if key[pygame.K_d] and yellow.y + VEL + yellow.width < HEIGHT:
        yellow.y += VEL


def red_movement(key, red):
    if key[pygame.K_UP] and red.x - VEL > MIDDLELINE.x + MIDDLELINE.width:
        red.x -= VEL
    if key[pygame.K_DOWN] and red.x + VEL + red.height < WIDTH: 
        red.x += VEL
    if key[pygame.K_RIGHT] and red.y - VEL > 0:
        red.y -= VEL
    if key[pygame.K_LEFT] and red.y + VEL + red.width < HEIGHT:
        red.y += VEL


def handle_bullets(yellow_bullets,red_bullets,yellow,red):
    for bullet in yellow_bullets:
        bullet.x +=BULLET_VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        elif bullet.x >WIDTH:
            yellow_bullets.remove(bullet)

    for bullet in red_bullets:
        bullet.x -=BULLET_VEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        elif bullet.x < 0:
            red_bullets.remove(bullet)


def main():

    yellow = pygame.Rect(100,230,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    red = pygame.Rect(700,230,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)

    yellow_bullets = []
    red_bullets = []

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(yellow.x+yellow.height , yellow.y + yellow.width//2 - 2 ,10,5)
                    yellow_bullets.append(bullet)
                if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(red.x , red.y + red.width//2 - 2 ,10,5)
                    red_bullets.append(bullet)


        print(yellow_bullets,red_bullets)
        key = pygame.key.get_pressed()
        yellow_movement(key,yellow)
        red_movement(key,red)
        
        handle_bullets(yellow_bullets,red_bullets,yellow,red)

        draw_window(yellow,red,yellow_bullets,red_bullets)
    pygame.quit()


if __name__ == "__main__":
    main()