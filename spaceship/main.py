import pygame
import os

WIDTH,HEIGHT=900,500
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("SPACEWAR")

FPS = 60
WHITE = (255,255,255)
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55,40
VEL=5

# IMAGES
YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join("spaceship","Assets","spaceship_yellow.png"))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE,(SPACESHIP_WIDTH, SPACESHIP_HEIGHT)),90)
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join("spaceship","Assets","spaceship_red.png"))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE,(SPACESHIP_WIDTH, SPACESHIP_HEIGHT)),270)



def draw_window(yellow,red):
    WIN.fill(WHITE)
    WIN.blit(YELLOW_SPACESHIP,(yellow.x,yellow.y))
    WIN.blit(RED_SPACESHIP,(red.x,red.y))
    pygame.display.update()

def yellow_movement(key,yellow):
    if key[pygame.K_w]:
        yellow.x += VEL
    if key[pygame.K_s]:
        yellow.x -= VEL
    if key[pygame.K_a]:
        yellow.y -= VEL
    if key[pygame.K_d]:
        yellow.y += VEL


def red_movement(key,red):
    if key[pygame.K_UP]:
        red.x -= VEL
    if key[pygame.K_DOWN]:
        red.x += VEL
    if key[pygame.K_LEFT]:
        red.y += VEL
    if key[pygame.K_RIGHT]:
        red.y -= VEL


def main():

    yellow = pygame.Rect(100,230,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    red = pygame.Rect(700,230,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)


    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        key = pygame.key.get_pressed()
        yellow_movement(key,yellow)
        red_movement(key,red)
        

        draw_window(yellow,red)
    pygame.quit()

if __name__ == "__main__":
    main()