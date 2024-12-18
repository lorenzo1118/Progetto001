import pygame
import sys

# Inizializza Pygame
pygame.init()

# Dimensioni della finestra del gioco
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Gioco con Nave e Alieni")

# Carica l'immagine di sfondo
background = pygame.image.load("img/bg.png")
background = pygame.transform.scale(background, (screen_width, screen_height))

# Carica l'immagine della nave
nave = pygame.image.load("img/nave.png")
nave = pygame.transform.scale(nave, (50, 50))  # Ridimensiona la nave

# Carica l'immagine dell'alieno
alien = pygame.image.load("img/alien.png")
alien = pygame.transform.scale(alien, (50, 50))  # Ridimensiona l'alieno

# Posizione iniziale della nave
nave_x = screen_width // 2 - 25  # Centra la nave orizzontalmente
nave_y = screen_height - 60  # Posiziona la nave vicino al fondo dello schermo

# Velocità della nave
nave_speed = 5

# Parametri degli alieni
alien_speed = 3  # Velocità di movimento degli alieni
alien_direction = 1  # 1 significa destra, -1 significa sinistra
alien_rows = 3  # Numero di righe di alieni
alien_cols = 5  # Numero di colonne di alieni
alien_gap = 80  # Aumenta la distanza tra gli alieni (distanza orizzontale)

# Calcolare la posizione iniziale centrata degli alieni
alien_start_x = (screen_width - (alien_cols * alien_gap)) // 2  # Centra la griglia orizzontalmente
alien_start_y = 50  # Posizione verticale iniziale degli alieni

# Crea una lista per memorizzare gli alieni
aliens = []
for row in range(alien_rows):
    alien_row = []
    for col in range(alien_cols):
        # Posizione iniziale di ogni alieno
        alien_x_pos = alien_start_x + col * alien_gap  # Posizione orizzontale centrata
        alien_y_pos = alien_start_y + row * alien_gap   # Posizione verticale
        alien_row.append(pygame.Rect(alien_x_pos, alien_y_pos, 50, 50))  # Raccogliamo le posizioni degli alieni
    aliens.append(alien_row)

# Clock per gestire il framerate
clock = pygame.time.Clock()

# Loop principale del gioco
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Gestione dei movimenti della nave
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        nave_x -= nave_speed  # Muove la nave a sinistra
    if keys[pygame.K_RIGHT]:
        nave_x += nave_speed  # Muove la nave a destra
    if keys[pygame.K_UP]:
        nave_y -= nave_speed  # Muove la nave in alto
    if keys[pygame.K_DOWN]:
        nave_y += nave_speed  # Muove la nave in basso

    # Evita che la nave esca dallo schermo
    if nave_x < 0:
        nave_x = 0
    if nave_x > screen_width - 50:
        nave_x = screen_width - 50
    if nave_y < 0:
        nave_y = 0
    if nave_y > screen_height - 50:
        nave_y = screen_height - 50

    # Movimento degli alieni (si muovono tutti insieme)
    for row in aliens:
        for alien_rect in row:
            alien_rect.x += alien_speed * alien_direction  # Muove gli alieni orizzontalmente

    # Inverti la direzione degli alieni quando toccano il bordo
    if aliens[0][0].x <= 0 or aliens[0][alien_cols - 1].x >= screen_width - 50:
        alien_direction *= -1  # Cambia direzione

    # Disegna lo sfondo
    screen.blit(background, (0, 0))

    # Disegna la nave
    screen.blit(nave, (nave_x, nave_y))

    # Disegna gli alieni
    for row in aliens:
        for alien_rect in row:
            screen.blit(alien, alien_rect.topleft)

    # Aggiorna lo schermo
    pygame.display.flip()

    # Imposta il frame rate (FPS)
    clock.tick(60)

# Esci correttamente
pygame.quit()
sys.exit()
