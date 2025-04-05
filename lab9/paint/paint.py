import pygame
import math
def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    
    radius = 15
    wid=15
    x = 0
    y = 0
    mode = 'blue'
    draw=True
    shape="circle"
    points = []
    screen.fill((0, 0, 0))
    while True:
        
        pressed = pygame.key.get_pressed()
        
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            
            # determin if X was clicked, or Ctrl+W or Alt+F4 was used
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
            
                # determine if a letter key was pressed
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
                elif event.key == pygame.K_e:
                    mode = 'black'
                elif event.key == pygame.K_c:
                    shape = 'circle'
                elif event.key == pygame.K_x:
                    shape = 'rect'
                elif event.key == pygame.K_v:
                    shape = 'rtrig'
                elif event.key == pygame.K_z:
                    shape = 'etrig'
                elif event.key == pygame.K_m:
                    shape = 'rhombus'
                elif event.key == pygame.K_n:
                    draw=not draw
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # left click grows radius
                    if shape=='circle':
                        radius = min(200, radius + 1)
                    else:
                        wid=min(400,wid+3)
                elif event.button == 3: # right click shrinks radius
                    if shape=='circle':
                        radius = max(1, radius - 1)
                    else:
                        wid=max(1,wid-3)
            if event.type == pygame.MOUSEMOTION:
                if(draw):
                    position = event.pos
                    if mode == 'blue':
                        color = (0, 0, 255)
                    elif mode == 'red':
                        color = (255, 0, 0)
                    elif mode == 'green':
                        color = (0, 255, 0)
                    elif mode == 'black':
                        color = (0, 0, 0)
                    if shape=='circle':
                        pygame.draw.circle(screen, color, (position[0], position[1]), radius)
                    elif shape=='rtrig':
                        #Draw right triangle
                        pygame.draw.polygon(screen, color, ((position[0], position[1]),(position[0]+wid, position[1]),(position[0], position[1]+wid)))
                    elif shape=='etrig':
                        #Draw equilateral triangle
                        h=math.sqrt(3)*wid/2
                        pygame.draw.polygon(screen, color, ((position[0], position[1]),(position[0]+wid/2, position[1]+h),(position[0]-wid/2, position[1]+h)))
                    elif shape=='rhombus':
                        #Draw rhombus
                        h=math.sqrt(3)*wid/2
                        pygame.draw.polygon(screen, color, ((position[0]+wid/2, position[1]+h),(position[0], position[1]),(position[0]-wid/2, position[1]+h),(position[0], position[1]+2*h)))
                    else:
                        #Draw square
                        pygame.draw.rect(screen, color, pygame.Rect(position[0], position[1],wid,wid))
        
        pygame.display.flip()
        
        clock.tick(60)

main()
