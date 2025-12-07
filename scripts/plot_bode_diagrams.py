#!/usr/bin/env python3
"""
Generazione diagrammi di Bode per filtri.
Passa-basso RC, passa-alto CR, passa-banda RLC, Butterworth vs Chebyshev.
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# Directory di output
OUTPUT_DIR = Path(__file__).parent.parent / "images" / "03_circuiti"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Configurazione stile
plt.rcParams['font.size'] = 10
plt.rcParams['axes.titlesize'] = 12
plt.rcParams['figure.facecolor'] = 'white'
plt.rcParams['axes.grid'] = True
plt.rcParams['grid.alpha'] = 0.3


def plot_bode_passa_basso():
    """Diagramma di Bode filtro passa-basso RC."""
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), sharex=True)

    # Parametri filtro
    fc = 1000  # frequenza di taglio 1kHz
    f = np.logspace(1, 5, 500)  # 10Hz - 100kHz
    omega = 2 * np.pi * f
    omega_c = 2 * np.pi * fc

    # Funzione di trasferimento H(jω) = 1 / (1 + jω/ωc)
    H = 1 / (1 + 1j * omega / omega_c)

    # Modulo in dB
    mag_db = 20 * np.log10(np.abs(H))

    # Fase in gradi
    phase_deg = np.angle(H, deg=True)

    # Plot modulo
    ax1.semilogx(f, mag_db, 'b-', linewidth=2, label='Risposta reale')

    # Approssimazione asintotica
    f_low = f[f < fc]
    f_high = f[f >= fc]
    asymp_low = np.zeros_like(f_low)
    asymp_high = -20 * np.log10(f_high / fc)
    ax1.semilogx(f_low, asymp_low, 'r--', linewidth=1.5, label='Asintoto')
    ax1.semilogx(f_high, asymp_high, 'r--', linewidth=1.5)

    # Punto -3dB
    ax1.plot(fc, -3, 'go', markersize=10, label=f'fc = {fc}Hz (-3dB)')
    ax1.axhline(y=-3, color='gray', linestyle=':', alpha=0.5)
    ax1.axvline(x=fc, color='gray', linestyle=':', alpha=0.5)

    ax1.set_ylabel('Modulo |H(f)| [dB]', fontsize=11)
    ax1.set_title('Diagramma di Bode - Filtro Passa-Basso RC\nH(jω) = 1/(1 + jωRC)', fontsize=13, fontweight='bold')
    ax1.set_ylim(-60, 10)
    ax1.legend(loc='lower left')

    # Annotazioni
    ax1.annotate('-20 dB/decade', xy=(10000, -30), fontsize=10, color='red')
    ax1.annotate('Banda\npassante', xy=(100, 2), fontsize=9, ha='center',
                bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))
    ax1.annotate('Banda di\narresto', xy=(30000, -35), fontsize=9, ha='center',
                bbox=dict(boxstyle='round', facecolor='lightsalmon', alpha=0.7))

    # Plot fase
    ax2.semilogx(f, phase_deg, 'b-', linewidth=2, label='Fase')

    # Asintoti fase
    ax2.axhline(y=0, color='r', linestyle='--', linewidth=1.5, alpha=0.7)
    ax2.axhline(y=-90, color='r', linestyle='--', linewidth=1.5, alpha=0.7)

    # Punto -45° a fc
    ax2.plot(fc, -45, 'go', markersize=10, label=f'fc = {fc}Hz (-45°)')
    ax2.axvline(x=fc, color='gray', linestyle=':', alpha=0.5)

    ax2.set_xlabel('Frequenza [Hz]', fontsize=11)
    ax2.set_ylabel('Fase φ [gradi]', fontsize=11)
    ax2.set_ylim(-100, 10)
    ax2.legend(loc='lower left')

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'bode_passa_basso_rc.png', dpi=150, bbox_inches='tight')
    plt.close()
    print(f"✓ Salvato: {OUTPUT_DIR / 'bode_passa_basso_rc.png'}")


def plot_bode_passa_alto():
    """Diagramma di Bode filtro passa-alto CR."""
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), sharex=True)

    # Parametri filtro
    fc = 1000  # frequenza di taglio 1kHz
    f = np.logspace(1, 5, 500)  # 10Hz - 100kHz
    omega = 2 * np.pi * f
    omega_c = 2 * np.pi * fc

    # Funzione di trasferimento H(jω) = jω/ωc / (1 + jω/ωc)
    H = (1j * omega / omega_c) / (1 + 1j * omega / omega_c)

    # Modulo in dB
    mag_db = 20 * np.log10(np.abs(H))

    # Fase in gradi
    phase_deg = np.angle(H, deg=True)

    # Plot modulo
    ax1.semilogx(f, mag_db, 'b-', linewidth=2, label='Risposta reale')

    # Approssimazione asintotica
    f_low = f[f < fc]
    f_high = f[f >= fc]
    asymp_low = 20 * np.log10(f_low / fc)
    asymp_high = np.zeros_like(f_high)
    ax1.semilogx(f_low, asymp_low, 'r--', linewidth=1.5, label='Asintoto')
    ax1.semilogx(f_high, asymp_high, 'r--', linewidth=1.5)

    # Punto -3dB
    ax1.plot(fc, -3, 'go', markersize=10, label=f'fc = {fc}Hz (-3dB)')
    ax1.axhline(y=-3, color='gray', linestyle=':', alpha=0.5)
    ax1.axvline(x=fc, color='gray', linestyle=':', alpha=0.5)

    ax1.set_ylabel('Modulo |H(f)| [dB]', fontsize=11)
    ax1.set_title('Diagramma di Bode - Filtro Passa-Alto CR\nH(jω) = jωRC/(1 + jωRC)', fontsize=13, fontweight='bold')
    ax1.set_ylim(-60, 10)
    ax1.legend(loc='lower right')

    # Annotazioni
    ax1.annotate('+20 dB/decade', xy=(100, -30), fontsize=10, color='red')
    ax1.annotate('Banda di\narresto', xy=(50, -35), fontsize=9, ha='center',
                bbox=dict(boxstyle='round', facecolor='lightsalmon', alpha=0.7))
    ax1.annotate('Banda\npassante', xy=(30000, 2), fontsize=9, ha='center',
                bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))

    # Plot fase
    ax2.semilogx(f, phase_deg, 'b-', linewidth=2, label='Fase')

    # Asintoti fase
    ax2.axhline(y=90, color='r', linestyle='--', linewidth=1.5, alpha=0.7)
    ax2.axhline(y=0, color='r', linestyle='--', linewidth=1.5, alpha=0.7)

    # Punto +45° a fc
    ax2.plot(fc, 45, 'go', markersize=10, label=f'fc = {fc}Hz (+45°)')
    ax2.axvline(x=fc, color='gray', linestyle=':', alpha=0.5)

    ax2.set_xlabel('Frequenza [Hz]', fontsize=11)
    ax2.set_ylabel('Fase φ [gradi]', fontsize=11)
    ax2.set_ylim(-10, 100)
    ax2.legend(loc='upper right')

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'bode_passa_alto_cr.png', dpi=150, bbox_inches='tight')
    plt.close()
    print(f"✓ Salvato: {OUTPUT_DIR / 'bode_passa_alto_cr.png'}")


def plot_bode_passa_banda():
    """Diagramma di Bode filtro passa-banda RLC."""
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), sharex=True)

    # Parametri filtro
    f0 = 10000  # frequenza centrale 10kHz
    Q = 10  # fattore di qualità
    BW = f0 / Q  # larghezza di banda

    f = np.logspace(2, 5.5, 500)  # 100Hz - 300kHz
    omega = 2 * np.pi * f
    omega_0 = 2 * np.pi * f0

    # Funzione di trasferimento normalizzata per filtro passa-banda
    # H(s) = (s/ω0/Q) / (1 + s/ω0/Q + (s/ω0)²)
    s = 1j * omega
    H = (s / omega_0 / Q) / (1 + s / omega_0 / Q + (s / omega_0)**2)

    # Modulo in dB
    mag_db = 20 * np.log10(np.abs(H))

    # Fase in gradi
    phase_deg = np.angle(H, deg=True)

    # Plot modulo
    ax1.semilogx(f, mag_db, 'b-', linewidth=2, label='Risposta')

    # Punti -3dB
    f1 = f0 - BW/2
    f2 = f0 + BW/2
    ax1.plot(f0, 0, 'go', markersize=10, label=f'f₀ = {f0/1000:.1f}kHz (0dB)')
    ax1.plot([f1, f2], [-3, -3], 'ro', markersize=8, label=f'f₁, f₂ (-3dB)')

    ax1.axhline(y=-3, color='gray', linestyle=':', alpha=0.5)
    ax1.axvline(x=f0, color='gray', linestyle=':', alpha=0.5)
    ax1.axvline(x=f1, color='red', linestyle=':', alpha=0.3)
    ax1.axvline(x=f2, color='red', linestyle=':', alpha=0.3)

    # Larghezza di banda
    ax1.annotate('', xy=(f2, -10), xytext=(f1, -10),
                arrowprops=dict(arrowstyle='<->', color='purple', lw=2))
    ax1.text(f0, -12, f'BW = {BW/1000:.1f}kHz', ha='center', fontsize=10, color='purple')

    ax1.set_ylabel('Modulo |H(f)| [dB]', fontsize=11)
    ax1.set_title(f'Diagramma di Bode - Filtro Passa-Banda RLC\nf₀ = {f0/1000}kHz, Q = {Q}, BW = {BW/1000:.1f}kHz',
                 fontsize=13, fontweight='bold')
    ax1.set_ylim(-50, 10)
    ax1.legend(loc='lower right')

    # Annotazioni pendenze
    ax1.annotate('+20 dB/dec', xy=(1000, -25), fontsize=9, color='blue')
    ax1.annotate('-20 dB/dec', xy=(100000, -25), fontsize=9, color='blue')

    # Plot fase
    ax2.semilogx(f, phase_deg, 'b-', linewidth=2, label='Fase')

    # Asintoti fase
    ax2.axhline(y=90, color='r', linestyle='--', linewidth=1, alpha=0.5)
    ax2.axhline(y=0, color='r', linestyle='--', linewidth=1, alpha=0.5)
    ax2.axhline(y=-90, color='r', linestyle='--', linewidth=1, alpha=0.5)

    # Punto 0° a f0
    ax2.plot(f0, 0, 'go', markersize=10, label=f'f₀ (0°)')
    ax2.axvline(x=f0, color='gray', linestyle=':', alpha=0.5)

    ax2.set_xlabel('Frequenza [Hz]', fontsize=11)
    ax2.set_ylabel('Fase φ [gradi]', fontsize=11)
    ax2.set_ylim(-100, 100)
    ax2.legend(loc='lower left')

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'bode_passa_banda_rlc.png', dpi=150, bbox_inches='tight')
    plt.close()
    print(f"✓ Salvato: {OUTPUT_DIR / 'bode_passa_banda_rlc.png'}")


def plot_butterworth_vs_chebyshev():
    """Confronto risposta Butterworth vs Chebyshev."""
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 9))

    fc = 1000  # frequenza di taglio
    f = np.logspace(1, 5, 500)
    omega = f / fc  # frequenza normalizzata

    orders = [2, 4, 6]
    colors = ['blue', 'green', 'red']

    # === Butterworth ===
    for n, color in zip(orders, colors):
        # |H(jω)|² = 1 / (1 + ω^(2n)) per Butterworth
        mag_sq = 1 / (1 + omega**(2*n))
        mag_db = 10 * np.log10(mag_sq)
        ax1.semilogx(f, mag_db, color=color, linewidth=2, label=f'n={n}')

    ax1.axhline(y=-3, color='gray', linestyle=':', alpha=0.7)
    ax1.axvline(x=fc, color='gray', linestyle=':', alpha=0.7)
    ax1.plot(fc, -3, 'ko', markersize=8)

    ax1.set_ylabel('Modulo |H(f)| [dB]', fontsize=11)
    ax1.set_title('Filtro Butterworth (Maximally Flat)\n|H(jω)|² = 1/(1 + ω²ⁿ)', fontsize=13, fontweight='bold')
    ax1.set_ylim(-60, 5)
    ax1.legend(title='Ordine', loc='lower left')
    ax1.set_xlabel('Frequenza [Hz]', fontsize=11)

    # Annotazione caratteristiche
    ax1.annotate('Risposta piatta\nin banda passante', xy=(100, -1), fontsize=9,
                bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))
    ax1.annotate(f'fc = {fc}Hz', xy=(fc, -5), fontsize=9, ha='center')

    # === Chebyshev Tipo 1 (ripple in banda passante) ===
    ripple_db = 1  # 1dB ripple
    epsilon = np.sqrt(10**(ripple_db/10) - 1)

    for n, color in zip(orders, colors):
        # Polinomi di Chebyshev del primo tipo
        # Per ω < 1: Tn(ω) = cos(n * arccos(ω))
        # Per ω >= 1: Tn(ω) = cosh(n * arccosh(ω))
        Tn = np.zeros_like(omega)
        mask_low = omega < 1
        mask_high = omega >= 1

        Tn[mask_low] = np.cos(n * np.arccos(omega[mask_low]))
        Tn[mask_high] = np.cosh(n * np.arccosh(omega[mask_high]))

        mag_sq = 1 / (1 + epsilon**2 * Tn**2)
        mag_db = 10 * np.log10(mag_sq)
        ax2.semilogx(f, mag_db, color=color, linewidth=2, label=f'n={n}')

    ax2.axhline(y=-3, color='gray', linestyle=':', alpha=0.7)
    ax2.axhline(y=-ripple_db, color='orange', linestyle='--', alpha=0.7, label=f'Ripple {ripple_db}dB')
    ax2.axvline(x=fc, color='gray', linestyle=':', alpha=0.7)

    ax2.set_xlabel('Frequenza [Hz]', fontsize=11)
    ax2.set_ylabel('Modulo |H(f)| [dB]', fontsize=11)
    ax2.set_title(f'Filtro Chebyshev Tipo I (Ripple {ripple_db}dB)\n|H(jω)|² = 1/(1 + ε²Tₙ²(ω))', fontsize=13, fontweight='bold')
    ax2.set_ylim(-60, 5)
    ax2.legend(title='Ordine', loc='lower left')

    # Annotazione caratteristiche
    ax2.annotate('Ondulazione (ripple)\nin banda passante', xy=(100, -0.5), fontsize=9,
                bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))
    ax2.annotate('Transizione\npiù ripida', xy=(2000, -20), fontsize=9,
                bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'bode_butterworth_vs_chebyshev.png', dpi=150, bbox_inches='tight')
    plt.close()
    print(f"✓ Salvato: {OUTPUT_DIR / 'bode_butterworth_vs_chebyshev.png'}")


def main():
    """Genera tutti i diagrammi di Bode."""
    print("Generazione diagrammi di Bode per filtri...")
    print(f"Directory output: {OUTPUT_DIR}\n")

    plot_bode_passa_basso()
    plot_bode_passa_alto()
    plot_bode_passa_banda()
    plot_butterworth_vs_chebyshev()

    print("\n✅ Tutti i diagrammi sono stati generati con successo!")


if __name__ == "__main__":
    main()
