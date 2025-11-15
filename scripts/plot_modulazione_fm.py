import matplotlib.pyplot as plt
import numpy as np

# Parametri
t = np.linspace(0, 4*np.pi, 1000)
f_c = 10  # frequenza portante
f_m = 1   # frequenza modulante
beta = 2  # indice di modulazione

# Segnale modulante
modulating = np.sin(2*np.pi*f_m*t)

# FM: s(t) = cos(2*pi*f_c*t + beta*sin(2*pi*f_m*t))
fm_signal = np.cos(2*np.pi*f_c*t + beta * modulating)

# Per mostrare la variazione di frequenza, plottiamo l'istante di zero crossing o qualcosa di simile
# Alternativa: plottare la fase accumulata

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))

# Segnale modulante
ax1.plot(t, modulating, color='blue')
ax1.set_title('Segnale Modulante')
ax1.grid(True)

# Segnale FM
ax2.plot(t, fm_signal, color='green')
ax2.set_title('Segnale Modulato FM')
ax2.grid(True)

plt.tight_layout()
plt.savefig('images/grafico_modulazione_fm.png', dpi=150)
plt.close()