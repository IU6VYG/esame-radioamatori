import matplotlib.pyplot as plt
import numpy as np
from utils import get_image_path

# Dati per il grafico: Carica e scarica di un condensatore
R = 1000  # Resistenza di 1kΩ
C = 100e-6  # Condensatore di 100μF
V_source = 5  # Tensione di alimentazione 5V
tau = R * C  # Costante di tempo

# Tempo da 0 a 5τ (quasi completa carica/scarica)
t = np.linspace(0, 5 * tau, 1000)

# Carica del condensatore (tensione che cresce esponenzialmente)
V_charge = V_source * (1 - np.exp(-t / tau))

# Scarica del condensatore (tensione che decade esponenzialmente)
V_discharge = V_source * np.exp(-t / tau)

# Corrente di carica (decresce esponenzialmente)
I_charge = (V_source / R) * np.exp(-t / tau)

# Corrente di scarica (negativa, decade in valore assoluto)
I_discharge = -(V_source / R) * np.exp(-t / tau)

# Crea il grafico con due subplot
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

# Grafico 1: Tensione
ax1.plot(t * 1000, V_charge, label='Carica (V)', color='blue', linewidth=2)
ax1.plot(t * 1000, V_discharge, label='Scarica (V)', color='red', linewidth=2)
ax1.set_xlabel('Tempo (ms)')
ax1.set_ylabel('Tensione (V)')
ax1.set_title('Carica e Scarica di un Condensatore')
ax1.grid(True, linestyle='--', alpha=0.7)
ax1.legend()
ax1.axhline(y=V_source, color='gray', linestyle=':', alpha=0.5, label=f'V_source = {V_source}V')
ax1.axvline(x=tau * 1000, color='green', linestyle=':', alpha=0.5, label=f'τ = {tau*1000:.1f}ms')

# Grafico 2: Corrente
ax2.plot(t * 1000, I_charge * 1000, label='Carica (I)', color='blue', linewidth=2)
ax2.plot(t * 1000, I_discharge * 1000, label='Scarica (I)', color='red', linewidth=2)
ax2.set_xlabel('Tempo (ms)')
ax2.set_ylabel('Corrente (mA)')
ax2.set_title('Corrente di Carica e Scarica')
ax2.grid(True, linestyle='--', alpha=0.7)
ax2.legend()
ax2.axhline(y=0, color='gray', linestyle='-', alpha=0.3)
ax2.axvline(x=tau * 1000, color='green', linestyle=':', alpha=0.5, label=f'τ = {tau*1000:.1f}ms')

plt.tight_layout()

# Salva l'immagine
output = get_image_path('01_elettronica', 'grafico_condensatore_carica.png')
plt.savefig(output, dpi=150)
print(f"Grafico salvato in {output}")