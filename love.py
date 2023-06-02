import pygame

# Inisialisasi Pygame
pygame.init()

# Ukuran layar
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Drawing Love")

# Warna
RED = (255, 0, 0)

# Fungsi untuk menggambar gambar love
def draw_love(x, y):
    # Gambar hati
    pygame.draw.polygon(screen, RED, [(x, y + 50), (x + 50, y), (x + 100, y + 50), (x + 50, y + 100)])

    # Gambar lingkaran
    pygame.draw.circle(screen, RED, (x + 25, y + 50), 25)
    pygame.draw.circle(screen, RED, (x + 75, y + 50), 25)

# Loop utama program
running = True
while running:
    # Tangkap event dari keyboard dan mouse
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Bersihkan layar
    screen.fill((255, 255, 255))

    # Gambar gambar love pada posisi (400, 300)
    draw_love(400, 300)

    # Update tampilan
    pygame.display.update()

# Keluar dari Pygame
pygame.quit()
