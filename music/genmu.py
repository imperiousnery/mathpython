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
COR_AZUL = (33, 150, 243)
COR_VERMELHO = (244, 67, 54)
COR_VERDE = (0, 150, 136)
COR_LARANJA = (255, 152, 0)
COR_ROXO = (156, 39, 176)
COR_AZUL_ESCURO = (63, 81, 181)
COR_CIANO = (0, 188, 212)
COR_VERMELHO_ESCURO = (255, 87, 34)
CORES_MATERIAL = [COR_AZUL, COR_VERMELHO, COR_VERDE, COR_LARANJA, COR_ROXO, COR_AZUL_ESCURO, COR_CIANO, COR_VERMELHO_ESCURO]

COR_FUNDO = CORES_MATERIAL[0]
COR_PLATAFORMA = CORES_MATERIAL[1]

# Classe do Personagem
class Personagem(pygame.sprite.Sprite):
    def __init__(self, x, y, forma, tamanho, cor):
        super().__init__()
        self.forma = forma
        self.tamanho = tamanho
        self.cor = cor
        self.image = self.criar_imagem()
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.velocidade_x = 0
        self.velocidade_y = 0
        self.pulando = False
        self.vidas = 3
        self.score = 0

    def criar_imagem(self):
        image = pygame.Surface(self.tamanho)
        image.fill(self.cor)

        if self.forma == 'quadrado':
            pygame.draw.rect(image, self.cor, (0, 0, self.tamanho[0], self.tamanho[1]))
        elif self.forma == 'circulo':
            pygame.draw.circle(image, self.cor, (self.tamanho[0] // 2, self.tamanho[1] // 2), self.tamanho[0] // 2)
        elif self.forma == 'triangulo':
            pontos = [(self.tamanho[0] // 2, 0), (0, self.tamanho[1]), (self.tamanho[0], self.tamanho[1])]
            pygame.draw.polygon(image, self.cor, pontos)

        return image

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
    def __init__(self, x, y, forma, tamanho, cor, velocidade):
        super().__init__()
        self.forma = forma
        self.tamanho = tamanho
        self.cor = cor
        self.velocidade = velocidade
        self.image = self.criar_imagem()
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.direcao = random.uniform(0, math.pi * 2)

    def criar_imagem(self):
        image = pygame.Surface(self.tamanho)
        image.fill(self.cor)

        if self.forma == 'quadrado':
            pygame.draw.rect(image, self.cor, (0, 0, self.tamanho[0], self.tamanho[1]))
        elif self.forma == 'circulo':
            pygame.draw.circle(image, self.cor, (self.tamanho[0] // 2, self.tamanho[1] // 2), self.tamanho[0] // 2)
        elif self.forma == 'triangulo':
            pontos = [(self.tamanho[0] // 2, 0), (0, self.tamanho[1]), (self.tamanho[0], self.tamanho[1])]
            pygame.draw.polygon(image, self.cor, pontos)

        return image

    def update(self, inimigos_group):
        self.rect.x += self.velocidade * math.cos(self.direcao)
        self.rect.y += self.velocidade * math.sin(self.direcao)

        # Verificar colisões com outros inimigos
        colisoes_inimigos = pygame.sprite.spritecollide(self, inimigos_group, False)
        for inimigo in colisoes_inimigos:
            if inimigo != self:
                if self.rect.right > inimigo.rect.left or self.rect.left < inimigo.rect.right:
                    self.velocidade *= -1
                if self.rect.bottom > inimigo.rect.top or self.rect.top < inimigo.rect.bottom:
                    self.velocidade *= -1

        # Verificar colisões com as bordas da janela
        if self.rect.left < 0 or self.rect.right > largura_janela:
            self.direcao += math.pi
        if self.rect.top < 0 or self.rect.bottom > altura_janela:
            self.direcao += math.pi

# Classe das Plataformas
class Plataforma(pygame.sprite.Sprite):
    def __init__(self, x, y, largura, altura, cor):
        super().__init__()
        self.image = pygame.Surface((largura, altura))
        self.image.fill(cor)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# Classe dos Tiros
class Tiro(pygame.sprite.Sprite):
    def __init__(self, x, y, direcao):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill(COR_AZUL)
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

formas = ['quadrado', 'circulo', 'triangulo']

personagem = Personagem(100, altura_janela - 100, random.choice(formas), (40, 80), random.choice(CORES_MATERIAL))
sprites.add(personagem)

plataforma = Plataforma(0, altura_janela - 20, largura_janela, 20, COR_PLATAFORMA)
plataforma_group.add(plataforma)

def criar_inimigos(n):
    for _ in range(n):
        forma = random.choice(formas)
        tamanho = (random.randint(20, 50), random.randint(20, 50))
        cor = random.choice(CORES_MATERIAL)
        velocidade = random.uniform(1, 3)
        inimigo = Inimigo(random.randint(100, largura_janela - 100), random.randint(200, altura_janela - 300),
                          forma, tamanho, cor, velocidade)
        sprites.add(inimigo)
        inimigos_group.add(inimigo)

# Função para reiniciar a fase
def reiniciar_fase():
    inimigos_group.empty()
    tiros_group.empty()
    personagem.rect.center = (100, altura_janela - 100)
    personagem.score = 0
    criar_inimigos(5)

# Criar inimigos iniciais
criar_inimigos(5)

# Configurações de fase
fase_atual = 1
max_inimigos_por_fase = 10

# Loop principal do jogo
jogo_ativo = True
clock = pygame.time.Clock()
while jogo_ativo:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jogo_ativo = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and len(inimigos_group) == 0:
                fase_atual += 1
                if fase_atual > max_inimigos_por_fase:
                    jogo_ativo = False
                else:
                    reiniciar_fase()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        personagem.velocidade_x = -8
    elif keys[pygame.K_d]:
        personagem.velocidade_x = 8
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
            reiniciar_fase()

    janela.fill(COR_FUNDO)
    sprites.draw(janela)
    plataforma_group.draw(janela)

    # Exibir vidas e score na tela
    fonte = pygame.font.Font(None, 36)
    texto_vidas = fonte.render(f"Vidas: {personagem.vidas}", True, COR_VERMELHO)
    texto_score = fonte.render(f"Score: {personagem.score}", True, COR_AZUL)
    janela.blit(texto_vidas, (10, 10))
    janela.blit(texto_score, (10, 50))

    pygame.display.flip()
    clock.tick(60)

# Encerramento do Pygame
pygame.quit()
