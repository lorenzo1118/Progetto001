import pygame
import sys
import random

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
nave = pygame.transform.scale(nave, (60, 60))

# Carica l'immagine dell'alieno
alien = pygame.image.load("img/alien.png")
alien = pygame.transform.scale(alien, (40, 40))

# Carica l'immagine del pulsante Start
start_button_img = pygame.image.load("img/start.png")
start_button_img = pygame.transform.scale(start_button_img, (150, 60))

# Carica l'immagine del proiettile
bullet = pygame.image.load("img/bullet.png")
bullet = pygame.transform.scale(bullet, (8, 16))

# Posizione del pulsante Start
start_button_rect = start_button_img.get_rect(center=(screen_width // 2, screen_height // 2))

# Posizione iniziale della nave
nave_x = screen_width // 2 - 30
nave_y = screen_height - 100

# Velocità della nave
nave_speed = 4

# Parametri degli alieni
alien_speed = 1
alien_direction = 1
alien_rows = 3
alien_cols = 5
alien_gap = 70
alien_move_range = 50  # Gamma di movimento limitata a sinistra e destra

# Parametri dei proiettili
bullet_speed = 4
bullets = []
alien_bullets = []

# Calcolare la posizione iniziale centrata degli alieni
alien_start_x = (screen_width - (alien_cols * alien_gap)) // 2
alien_start_y = 50

# Crea una lista per memorizzare gli alieni
aliens = []
for row in range(alien_rows):
    alien_row = []
    for col in range(alien_cols):
        alien_x_pos = alien_start_x + col * alien_gap
        alien_y_pos = alien_start_y + row * alien_gap
        alien_row.append(pygame.Rect(alien_x_pos, alien_y_pos, 40, 40))
    aliens.append(alien_row)

# Clock per gestire il framerate
clock = pygame.time.Clock()

# Stato del gioco
game_started = False
game_over = False

# Funzione per resettare il gioco
def reset_game():
    global nave_x, nave_y, bullets, alien_bullets, game_over, game_started, aliens, alien_direction
    nave_x = screen_width // 2 - 30
    nave_y = screen_height - 100
    bullets = []
    alien_bullets = []
    alien_direction = 1
    aliens.clear()
    for row in range(alien_rows):
        alien_row = []
        for col in range(alien_cols):
            alien_x_pos = alien_start_x + col * alien_gap
            alien_y_pos = alien_start_y + row * alien_gap
            alien_row.append(pygame.Rect(alien_x_pos, alien_y_pos, 40, 40))
        aliens.append(alien_row)
    game_over = False
    game_started = True

# Funzione per sparare dalla nave
def shoot_from_ship():
    bullet_rect = pygame.Rect(nave_x + 26, nave_y, 8, 16)
    bullets.append([bullet_rect, 0, -bullet_speed])

# Funzione per far sparare gli alieni
def alien_shoot():
    if random.random() < 0.01:
        alien_row = random.choice(aliens)
        if alien_row:
            alien = random.choice(alien_row)
            bullet_rect = pygame.Rect(alien.x + 16, alien.y + 40, 8, 16)
            alien_bullets.append([bullet_rect, 0, bullet_speed])

# Loop principale del gioco
running = True
alien_move_counter = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Controllo clic sul pulsante Start
        if event.type == pygame.MOUSEBUTTONDOWN:
            if start_button_rect.collidepoint(event.pos):
                if not game_started or game_over:
                    reset_game()

    # Disegna la schermata di avvio o game over
    if not game_started or game_over:
        screen.blit(background, (0, 0))
        screen.blit(start_button_img, start_button_rect.topleft)
    else:
        # Gestione dei movimenti della nave
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            nave_x -= nave_speed
        if keys[pygame.K_RIGHT]:
            nave_x += nave_speed
        if keys[pygame.K_SPACE]:
            shoot_from_ship()

        # Evita che la nave esca dallo schermo
        nave_x = max(0, min(screen_width - 60, nave_x))

        # Movimento degli alieni
        alien_move_counter += alien_speed
        if alien_move_counter >= alien_move_range:
            alien_direction *= -1
            alien_move_counter = 0

        for row in aliens:
            for alien_rect in row:
                alien_rect.x += alien_direction * alien_speed

        # Sparo degli alieni
        alien_shoot()

        # Gestisci i proiettili della nave
        for bullet_data in bullets[:]:
            bullet_rect, bullet_dx, bullet_dy = bullet_data
            bullet_rect.y += bullet_dy
            if bullet_rect.y < 0:
                bullets.remove(bullet_data)
            else:
                # Controlla collisioni con gli alieni
                for row in aliens[:]:
                    for alien_rect in row[:]:
                        if bullet_rect.colliderect(alien_rect):
                            bullets.remove(bullet_data)
                            row.remove(alien_rect)
                            break

        # Gestisci i proiettili degli alieni
        for bullet_data in alien_bullets[:]:
            bullet_rect, bullet_dx, bullet_dy = bullet_data
            bullet_rect.y += bullet_dy
            if bullet_rect.y > screen_height:
                alien_bullets.remove(bullet_data)
            elif bullet_rect.colliderect(pygame.Rect(nave_x, nave_y, 60, 60)):
                game_over = True

        # Disegna lo sfondo
        screen.blit(background, (0, 0))

        # Disegna la nave
        screen.blit(nave, (nave_x, nave_y))

        # Disegna gli alieni
        for row in aliens:
            for alien_rect in row:
                screen.blit(alien, alien_rect.topleft)

        # Disegna i proiettili della nave
        for bullet_data in bullets:
            bullet_rect, _, _ = bullet_data
            screen.blit(bullet, bullet_rect.topleft)

        # Disegna i proiettili degli alieni
        for bullet_data in alien_bullets:
            bullet_rect, _, _ = bullet_data
            screen.blit(bullet, bullet_rect.topleft)

        # Controlla se il gioco è finito
        if not any(aliens) or game_over:
            game_over = True

    # Aggiorna lo schermo
    pygame.display.flip()
    clock.tick(60)

# Esci dal gioco
pygame.quit()
sys.exit()
