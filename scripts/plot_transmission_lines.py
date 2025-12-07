#!/usr/bin/env python3
"""
Generazione diagrammi linee di trasmissione.
Onde stazionarie, impedenza, carta di Smith, attenuazione cavi.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Circle, FancyArrowPatch
import numpy as np
from pathlib import Path

# Directory di output
OUTPUT_DIR = Path(__file__).parent.parent / "images" / "06_antenne"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Configurazione stile
plt.rcParams['font.size'] = 11
plt.rcParams['axes.titlesize'] = 14
plt.rcParams['figure.facecolor'] = 'white'


def plot_onde_stazionarie():
    """
    Visualizzazione onde stazionarie per diversi valori di SWR.
    """
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    x = np.linspace(0, 2, 500)  # 2 lunghezze d'onda

    swr_values = [(1.0, 'SWR = 1:1 (perfetto)'),
                  (1.5, 'SWR = 1.5:1 (buono)'),
                  (2.0, 'SWR = 2:1 (accettabile)'),
                  (3.0, 'SWR = 3:1 (alto)')]

    colors = ['green', 'blue', 'orange', 'red']

    for ax, (swr, title), color in zip(axes.flat, swr_values, colors):
        # Coefficiente di riflessione
        gamma = (swr - 1) / (swr + 1)

        # Onda incidente e riflessa
        v_inc = np.sin(2 * np.pi * x)
        v_ref = gamma * np.sin(2 * np.pi * x + np.pi)

        # Onda stazionaria (inviluppo)
        v_max = 1 + gamma
        v_min = 1 - gamma

        # Plot
        ax.fill_between(x, -v_max, v_max, alpha=0.2, color=color)
        ax.plot(x, v_max * np.ones_like(x), '--', color=color, linewidth=1.5, label='V_max')
        ax.plot(x, -v_max * np.ones_like(x), '--', color=color, linewidth=1.5)
        ax.plot(x, v_min * np.ones_like(x), ':', color=color, linewidth=1.5, label='V_min')
        ax.plot(x, -v_min * np.ones_like(x), ':', color=color, linewidth=1.5)

        # Onda risultante
        v_tot = np.sin(2 * np.pi * x) * (1 + gamma * np.cos(4 * np.pi * x))
        ax.plot(x, v_tot, color=color, linewidth=2, label='V totale')

        ax.set_title(title, fontweight='bold', color=color)
        ax.set_xlabel('Posizione (λ)')
        ax.set_ylabel('Ampiezza (V)')
        ax.set_xlim(0, 2)
        ax.set_ylim(-2.2, 2.2)
        ax.grid(True, linestyle='--', alpha=0.5)
        ax.axhline(0, color='black', linewidth=0.5)
        ax.legend(loc='upper right', fontsize=8)

        # Annotazione
        ax.text(1.7, 1.8, f'ρ = {gamma:.2f}', fontsize=10,
                bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

    plt.suptitle('Onde Stazionarie per Diversi Valori di SWR', fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'onde_stazionarie_swr.png', dpi=150, bbox_inches='tight')
    plt.close()
    print(f"✓ Salvato: {OUTPUT_DIR / 'onde_stazionarie_swr.png'}")


def plot_impedenza_linea():
    """
    Grafico impedenza vs posizione lungo una linea di trasmissione.
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    x = np.linspace(0, 1, 500)  # 1 lunghezza d'onda

    # Caso 1: Carico reattivo (Z_L = 100 + j50)
    Z0 = 50
    Z_L = 100 + 50j
    gamma = (Z_L - Z0) / (Z_L + Z0)
    gamma_mag = np.abs(gamma)
    gamma_phase = np.angle(gamma)

    # Impedenza lungo la linea
    beta_x = 2 * np.pi * x
    Z_in = Z0 * (Z_L + 1j * Z0 * np.tan(beta_x)) / (Z0 + 1j * Z_L * np.tan(beta_x))

    ax1.plot(x, np.abs(Z_in), 'b-', linewidth=2, label='|Z| (modulo)')
    ax1.plot(x, np.real(Z_in), 'g--', linewidth=1.5, label='R (parte reale)')
    ax1.plot(x, np.imag(Z_in), 'r:', linewidth=1.5, label='X (parte imm.)')
    ax1.axhline(50, color='gray', linestyle='--', alpha=0.5, label='Z₀ = 50Ω')

    ax1.set_title(f'Impedenza lungo la linea\nZ_L = {Z_L.real:.0f} + j{Z_L.imag:.0f} Ω', fontweight='bold')
    ax1.set_xlabel('Posizione dalla sorgente (λ)')
    ax1.set_ylabel('Impedenza (Ω)')
    ax1.set_xlim(0, 1)
    ax1.set_ylim(-100, 200)
    ax1.grid(True, linestyle='--', alpha=0.5)
    ax1.legend(loc='upper right')

    # Caso 2: Confronto carichi diversi
    carichi = [
        (50, 'Z_L = 50Ω (adattato)', 'green'),
        (100, 'Z_L = 100Ω', 'blue'),
        (25, 'Z_L = 25Ω', 'orange'),
        (0, 'Z_L = 0 (corto)', 'red'),
    ]

    for Z_L, label, color in carichi:
        if Z_L == 0:
            Z_in = 1j * Z0 * np.tan(beta_x)
        else:
            Z_in = Z0 * (Z_L + 1j * Z0 * np.tan(beta_x)) / (Z0 + 1j * Z_L * np.tan(beta_x))
        ax2.plot(x, np.abs(Z_in), color=color, linewidth=2, label=label)

    ax2.set_title('Modulo impedenza per carichi diversi', fontweight='bold')
    ax2.set_xlabel('Posizione dalla sorgente (λ)')
    ax2.set_ylabel('|Z| (Ω)')
    ax2.set_xlim(0, 1)
    ax2.set_ylim(0, 300)
    ax2.grid(True, linestyle='--', alpha=0.5)
    ax2.legend(loc='upper right')

    plt.suptitle('Impedenza su Linea di Trasmissione', fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'impedenza_linea.png', dpi=150, bbox_inches='tight')
    plt.close()
    print(f"✓ Salvato: {OUTPUT_DIR / 'impedenza_linea.png'}")


