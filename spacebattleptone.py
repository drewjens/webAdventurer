import pygame
import time 
import random
pygame.font.init()

WIDTH = 1000
HEIGHT = 500
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("game1")


BG = pygame.transform.scale(pygame.image.load("spaceBG.png"), (WIDTH, HEIGHT))
SHIP = pygame.transform.scale(pygame.image.load("spaceship.png"), (60, 40))

PLAYER_HEIGHT = 40
PLAYER_WIDTH = 40
#PLAYER_VEL = 2

BULLET_WIDTH = 50
BULLET_HEIGHT = 4
#BULLET_START_X = WIDTH+BULLET_WIDTH
BULLET_VEL = 5

FONT = pygame.font.SysFont("comicsans", 30)

def draw(player, elapsed_time, bullets):
    WINDOW.blit(BG, (0, 0))

    #time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    #WINDOW.blit(time_text, (10, 10))

    time_remaining = FONT.render(f"Time remaining: {30 - round(elapsed_time)}s", 1, "white")
    WINDOW.blit(time_remaining, (10, 10))
    
    #pygame.draw.rect(WINDOW, "purple", player)
    WINDOW.blit(SHIP, player)

    for bullet in bullets:
        pygame.draw.rect(WINDOW, "red", bullet)
   

    pygame.display.update()


def main():
    run = True

    player = SHIP.get_rect()
    #player = pygame.Rect(WIDTH/2, HEIGHT/2, PLAYER_WIDTH, PLAYER_HEIGHT)

    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0

    bullet_add_increment = 2000
    bullet_count = 0

    bullets = []
    hit = False

    player_vel_left = 1
    player_vel_right = 1
    player_vel_up = 1
    player_vel_down = 1


    while run:
        bullet_count += clock.tick(60)
        elapsed_time = time.time() - start_time


        if bullet_count > bullet_add_increment:
            for _ in range(5):
                bullet_y = random.randint(0, HEIGHT-BULLET_HEIGHT)
                bullet = pygame.Rect(WIDTH + BULLET_WIDTH, bullet_y, BULLET_WIDTH, BULLET_HEIGHT)
                bullets.append(bullet)

        bullet_add_increment = max(200, bullet_add_increment-1)
        if bullet_count > bullet_add_increment:
            bullet_count = 0


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break


        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - player_vel_left >= 0:
            player_vel_right = 1
            player_vel_up = 1
            player_vel_down = 1
            player.x-=player_vel_left
            player_vel_left+=.1
        if keys[pygame.K_RIGHT]and player.x + player_vel_right+PLAYER_WIDTH <= WIDTH: 
            player_vel_left = 1
            player_vel_up = 1
            player_vel_down = 1       
            player.x+=player_vel_right
            player_vel_right+=.1
        if keys[pygame.K_DOWN] and player.y + player_vel_down+PLAYER_HEIGHT <= HEIGHT:
            player_vel_left = 1
            player_vel_right = 1
            player_vel_up = 1
            player.y+=player_vel_down
            player_vel_down+=.1
        if keys[pygame.K_UP] and player.y - player_vel_up >= 0:
            player_vel_left = 1
            player_vel_right = 1
            player_vel_down = 1
            player.y-=player_vel_up
            player_vel_up+=.1

        for bullet in bullets[:]:
            bullet.x-= BULLET_VEL
            if bullet.x + BULLET_WIDTH < 0:
                bullets.remove(bullet)
            elif bullet.x - bullet.width <= player.x and bullet.colliderect(player):
                bullets.remove(bullet)
                hit = True
                break


        if round(elapsed_time) > 30:
            won_text = FONT.render("CONGRATULATIONS! THE CODE IS 9243", 1, "white")
            WINDOW.blit(won_text, (WIDTH/2 - won_text.get_width()/2, HEIGHT/2 - won_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(4000)
            break


        if hit:
            lost_text = FONT.render("GAME OVER", 1, "white")
            WINDOW.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(4000)
            break

        draw(player, elapsed_time, bullets)


    pygame.quit

if __name__ == "__main__":
    main()
