import matplotlib.pyplot as plt
import numpy as np
from utils import get_image_path

# Dati per il grafico: Reattanza capacitiva e induttiva vs frequenza
C = 100e-6  # Condensatore di 100μF
L = 10e-3   # Induttore di 10mH

# Frequenza da 1Hz a 100kHz (scala logaritmica)
f = np.logspace(0, 5, 1000)  # Da 10^0 a 10^5 Hz

# Reattanza capacitiva: X_C = 1/(2πfC)
X_C = 1 / (2 * np.pi * f * C)

# Reattanza induttiva: X_L = 2πfL
X_L = 2 * np.pi * f * L

# Crea il grafico
plt.figure(figsize=(10, 6))
plt.semilogx(f, X_C, label=f'X_C (C = {C*1e6:.0f}μF)', color='blue', linewidth=2)
plt.semilogx(f, X_L, label=f'X_L (L = {L*1e3:.0f}mH)', color='red', linewidth=2)

# Trova la frequenza di risonanza (dove X_C = X_L)
f_resonance = 1 / (2 * np.pi * np.sqrt(L * C))
plt.axvline(x=f_resonance, color='green', linestyle='--', alpha=0.7, 
            label=f'Risonanza = {f_resonance:.1f}Hz')

plt.xlabel('Frequenza (Hz)')
plt.ylabel('Reattanza (Ω)')
plt.title('Reattanza Capacitiva e Induttiva vs Frequenza')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.ylim(0, 1000)  # Limita l'asse Y per migliore visualizzazione
plt.tight_layout()

# Salva l'immagine
output = get_image_path('01_elettronica', 'grafico_reattanza_frequenza.png')
plt.savefig(output, dpi=150)
print(f"Grafico salvato in {output}")