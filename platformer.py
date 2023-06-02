import pygame
from pygame.locals import *
import sys

# Inisialisasi Pygame
pygame.init()

# Ukuran layar
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Platformer Game")

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

# Loop utama game
running = True
while running:
    screen.fill(WHITE)

    # Tangkap event dari keyboard dan pengendali
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

    # Dapatkan input dari pengendali
    joystick_count = pygame.joystick.get_count()
    for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()

        # Pergerakan pemain
        axis_x = joystick.get_axis(0)
        axis_y = joystick.get_axis(1)
        player_x += int(axis_x * player_vel)
        player_y -= int(axis_y * player_vel)

    # Batasi pemain di dalam layar
    if player_x < 0:
        player_x = 0
    if player_x > WIDTH - player_width:
        player_x = WIDTH - player_width
    if player_y < 0:
        player_y = 0
    if player_y > HEIGHT - player_height:
        player_y = HEIGHT - player_height

    # Gambar pemain
    pygame.draw.rect(screen, RED, (player_x, player_y, player_width, player_height))

    # Update tampilan
    pygame.display.update()

# Keluar dari Pygame
pygame.quit()
sys.exit()
