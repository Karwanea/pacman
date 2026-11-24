import pygame


pygame.init()
screen = pygame.display.set_mode((1200, 1200))
clock = pygame.time.Clock()
running = True
# test_ghost = pygame.image.load("/Users/el attar/Desktop/pacman/test_ghost.jpg")
test_ghost = pygame.image.load("/home/kael-att/pacman/test_ghost.jpg")
img_test_ghost = pygame.transform.scale(test_ghost, (40, 40))

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 1200

MAZE_WIDTH = 800
MAZE_HEIGHT = 800

middle_x = screen.get_width() / 2
middle_y = screen.get_height() / 2

circle_pos = pygame.Vector2(middle_x, middle_y)

rect_pos = pygame.Rect(200, 200, 800, 800)

player_pos = pygame.Vector2(200, 200)

player_mouv = pygame.Vector2(1, 0)

dt = clock.tick(60) / 1000

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if event.type == pygame.KEYDOWN:
        #     if pygame.K_ESCAPE:
        #         running = False
    
    screen.fill("black")

    pygame.draw.circle(screen, "red", circle_pos, 40)

    pygame.draw.rect(screen, "red", rect_pos, 2)

    screen.blit(img_test_ghost, (player_pos))
    
    keys = pygame.key.get_pressed()
    # if keys[pygame.K_UP]:
    #     circle_pos.y -= 250 * dt
    # if keys[pygame.K_DOWN]:
    #     circle_pos.y += 250 * dt
    # if keys[pygame.K_LEFT]:
    #     circle_pos.x -= 250 * dt
    # if keys[pygame.K_RIGHT]:
    #     circle_pos.x += 250 * dt

    if keys[pygame.K_w]:
        player_mouv = (0, -1)
    if keys[pygame.K_s]:
        player_mouv = (0, 1)
    if keys[pygame.K_a]:
        player_mouv = (-1, 0)
    if keys[pygame.K_d]:
        player_mouv = (1, 0)
 

    target = player_pos + (pygame.Vector2(player_mouv) * 10 * dt)
    real_target_x = max(203, min(target.x ,957))
    real_target_y = max(203, min(target.y ,957))

    real_mouv = pygame.Vector2(real_target_x, real_target_y)

    if target.x != real_target_x or target.y != real_target_y:
        player_mouv = pygame.Vector2(0, 0)

    player_pos = real_mouv

    pygame.display.flip()

pygame.quit()



    # if keys[pygame.K_w]:
    #     new_y = player_pos.y - 600 * dt
    #     if new_y >= rect_pos.top:
    #         player_pos.y -= 600 * dt
    # if keys[pygame.K_s]:
    #     new_y = player_pos.y + 600 * dt
    #     if new_y + 40 <= rect_pos.bottom:
    #         player_pos.y += 600 * dt
    # if keys[pygame.K_a]:
    #     new_x = player_pos.x - 600 * dt
    #     if new_x >= rect_pos.left:
    #         player_pos.x -= 600 * dt
    # if keys[pygame.K_d]:
    #     new_x = player_pos.x + 600 * dt
    #     if new_x + 40 <= rect_pos.right:
    #         player_pos.x += 600 * dt