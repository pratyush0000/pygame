import pygame
import os
import button
pygame.font.init()
pygame.mixer.init()

WIDTH,HEIGHT=900,500
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("SPACEWAR")

FPS = 60
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)

BULLET_HIT_SOUND =  pygame.mixer.Sound('Assets/Grenade+1.mp3')
BULLET__FIRE_SOUND = pygame.mixer.Sound('Assets/Gun+Silencer.mp3')
LOBBYSOUND = pygame.mixer.Sound('Assets/gamemenusound.mp3')
START_CLICK_SOUND = pygame.mixer.Sound('Assets/gamestartsound.mp3')
MENU_CLICK_SOUND = pygame.mixer.Sound('Assets/menuclicksound.mp3')
QUIT_CLICK_SOUND = pygame.mixer.Sound('Assets/quitclicksound.mp3')

HEALTH_FONT = pygame.font.SysFont('comicsans',40)
WINNER_FONT = pygame.font.SysFont('comicsans',120)
MENU_FONT = pygame.font.SysFont('arialblack',40)

SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55,40
VEL=5
BULLET_VEL = 7
MAX_BULLETS = 5

YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2

MIDDLELINE = pygame.Rect(WIDTH//2 - 5,0,10,HEIGHT)

# IMAGES

ENDMENU_IMG = pygame.transform.scale(pygame.image.load("Assets/menubuttonimg.png").convert_alpha(),(100,100))
ENDMENU_BUTTON = button.Button(WIDTH//3-ENDMENU_IMG.get_width()//2   ,   HEIGHT//1.5-ENDMENU_IMG.get_height()//2  ,  ENDMENU_IMG,1)

ENDRESTART_IMG = pygame.transform.scale(pygame.image.load("Assets/restartgamebuttonimg.png").convert_alpha(),(100,100))
ENDRESTART_BUTTON = button.Button(WIDTH//2 - ENDRESTART_IMG.get_width()//2   ,   HEIGHT//1.5 - ENDRESTART_IMG.get_height()//2  ,  ENDRESTART_IMG,1)

ENDQUIT_IMG = pygame.transform.scale(pygame.image.load("Assets/quitgamebuttonimg.png").convert_alpha(),(100,100))
ENDQUIT_BUTTON = button.Button(WIDTH//1.5 - ENDQUIT_IMG.get_width()//2  ,   HEIGHT//1.5 - ENDQUIT_IMG.get_height()//2,ENDQUIT_IMG,1)


SPACEWAR_BG = pygame.transform.scale(pygame.image.load("Assets/spacewarbg.png").convert_alpha(),(900,605))
TITLE_IMG = pygame.transform.scale(pygame.image.load("Assets/titleimg.png").convert_alpha(),(600,100))

START_IMG = pygame.transform.scale(pygame.image.load("Assets/startbutton.png").convert_alpha(),(200,75))
START_BUTTON = button.Button(WIDTH//2-START_IMG.get_width()//2,HEIGHT//2-START_IMG.get_height()//4,START_IMG,1)

QUIT_IMG = pygame.transform.scale(pygame.image.load("Assets/quitbutton.png").convert_alpha(),(200,75))
QUIT_BUTTON = button.Button(WIDTH//2 - QUIT_IMG.get_width()//2 , HEIGHT//2 + QUIT_IMG.get_height(),QUIT_IMG,1)

YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join("Assets","spaceship_yellow.png"))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE,(SPACESHIP_WIDTH, SPACESHIP_HEIGHT)),90)
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join("Assets","spaceship_red.png"))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE,(SPACESHIP_WIDTH, SPACESHIP_HEIGHT)),270)
SPACEBG = pygame.image.load(os.path.join("Assets","spacebg.png"))
BG = pygame.transform.scale(SPACEBG,(WIDTH,HEIGHT))




