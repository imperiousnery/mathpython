import numpy as np
import matplotlib.pyplot as plt

def generate_scale(root_frequency, intervals):
    scale = [root_frequency]

    current_frequency = root_frequency
    for interval in intervals:
        current_frequency *= 2 ** (interval / 12)
        scale.append(current_frequency)

    return scale

def plot_scale(scale, scale_name):
    x = np.arange(len(scale))
    y = np.array(scale)

    plt.figure()
    plt.plot(x, y, 'bo-')
    plt.xticks(x, scale_name, rotation='vertical')
    plt.xlabel('Nota Musical')
    plt.ylabel('Frequência (Hz)')
    plt.title('Escala Musical: ' + scale_name)
    plt.grid(True)

    plt.savefig(scale_name + '_scale.png')

# Frequência da nota A4 (Lá 440 Hz)
root_frequency = 440.0

# Intervalos das escalas musicais em relação à nota A4
intervals = [0, 2, 4, 5, 7, 9, 11]

# Geração das escalas musicais
custom_scale = generate_scale(root_frequency, intervals)

# Plotagem e salvamento da imagem da escala musical personalizada
plot_scale(custom_scale, 'Minha Escala Personalizada')

plt.show()
