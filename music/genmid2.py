from midiutil import MIDIFile

def generate_scale_midi(scale_name, root_note, intervals, duration, output_file):
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

    # Salvamento do arquivo MIDI
    with open(output_file, 'wb') as file:
        midi_file.writeFile(file)

# Definição da escala
scale_name = "Escala Maior"
root_note = 60  # C4 (MIDI note number)
intervals = [0, 2, 4, 5, 7, 9, 11]  # Tom, Tom, Semitom, Tom, Tom, Tom, Semitom
duration = 1  # Duração da nota (em segundos)
output_file = "scale.mid"  # Nome do arquivo MIDI de saída

# Geração do arquivo MIDI da escala escolhida
generate_scale_midi(scale_name, root_note, intervals, duration, output_file)