def start():
    START = False  # Initialize START as False
    run = True

    LOBBYSOUND.play(-1)

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        WIN.blit(SPACEWAR_BG,(0,0))
        WIN.blit(TITLE_IMG,(WIDTH//2 - TITLE_IMG.get_width()//2, HEIGHT//4 - TITLE_IMG.get_height()//4))

        # Check if the start button is clicked
        if START_BUTTON.draw(WIN):
            START = True  # Set START to True if the button is clicked
            LOBBYSOUND.stop()
            START_CLICK_SOUND.play()
            break  # Exit the loop to start the game
        if QUIT_BUTTON.draw(WIN):
            LOBBYSOUND.stop()
            QUIT_CLICK_SOUND.play()
            pygame.time.delay(550)
            run = False


        pygame.display.update()

    if START:
        main()  # If START is True, start the main game



def draw_window(yellow,red,yellow_bullets,red_bullets,red_health,yellow_health):
    # WIN.fill(WHITE)
    WIN.blit(BG,(0,0))
    pygame.draw.rect(WIN,BLACK,MIDDLELINE)

    red_health_text = HEALTH_FONT.render("Health: " + str(red_health),1,WHITE)
    yellow_health_text = HEALTH_FONT.render("Health: " + str(yellow_health),1,WHITE)

    WIN.blit(yellow_health_text,(10,10))
    WIN.blit(red_health_text,(WIDTH-red_health_text.get_width()-10,10))

    WIN.blit(YELLOW_SPACESHIP,(yellow.x,yellow.y))
    WIN.blit(RED_SPACESHIP,(red.x,red.y))

    for bullet in red_bullets:
        pygame.draw.rect(WIN,RED, bullet)
    for bullet in yellow_bullets:
        pygame.draw.rect(WIN,YELLOW, bullet)
    

    pygame.display.update()

def yellow_movement(key,yellow):
    if key[pygame.K_w] and yellow.y - VEL > 0:
        yellow.y -= VEL
    if key[pygame.K_s] and yellow.y + VEL + yellow.width < HEIGHT:
        yellow.y += VEL
    if key[pygame.K_d] and yellow.x + VEL + yellow.height < MIDDLELINE.x:
        yellow.x += VEL
    if key[pygame.K_a] and yellow.x - VEL > 0:
        yellow.x -= VEL


def red_movement(key, red):
    if key[pygame.K_UP] and red.y - VEL > 0:
        red.y -= VEL
    if key[pygame.K_DOWN] and red.y + VEL + red.width < HEIGHT:
        red.y += VEL
    if key[pygame.K_LEFT] and red.x - VEL > MIDDLELINE.x + MIDDLELINE.width:
        red.x -= VEL
    if key[pygame.K_RIGHT] and red.x + VEL + red.height < WIDTH: 
        red.x += VEL


def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    for bulletyellow in yellow_bullets:
        bulletyellow.x += BULLET_VEL
        if red.colliderect(bulletyellow):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bulletyellow)
        elif bulletyellow.x > WIDTH:
            yellow_bullets.remove(bulletyellow)

    for bulletred in red_bullets:
        bulletred.x -= BULLET_VEL
        if yellow.colliderect(bulletred):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bulletred)
        elif bulletred.x < 0:
            red_bullets.remove(bulletred)

    # Check for collisions between yellow bullets and red bullets
    for bulletyellow in yellow_bullets:
        for bulletred in red_bullets:
            if bulletyellow.colliderect(bulletred):
                yellow_bullets.remove(bulletyellow)
                red_bullets.remove(bulletred)
                BULLET_HIT_SOUND.play()

    # Check for collisions between red bullets and yellow bullets
    for bulletred in red_bullets:
        for bulletyellow in yellow_bullets:
            if bulletred.colliderect(bulletyellow):
                red_bullets.remove(bulletred)
                yellow_bullets.remove(bulletyellow)
                BULLET_HIT_SOUND.play()

def draw_winner(text):
    # pygame.time.delay(5000)
    MENU = False
    START = False 
    run = True
    QUIT=False

    LOBBYSOUND.play(-1)

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_text = WINNER_FONT.render(text,1,WHITE)
        WIN.blit(draw_text,(WIDTH/2 - draw_text.get_width()/2,HEIGHT/4 - draw_text.get_height()/4))

        if ENDMENU_BUTTON.draw(WIN):
            MENU=True
            LOBBYSOUND.stop()
            MENU_CLICK_SOUND.play()
            break
        if ENDRESTART_BUTTON.draw(WIN):
            START=True
            LOBBYSOUND.stop()
            START_CLICK_SOUND.play()
            break
        if ENDQUIT_BUTTON.draw(WIN):
            QUIT=True
            LOBBYSOUND.stop()
            QUIT_CLICK_SOUND.play()
            pygame.time.delay(550)
            break

        pygame.display.update()

    if START:
        main()  # If START is True, start the main game
    if MENU:
        start() 
    if QUIT:
        pygame.quit()


def main():
    pygame.init()
    yellow = pygame.Rect(100,230,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    red = pygame.Rect(700,230,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)

    yellow_bullets = []
    red_bullets = []

    red_health = 10
    yellow_health = 10

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS:
                    bulletyellow = pygame.Rect(yellow.x+yellow.height , yellow.y + yellow.width//2 - 2 ,10,5)
                    yellow_bullets.append(bulletyellow)
                    BULLET__FIRE_SOUND.play()
                if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS:
                    bulletred = pygame.Rect(red.x , red.y + red.width//2 - 2 ,10,5)
                    red_bullets.append(bulletred)
                    BULLET__FIRE_SOUND.play()

            if event.type == RED_HIT:
                red_health -= 1
                BULLET_HIT_SOUND.play()
            if event.type == YELLOW_HIT:
                yellow_health -= 1
                BULLET_HIT_SOUND.play()

        winner_text = ""

        if red_health<=0:
            winner_text = "Yellow WINS!"

        if yellow_health <=0:
            winner_text = "Red WINS!"

        if winner_text != "":
            draw_winner(winner_text)
            break

        print(yellow_bullets,red_bullets)
        key = pygame.key.get_pressed()
        yellow_movement(key,yellow)
        red_movement(key,red)
        
        handle_bullets(yellow_bullets,red_bullets,yellow,red)

        draw_window(yellow,red,yellow_bullets,red_bullets,red_health,yellow_health)
    pygame.quit()


if __name__ == "__main__":
    start()  # Start the application