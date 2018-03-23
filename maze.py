# Imports
import pygame
import intersects

# Initialize game engine
pygame.init()


# Window
WIDTH = 800
HEIGHT = 600
SIZE = (WIDTH, HEIGHT)
TITLE = "Maze"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)


# Timer
clock = pygame.time.Clock()
refresh_rate = 60

# Sound Effects
coin_sound = pygame.mixer.Sound("sounds/coin_sound.ogg")
pygame.mixer.music.load("sounds/game_music.ogg")

# Colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (30, 95, 201)
PINK = (255, 0, 175)

#fonts
MY_FONT = pygame.font.Font(None, 60)

# make walls
wall1 =  [300, 275, 200, 25]
wall2 =  [400, 450, 200, 25]
wall3 =  [100, 100, 25, 200]
wall4 = [0, 0, 380, 30]
wall5 = [420, 0, 410,30]
wall6 = [0, 570, 380, 30]
wall7 = [420, 570, 410, 30]
wall8 = [600, 275, 25, 200]
wall9 = [0, 350, 30, 220]
wall10 = [0, 0, 30, 300]
wall11 = [420, 0, 30, 300]
wall12 = [420, 350, 30, 220]
wall13 = [770, 0, 30, 300]
wall14 = [770, 350, 30, 220]
wall15 = [0, 445, 425, 30]
wall16 = [300, 300, 30 ,175]

walls = [wall1, wall2, wall3, wall4, wall5, wall6, wall7, wall8, wall9, wall10, wall11, wall12, wall13, wall14, wall15, wall16]

# Make coins
coin1 = [250, 500, 25, 25]
coin2 = [350, 200, 25, 25]
coin3 = [150, 150, 25, 25]
coin4 = [700, 200, 25, 25]
coin5 = [600, 500, 25, 25]
coin6 = [500, 350, 25, 25]
coin7 = [200, 400, 25, 25]
coin8 = [400, 310, 25, 25]
coin9 = [550, 70, 25, 25]
coin10 = [50, 50, 25, 25]
coin11 = [60, 300, 25, 25]
coin12 = [275, 500, 25, 25]
coin13 = [225, 500, 25, 25]
coin14 = [200, 500, 25, 25]
coin15 = [600, 75, 25, 25]
coins = [coin1, coin2, coin3, coin4, coin5, coin6, coin7, coin8, coin9, coin10, coin11, coin12, coin13, coin14, coin15]

#stages
START = 0
PLAYING = 1
END = 2
PAUSE = 3

def setup():
    global player1, vel1, score1, player2, vel2, score2, stage, time_remaining, ticks

    player1 = [200, 150, 25, 25]
    vel1 = [0, 0]
    score1 = 0

    player2 = [500, 150, 25, 25]
    vel2 = [0, 0]
    score2 = 0

    stage = START
    time_remaining = 20
    ticks = 0
    

