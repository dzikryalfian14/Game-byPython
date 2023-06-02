import pygame
import random
from pygame.locals import *

# Inisialisasi Pygame
pygame.init()

# Ukuran layar
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Warna
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Ukuran dan posisi awal ular
snake_block = 20
snake_speed = 30
snake_x = WIDTH // 2
snake_y = HEIGHT // 2

# Kecepatan awal pergerakan ular
snake_x_change = 0
snake_y_change = 0

# Inisialisasi tubuh ular
snake_body = []
snake_length = 1

# Inisialisasi score
score = 0

# Fungsi untuk menampilkan skor
font_style = pygame.font.SysFont(None, 30)
score_font = pygame.font.SysFont(None, 40)

def show_score():
    score_text = score_font.render("Score: " + str(score), True, BLACK)
    screen.blit(score_text, [10, 10])

# Fungsi untuk menggambar ular
def draw_snake(snake_block, snake_body):
    for x in snake_body:
        pygame.draw.rect(screen, GREEN, [x[0], x[1], snake_block, snake_block])

# Fungsi untuk menjalankan game
def game_loop():
    # Inisialisasi variabel global
    global snake_x, snake_y, snake_x_change, snake_y_change, snake_body, snake_length, score

    # Inisialisasi variabel game loop
    game_over = False
    game_close = False

    # Posisi makanan awal
    food_x = round(random.randrange(0, WIDTH - snake_block) / 20) * 20
    food_y = round(random.randrange(0, HEIGHT - snake_block) / 20) * 20

    # Loop utama game
    while not game_over:

        while game_close:
            # Tampilkan skor saat game berakhir
            screen.fill(WHITE)
            game_over_text = font_style.render("Game Over! Press SPACE to play again", True, BLACK)
            score_text = score_font.render("Your Score: " + str(score), True, BLACK)
            screen.blit(game_over_text, [WIDTH // 2 - 200, HEIGHT // 2])
            screen.blit(score_text, [WIDTH // 2 - 100, HEIGHT // 2 + 50])
            pygame.display.update()

            # Tangkap event dari keyboard saat game berakhir
            for event in pygame.event.get():
                if event.type == QUIT:
                    game_over = True
                    game_close = False
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        # Reset variabel game loop saat SPACE ditekan
                        snake_x = WIDTH // 2
                        snake_y = HEIGHT // 2
                        snake_x_change = 0
                        snake_y_change = 0
                        snake_body = []
                        snake_length = 1
                        score = 0
                        food_x = round(random.randrange(0, WIDTH - snake_block) / 20) * 20
                        food_y = round(random.randrange(0, HEIGHT - snake_block) / 20) * 20
                        game_close = False

        # Tangkap event dari keyboard saat game sedang berjalan
        for event in pygame.event.get():
            if event.type == QUIT:
                game_over = True
            if event.type == KEYDOWN:
                if event.key == K_LEFT and snake_x_change != snake_block:
                    snake_x_change = -snake_block
                    snake_y_change = 0
                elif event.key == K_RIGHT and snake_x_change != -snake_block:
                    snake_x_change = snake_block
                    snake_y_change = 0
                elif event.key == K_UP and snake_y_change != snake_block:
                    snake_y_change = -snake_block
                    snake_x_change = 0
                elif event.key == K_DOWN and snake_y_change != -snake_block:
                    snake_y_change = snake_block
                    snake_x_change = 0

        # Perbarui posisi ular
        snake_x += snake_x_change
        snake_y += snake_y_change

        # Batasi ular di dalam layar
        if snake_x >= WIDTH or snake_x < 0 or snake_y >= HEIGHT or snake_y < 0:
            game_close = True
        # Deteksi tubuh ular bertabrakan dengan dirinya sendiri
        for segment in snake_body[1:]:
            if segment == [snake_x, snake_y]:
                game_close = True

        # Perbarui tampilan layar
        screen.fill(WHITE)
        pygame.draw.rect(screen, RED, [food_x, food_y, snake_block, snake_block])
        snake_head = []
        snake_head.append(snake_x)
        snake_head.append(snake_y)
        snake_body.append(snake_head)
        if len(snake_body) > snake_length:
            del snake_body[0]

        # Deteksi ular memakan makanan
        for segment in snake_body[:-1]:
            if segment == snake_head:
                game_close = True

        # Gambar ular
        draw_snake(snake_block, snake_body)

        # Gambar skor
        show_score()

        # Update tampilan
        pygame.display.update()

        # Deteksi ular memakan makanan
        if snake_x == food_x and snake_y == food_y:
            food_x = round(random.randrange(0, WIDTH - snake_block) / 20) * 20
            food_y = round(random.randrange(0, HEIGHT - snake_block) / 20) * 20
            snake_length += 1
            score += 10

        # Kontrol kecepatan ular
        clock = pygame.time.Clock()
        clock.tick(snake_speed)

    # Keluar dari Pygame
    pygame.quit()

# Jalankan game
game_loop()
