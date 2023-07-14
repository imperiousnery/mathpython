import pygame
import cairo
import random

# Inicialização do Pygame
pygame.init()

# Configurações da janela do jogo
largura_janela = 800
altura_janela = 600
janela = pygame.display.set_mode((largura_janela, altura_janela))
pygame.display.set_caption("Jogo Complexo com Cairo")

# Cores
COR_FUNDO = (30, 30, 30)
COR_TEXTO = (255, 255, 255)

# Classe do Jogador
class Jogador(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        elif keys[pygame.K_RIGHT]:
            self.rect.x += 5
        if keys[pygame.K_UP]:
            self.rect.y -= 5
        elif keys[pygame.K_DOWN]:
            self.rect.y += 5

# Classe dos Inimigos
class Inimigo(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.velocidade_x = random.choice([-2, 2])
        self.velocidade_y = random.choice([-2, 2])

    def update(self):
        self.rect.x += self.velocidade_x
        self.rect.y += self.velocidade_y

        if self.rect.left < 0 or self.rect.right > largura_janela:
            self.velocidade_x *= -1
        if self.rect.top < 0 or self.rect.bottom > altura_janela:
            self.velocidade_y *= -1

# Classe do Tiro
class Tiro(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        self.rect.y -= 5
        if self.rect.bottom < 0:
            self.kill()

# Criação dos grupos de sprites
sprites = pygame.sprite.Group()
jogador_group = pygame.sprite.Group()
inimigos_group = pygame.sprite.Group()
tiros_group = pygame.sprite.Group()

# Criação do jogador
jogador = Jogador(largura_janela // 2, altura_janela // 2)
sprites.add(jogador)
jogador_group.add(jogador)

# Loop principal do jogo
jogo_ativo = True
clock = pygame.time.Clock()
while jogo_ativo:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jogo_ativo = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                tiro = Tiro(jogador.rect.centerx, jogador.rect.top)
                sprites.add(tiro)
                tiros_group.add(tiro)

    # Criar inimigos aleatoriamente
    if random.random() < 0.01:
        inimigo = Inimigo(random.randint(0, largura_janela), random.randint(0, altura_janela))
        sprites.add(inimigo)
        inimigos_group.add(inimigo)

    # Atualizar os sprites
    sprites.update()

    # Verificar colisões
    colisoes_inimigos = pygame.sprite.spritecollide(jogador, inimigos_group, False)
    if colisoes_inimigos:
        jogo_ativo = False

    colisoes_tiros = pygame.sprite.groupcollide(tiros_group, inimigos_group, True, True)

    # Renderizar a cena
    janela.fill(COR_FUNDO)
    sprites.draw(janela)

    pygame.display.flip()
    clock.tick(60)

# Encerramento do Pygame
pygame.quit()
