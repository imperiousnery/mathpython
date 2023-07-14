import numpy as np
from pydub import AudioSegment

# Configurações das notas
notas_piano = {
    "c": 262, "d": 294, "e": 330, "f": 349, "g": 392, "a": 440, "b": 494
}

# Gera e salva os arquivos de som
for nota, frequencia in notas_piano.items():
    duracao = 1000  # Duração da nota em milissegundos
    amostras_por_segundo = 44100  # Taxa de amostragem em Hz
    tempo = np.linspace(0, duracao / 1000, int(duracao * amostras_por_segundo / 1000), False)
    onda_senoidal = np.sin(2 * np.pi * frequencia * tempo)
    onda_senoidal_int = (onda_senoidal * 32767).astype(np.int16)
    som = AudioSegment(onda_senoidal_int.tobytes(), frame_rate=amostras_por_segundo, channels=1, sample_width=2)
    som.export(f"piano_{nota}.wav", format="wav")  # Salva o arquivo

print("Arquivos gerados com sucesso!")
