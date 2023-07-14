import random
from midiutil import MIDIFile

def generate_guitar_scale(scale_name, root_note, intervals, duration):
    # Criação do objeto MIDIFile
    midi_file = MIDIFile(1)

    # Configuração das informações básicas do arquivo MIDI
    track = 0
    time = 0
    tempo = 120  # BPM
    midi_file.addTrackName(track, time, "Scale: " + scale_name)
    midi_file.addTempo(track, time, tempo)

    # Conversão da nota raiz para número MIDI
    root_note_midi = root_note + 12  # Ajuste de oitava (A0 = 21)

    # Geração das notas da escala
    current_note = root_note_midi
    volume = 100
    for interval in intervals:
        midi_file.addNote(track, 0, current_note, time, duration, volume)
        current_note += interval

    return midi_file

# Definição da escala de violão
scale_name = "Escala de Violão"
root_note = 40  # E2 (MIDI note number)
intervals = [2, 2, 1, 2, 2, 2, 1]  # Intervalos de uma escala maior
duration = 0.5  # Duração de cada nota (em segundos)

# Geração do arquivo MIDI com a escala de violão
midi_file = generate_guitar_scale(scale_name, root_note, intervals, duration)

# Nome do arquivo MIDI de saída
output_file = "{}_{}_{}.mid".format(scale_name.replace(" ", ""), root_note, "-".join(str(i) for i in intervals))

# Salvamento do arquivo MIDI
with open(output_file, 'wb') as file:
    midi_file.writeFile(file)

# Imprimindo as informações
print("Escala: {}".format(scale_name))
print("Nota Raiz: {}".format(root_note))
print("Intervalos: {}".format(intervals))
print("Duração das Notas: {} segundos".format(duration))
print("Arquivo de Saída: {}".format(output_file))
