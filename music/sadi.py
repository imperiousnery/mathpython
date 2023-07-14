import random
from midiutil import MIDIFile

def generate_undertale_music(duration, output_file):
    # Criação do objeto MIDIFile
    midi_file = MIDIFile(1)

    # Configuração das informações básicas do arquivo MIDI
    track = 0
    time = 0
    tempo = 120  # BPM
    midi_file.addTrackName(track, time, "Undertale Music")
    midi_file.addTempo(track, time, tempo)

    # Definição das escalas utilizadas em Undertale
    scales = {
        "Cmaj": ["C", "D", "E", "F", "G", "A", "B"],
        "Dm": ["D", "E", "F", "G", "A", "Bb", "C"],
        "Em": ["E", "F#", "G", "A", "B", "C", "D"],
        "Fmaj": ["F", "G", "A", "Bb", "C", "D", "E"],
        "Gmaj": ["G", "A", "B", "C", "D", "E", "F#"],
        "Am": ["A", "B", "C", "D", "E", "F", "G"]
    }

    # Definição dos acordes utilizados em Undertale
    chords = {
        "Cmaj": ["C", "E", "G"],
        "Dm": ["D", "F", "A"],
        "Em": ["E", "G", "B"],
        "Fmaj": ["F", "A", "C"],
        "Gmaj": ["G", "B", "D"],
        "Am": ["A", "C", "E"]
    }

    # Geração das notas da música
    while time < duration * 60:  # A duração é especificada em minutos
        # Gerar acorde aleatório
        chord_name = random.choice(list(chords.keys()))
        chord = chords[chord_name]
        scale = scales[chord_name]

        # Adicionar acorde ao arquivo MIDI
        for note in chord:
            midi_note = get_midi_note_number(note)
            if midi_note is not None:
                midi_file.addNote(track, 0, midi_note, time, 2, 100)  # Duração do acorde é de 2 segundos

        # Gerar notas de transição entre os acordes (padrão de música clássica)
        transition_notes = generate_transition_notes(chord, scale)

        # Adicionar notas de transição ao arquivo MIDI
        transition_time = time + 2
        for note in transition_notes:
            midi_note = get_midi_note_number(note)
            if midi_note is not None:
                midi_file.addNote(track, 1, midi_note, transition_time, 1, 100)  # Duração de cada nota de transição é de 1 segundo
                transition_time += 1

        time += 4  # Avançar 4 segundos para o próximo acorde

    # Salvamento do arquivo MIDI
    with open(output_file, 'wb') as file:
        midi_file.writeFile(file)

def generate_transition_notes(chord, scale):
    # Gerar notas de transição entre os acordes (padrão de música clássica)
    transition_notes = []
    for _ in range(6):
        transition_notes.append(random.choice(chord))
        transition_notes.append(random.choice(scale))
    return transition_notes

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
    return note_map.get(note)

# Definição da duração da música em minutos
duration = 1

# Nome do arquivo MIDI de saída
output_file = "undertale_music.mid"

# Geração do arquivo MIDI com a música no estilo Undertale
generate_undertale_music(duration, output_file)

# Imprimindo as informações
print("Duração: {} minutos".format(duration))
print("Arquivo de Saída: {}".format(output_file))
