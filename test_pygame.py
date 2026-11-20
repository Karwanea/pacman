import pygame

pygame.init()
screen = pygame.display.set_mode((1200, 1200))
clock = pygame.time.Clock()
running = True
test_ghost = pygame.image.load("/home/kael-att/pacman/test_ghost.jpg")
img_test_ghost = pygame.transform.scale(test_ghost, (40, 40))

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 1200

middle_x = WINDOW_WIDTH //2
middle_y = WINDOW_HEIGHT // 2

def draw_square():

    for middle_x 


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if pygame.K_ESCAPE:
                running = False

    screen.fill("black")

    clock.tick(60)

    screen.blit(img_test_ghost, (200, 200))

    pygame.display.flip()

    

pygame.quit()



