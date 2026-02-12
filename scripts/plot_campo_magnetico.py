import matplotlib.pyplot as plt
import numpy as np
from utils import get_image_path

# Dati per il grafico: Campo magnetico B = μ0 * I / (2 * π * r)
mu0 = 4 * np.pi * 1e-7  # Permeabilità del vuoto
I = 10  # Corrente in A
r = np.linspace(0.001, 0.1, 100)  # Distanza da 0.001 m a 0.1 m
B = (mu0 * I) / (2 * np.pi * r)  # Induzione magnetica in T

# Crea il grafico
plt.figure(figsize=(8, 6))
plt.plot(r, B, label='B = μ₀ I / (2π r)', color='blue', linewidth=2)
plt.xlabel('Distanza r (m)')
plt.ylabel('Induzione Magnetica B (T)')
plt.title('Campo Magnetico attorno a un Conduttore')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.tight_layout()

# Salva l'immagine
output = get_image_path('01_elettronica', 'grafico_campo_magnetico.png')
plt.savefig(output, dpi=150)
print(f"Grafico salvato in {output}")