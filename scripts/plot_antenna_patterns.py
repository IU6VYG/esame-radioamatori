#!/usr/bin/env python3
"""
Generazione diagrammi di radiazione per antenne radioamatoriali.
Genera pattern polari per dipolo, Yagi, loop e verticale.
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# Directory di output
OUTPUT_DIR = Path(__file__).parent.parent / "images" / "06_antenne"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Configurazione stile
plt.rcParams['font.size'] = 12
plt.rcParams['axes.titlesize'] = 14
plt.rcParams['figure.facecolor'] = 'white'


def pattern_dipolo():
    """
    Pattern di radiazione dipolo a mezz'onda.
    Forma a "8" con massimo perpendicolare all'antenna.
    """
    theta = np.linspace(0, 2 * np.pi, 360)

    # Pattern dipolo: |cos(π/2 * cos(θ)) / sin(θ)|
    # Semplificato come |sin(θ)|² per visualizzazione
    r = np.abs(np.sin(theta)) ** 2

    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'}, figsize=(8, 8))
    ax.plot(theta, r, 'b-', linewidth=2.5, label='Piano E')
    ax.fill(theta, r, alpha=0.3, color='blue')

    # Configurazione
    ax.set_theta_zero_location('N')
    ax.set_theta_direction(-1)
    ax.set_title('Diagramma di Radiazione\nDipolo a Mezz\'onda (λ/2)', pad=20, fontweight='bold')
    ax.set_rticks([0.25, 0.5, 0.75, 1.0])
    ax.set_rlabel_position(45)
    ax.grid(True, linestyle='--', alpha=0.7)

    # Annotazioni
    ax.annotate('MAX', xy=(np.pi/2, 1), xytext=(np.pi/2, 1.15),
                ha='center', fontweight='bold', color='green')
    ax.annotate('MAX', xy=(3*np.pi/2, 1), xytext=(3*np.pi/2, 1.15),
                ha='center', fontweight='bold', color='green')
    ax.annotate('NULL', xy=(0, 0.1), ha='center', color='red', fontsize=10)
    ax.annotate('NULL', xy=(np.pi, 0.1), ha='center', color='red', fontsize=10)

    # Indicazione antenna
    ax.annotate('← Antenna →', xy=(0, 0.5), ha='center', fontsize=10,
                bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.8))

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'pattern_dipolo.png', dpi=150, bbox_inches='tight')
    plt.close()
    print(f"✓ Salvato: {OUTPUT_DIR / 'pattern_dipolo.png'}")


def pattern_yagi():
    """
    Pattern di radiazione antenna Yagi (3 elementi).
    Diagramma direttivo con lobo principale e F/B ratio.
    """
    theta = np.linspace(0, 2 * np.pi, 360)

    # Pattern Yagi semplificato: lobo principale + lobo posteriore attenuato
    # Usando combinazione di funzioni per simulare direttività
    main_lobe = np.maximum(0, np.cos(theta)) ** 3
    back_lobe = np.maximum(0, -np.cos(theta)) ** 2 * 0.15  # F/B ~16 dB
    side_lobes = np.abs(np.sin(2 * theta)) ** 4 * 0.1

    r = main_lobe + back_lobe + side_lobes
    r = r / np.max(r)  # Normalizza

    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'}, figsize=(8, 8))
    ax.plot(theta, r, 'r-', linewidth=2.5)
    ax.fill(theta, r, alpha=0.3, color='red')

    # Configurazione
    ax.set_theta_zero_location('N')
    ax.set_theta_direction(-1)
    ax.set_title('Diagramma di Radiazione\nAntenna Yagi 3 Elementi', pad=20, fontweight='bold')
    ax.set_rticks([0.25, 0.5, 0.75, 1.0])
    ax.set_rlabel_position(45)
    ax.grid(True, linestyle='--', alpha=0.7)

    # Annotazioni
    ax.annotate('Lobo\nPrincipale', xy=(0, 0.85), xytext=(0.3, 0.7),
                ha='left', fontweight='bold', color='darkred',
                arrowprops=dict(arrowstyle='->', color='darkred'))
    ax.annotate('F/B ≈ 16 dB', xy=(np.pi, 0.15), xytext=(np.pi - 0.5, 0.35),
                ha='right', fontsize=10, color='gray',
                arrowprops=dict(arrowstyle='->', color='gray'))

    # Freccia direzione
    ax.annotate('', xy=(0, 1.1), xytext=(0, 0.6),
                arrowprops=dict(arrowstyle='->', color='green', lw=2))
    ax.text(0.15, 1.15, 'DIR', ha='left', fontweight='bold', color='green', fontsize=11)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'pattern_yagi.png', dpi=150, bbox_inches='tight')
    plt.close()
    print(f"✓ Salvato: {OUTPUT_DIR / 'pattern_yagi.png'}")


def pattern_loop():
    """
    Pattern di radiazione antenna loop (quadro magnetico).
    Bidirezionale con nulli nel piano del loop.
    """
    theta = np.linspace(0, 2 * np.pi, 360)

    # Pattern loop: simile al dipolo ma ruotato
    # Massimo perpendicolare al piano del loop
    r = np.abs(np.cos(theta)) ** 2

    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'}, figsize=(8, 8))
    ax.plot(theta, r, 'g-', linewidth=2.5)
    ax.fill(theta, r, alpha=0.3, color='green')

    # Configurazione
    ax.set_theta_zero_location('N')
    ax.set_theta_direction(-1)
    ax.set_title('Diagramma di Radiazione\nAntenna Loop (Quadro Magnetico)', pad=20, fontweight='bold')
    ax.set_rticks([0.25, 0.5, 0.75, 1.0])
    ax.set_rlabel_position(135)
    ax.grid(True, linestyle='--', alpha=0.7)

    # Annotazioni
    ax.annotate('MAX', xy=(0, 1), xytext=(0.2, 1.1),
                ha='left', fontweight='bold', color='darkgreen')
    ax.annotate('MAX', xy=(np.pi, 1), xytext=(np.pi + 0.2, 1.1),
                ha='left', fontweight='bold', color='darkgreen')
    ax.annotate('NULL', xy=(np.pi/2, 0.05), ha='center', color='red', fontsize=10)
    ax.annotate('NULL', xy=(3*np.pi/2, 0.05), ha='center', color='red', fontsize=10)

    # Simbolo loop al centro
    circle = plt.Circle((0, 0), 0.15, transform=ax.transData._b,
                         fill=False, color='green', linewidth=3)
    ax.add_patch(circle)
    ax.text(0, 0, '◯', ha='center', va='center', fontsize=20, color='green')

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'pattern_loop.png', dpi=150, bbox_inches='tight')
    plt.close()
    print(f"✓ Salvato: {OUTPUT_DIR / 'pattern_loop.png'}")


def pattern_verticale():
    """
    Pattern di radiazione antenna verticale (ground plane).
    Omnidirezionale sul piano orizzontale.
    """
    theta = np.linspace(0, 2 * np.pi, 360)

    # Pattern verticale: omnidirezionale (cerchio) sul piano azimutale
    r = np.ones_like(theta)

    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'}, figsize=(8, 8))
    ax.plot(theta, r, 'm-', linewidth=2.5)
    ax.fill(theta, r, alpha=0.3, color='magenta')

    # Configurazione
    ax.set_theta_zero_location('N')
    ax.set_theta_direction(-1)
    ax.set_title('Diagramma di Radiazione\nAntenna Verticale λ/4 (Piano Azimutale)', pad=20, fontweight='bold')
    ax.set_rticks([0.25, 0.5, 0.75, 1.0])
    ax.set_rlabel_position(45)
    ax.grid(True, linestyle='--', alpha=0.7)

    # Annotazioni cardinali
    for angle, label in [(0, 'N'), (np.pi/2, 'E'), (np.pi, 'S'), (3*np.pi/2, 'W')]:
        ax.annotate(label, xy=(angle, 1.1), ha='center', va='center',
                    fontweight='bold', fontsize=12, color='purple')

    # Indicatore omnidirezionale
    ax.text(np.pi/4, 0.5, 'OMNIDIREZIONALE\n360°', ha='center', va='center',
            fontsize=11, fontweight='bold', color='purple',
            bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

    # Simbolo antenna al centro
    ax.plot([0, 0], [0, 0.15], 'k-', linewidth=3)
    ax.plot(0, 0.15, 'k^', markersize=10)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'pattern_verticale.png', dpi=150, bbox_inches='tight')
    plt.close()
    print(f"✓ Salvato: {OUTPUT_DIR / 'pattern_verticale.png'}")


def pattern_verticale_elevazione():
    """
    Pattern di radiazione antenna verticale - piano di elevazione.
    Mostra l'angolo di irradiazione verso l'orizzonte.
    """
    theta = np.linspace(0, np.pi, 180)  # Solo 0-180° (sopra terra)

    # Pattern elevazione verticale λ/4 su ground perfetto
    # Massimo a basso angolo (~25-30°)
    r = np.sin(theta) * np.cos(np.pi/2 * np.cos(theta))
    r = np.abs(r)
    r = r / np.max(r) if np.max(r) > 0 else r

    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'}, figsize=(8, 6))

    # Plotta solo la metà superiore
    theta_full = np.concatenate([theta, theta + np.pi])
    r_full = np.concatenate([r, np.zeros_like(r)])

    ax.plot(theta, r, 'm-', linewidth=2.5)
    ax.fill(theta, r, alpha=0.3, color='magenta')

    # Linea di terra
    ax.plot([0, np.pi], [1.05, 1.05], 'brown', linewidth=4, label='Terra')
    ax.fill_between([0, np.pi], 0, -0.1, color='brown', alpha=0.3)

    # Configurazione
    ax.set_theta_zero_location('E')
    ax.set_theta_direction(1)
    ax.set_thetamin(0)
    ax.set_thetamax(180)
    ax.set_title('Antenna Verticale λ/4\nPiano di Elevazione', pad=20, fontweight='bold')
    ax.set_rticks([0.25, 0.5, 0.75, 1.0])
    ax.grid(True, linestyle='--', alpha=0.7)

    # Annotazioni
    ax.annotate('Angolo basso\n(DX)', xy=(np.radians(25), 0.9),
                xytext=(np.radians(45), 0.6),
                arrowprops=dict(arrowstyle='->', color='green'),
                fontweight='bold', color='green')

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'pattern_verticale_elevazione.png', dpi=150, bbox_inches='tight')
    plt.close()
    print(f"✓ Salvato: {OUTPUT_DIR / 'pattern_verticale_elevazione.png'}")


def confronto_guadagni():
    """
    Bar chart di confronto guadagni tra diversi tipi di antenne.
    """
    antenne = [
        'Dipolo λ/2',
        'Dipolo\nripiegato',
        'Verticale\nλ/4',
        'Yagi\n3 elem.',
        'Yagi\n5 elem.',
        'Quad\n2 elem.',
        'Parabolica\n1m @10GHz'
    ]

    guadagni_dbi = [2.15, 2.15, 2.0, 7.5, 10.0, 8.0, 30.0]

    # Colori per categoria
    colors = ['#3498db', '#3498db', '#9b59b6', '#e74c3c', '#e74c3c', '#2ecc71', '#f39c12']

    fig, ax = plt.subplots(figsize=(12, 7))

    bars = ax.bar(antenne, guadagni_dbi, color=colors, edgecolor='black', linewidth=1.2)

    # Etichette valori
    for bar, gain in zip(bars, guadagni_dbi):
        height = bar.get_height()
        ax.annotate(f'{gain} dBi',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 5),
                    textcoords="offset points",
                    ha='center', va='bottom',
                    fontweight='bold', fontsize=11)

    # Linea di riferimento dipolo
    ax.axhline(y=2.15, color='blue', linestyle='--', linewidth=1.5, alpha=0.7)
    ax.text(6.5, 2.5, 'Riferimento dipolo (0 dBd)', fontsize=10, color='blue', ha='right')

    # Configurazione
    ax.set_ylabel('Guadagno (dBi)', fontsize=12, fontweight='bold')
    ax.set_xlabel('Tipo di Antenna', fontsize=12, fontweight='bold')
    ax.set_title('Confronto Guadagno Antenne Radioamatoriali', fontsize=14, fontweight='bold', pad=15)
    ax.set_ylim(0, 35)
    ax.grid(axis='y', linestyle='--', alpha=0.5)

    # Legenda categorie
    from matplotlib.patches import Patch
    legend_elements = [
        Patch(facecolor='#3498db', label='Dipoli'),
        Patch(facecolor='#9b59b6', label='Verticali'),
        Patch(facecolor='#e74c3c', label='Direttive (Yagi)'),
        Patch(facecolor='#2ecc71', label='Quad'),
        Patch(facecolor='#f39c12', label='Paraboliche')
    ]
    ax.legend(handles=legend_elements, loc='upper left', fontsize=10)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'confronto_guadagni.png', dpi=150, bbox_inches='tight')
    plt.close()
    print(f"✓ Salvato: {OUTPUT_DIR / 'confronto_guadagni.png'}")


def main():
    """Genera tutti i diagrammi di radiazione antenna."""
    print("Generazione diagrammi di radiazione antenne...")
    print(f"Directory output: {OUTPUT_DIR}\n")

    pattern_dipolo()
    pattern_yagi()
    pattern_loop()
    pattern_verticale()
    pattern_verticale_elevazione()
    confronto_guadagni()

    print("\n✅ Tutti i diagrammi sono stati generati con successo!")


if __name__ == "__main__":
    main()