def plot_carta_smith():
    """
    Carta di Smith semplificata con esempi di impedenza.
    """
    fig, ax = plt.subplots(figsize=(10, 10))

    # Cerchio esterno (|Γ| = 1)
    theta = np.linspace(0, 2 * np.pi, 100)
    ax.plot(np.cos(theta), np.sin(theta), 'k-', linewidth=2)

    # Cerchi di resistenza costante (r = R/Z0)
    r_values = [0, 0.5, 1, 2, 5]
    for r in r_values:
        center = r / (1 + r)
        radius = 1 / (1 + r)
        circle = plt.Circle((center, 0), radius, fill=False, color='blue', linewidth=0.8)
        ax.add_patch(circle)
        if r > 0:
            ax.text(center + radius + 0.02, 0.02, f'r={r}', fontsize=8, color='blue')

    # Archi di reattanza costante (x = X/Z0)
    x_values = [0.5, 1, 2, 5]
    for x in x_values:
        # Arco superiore (induttivo, +jX)
        center_x = 1
        center_y = 1 / x
        radius = 1 / x
        angles = np.linspace(-np.pi / 2, np.arctan2(-center_y, 1 - center_x), 50)
        arc_x = center_x + radius * np.cos(angles)
        arc_y = center_y + radius * np.sin(angles)
        mask = arc_x ** 2 + arc_y ** 2 <= 1.01
        ax.plot(arc_x[mask], arc_y[mask], 'r-', linewidth=0.8)

        # Arco inferiore (capacitivo, -jX)
        arc_y_neg = -arc_y
        ax.plot(arc_x[mask], arc_y_neg[mask], 'r-', linewidth=0.8)

    # Asse reale
    ax.axhline(0, color='black', linewidth=0.5)
    ax.plot([-1, 1], [0, 0], 'k-', linewidth=1)

    # Punti esempio
    esempi = [
        (0, 0, 'Z = Z₀\n(adattato)', 'green'),
        (-1, 0, 'Corto\nZ = 0', 'red'),
        (1, 0, 'Aperto\nZ = ∞', 'orange'),
        (0.5, 0.5, 'Z = 100+j100Ω', 'purple'),
        (0.33, -0.33, 'Z = 50-j50Ω', 'brown'),
    ]

    for x, y, label, color in esempi:
        ax.plot(x, y, 'o', color=color, markersize=10)
        ax.annotate(label, xy=(x, y), xytext=(x + 0.1, y + 0.15),
                    fontsize=9, color=color,
                    arrowprops=dict(arrowstyle='->', color=color, lw=0.5))

    # Etichette
    ax.text(0, -1.15, 'Carta di Smith Semplificata', ha='center', fontsize=14, fontweight='bold')
    ax.text(-1.1, 0, 'Corto', ha='right', fontsize=9)
    ax.text(1.1, 0, 'Aperto', ha='left', fontsize=9)
    ax.text(0, 1.1, '+jX (Induttivo)', ha='center', fontsize=9, color='red')
    ax.text(0, -1.05, '-jX (Capacitivo)', ha='center', fontsize=9, color='red')

    # Legenda
    ax.plot([], [], 'b-', linewidth=1, label='Cerchi R costante')
    ax.plot([], [], 'r-', linewidth=1, label='Archi X costante')
    ax.legend(loc='upper left', fontsize=9)

    ax.set_xlim(-1.3, 1.5)
    ax.set_ylim(-1.3, 1.3)
    ax.set_aspect('equal')
    ax.axis('off')

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'carta_smith.png', dpi=150, bbox_inches='tight')
    plt.close()
    print(f"✓ Salvato: {OUTPUT_DIR / 'carta_smith.png'}")


