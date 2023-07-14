import pygame
import math
import random

# Inicialização do Pygame
pygame.init()

# Configurações da janela do jogo
largura_janela = 800
altura_janela = 600
janela = pygame.display.set_mode((largura_janela, altura_janela))
pygame.display.set_caption("Jogo com Conceitos Matemáticos")

# Cores
COR_FUNDO = (30, 30, 30)
COR_TEXTO = (255, 255, 255)
COR_JOGADOR = (255, 0, 0)
COR_INIMIGO = (0, 255, 0)
COR_OBSTACULO = (0, 0, 255)
COR_PONTO = (255, 255, 0)

# Fonte
pygame.font.init()
fonte = pygame.font.SysFont('Arial', 24)

# Classe do Jogador
class Jogador(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((40, 40), pygame.SRCALPHA)
        self.image.fill((0, 0, 0, 0))
        pygame.draw.circle(self.image, COR_JOGADOR, (20, 20), 20)
        pygame.draw.circle(self.image, (255, 255, 255, 100), (20, 20), 20, 5)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.velocidade = 0.2
        self.angulo = 0

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.angulo += self.velocidade
        elif keys[pygame.K_RIGHT]:
            self.angulo -= self.velocidade

        self.rect.x = largura_janela // 2 + math.cos(self.angulo) * 200
        self.rect.y = altura_janela // 2 + math.sin(self.angulo) * 200

# Classe dos Inimigos
class Inimigo(pygame.sprite.Sprite):
    def __init__(self, x, y, equacao):
        super().__init__()
        self.image = pygame.Surface((20, 20), pygame.SRCALPHA)
        self.image.fill((0, 0, 0, 0))
        pygame.draw.circle(self.image, COR_INIMIGO, (10, 10), 10)
        pygame.draw.circle(self.image, (255, 255, 255, 100), (10, 10), 10, 5)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.equacao = equacao

    def update(self):
        self.rect.x += 2
        self.rect.y = self.equacao(self.rect.x)

# Classe dos Obstáculos
class Obstaculo(pygame.sprite.Sprite):
    def __init__(self, x, y, forma):
        super().__init__()
        self.image = pygame.Surface((50, 50), pygame.SRCALPHA)
        self.image.fill((0, 0, 0, 0))
        if forma == 'circulo':
            pygame.draw.circle(self.image, COR_OBSTACULO, (25, 25), 25)
            pygame.draw.circle(self.image, (255, 255, 255, 100), (25, 25), 25, 5)
        elif forma == 'retangulo':
            pygame.draw.rect(self.image, COR_OBSTACULO, (5, 5, 40, 40))
            pygame.draw.rect(self.image, (255, 255, 255, 100), (5, 5, 40, 40), 5)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.forma = forma

    def update(self):
        if self.forma == 'circulo':
            self.rect.x += 2
        elif self.forma == 'retangulo':
            self.rect.x -= 2

# Classe dos Pontos
class Ponto(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((10, 10), pygame.SRCALPHA)
        self.image.fill((0, 0, 0, 0))
        pygame.draw.circle(self.image, COR_PONTO, (5, 5), 5)
        pygame.draw.circle(self.image, (255, 255, 255, 100), (5, 5), 5, 2)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

# Criação dos grupos de sprites
sprites = pygame.sprite.Group()
jogador_group = pygame.sprite.Group()
inimigos_group = pygame.sprite.Group()
obstaculos_group = pygame.sprite.Group()
pontos_group = pygame.sprite.Group()

# Criação do jogador
jogador = Jogador(largura_janela // 2, altura_janela // 2)
sprites.add(jogador)
jogador_group.add(jogador)

# Funções de equações matemáticas para inimigos
def equacao_seno(x):
    return altura_janela // 2 + math.sin(x / 100) * 200

def equacao_cosseno(x):
    return altura_janela // 2 + math.cos(x / 100) * 200

# Criação dos inimigos
inimigo_seno = Inimigo(0, equacao_seno(0), equacao_seno)
inimigo_cosseno = Inimigo(0, equacao_cosseno(0), equacao_cosseno)
sprites.add(inimigo_seno, inimigo_cosseno)
inimigos_group.add(inimigo_seno, inimigo_cosseno)

# Criação dos obstáculos
obstaculo_circulo = Obstaculo(largura_janela, altura_janela // 2, 'circulo')
obstaculo_retangulo = Obstaculo(0, altura_janela // 2, 'retangulo')
sprites.add(obstaculo_circulo, obstaculo_retangulo)
obstaculos_group.add(obstaculo_circulo, obstaculo_retangulo)

# Função para gerar um ponto dentro da área de jogo
def gerar_ponto():
    x = random.randint(100, largura_janela - 100)
    y = random.randint(100, altura_janela - 100)
    return Ponto(x, y)

# Criação dos pontos
ponto = gerar_ponto()
sprites.add(ponto)
pontos_group.add(ponto)

# Loop principal do jogo
jogo_ativo = True
clock = pygame.time.Clock()
while jogo_ativo:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jogo_ativo = False

    sprites.update()

    # Verificar colisões com inimigos
    colisoes_inimigos = pygame.sprite.spritecollide(jogador, inimigos_group, False)
    if colisoes_inimigos:
        jogo_ativo = False

    # Verificar colisões com obstáculos
    colisoes_obstaculos = pygame.sprite.spritecollide(jogador, obstaculos_group, False)
    if colisoes_obstaculos:
        jogo_ativo = False

    # Verificar colisões com pontos
    colisoes_pontos = pygame.sprite.spritecollide(jogador, pontos_group, True)
    if colisoes_pontos:
        # Gerar novo ponto dentro da área de jogo
        ponto = gerar_ponto()
        sprites.add(ponto)
        pontos_group.add(ponto)

    # Renderizar a cena
    janela.fill(COR_FUNDO)
    sprites.draw(janela)

    # Exibir informações na tela
    texto_pontos = fonte.render(f"Total de Pontos: {len(pontos_group)}", True, COR_TEXTO)
    janela.blit(texto_pontos, (10, 10))

    pygame.display.flip()
    clock.tick(60)

# Encerramento do Pygame
pygame.quit()
