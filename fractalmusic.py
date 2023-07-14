from midiutil.MidiFile import MIDIFile

def generate_fractal_pattern(initial_notes, iterations):
    pattern = initial_notes

    for _ in range(iterations):
        new_pattern = []
        for note in pattern:
            new_pattern.extend([note - 1, note + 1])
        pattern = new_pattern

    return pattern

# Parâmetros do sistema
initial_notes = [60]  # Nota inicial (60 é a nota "C4")
iterations = 5  # Número de iterações fractais

# Gerar padrão fractal de notas
fractal_pattern = generate_fractal_pattern(initial_notes, iterations)

# Configurações MIDI
output_file = "fractal_music.mid"
track = 0
channel = 0
time = 0  # Tempo inicial em pulsos por tempo
duration = 1  # Duração de cada nota em pulsos por tempo
tempo = 120  # BPM (batidas por minuto)
volume = 100  # Volume da nota

# Criação do arquivo MIDI
midi_file = MIDIFile(numTracks=1)
midi_file.addTempo(track, time, tempo)

# Adicionar notas ao arquivo MIDI
for i, note in enumerate(fractal_pattern):
    midi_file.addNote(track, channel, note, time, duration, volume)

# Salvar arquivo MIDI
with open(output_file, "wb") as file:
    midi_file.writeFile(file)
