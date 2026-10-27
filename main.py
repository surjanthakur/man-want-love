import pygame

pygame.init()


SCREEN_WIDTH = 800
SCREEN_HIGHT = 800


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HIGHT))
clock = pygame.time.Clock()

pygame.display.set_caption("man-want-love❤️")

x = 200
y = 300

image = pygame.image.load("./assets/fighter/idle.png")

rect = image.get_rect()
rect.center = (x, y)

run_game = True

while run_game:
    screen.blit(image, rect)

    # event to stop game when user quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_game = False

            # update everthing we draw
    pygame.display.update()
    screen.fill(color="blue")


pygame.quit()
