#borders
import pygame


WIDTH,HEIGHT=900,500
WIN=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("SPACEWAR")

#variables
WHITE=(255,255,255)
BLACK=(0,0,0)
FPS = 60
VEL=5
SPACESHIP_WIDTH=45
SPACESHIP_HEIGHT=35

CENTRE_LINE=pygame.Rect(WIDTH/2-5,0,10,HEIGHT)

#images
YELLOW_SPACESHIP_IMG= pygame.image.load('practice/assets/spaceship_yellow.png') 
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMG,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),90) 
RED_SPACESHIP_IMG= pygame.image.load('practice/assets/spaceship_red.png') 
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMG,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),270) 

def drawwindow(red,yellow):
    WIN.fill(WHITE)
    pygame.draw.rect(WIN,BLACK,CENTRE_LINE)
    WIN.blit(YELLOW_SPACESHIP,(yellow.x,yellow.y)) 
    WIN.blit(RED_SPACESHIP,(red.x,red.y))

    pygame.display.update()


def yellow_handle_movement(keys_pressed,yellow):
    if keys_pressed[pygame.K_a]:
        yellow.x-=VEL
    if keys_pressed[pygame.K_d]: 
        yellow.x+=VEL
    if keys_pressed[pygame.K_w]: 
        yellow.y-=VEL
    if keys_pressed[pygame.K_s]: 
        yellow.y+=VEL

def red_handle_movement(keys_pressed,red):
    if keys_pressed[pygame.K_LEFT]: 
        red.x-=VEL
    if keys_pressed[pygame.K_RIGHT]: 
        red.x+=VEL
    if keys_pressed[pygame.K_UP]:
        red.y-=VEL
    if keys_pressed[pygame.K_DOWN]: 
        red.y+=VEL

def main():

    red=pygame.Rect(700,300,SPACESHIP_WIDTH,SPACESHIP_HEIGHT) 
    yellow=pygame.Rect(100,300,SPACESHIP_WIDTH,SPACESHIP_HEIGHT) 

    clock= pygame.time.Clock()
    run=True
    while run:
        clock.tick(FPS) 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed= pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed,yellow)
        red_handle_movement(keys_pressed,red)


        drawwindow(red,yellow)

    pygame.quit()

if __name__ == "__main__":
    main()