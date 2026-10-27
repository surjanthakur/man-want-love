import sys

import pygame

# initializes internal elements
pygame.init()


SCREEN_WIDTH = 500
SCREEN_HIGHT = 300

run_game = True
# set screen hight , widht
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HIGHT))
# give us a object
clock = pygame.time.Clock()
# set a name for game
pygame.display.set_caption("man-want-love❤️")

main_surface_img = pygame.image.load(
    "./assets/Land-assets/Backgrounds/nature_1/orig.png"
)
ground_tile_1 = pygame.image.load("./assets/Land_assets/Tiles/Tile_01.png")


while run_game:

    # event to stop game when user quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_game = False

    screen.blit(main_surface_img, (0, 0))
    screen.blit(ground_tile_1, (0, 0))
    # update everthing we draw
    pygame.display.update()
    clock.tick(60)


print("game quited")
# to unintialize all the elements and exit game
pygame.quit()
sys.exit()
