import matplotlib.pyplot as plt
import numpy as np

# Parametri comuni
t = np.linspace(0, 2*np.pi, 100)
omega = 1

# 1. Polarizzazione lineare
E_y = np.sin(omega * t)
E_x = np.zeros_like(t)

fig1, ax1 = plt.subplots(figsize=(8, 6))
ax1.plot(t, E_y, label='E_y (lineare)', color='blue')
ax1.plot(t, E_x, label='E_x', color='red', linestyle='--')
ax1.set_xlabel('Tempo')
ax1.set_ylabel('Campo Elettrico')
ax1.set_title('Polarizzazione Lineare')
ax1.legend()
ax1.grid(True)
plt.tight_layout()
plt.savefig('images/grafico_polarizzazione_lineare.png', dpi=150)
plt.close()

# 2. Polarizzazione circolare
E_x_destra = np.cos(omega * t)
E_y_destra = np.sin(omega * t)
E_x_sinistra = np.cos(omega * t)
E_y_sinistra = -np.sin(omega * t)

fig2, (ax2a, ax2b) = plt.subplots(1, 2, figsize=(12, 5))
ax2a.plot(E_x_destra, E_y_destra, color='green')
ax2a.set_xlabel('E_x')
ax2a.set_ylabel('E_y')
ax2a.set_title('Polarizzazione Circolare Destra')
ax2a.grid(True)
ax2a.axis('equal')

ax2b.plot(E_x_sinistra, E_y_sinistra, color='purple')
ax2b.set_xlabel('E_x')
ax2b.set_ylabel('E_y')
ax2b.set_title('Polarizzazione Circolare Sinistra')
ax2b.grid(True)
ax2b.axis('equal')

plt.tight_layout()
plt.savefig('images/grafico_polarizzazione_circolare.png', dpi=150)
plt.close()

# 3. Polarizzazione ellittica
E_x_ell = np.cos(omega * t)
E_y_ell = 0.5 * np.sin(omega * t)

fig3, ax3 = plt.subplots(figsize=(8, 6))
ax3.plot(E_x_ell, E_y_ell, color='orange')
ax3.set_xlabel('E_x')
ax3.set_ylabel('E_y')
ax3.set_title('Polarizzazione Ellittica')
ax3.grid(True)
ax3.axis('equal')
plt.tight_layout()
plt.savefig('images/grafico_polarizzazione_ellittica.png', dpi=150)
plt.close()

print("Grafici delle polarizzazioni generati!")