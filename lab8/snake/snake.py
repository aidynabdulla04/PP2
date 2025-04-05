import pygame
import random

pygame.init()

#game variables
width = 800
height = 600
screen = pygame.display.set_mode((width,height))
done = False
score = 0

#head variable

coor_head = [100,100]

#body variable

coor_body = [
    [30,100],
    [40,100],
    [50,100],
    [60,100],
    [70,100],
    [80,100],
    [90,100],
    [100,100]
]

#apple
apple_x = random.randrange(1,width//10)*10
apple_y = random.randrange(1,height//10)*10
coor_apple = [apple_x, apple_y]
eaten = False

#direction
next_dir = "r" #right direction
direc = "r" #right direction
global next_level
next_level=int(40)
level=int(1)
T=int(0)
def score_update(font, size, color):
    global score
    score_font = pygame.font.SysFont(font,size)
    score_render = score_font.render("Score: "+str(score),True,color)
    score_rect = score_render.get_rect()


    screen.blit(score_render,score_rect)

    pygame.display.update()

def game_over_message(font, size, color):
    global score
    global done
    game_over_font = pygame.font.SysFont(font,size)
    game_over_surface = game_over_font.render("Game Over, your final score: "+str(score),True,color)
    game_over_rect = pygame.Rect(100,100,400,400)

    screen.blit(game_over_surface,game_over_rect)
    pygame.display.update()
    pygame.time.delay(3000)
    done = True

def lev_update(font, size, color):
    global level
    global next_level
    #Add counter to score and level
    next_level_font = pygame.font.SysFont("times new roman",20)
    next_level_render = next_level_font.render("Next Level: "+str(next_level),True,(128,128,128))
    next_level_rect = next_level_render.get_rect()
    screen.blit(next_level_render,(625,0))
    pygame.display.update()
    
    level_font = pygame.font.SysFont(font,size)
    level_render = level_font.render("Level: "+str(level),True,color)
    level_rect = level_render.get_rect()
    screen.blit(level_render,(300,0))
    pygame.display.update()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                next_dir = "r"
            if event.key == pygame.K_LEFT:
                next_dir = "l"
            if event.key == pygame.K_UP:
                next_dir = "u"
            if event.key == pygame.K_DOWN:
                next_dir = "d"
    
    for seg in coor_body[:-1]:
        if coor_head[0] == seg[0] and coor_head[1] == seg[1]:
            game_over_message("times new roman",50,(255,0,0))

    screen.fill((0,0,0))
    #logic
    if next_dir == "r" and direc != "l":
        direc = "r"
    if next_dir == "l" and direc != "r":
        direc = "l"
    if next_dir == "u" and direc != "d":
        direc = "u"
    if next_dir == "d" and direc != "u":
        direc = "d"



    if direc == "r":
        coor_head[0] += 10
    if direc == "l":
        coor_head[0] -= 10
    if direc == "u":
        coor_head[1] -= 10
    if direc == "d":
        coor_head[1] += 10

    new_coor = [coor_head[0],coor_head[1]]
    coor_body.append(new_coor)
    coor_body.pop(0)
    #Checking for border (wall) collision and whether the snake is leaving the playing area
    if coor_head[0]==0 or coor_head[0]==800 or coor_head[1]==0 or coor_head[1]==600:
        game_over_message("times new roman",50,(255,0,0))
    #Add levels. For example, when the snake receives 3-4 foods or depending on score 
    if coor_head[0] == coor_apple[0] and coor_head[1] == coor_apple[1]:
        eaten = True
        score += 10
        if score==next_level:
            next_level+=score+20
            level+=1
            #Increase speed when the user passes to the next level
            T+=20
        
    #Generate random position for food, so that it does not fall on a wall or a snake
    if eaten:
        coor_apple[0] = random.randrange(1,width//10)*10
        coor_apple[1] = random.randrange(1,height//10)*10
        while True:
            check=True
            if(coor_apple[0]==0 or coor_apple[0]==800 or coor_apple[1]==0 or coor_apple[1]==600):
                coor_apple[0] = random.randrange(1,width//10)*10
                coor_apple[1] = random.randrange(1,height//10)*10
            else:
                for el in coor_body:
                    if el[0]==coor_apple[0]:
                        check=False
                        break
                    elif el[1]==coor_apple[1]:
                        check=False
                        break
                if check: break
                else:
                    coor_apple[0] = random.randrange(1,width//10)*10
                    coor_apple[1] = random.randrange(1,height//10)*10
        eaten = False

    # drawing section
    if not eaten:
        pygame.draw.rect(screen,(0,255,0),pygame.Rect(coor_apple[0],coor_apple[1],10,10))

    for el in coor_body:
        pygame.draw.rect(screen,(255,255,255),pygame.Rect(el[0],el[1],10,10))
    
    pygame.draw.rect(screen,(128,128,128),pygame.Rect(coor_head[0],coor_head[1],10,10))

    score_update("times new roman",20,(128,128,128))
    lev_update("times new roman",20,(128,128,128))

    #Increase speed when the user passes to the next level
    pygame.time.delay(100-T)

    pygame.display.flip()

pygame.quit()
