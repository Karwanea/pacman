import pygame

pygame.init()
screen = pygame.display.set_mode((1200, 1200))
clock = pygame.time.Clock()
running = True
test_ghost = pygame.image.load("/Users/el attar/Desktop/pacman/test_ghost.jpg")
# test_ghost = pygame.image.load("/home/kael-att/pacman/test_ghost.jpg")
img_test_ghost = pygame.transform.scale(test_ghost, (40, 40))

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 1200

middle_x = screen.get_width() / 2
middle_y = screen.get_height() / 2

circle_pos = pygame.Vector2(middle_x, middle_y)

rect_pos = pygame.Rect(200, 200, middle_x, middle_y)

player_pos = circle_pos

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if event.type == pygame.KEYDOWN:
        #     if pygame.K_ESCAPE:
        #         running = False
    
    

    screen.fill("black")

    pygame.draw.circle(screen, "red", player_pos, 40)

    pygame.draw.rect(screen, "red", rect_pos, 5)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player_pos.y -= 250 * dt
    if keys[pygame.K_DOWN]:
        player_pos.y += 250 * dt
    if keys[pygame.K_LEFT]:
        player_pos.x -= 250 * dt
    if keys[pygame.K_RIGHT]:
        player_pos.x += 250 * dt
    if keys[pygame.K_w]:
        player_pos.y -= 250 * dt
    if keys[pygame.K_s]:
        player_pos.y += 250 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 250 * dt
    if keys[pygame.K_d]:
        player_pos.x += 250 * dt

    screen.blit(img_test_ghost, (200, 200))

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()



