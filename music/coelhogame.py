import pygame
import random

# Inicialização do Pygame
pygame.init()

# Cores inspiradas em sistemas solares e elementos espaciais
BACKGROUND_COLOR = (5, 5, 25)
PLAYER_COLOR = (255, 165, 0)
PLAYER_GUN_COLOR = (220, 220, 220)
ENEMY_COLOR = (150, 150, 150)
ENEMY_EYE_COLOR = (50, 50, 50)
BULLET_COLOR = (255, 255, 255)
SCORE_COLOR = (255, 255, 255)

# Dimensões da tela
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Classe Player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((60, 40), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.draw_player()
        self.rect.x = (SCREEN_WIDTH - self.rect.width) // 2
        self.rect.y = SCREEN_HEIGHT - self.rect.height - 20

    def draw_player(self):
        pygame.draw.rect(self.image, PLAYER_COLOR, pygame.Rect(0, 0, 60, 40))
        pygame.draw.rect(self.image, PLAYER_GUN_COLOR, pygame.Rect(25, 0, 10, 20))

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        self.rect.x = max(0, min(self.rect.x, SCREEN_WIDTH - self.rect.width))

    def shoot(self):
        x_bullet = self.rect.x + self.rect.width // 2
        y_bullet = self.rect.y
        bullet = Bullet(x_bullet, y_bullet)
        all_sprites.add(bullet)
        bullets.add(bullet)

# Classe Enemy
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 40), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.draw_enemy()
        self.rect.x = random.randint(0, SCREEN_WIDTH - 40)
        self.rect.y = random.randint(50, 200)
        self.direction = 1

    def draw_enemy(self):
        pygame.draw.rect(self.image, ENEMY_COLOR, pygame.Rect(0, 0, 40, 40))
        pygame.draw.circle(self.image, ENEMY_EYE_COLOR, (12, 16), 4)
        pygame.draw.circle(self.image, ENEMY_EYE_COLOR, (28, 16), 4)

    def update(self):
        self.rect.x += self.direction
        if self.rect.x <= 0 or self.rect.x >= SCREEN_WIDTH - 40:
            self.rect.y += 20
            self.direction *= -1

# Classe Bullet
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((5, 20), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.midbottom = (x, y)
        self.draw_bullet()

    def draw_bullet(self):
        pygame.draw.rect(self.image, BULLET_COLOR, pygame.Rect(0, 0, 5, 20))

    def update(self):
        self.rect.y -= 10
        if self.rect.y < 0:
            self.kill()

# Inicialização da tela
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Invader")

# Sprites
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()

# Criação dos inimigos
for _ in range(10):
    enemy = Enemy()
    all_sprites.add(enemy)
    enemies.add(enemy)

# Criação do jogador
player = Player()
all_sprites.add(player)

# Carregamento do som do tiro
sound_shoot = pygame.mixer.Sound("tiro.wav")

# Score
score = 0
fonte = pygame.font.Font(None, 36)

# Loop principal do jogo
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()

    all_sprites.update()

    # Verifica colisão entre tiro e inimigo
    hits = pygame.sprite.groupcollide(bullets, enemies, True, True)
    for hit in hits:
        score += 1

    # Preenchimento do fundo
    screen.fill(BACKGROUND_COLOR)

    # Desenho dos sprites
    all_sprites.draw(screen)

    # Desenho do score
    score_text = fonte.render("Score: " + str(score), True, SCORE_COLOR)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

# Encerramento do Pygame
pygame.quit()
