import pygame
import datetime
x = datetime.datetime.now()
m=x.strftime("%M")
s=x.strftime("%S")
s=int(s)
image = pygame.image.load('mickeyclockh.jpg')
image1 = pygame.image.load('hour.png')
image2 = pygame.image.load('hand.png')
pygame.init()
screen = pygame.display.set_mode((1400, 1050))
done = False
clock = pygame.time.Clock()
angle=-53
angle-=s*6
angle2=60
angle2-=6*int(m)
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill((255, 255, 255))
    pressed = pygame.key.get_pressed()
    screen.blit(image, (0, 0))
    if(s==60):
        angle2-=6
        s=0
    image_rect = image1.get_rect(topleft=(700-175, 525-150))
    offset_center_to_pivot = pygame.math.Vector2((700,525)) - image_rect.center
    rotated_offset = offset_center_to_pivot.rotate(-angle)
    rotated_image_center = (700 - rotated_offset.x, 525 - rotated_offset.y)
    rotated_image = pygame.transform.rotate(image1, angle)
    angle -= 6
    rotated_image_rect = rotated_image.get_rect(center=rotated_image_center)
    screen.blit(rotated_image, rotated_image_rect)
    
    image_rectt = image2.get_rect(topleft=(700, 525-155))
    offset_center_to_pivott = pygame.math.Vector2((700,525)) - image_rectt.center
    rotated_offsett = offset_center_to_pivott.rotate(-angle2)
    rotated_image_centerr = (700 - rotated_offsett.x, 525 - rotated_offsett.y)
    rotated_imagee = pygame.transform.rotate(image2, angle2)
    rotated_image_rectt = rotated_imagee.get_rect(center=rotated_image_centerr)
    screen.blit(rotated_imagee, rotated_image_rectt)
    s+=1
    pygame.display.flip()
    clock.tick(1)
