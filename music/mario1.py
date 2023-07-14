import pygame
import random
import math

# Inicialização do Pygame
pygame.init()

# Configurações da janela do jogo
largura_janela = 800
altura_janela = 600
janela = pygame.display.set_mode((largura_janela, altura_janela))
pygame.display.set_caption("Jogo de Plataforma")

# Cores do Material Design
CORES_MATERIAL = [
    (33, 150, 243),  # Azul
    (244, 67, 54),   # Vermelho
    (0, 150, 136),   # Verde
    (255, 152, 0),   # Laranja
    (156, 39, 176),  # Roxo
    (63, 81, 181),   # Azul Escuro
    (0, 188, 212),   # Ciano
    (255, 87, 34)    # Vermelho Escuro
]

COR_FUNDO = (255, 255, 255)

# Classe do Personagem
class Personagem(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((40, 80))
        self.image.fill(CORES_MATERIAL[1])  # Vermelho
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.velocidade_x = 0
        self.velocidade_y = 0
        self.pulando = False
        self.vidas = 3

    def update(self, plataforma_group):
        self.rect.x += self.velocidade_x
        self.rect.y += self.velocidade_y

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > largura_janela:
            self.rect.right = largura_janela

        colisoes_plataformas = pygame.sprite.spritecollide(self, plataforma_group, False)
        for plataforma in colisoes_plataformas:
            if self.velocidade_y > 0 and self.rect.bottom > plataforma.rect.top:
                self.rect.bottom = plataforma.rect.top
                self.velocidade_y = 0
                self.pulando = False
            elif self.velocidade_y < 0 and self.rect.top < plataforma.rect.bottom:
                self.rect.top = plataforma.rect.bottom
                self.velocidade_y = 0

# Classe dos Inimigos
class Inimigo(pygame.sprite.Sprite):
    def __init__(self, x, y, tamanho, cor):
        super().__init__()
        self.image = pygame.Surface(tamanho)
        self.image.fill(cor)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.velocidade_x = random.randint(-3, 3)
        self.velocidade_y = random.randint(-3, 3)

    def update(self, inimigos_group):
        self.rect.x += self.velocidade_x
        self.rect.y += self.velocidade_y

        # Verificar colisões com outros inimigos
        colisoes_inimigos = pygame.sprite.spritecollide(self, inimigos_group, False)
        for inimigo in colisoes_inimigos:
            if inimigo != self:
                if self.rect.right > inimigo.rect.left or self.rect.left < inimigo.rect.right:
                    self.velocidade_x *= -1
                if self.rect.bottom > inimigo.rect.top or self.rect.top < inimigo.rect.bottom:
                    self.velocidade_y *= -1

        # Verificar colisões com as bordas da janela
        if self.rect.left < 0 or self.rect.right > largura_janela:
            self.velocidade_x *= -1
        if self.rect.top < 0 or self.rect.bottom > altura_janela:
            self.velocidade_y *= -1

# Classe das Plataformas
class Plataforma(pygame.sprite.Sprite):
    def __init__(self, x, y, largura, altura):
        super().__init__()
        self.image = pygame.Surface((largura, altura))
        self.image.fill(CORES_MATERIAL[2])  # Verde
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# Classe dos Tiros
class Tiro(pygame.sprite.Sprite):
    def __init__(self, x, y, direcao):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill(CORES_MATERIAL[0])  # Azul
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.velocidade = 10
        self.direcao = direcao

    def update(self, inimigos_group, tiros_group):
        self.rect.x += self.velocidade * math.cos(self.direcao)
        self.rect.y += self.velocidade * math.sin(self.direcao)

        # Verificar colisões com inimigos
        colisoes_inimigos = pygame.sprite.spritecollide(self, inimigos_group, True)
        if colisoes_inimigos:
            self.kill()

        # Remover tiros que saíram da tela
        if self.rect.right < 0 or self.rect.left > largura_janela or self.rect.bottom < 0 or self.rect.top > altura_janela:
            self.kill()

# Criação dos sprites
sprites = pygame.sprite.Group()
plataforma_group = pygame.sprite.Group()
inimigos_group = pygame.sprite.Group()
tiros_group = pygame.sprite.Group()

personagem = Personagem(100, altura_janela - 100)
sprites.add(personagem)

plataforma = Plataforma(0, altura_janela - 20, largura_janela, 20)
plataforma_group.add(plataforma)

for _ in range(5):
    x = random.randint(100, largura_janela - 100)
    y = random.randint(200, altura_janela - 300)
    tamanho = (random.randint(20, 50), random.randint(20, 50))
    cor = random.choice(CORES_MATERIAL)
    inimigo = Inimigo(x, y, tamanho, cor)
    sprites.add(inimigo)
    inimigos_group.add(inimigo)

# Loop principal do jogo
jogo_ativo = True
clock = pygame.time.Clock()
while jogo_ativo:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jogo_ativo = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Botão esquerdo do mouse
            tiro = Tiro(personagem.rect.centerx, personagem.rect.centery, math.atan2(event.pos[1] - personagem.rect.centery, event.pos[0] - personagem.rect.centerx))
            sprites.add(tiro)
            tiros_group.add(tiro)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        personagem.velocidade_x = -5
    elif keys[pygame.K_d]:
        personagem.velocidade_x = 5
    else:
        personagem.velocidade_x = 0

    if keys[pygame.K_w] and not personagem.pulando:
        personagem.velocidade_y = -12
        personagem.pulando = True

    personagem.velocidade_y += 0.5
    personagem.update(plataforma_group)
    inimigos_group.update(inimigos_group)
    tiros_group.update(inimigos_group, tiros_group)

    # Verificar colisões com os inimigos
    colisoes_inimigos = pygame.sprite.spritecollide(personagem, inimigos_group, False)
    if colisoes_inimigos:
        personagem.vidas -= 1
        if personagem.vidas <= 0:
            jogo_ativo = False
        else:
            # Reposicionar o personagem
            personagem.rect.center = (100, altura_janela - 100)

    janela.fill(COR_FUNDO)
    sprites.draw(janela)
    plataforma_group.draw(janela)

    # Exibir vidas na tela
    fonte = pygame.font.Font(None, 36)
    texto_vidas = fonte.render(f"Vidas: {personagem.vidas}", True, CORES_MATERIAL[1])  # Vermelho
    janela.blit(texto_vidas, (10, 10))

    pygame.display.flip()
    clock.tick(60)

# Encerramento do Pygame
pygame.quit()
