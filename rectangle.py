import pygame

pygame.init()

screen= pygame.display.set_mode((600, 700))

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    pygame.draw.rect(screen, ('green'), pygame.Rect(300, 400, 100, 200))
    pygame.display.flip()