# Game loop
setup()
win = 0
done = False

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    ''' for now, we'll just check to see if the X is clicked '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:

                if stage == START:
                    if event.key == pygame.K_SPACE:
                        stage = PLAYING

                elif stage == PLAYING:
                    pygame.mixer.music.play()
                    if event.key == pygame.K_SPACE:
                        stage = PAUSE
                elif stage == END:
                    if event.key == pygame.K_SPACE:
                        setup()
                elif stage == PAUSE:
                    if event.key == pygame.K_SPACE:
                        stage = PLAYING

        if PLAYING:
            pressed = pygame.key.get_pressed()

            up1 = pressed[pygame.K_UP]
            down1 = pressed[pygame.K_DOWN]
            left1 = pressed[pygame.K_LEFT]
            right1 = pressed[pygame.K_RIGHT]

            if left1:
                vel2[0] = -5
            elif right1:
                vel2[0] = 5
            else:
                vel2[0] = 0

            if up1:
                vel2[1] = -5
            elif down1:
                vel2[1] = 5
            else:
                vel2[1] = 0


            up2 = pressed[pygame.K_w]
            down2 = pressed[pygame.K_s]
            left2 = pressed[pygame.K_a]
            right2 = pressed[pygame.K_d]

            if left2:
                vel1[0] = -5
            elif right2:
                vel1[0] = 5
            else:
                vel1[0] = 0

            if up2:
                vel1[1] = -5
            elif down2:
                vel1[1] = 5
            else:
                vel1[1] = 0

    
        
        
    # Game logic (Check for collisions, update points, etc.)
    ''' move the player in horizontal direction '''
    player1[0] += vel1[0]
    player2[0] += vel2[0]

    ''' resolve collisions horizontally '''
    for w in walls:
        if intersects.rect_rect(player1, w):        
            if vel1[0] > 0:
                player1[0] = w[0] - player1[2]
            elif vel1[0] < 0:
                player1[0] = w[0] + w[2]

        if intersects.rect_rect(player2, w):        
            if vel2[0] > 0:
                player2[0] = w[0] - player2[2]
            elif vel2[0] < 0:
                player2[0] = w[0] + w[2]

        

    ''' move the player in vertical direction '''
    player1[1] += vel1[1]
    player2[1] += vel2[1]
    
    ''' resolve collisions vertically '''
    for w in walls:
        if intersects.rect_rect(player1, w):                    
            if vel1[1] > 0:
                player1[1] = w[1] - player1[3]
            if vel1[1]< 0:
                player1[1] = w[1] + w[3]

        if intersects.rect_rect(player2, w):                    
            if vel2[1] > 0:
                player2[1] = w[1] - player2[3]
            if vel2[1]< 0:
                player2[1] = w[1] + w[3]

    ''' here is where you should resolve player collisions with screen edges '''
    if player1[1] < -(player1[3]):
        player1[1] = HEIGHT + 1
    if player1[1] > HEIGHT + 1:
        player1[1] = -(player1[3])

    if player1[0] < -(player1[2]):
        player1[0] = WIDTH + 1
    if player1[0] > WIDTH + 1:
        player1[0] = -(player1[2])


    if player2[1] < -(player2[3]):
        player2[1] = HEIGHT + 1
    if player2[1] > HEIGHT + 1:
        player2[1] = -(player2[3])

    if player2[0] < -(player2[2]):
        player2[0] = WIDTH + 1
    if player2[0] > WIDTH + 1:
        player2[0] = -(player2[2])

  

                
    '''get the coins '''
    hit_list1 = []
    hit_list2 = []

    
    hit_list1 = [c for c in coins if intersects.rect_rect(player1, c)]

    for hit in hit_list1:
        coins.remove(hit)
        score1 += 1
        coin_sound.play()
    hit_list2 = [c for c in coins if intersects.rect_rect(player2, c)]

    for hit in hit_list2:
        coins.remove(hit)
        score2 += 1
        coin_sound.play()

#winning situations

    if len(coins) == 0 or time_remaining ==0:
        if score1 > score2:
            win = 1
        elif score2 > score1:
            win = 2
        else:
            win = 3
        
        stage = END

    ''' timer '''
    if stage == PLAYING:
        ticks-= 1

        if ticks % refresh_rate ==0:
            time_remaining -=1
        if time_remaining == 0:
            stage = END

        
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(BLUE)

    pygame.draw.rect(screen, WHITE, player1)
    pygame.draw.rect(screen, PINK, player2)

    
    for w in walls:
        pygame.draw.rect(screen, RED, w)

    for c in coins:
        pygame.draw.rect(screen, YELLOW, c)
        
    if win == 1:
        font = pygame.font.Font(None, 48)
        text = font.render("White Player WINSSS!!!!", 1, WHITE)
        screen.blit(text, [300, 100])
        
    if win == 2:
        font = pygame.font.Font(None, 48)
        text = font.render("Pink Player WINSSS!!!!", 1, PINK)
        screen.blit(text, [300, 100])
    if win == 3:
        font = pygame.font.Font(None, 48)
        text = font.render("Draw, you both suck!", 1, GREEN)
        screen.blit(text, [300, 100])
    if win == 4:
        font = pygame.font.Font(None, 48)
        text = font.render("YOU WIN!!!!", 1, GREEN)
        screen.blit(text, [300, 100])
        
    #scoring text
    font = pygame.font.Font(None, 36)
    score_text1 = font.render("White Score: " + str(score1), 1, WHITE)
    screen.blit(score_text1, [10,25])
    font = pygame.font.Font(None, 36)
    score_text1 = font.render("Pink Score: " + str(score2), 1, PINK)
    screen.blit(score_text1, [635,25])
    ''' timer '''
    timer_text = MY_FONT.render(str(time_remaining),True,BLACK)
    screen.blit(timer_text, [400,50])

    ''' splash screen '''
    if stage == START:
        text1 = MY_FONT.render("BLOCK RACER!", True, WHITE)
        text2 = MY_FONT.render("Press Space to Begin", True, WHITE)
        screen.blit(text1, [350,150])
        screen.blit(text2, [225,200])
    
    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
