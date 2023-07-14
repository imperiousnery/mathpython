import numpy as np
import matplotlib.pyplot as plt

def generate_scale(root_frequency, intervals):
    scale = [root_frequency]

    current_frequency = root_frequency
    for interval in intervals:
        current_frequency *= 2 ** (interval / 12)
        scale.append(current_frequency)

    return scale

def plot_scale(scale, scale_name, note_names):
    x = np.arange(len(scale))
    y = np.array(scale)

    plt.figure()
    plt.plot(x, y, 'bo-')
    plt.xticks(x, note_names, rotation='vertical')
    plt.xlabel('Nota Musical')
    plt.ylabel('Frequência (Hz)')
    plt.title('Escala Musical: ' + scale_name)
    plt.grid(True)

    plt.savefig(scale_name + '_scale.png')

# Frequência da nota A4 (Lá 440 Hz)
root_frequency = 440.0

# Intervalos das escalas musicais em relação à nota A4
major_intervals = [0, 2, 4, 5, 7, 9, 11]
minor_intervals = [0, 2, 3, 5, 7, 8, 10]
harmonic_minor_intervals = [0, 2, 3, 5, 7, 8, 11]
melodic_minor_intervals = [0, 2, 3, 5, 7, 9, 11]
dorian_intervals = [0, 2, 3, 5, 7, 9, 10]
phrygian_intervals = [0, 1, 3, 5, 7, 8, 10]
lydian_intervals = [0, 2, 4, 6, 7, 9, 11]
mixolydian_intervals = [0, 2, 4, 5, 7, 9, 10]
locrian_intervals = [0, 1, 3, 5, 6, 8, 10]
chromatic_intervals = list(range(12))
whole_tone_intervals = [0, 2, 4, 6, 8, 10]
pentatonic_major_intervals = [0, 2, 4, 7, 9]
pentatonic_minor_intervals = [0, 3, 5, 7, 10]
blues_intervals = [0, 3, 5, 6, 7, 10]
augmented_intervals = [0, 3, 4, 6, 8, 9]
diminished_intervals = [0, 2, 3, 5, 6, 8, 9, 11]

# Nomes das notas musicais
note_names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

# Geração das escalas musicais
major_scale = generate_scale(root_frequency, major_intervals)
minor_scale = generate_scale(root_frequency, minor_intervals)
harmonic_minor_scale = generate_scale(root_frequency, harmonic_minor_intervals)
melodic_minor_scale = generate_scale(root_frequency, melodic_minor_intervals)
dorian_scale = generate_scale(root_frequency, dorian_intervals)
phrygian_scale = generate_scale(root_frequency, phrygian_intervals)
lydian_scale = generate_scale(root_frequency, lydian_intervals)
mixolydian_scale = generate_scale(root_frequency, mixolydian_intervals)
locrian_scale = generate_scale(root_frequency, locrian_intervals)
chromatic_scale = generate_scale(root_frequency, chromatic_intervals)
whole_tone_scale = generate_scale(root_frequency, whole_tone_intervals)
pentatonic_major_scale = generate_scale(root_frequency, pentatonic_major_intervals)
pentatonic_minor_scale = generate_scale(root_frequency, pentatonic_minor_intervals)
blues_scale = generate_scale(root_frequency, blues_intervals)
augmented_scale = generate_scale(root_frequency, augmented_intervals)
diminished_scale = generate_scale(root_frequency, diminished_intervals)

# Plotagem e salvamento das imagens das escalas musicais
plot_scale(major_scale, 'Escala Maior', note_names)
plot_scale(minor_scale, 'Escala Menor', note_names)
plot_scale(harmonic_minor_scale, 'Escala Menor Harmônica', note_names)
plot_scale(melodic_minor_scale, 'Escala Menor Melódica', note_names)
plot_scale(dorian_scale, 'Escala Dórica', note_names)
plot_scale(phrygian_scale, 'Escala Frígia', note_names)
plot_scale(lydian_scale, 'Escala Lídia', note_names)
plot_scale(mixolydian_scale, 'Escala Mixolídia', note_names)
plot_scale(locrian_scale, 'Escala Lócria', note_names)
plot_scale(chromatic_scale, 'Escala Cromática', note_names)
plot_scale(whole_tone_scale, 'Escala Tom Completo', note_names)
plot_scale(pentatonic_major_scale, 'Escala Pentatônica Maior', note_names)
plot_scale(pentatonic_minor_scale, 'Escala Pentatônica Menor', note_names)
plot_scale(blues_scale, 'Escala Blues', note_names)
plot_scale(augmented_scale, 'Escala Aumentada', note_names)
plot_scale(diminished_scale, 'Escala Diminuta', note_names)

plt.show()