def plot_attenuazione_cavi():
    """
    Confronto attenuazione per diversi tipi di cavo coassiale.
    """
    fig, ax = plt.subplots(figsize=(12, 7))

    # Frequenze (MHz)
    freq = np.array([1, 3.5, 7, 14, 21, 28, 50, 144, 432, 1296])

    # Attenuazione tipica (dB/100m) per vari cavi
    cavi = {
        'RG-58': {'att': [0.3, 0.5, 0.8, 1.1, 1.4, 1.6, 2.2, 4.0, 7.5, 15], 'color': 'red', 'style': '-'},
        'RG-213': {'att': [0.15, 0.25, 0.35, 0.5, 0.6, 0.7, 1.0, 1.8, 3.2, 6], 'color': 'blue', 'style': '-'},
        'LMR-400': {'att': [0.08, 0.13, 0.19, 0.27, 0.33, 0.38, 0.5, 0.9, 1.6, 3], 'color': 'green', 'style': '-'},
        'Ecoflex 15': {'att': [0.05, 0.09, 0.12, 0.17, 0.21, 0.24, 0.32, 0.55, 1.0, 1.9], 'color': 'purple', 'style': '-'},
        'Aircom Plus': {'att': [0.04, 0.07, 0.1, 0.14, 0.17, 0.2, 0.27, 0.46, 0.82, 1.5], 'color': 'orange', 'style': '-'},
    }

    for nome, dati in cavi.items():
        ax.semilogy(freq, dati['att'], dati['style'], color=dati['color'],
                    linewidth=2, marker='o', markersize=5, label=nome)

    # Bande radioamatoriali
    bande = [(3.5, '80m'), (7, '40m'), (14, '20m'), (28, '10m'), (50, '6m'), (144, '2m'), (432, '70cm')]
    for f, nome in bande:
        ax.axvline(f, color='gray', linestyle=':', alpha=0.5)
        ax.text(f, 0.03, nome, ha='center', fontsize=8, color='gray', rotation=90)

    ax.set_xlabel('Frequenza (MHz)', fontsize=12, fontweight='bold')
    ax.set_ylabel('Attenuazione (dB/100m)', fontsize=12, fontweight='bold')
    ax.set_title('Confronto Attenuazione Cavi Coassiali', fontsize=14, fontweight='bold')
    ax.set_xlim(1, 1500)
    ax.set_ylim(0.03, 20)
    ax.set_xscale('log')
    ax.grid(True, which='both', linestyle='--', alpha=0.5)
    ax.legend(loc='upper left', fontsize=10)

    # Nota
    ax.text(500, 0.05, 'Nota: valori tipici a 20°C', fontsize=9, style='italic')

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'attenuazione_cavi.png', dpi=150, bbox_inches='tight')
    plt.close()
    print(f"✓ Salvato: {OUTPUT_DIR / 'attenuazione_cavi.png'}")


def plot_velocita_propagazione():
    """
    Confronto velocità di propagazione per diversi dielettrici.
    """
    fig, ax = plt.subplots(figsize=(10, 6))

    dielettrici = ['Aria\n(vuoto)', 'PTFE\n(Teflon)', 'Polietilene\nespanso', 'Polietilene\nsolido', 'PVC']
    epsilon_r = [1.0, 2.1, 1.5, 2.3, 3.5]
    velocita = [100 / np.sqrt(e) for e in epsilon_r]  # % velocità luce

    colors = ['gold', 'cyan', 'lightgreen', 'lightblue', 'lightcoral']

    bars = ax.bar(dielettrici, velocita, color=colors, edgecolor='black', linewidth=1.5)

    # Etichette sui bar
    for bar, v, e in zip(bars, velocita, epsilon_r):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height + 1,
                f'{v:.0f}%\nεr={e}', ha='center', fontsize=10, fontweight='bold')

    ax.set_ylabel('Velocità di propagazione (% c)', fontsize=12, fontweight='bold')
    ax.set_title('Velocità di Propagazione nei Cavi Coassiali', fontsize=14, fontweight='bold')
    ax.set_ylim(0, 110)
    ax.axhline(100, color='red', linestyle='--', linewidth=1, label='Velocità luce (c)')
    ax.legend(loc='upper right')
    ax.grid(axis='y', linestyle='--', alpha=0.5)

    # Formula
    ax.text(0.02, 0.98, r'$v = \frac{c}{\sqrt{\varepsilon_r}}$', transform=ax.transAxes,
            fontsize=14, va='top', bbox=dict(boxstyle='round', facecolor='lightyellow'))

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'velocita_propagazione.png', dpi=150, bbox_inches='tight')
    plt.close()
    print(f"✓ Salvato: {OUTPUT_DIR / 'velocita_propagazione.png'}")


def main():
    """Genera tutti i diagrammi linee di trasmissione."""
    print("Generazione diagrammi linee di trasmissione...")
    print(f"Directory output: {OUTPUT_DIR}\n")

    plot_onde_stazionarie()
    plot_impedenza_linea()
    plot_carta_smith()
    plot_attenuazione_cavi()
    plot_velocita_propagazione()

    print("\n✅ Tutti i diagrammi sono stati generati con successo!")


if __name__ == "__main__":
    main()
