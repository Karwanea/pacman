import pygame
import import_image


pygame.init()
screen = pygame.display.set_mode((1200, 1200))
clock = pygame.time.Clock()
running = True

test_pac = pygame.transform.scale(import_image.img_pac_droite, (40, 40))
pac_ferme = pygame.transform.scale(import_image.img_pac_ferme, (40, 40))


red_right_1 = pygame.transform.scale(import_image.img_red_right_1, (40, 40))
red_right_2 = pygame.transform.scale(import_image.img_red_right_2, (40, 40))

red_left_1 = pygame.transform.scale(import_image.img_red_left_1, (40, 40))
red_left_2 = pygame.transform.scale(import_image.img_red_left_2, (40, 40))

red_up_1 = pygame.transform.scale(import_image.img_red_up_1, (40, 40))
red_up_2 = pygame.transform.scale(import_image.img_red_up_2, (40, 40))

red_down_1 = pygame.transform.scale(import_image.img_red_down_1, (40, 40))
red_down_2 = pygame.transform.scale(import_image.img_red_down_2, (40, 40))


WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 1200

MAZE_WIDTH = 800
MAZE_HEIGHT = 800

middle_x = screen.get_width() / 2
middle_y = screen.get_height() / 2

circle_pos = pygame.Vector2(middle_x, middle_y)

rect_pos = pygame.Rect(200, 200, 800, 800)

player_pos = pygame.Vector2(200, 200)

ghost_pos = pygame.Vector2(400, 400)

player_mouv = pygame.Vector2(1, 0)

dt = clock.tick(60) / 1000

pac_right = pygame.transform.rotate(test_pac, 0)

pac_left = pygame.transform.rotate(test_pac, 180)

pac_top = pygame.transform.rotate(test_pac, 90)

pac_bottom = pygame.transform.rotate(test_pac, 270)

direction_pac = {
    "right": pac_right, "left": pac_left, "up": pac_top, "bottom": pac_bottom, "False": pac_ferme
}

way = "right"

mouth_open = True

mouv_ghost_red = True

mouv_ghost_blue = False

mouv_ghost_orange = True

mouv_ghost_pink = False

anim_timer = 0

anim_timer_ghost = 0

score = 0

time = 0

def switch_image(anim_timer_ghost, ghost_pos, mouv_ghost, version_1, version_2):

    if anim_timer_ghost >= 2.0:
        mouv_ghost = not mouv_ghost
        anim_timer_ghost -= 2.0
    # if ghost_pos == (0, 0):
    #     anim_timer_ghost = 0
    #     if not mouv_ghost:
    #         mouv_ghost = not mouv_ghost
    if mouv_ghost == True:
        screen.blit(version_1, (ghost_pos))
    if not mouv_ghost:
        screen.blit(version_2, (ghost_pos))
    return anim_timer_ghost, mouv_ghost


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if event.type == pygame.KEYDOWN:
        #     if pygame.K_ESCAPE:
        #         running = False
    
    font = pygame.font.Font(None, 20)

    screen.fill("black")

    pygame.draw.circle(screen, "red", circle_pos, 40)

    pygame.draw.rect(screen, "red", rect_pos, 2)

    score += dt

    # time += dt / 100

    score_message = font.render(f"SCORE : {round(score)}", True, "white")

    # time_message = font.render(f"time : {time}", True, "white")
    
    screen.blit(score_message, (200, 1100))

    # screen.blit(time_message, (400, 1100))
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        player_mouv = (0, -1)
        way = "up"
    if keys[pygame.K_s]:
        player_mouv = (0, 1)
        way = "bottom"
    if keys[pygame.K_a]:
        player_mouv = (-1, 0)
        way = "left"
    if keys[pygame.K_d]:
        player_mouv = (1, 0)
        way = "right"


    target = player_pos + (pygame.Vector2(player_mouv) * 10 * dt)
    real_target_x = max(203, min(target.x ,957))
    real_target_y = max(203, min(target.y ,957))

    real_mouv = pygame.Vector2(real_target_x, real_target_y)

    if target.x != real_target_x or target.y != real_target_y:
        player_mouv = pygame.Vector2(0, 0)

    player_pos = real_mouv

    anim_timer += dt
    if anim_timer >= 2.0:
        mouth_open = not mouth_open
        anim_timer -= 2.0
    if player_mouv == (0, 0):
        anim_timer = 0
        if not mouth_open:
            mouth_open = not mouth_open
    if mouth_open == True:
        screen.blit(direction_pac[way], (player_pos))
    if not mouth_open:
        screen.blit(pac_ferme, (player_pos))

    anim_timer_ghost += dt

    anim_timer_ghost, mouv_ghost_red = switch_image(anim_timer_ghost, ghost_pos, mouv_ghost_red, red_right_1, red_right_2)


    # anim_timer_ghost, mouv_ghost_pink = switch_image(anim_timer_ghost, ghost_pos, mouv_ghost_pink, red_right_1, red_right_2)
    # anim_timer_ghost, mouv_ghost_orange = switch_image(anim_timer_ghost, ghost_pos, mouv_ghost_orange, red_right_1, red_right_2)
    # anim_timer_ghost, mouv_ghost_blue = switch_image(anim_timer_ghost, ghost_pos, mouv_ghost_blue, red_right_1, red_right_2)


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
    # 
    # 
    # 
    # 
    #     # if keys[pygame.K_UP]:
    #     circle_pos.y -= 250 * dt
    # if keys[pygame.K_DOWN]:
    #     circle_pos.y += 250 * dt
    # if keys[pygame.K_LEFT]:
    #     circle_pos.x -= 250 * dt
    # if keys[pygame.K_RIGHT]:
    #     circle_pos.x += 250 * dt
