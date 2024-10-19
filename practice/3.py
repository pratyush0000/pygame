#moving the spaceships
import pygame


WIDTH,HEIGHT=900,500
WIN=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("SPACEWAR")

#variables
WHITE=(255,255,255)
FPS = 60
VEL=5
SPACESHIP_WIDTH=45
SPACESHIP_HEIGHT=35

#images
YELLOW_SPACESHIP_IMG= pygame.image.load('practice/assets/spaceship_yellow.png') 
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMG,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),90) 
RED_SPACESHIP_IMG= pygame.image.load('practice/assets/spaceship_red.png') 
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMG,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),270) 

def drawwindow(red,yellow):
    WIN.fill(WHITE)

    WIN.blit(YELLOW_SPACESHIP,(yellow.x,yellow.y)) #we have access to x and y because pygame rect defines x and y
    WIN.blit(RED_SPACESHIP,(red.x,red.y))

    pygame.display.update()


def yellow_handle_movement(keys_pressed,yellow):
    if keys_pressed[pygame.K_a]: #left
        yellow.x-=VEL
    if keys_pressed[pygame.K_d]: #right
        yellow.x+=VEL
    if keys_pressed[pygame.K_w]: #up
        yellow.y-=VEL
    if keys_pressed[pygame.K_s]: #down
        yellow.y+=VEL

def red_handle_movement(keys_pressed,red):
    if keys_pressed[pygame.K_LEFT]: #left
        red.x-=VEL
    if keys_pressed[pygame.K_RIGHT]: #right
        red.x+=VEL
    if keys_pressed[pygame.K_UP]: #up
        red.y-=VEL
    if keys_pressed[pygame.K_DOWN]: #down
        red.y+=VEL

def main():

    red=pygame.Rect(700,300,SPACESHIP_WIDTH,SPACESHIP_HEIGHT) #x,y,width,height
    yellow=pygame.Rect(100,300,SPACESHIP_WIDTH,SPACESHIP_HEIGHT) #x,y,width,height

    clock= pygame.time.Clock()
    run=True
    while run:
        clock.tick(FPS) 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed= pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed,yellow)
        red_handle_movement(keys_pressed,red) #call func


        # yellow.x+=1 #to show it moving
        drawwindow(red,yellow)#put red and yellow in it

    pygame.quit()

if __name__ == "__main__":
    main()