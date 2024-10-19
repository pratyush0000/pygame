#adding the spaceshipsssssss
import pygame


WIDTH,HEIGHT=900,500
WIN=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("SPACEWAR")

#variables
WHITE=(255,255,255)
FPS = 60
SPACESHIP_WIDTH=45
SPACESHIP_HEIGHT=35

#images
YELLOW_SPACESHIP_IMG= pygame.image.load('practice/assets/spaceship_yellow.png') #yellow spaceship load
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMG,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),90) #scale and rotate
RED_SPACESHIP_IMG= pygame.image.load('practice/assets/spaceship_red.png') #red spaceship load
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMG,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),270) #scale and rotate

def drawwindow(): #watever is drawn later, comes on top.
    WIN.fill(WHITE)
    #blit is used to draw surfeces. images are imported as surfaces
    WIN.blit(YELLOW_SPACESHIP,(150,230))
    WIN.blit(RED_SPACESHIP,(700,230))

    pygame.display.update()


def main():
    clock= pygame.time.Clock() #clock object to set fps
    run=True
    while run:
        clock.tick(FPS) #set fps
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        drawwindow()

    pygame.quit()

if __name__ == "__main__":
    main()