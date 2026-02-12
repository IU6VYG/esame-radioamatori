import matplotlib.pyplot as plt
import numpy as np
from utils import get_image_path

# Dati per il grafico: Curva V-I di un resistore (Legge di Ohm)
R = 1000  # Resistenza di 1kΩ
V = np.linspace(0, 10, 100)  # Tensione da 0 a 10V
I = V / R  # Corrente secondo la Legge di Ohm

# Crea il grafico
plt.figure(figsize=(8, 6))
plt.plot(V, I, label=f'R = {R} Ω', color='red', linewidth=2)
plt.xlabel('Tensione (V)')
plt.ylabel('Corrente (A)')
plt.title('Curva Caratteristica V-I di un Resistore')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.tight_layout()

# Salva l'immagine
output = get_image_path('01_elettronica', 'grafico_resistore_vi.png')
plt.savefig(output, dpi=150)
print(f"Grafico salvato in {output}")