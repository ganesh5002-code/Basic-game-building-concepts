import pygame

pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("My first game screen")
font = pygame.font.Font(None, 36) 
text_surface = font.render("Rectangle", True, (0, 0, 0))
text_rect = text_surface.get_rect(center=(width // 2, height // 4))

rect_width, rect_height = 200, 120
rect = pygame.Rect(
(width - rect_width) // 2,
(height - rect_height) // 2,
rect_width,
rect_height
)
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (64, 244, 208), rect)
    screen.blit(text_surface, text_rect)
    pygame.display.flip()

pygame.quit()
