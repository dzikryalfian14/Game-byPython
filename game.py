import pygame
from pygame.locals import *

# Inisialisasi Pygame
pygame.init()

# Ukuran layar
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game yang Dikendalikan")

# Warna
WHITE = (255, 255, 255)

# Koordinat pemain
player_x = 300
player_y = 400

# Kecepatan pemain
player_speed = 5

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
        player_x -= player_speed
    if keys[K_RIGHT]:
        player_x += player_speed
    if keys[K_UP]:
        player_y -= player_speed
    if keys[K_DOWN]:
        player_y += player_speed

    # Batasi pemain di dalam layar
    if player_x < 0:
        player_x = 0
    if player_x > WIDTH - 32:
        player_x = WIDTH - 32
    if player_y < 0:
        player_y = 0
    if player_y > HEIGHT - 32:
        player_y = HEIGHT - 32

    # Gambar pemain
    pygame.draw.rect(screen, (255, 0, 0), (player_x, player_y, 32, 32))

    # Update tampilan
    pygame.display.update()

# Keluar dari Pygame
pygame.quit()
