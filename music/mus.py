import random
from midiutil import MIDIFile

def generate_8bit_music(duration, output_file):
    # Criação do objeto MIDIFile
    midi_file = MIDIFile(1)

    # Configuração das informações básicas do arquivo MIDI
    track = 0
    time = 0
    tempo = 120  # BPM
    midi_file.addTrackName(track, time, "8-bit Music")
    midi_file.addTempo(track, time, tempo)

    # Geração das notas da música
    for _ in range(int(duration * 4)):  # Cada unidade de tempo é de 0.25 segundos
        # Gerar acordes aleatórios
        chords = random.choices(["C", "Dm", "Em", "F", "G", "Am"], k=4)

        # Gerar melodia aleatória
        melody = random.choices([60, 62, 64, 65, 67, 69, 71], k=4)

        # Adicionar acordes ao arquivo MIDI
        for chord in chords:
            midi_notes = []
            for note in chord:
                midi_note = get_midi_note_number(note)
                midi_notes.append(midi_note)
                midi_file.addNote(track, 0, midi_note, time, 0.25, 100)  # Duração de cada nota do acorde é de 0.25 segundos
            time += 0.25

        # Adicionar melodia ao arquivo MIDI
        for note in melody:
            midi_file.addNote(track, 0, note, time, 0.25, 100)  # Duração de cada nota da melodia é de 0.25 segundos
            time += 0.25

    # Salvamento do arquivo MIDI
    with open(output_file, 'wb') as file:
        midi_file.writeFile(file)

def get_midi_note_number(note):
    # Mapeamento das notas para números MIDI
    note_map = {
        "C": 60,
        "C#": 61,
        "Db": 61,
        "D": 62,
        "D#": 63,
        "Eb": 63,
        "E": 64,
        "F": 65,
        "F#": 66,
        "Gb": 66,
        "G": 67,
        "G#": 68,
        "Ab": 68,
        "A": 69,
        "A#": 70,
        "Bb": 70,
        "B": 71
    }
    return note_map[note]

# Definição da duração da música em minutos
duration = 1

# Nome do arquivo MIDI de saída
output_file = "8bit_music.mid"

# Geração do arquivo MIDI com a música estilo 8-bit
generate_8bit_music(duration, output_file)

# Imprimindo as informações
print("Duração: {} minutos".format(duration))
print("Arquivo de Saída: {}".format(output_file))
