import matplotlib.pyplot as plt
import numpy as np

# Parametri
t = np.linspace(0, 4*np.pi, 1000)  # Due periodi
omega = 1  # pulsazione
V_m = 1  # ampiezza

# Segnale sinusoidale
v_t = V_m * np.sin(omega * t)

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(t, v_t, color='blue', linewidth=2)
ax.set_xlabel('Tempo (t)')
ax.set_ylabel('v(t)')
ax.set_title('Segnale Sinusoidale: v(t) = sin(ωt)')
ax.grid(True)
ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)

# Aggiungi etichette per periodo
ax.annotate('T = 2π', xy=(2*np.pi, 0), xytext=(2*np.pi + 0.5, 0.5),
            arrowprops=dict(arrowstyle='->', color='red'))
ax.annotate('f = 1/T', xy=(np.pi, 0.8), xytext=(np.pi + 0.5, 0.9),
            fontsize=10, color='green')

plt.tight_layout()
plt.savefig('images/grafico_segnale_sinusoidale.png', dpi=150)
plt.close()