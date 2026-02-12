import matplotlib.pyplot as plt
import numpy as np
from utils import get_image_path

# Dati per il grafico: Campo elettrico E = V / d, con V = 100 V
d = np.linspace(0.01, 0.05, 100)  # Distanza da 0.01 m a 0.05 m
E = 100 / d  # Intensità del campo

# Crea il grafico
plt.figure(figsize=(8, 6))
plt.plot(d, E, label='E = 100 / d (V/m)', color='blue', linewidth=2)
plt.xlabel('Distanza (m)')
plt.ylabel('Intensità di Campo Elettrico (V/m)')
plt.title('Campo Elettrico vs Distanza')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.tight_layout()

# Salva l'immagine
output = get_image_path('01_elettronica', 'grafico_campo_elettrico.png')
plt.savefig(output, dpi=150)
print(f"Grafico salvato in {output}")