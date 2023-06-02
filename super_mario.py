import pygame
from pygame.locals import *

# Inisialisasi Pygame
pygame.init()

# Ukuran layar
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Super Mario Sederhana")

# Warna
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Posisi dan ukuran pemain
player_x = 50
player_y = 450
player_width = 40
player_height = 60
player_vel = 5
is_jumping = False
jump_count = 10

# Posisi dan ukuran platform
platform_x = 0
platform_y = 500
platform_width = WIDTH

# Loop utama game
running = True
while running:
    screen.fill(WHITE)

    # Tangkap event dari keyboard
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Dapatkan keadaan tombol yang ditekan
    keys = pygame.key.get_pressed()

    # Pergerakan pemain
    if keys[K_LEFT]:
        player_x -= player_vel
    if keys[K_RIGHT]:
        player_x += player_vel

    # Melompat
    if not is_jumping:
        if keys[K_SPACE]:
            is_jumping = True
    else:
        if jump_count >= -10:
            neg = 1
            if jump_count < 0:
                neg = -1
            player_y -= (jump_count ** 2) * 0.5 * neg
            jump_count -= 1
        else:
            is_jumping = False
            jump_count = 10

    # Batasi pemain di dalam layar
    if player_x < 0:
        player_x = 0
    if player_x > WIDTH - player_width:
        player_x = WIDTH - player_width

    # Gambar platform
    pygame.draw.rect(screen, BLUE, (platform_x, platform_y, platform_width, 10))

    # Gambar pemain
    pygame.draw.rect(screen, RED, (player_x, player_y, player_width, player_height))

    # Update tampilan
    pygame.display.update()

# Keluar dari Pygame
pygame.quit()
