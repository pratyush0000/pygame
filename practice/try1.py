import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
player1 = pygame.Rect((300,250,50,50))

clock = pygame.time.Clock()

run = True

playerspeed=4

while run:

    screen.fill((0,0,0))

    pygame.draw.rect(screen,(0,0,255),player1,border_radius=100,width=5)

    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True:
        player1.move_ip(-playerspeed,0)
    if key[pygame.K_d] == True:
        player1.move_ip(playerspeed,0)
    if key[pygame.K_w] == True:
        player1.move_ip(0,-playerspeed)
    if key[pygame.K_s] == True:
        player1.move_ip(0,playerspeed)

    if player1.left < 0:
        player1.left = 0
    if player1.right > SCREEN_WIDTH:
        player1.right = SCREEN_WIDTH
    if player1.top <= 0:
        player1.top = 0
    if player1.bottom >= SCREEN_HEIGHT:
        player1.bottom = SCREEN_HEIGHT

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

    clock.tick(144)

pygame.quit()