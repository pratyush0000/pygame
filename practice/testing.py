import pygame

WIDTH,HEIGHT=900,500
WIN=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("SPACEWAR")


#var
WHITE=(255,255,255)
BLACK=(0,0,0)
VEL=5
SPACESHIP_WIDTH=45
SPACESHIP_HEIGHT=35
FPS = 60
CENTRE_LINE=pygame.Rect(WIDTH/2-5,0,10,HEIGHT)


YELLOW_SPACESHIP_IMG= pygame.image.load('practice/assets/spaceship_yellow.png') #yellow spaceship load
YELLOW_SPACESHIP=pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMG,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),90)
RED_SPACESHIP_IMG= pygame.image.load('practice/assets/spaceship_red.png') #red spaceship load
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMG,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),270) #scale and rotate

def drawwindow(red,yellow): #watever is drawn later, comes on top.
    WIN.fill(WHITE)
    pygame.draw.rect(WIN,BLACK,CENTRE_LINE)
    WIN.blit(YELLOW_SPACESHIP,(yellow.x,yellow.y)) #we have access to x and y because pygame rect defines x and y
    WIN.blit(RED_SPACESHIP,(red.x,red.y))
    pygame.display.update()

def yellow_handle_movement(keys_pressed,yellow):
    if keys_pressed[pygame.K_a] and yellow.x - VEL > 0:
        yellow.x-=VEL
    if keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.width < CENTRE_LINE.x: 
        yellow.x+=VEL
    if keys_pressed[pygame.K_w] and yellow.y + VEL > 5: 
        yellow.y-=VEL
    if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.width < HEIGHT: 
        yellow.y+=VEL

def red_handle_movement(keys_pressed,red):
    if keys_pressed[pygame.K_LEFT] and red.x - VEL> CENTRE_LINE.x:  
        red.x-=VEL
    if keys_pressed[pygame.K_RIGHT] and red.x + VEL + SPACESHIP_HEIGHT < WIDTH: 
        red.x+=VEL
    if keys_pressed[pygame.K_UP] and red.y + VEL > 5:
        red.y-=VEL
    if keys_pressed[pygame.K_DOWN] and red.y + VEL + red.width < HEIGHT:
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

        #yellow.x+=1 #to show it moving
        drawwindow(red,yellow)

    pygame.quit()

if __name__ == "__main__":
    main()