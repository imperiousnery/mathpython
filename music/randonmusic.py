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

    # Definição das notas e durações da partitura da Moonlight Sonata
    notes = ["E5", "D#5", "E5", "D#5", "E5", "B4", "D5", "C5", "A4", "G4", "E4", "G4", "A4", "F4", "G4", "E5", "D#5", "E5",
             "D#5", "E5", "B4", "D5", "C5", "A4", "G4", "E4", "G4", "A4", "F4", "G4", "E5", "D#5", "E5", "D#5", "E5", "B4",
             "D5", "C5", "A4", "G4", "E4", "G4", "A4", "F4", "G4", "E5", "D#5", "E5", "D#5", "E5", "B4", "D5", "C5", "A4",
             "G4", "E4", "G4", "A4", "F4", "G4", "E5", "D#5", "E5", "D#5", "E5", "B4", "D5", "C5", "A4", "G4", "E4", "G4",
             "A4", "F4", "G4", "E5", "D#5", "E5", "D#5", "E5", "B4", "D5", "C5", "A4", "G4", "E4", "G4", "A4", "F4", "G4",
             "E5", "D#5", "E5", "D#5", "E5", "B4", "D5", "C5", "A4", "G4", "E4", "G4", "A4", "F4", "G4", "E5", "D#5", "E5",
             "D#5", "E5", "B4", "D5", "C5", "A4", "G4", "E4", "G4", "A4", "F4", "G4", "E5", "D#5", "E5", "D#5", "E5", "B4",
             "D5", "C5", "A4", "G4", "E4", "G4", "A4", "F4", "G4", "E5", "D#5", "E5", "D#5", "E5", "B4", "D5", "C5", "A4",
             "G4", "E4", "G4", "A4", "F4", "G4"]

    durations = [1.5] * len(notes)  # Definindo todas as durações como 1

    # Adicionando as notas e durações ao arquivo MIDI
    for note, duration in zip(notes, durations):
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
        "Db0": 13,
        "D0": 14,
        "D#0": 15,
        "Eb0": 15,
        "E0": 16,
        "F0": 17,
        "F#0": 18,
        "Gb0": 18,
        "G0": 19,
        "G#0": 20,
        "Ab0": 20,
        "A0": 21,
        "A#0": 22,
        "Bb0": 22,
        "B0": 23,
        "C1": 24,
        "C#1": 25,
        "Db1": 25,
        "D1": 26,
        "D#1": 27,
        "Eb1": 27,
        "E1": 28,
        "F1": 29,
        "F#1": 30,
        "Gb1": 30,
        "G1": 31,
        "G#1": 32,
        "Ab1": 32,
        "A1": 33,
        "A#1": 34,
        "Bb1": 34,
        "B1": 35,
        "C2": 36,
        "C#2": 37,
        "Db2": 37,
        "D2": 38,
        "D#2": 39,
        "Eb2": 39,
        "E2": 40,
        "F2": 41,
        "F#2": 42,
        "Gb2": 42,
        "G2": 43,
        "G#2": 44,
        "Ab2": 44,
        "A2": 45,
        "A#2": 46,
        "Bb2": 46,
        "B2": 47,
        "C3": 48,
        "C#3": 49,
        "Db3": 49,
        "D3": 50,
        "D#3": 51,
        "Eb3": 51,
        "E3": 52,
        "F3": 53,
        "F#3": 54,
        "Gb3": 54,
        "G3": 55,
        "G#3": 56,
        "Ab3": 56,
        "A3": 57,
        "A#3": 58,
        "Bb3": 58,
        "B3": 59,
        "C4": 60,
        "C#4": 61,
        "Db4": 61,
        "D4": 62,
        "D#4": 63,
        "Eb4": 63,
        "E4": 64,
        "F4": 65,
        "F#4": 66,
        "Gb4": 66,
        "G4": 67,
        "G#4": 68,
        "Ab4": 68,
        "A4": 69,
        "A#4": 70,
        "Bb4": 70,
        "B4": 71,
        "C5": 72,
        "C#5": 73,
        "Db5": 73,
        "D5": 74,
        "D#5": 75,
        "Eb5": 75,
        "E5": 76,
        "F5": 77,
        "F#5": 78,
        "Gb5": 78,
        "G5": 79,
        "G#5": 80,
        "Ab5": 80,
        "A5": 81,
        "A#5": 82,
        "Bb5": 82,
        "B5": 83,
        "C6": 84,
        "C#6": 85,
        "Db6": 85,
        "D6": 86,
        "D#6": 87,
        "Eb6": 87,
        "E6": 88,
        "F6": 89,
        "F#6": 90,
        "Gb6": 90,
        "G6": 91,
        "G#6": 92,
        "Ab6": 92,
        "A6": 93,
        "A#6": 94,
        "Bb6": 94,
        "B6": 95,
        "C7": 96,
        "C#7": 97,
        "Db7": 97,
        "D7": 98,
        "D#7": 99,
        "Eb7": 99,
        "E7": 100,
        "F7": 101,
        "F#7": 102,
        "Gb7": 102,
        "G7": 103,
        "G#7": 104,
        "Ab7": 104,
        "A7": 105,
        "A#7": 106,
        "Bb7": 106,
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
