import numpy as np
import matplotlib.pyplot as plt

class Particle:
    def __init__(self, mass, position, velocity):
        self.mass = mass
        self.position = position
        self.velocity = velocity

class System:
    def __init__(self, particles):
        self.particles = particles

    def update(self, dt):
        num_particles = len(self.particles)

        for i in range(num_particles):
            acceleration = np.zeros(2)

            for j in range(num_particles):
                if i != j:
                    diff = self.particles[j].position - self.particles[i].position
                    dist = np.linalg.norm(diff)
                    force = (self.particles[j].mass / dist**3) * diff
                    acceleration += force

            self.particles[i].velocity += acceleration * dt
            self.particles[i].position += self.particles[i].velocity * dt

def simulate(system, num_steps, dt):
    positions = []

    for _ in range(num_steps):
        positions.append([particle.position for particle in system.particles])
        system.update(dt)

    return np.array(positions)

# Parâmetros do sistema
num_particles = 100
num_steps = 1000
dt = 0.01

# Inicialização das partículas
particles = []
for _ in range(num_particles):
    mass = np.random.uniform(0.1, 1.0)
    position = np.random.uniform(-1, 1, size=2)
    velocity = np.zeros(2)
    particles.append(Particle(mass, position, velocity))

# Criação do sistema
system = System(particles)

# Simulação do sistema de partículas
positions = simulate(system, num_steps, dt)

# Plotagem das posições das partículas ao longo do tempo
plt.figure(figsize=(8, 8))
plt.scatter(positions[:, :, 0], positions[:, :, 1], s=5)
plt.xlabel('Posição X')
plt.ylabel('Posição Y')
plt.title('Simulação do Sistema de Partículas')
plt.show()
