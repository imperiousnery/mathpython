import pygame
import time

# Inicializa o Pygame
pygame.init()

# Configurações da música
musica_mario = "ccggaagffeeddcc"
tempo_notas = [0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3,0.3, 0.3, 0.3]
nota_to_int = {"c": 262, "d": 294, "e": 330, "f": 349, "g": 392, "a": 440, "b": 494, "<": 0, ">": 0}

# Configurações do mixer de áudio
pygame.mixer.init()
pygame.mixer.set_num_channels(1)

# Função para tocar uma nota
def tocar_nota(nota, tempo):
    if nota == "<":
        time.sleep(tempo)
    else:
        pygame.mixer.Channel(0).set_volume(0.5, 0.5)
        pygame.mixer.Channel(0).play(pygame.mixer.Sound(f"piano_{nota}.wav"))
        time.sleep(tempo)

# Toca a música
for nota, tempo in zip(musica_mario, tempo_notas):
    tocar_nota(nota, tempo)

# Encerra o Pygame
pygame.quit()
