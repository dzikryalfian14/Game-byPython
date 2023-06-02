import pygame

# Inisialisasi Pygame
pygame.init()

# Ukuran layar
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Drawing Smiley Faces")

# Warna
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)

# Fungsi untuk menggambar wajah senyum
def draw_smiley_face(x, y):
    # Gambar kepala
    pygame.draw.circle(screen, YELLOW, (x, y), 100)

    # Gambar mata kiri
    pygame.draw.circle(screen, BLACK, (x - 40, y - 30), 15)

    # Gambar mata kanan
    pygame.draw.circle(screen, BLACK, (x + 40, y - 30), 15)

    # Gambar mulut
    pygame.draw.arc(screen, BLACK, (x - 40, y - 20, 80, 60), 3.14, 6.28, 5)

# Loop utama program
running = True
while running:
    # Tangkap event dari keyboard dan mouse
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Bersihkan layar
    screen.fill(WHITE)

    # Gambar wajah senyum pada posisi (400, 300)
    draw_smiley_face(400, 300)

    # Update tampilan
    pygame.display.update()

# Keluar dari Pygame
pygame.quit()
