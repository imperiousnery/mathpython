import random
import os
from midiutil import MIDIFile

def generate_moonlight_sonata():
    # Criação do objeto MIDIFile
    midi_file = MIDIFile(1)

    # Configuração das informações básicas do arquivo MIDI
    track = 0
    time = 0
    tempo = 360  # BPM
    midi_file.addTrackName(track, time, "Moonlight Sonata")
    midi_file.addTempo(track, time, tempo)

    # Notas da escala
    scale = [
        "C4", "D4", "E4", "F4", "G4", "A4", "B4",
        "C5", "D5", "E5", "F5", "G5", "A5", "B5",
        "C6", "D6", "E6", "F6", "G6", "A6", "B6"
    ]

    # Geração das notas da música
    for _ in range(500):
        # Selecionar uma nota aleatória da escala
        note = random.choice(scale)
        duration = random.uniform(0.2, 1.0)  # Duração aleatória para cada nota

        midi_note = get_midi_note_number(note)
        if midi_note is not None:
            midi_file.addNote(track, 0, midi_note, time, duration, 50)
            time += duration

    return midi_file


def get_midi_note_number(note):
    # Mapeamento das notas para números MIDI
    note_map = {
        "C0": 12,
        "C#0": 13,
        # Restante do mapeamento...
        "B6": 95,
        "C7": 96,
        "C#7": 97,
        # Restante do mapeamento...
        "B7": 107,
        "C8": 108
    }
    return note_map.get(note)


# Geração da música "Moonlight Sonata"
midi_file = generate_moonlight_sonata()

# Pasta de saída para o arquivo MIDI
output_folder = "output"

# Criação do diretório de saída
os.makedirs(output_folder, exist_ok=True)

# Obtenção da data e hora atual

# Criação do nome do arquivo com a data e hora
file_name = f"_moonlight_sonata.mid"

# Caminho completo para o arquivo de saída
output_file = os.path.join(output_folder, file_name)

# Salvamento do arquivo MIDI
with open(output_file, 'wb') as file:
    midi_file.writeFile(file)

# Imprimindo as informações
print("Arquivo de Saída: {}".format(output_file))
