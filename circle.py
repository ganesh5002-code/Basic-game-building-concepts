import pygame

pygame.init()

screen = pygame.display.set_mode((500, 600))
screen.fill('white')
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pygame.draw.circle(screen, ('green'), (300, 500), 80, 5)
    pygame.display.flip()
