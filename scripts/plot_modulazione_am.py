import matplotlib.pyplot as plt
import numpy as np

# Parametri
t = np.linspace(0, 4*np.pi, 1000)
f_c = 10  # frequenza portante
f_m = 1   # frequenza modulante
A_c = 1   # ampiezza portante
m = 0.5   # indice di modulazione

# Segnale modulante
modulating = np.sin(2*np.pi*f_m*t)

# AM: s(t) = (A_c + m*modulating) * cos(2*pi*f_c*t)
am_signal = (A_c + m * modulating) * np.cos(2*np.pi*f_c*t)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))

# Segnale modulante
ax1.plot(t, modulating, color='blue')
ax1.set_title('Segnale Modulante')
ax1.grid(True)

# Segnale AM
ax2.plot(t, am_signal, color='red')
ax2.set_title('Segnale Modulato AM')
ax2.grid(True)

plt.tight_layout()
plt.savefig('images/grafico_modulazione_am.png', dpi=150)
plt.close()