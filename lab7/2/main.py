import pygame
import os

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((512, 512))
done = False
_songs=[]
l=os.listdir()
for i in l:
        if(os.path.isfile(i)):
            if(i[len(i)-3:len(i)]=="mp3"):
                _songs.append(i)
image = pygame.image.load('play.webp')
image1 = pygame.image.load('pause.png')
k=int(0)
pygame.mixer.music.load(_songs[k])
pygame.mixer.music.play()
space=True
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        k+=1
                        k=k%len(_songs)
                        pygame.mixer.music.load(_songs[k])
                        pygame.mixer.music.play()
                    if event.key == pygame.K_LEFT:
                        k-=1
                        k=k%len(_songs)
                        pygame.mixer.music.load(_songs[k])
                        pygame.mixer.music.play()
                    if event.key == pygame.K_SPACE:
                        space=not space
                        if(space):
                            pygame.mixer.music.play()
                        else:
                            pygame.mixer.music.stop()
        screen.fill((255, 255, 255))
        if(space):
            screen.blit(image, (0, 0))
        else:
            screen.blit(image1, (0, 0))
        pygame.display.flip()
        clock.tick(60)
