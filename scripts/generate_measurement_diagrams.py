#!/usr/bin/env python3
"""
Generazione schemi a blocchi strumenti di misura.
Multimetro, oscilloscopio, analizzatore di spettro, ROSmetro, wattmetro.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle
import numpy as np
from pathlib import Path

# Directory di output
OUTPUT_DIR = Path(__file__).parent.parent / "images" / "08_misure"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Configurazione stile
plt.rcParams['font.size'] = 10
plt.rcParams['axes.titlesize'] = 14
plt.rcParams['figure.facecolor'] = 'white'


def draw_block(ax, x, y, w, h, text, color='lightblue', fontsize=9):
    """Disegna un blocco rettangolare con testo."""
    rect = FancyBboxPatch((x - w/2, y - h/2), w, h,
                          boxstyle="round,pad=0.02",
                          facecolor=color, edgecolor='black', linewidth=1.5)
    ax.add_patch(rect)
    ax.text(x, y, text, ha='center', va='center', fontsize=fontsize,
            fontweight='bold', wrap=True)


def draw_arrow(ax, x1, y1, x2, y2, color='black'):
    """Disegna una freccia tra due punti."""
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='->', color=color, lw=1.5))


def schema_multimetro():
    """Schema a blocchi multimetro digitale."""
    fig, ax = plt.subplots(figsize=(14, 8))

    # Blocchi principali
    draw_block(ax, 1, 5, 1.8, 1.2, 'Ingresso\nV/A/Ω', 'lightyellow')
    draw_block(ax, 3.5, 6, 2, 1, 'Selettore\nFunzione', 'lightgreen')
    draw_block(ax, 3.5, 4, 2, 1, 'Attenuatore\nGamma', 'lightgreen')

    draw_block(ax, 6, 5, 2, 1.2, 'Convertitore\nAC/DC', 'lightblue')
    draw_block(ax, 9, 5, 2, 1.2, 'ADC\n(Convertitore\nA/D)', 'lightsalmon')
    draw_block(ax, 12, 5, 2, 1.2, 'Microprocessore\nLogica', 'plum')
    draw_block(ax, 12, 2.5, 2.5, 1.5, 'Display LCD\n"13.85 V"', 'lightgray')

    draw_block(ax, 6, 2.5, 2, 1, 'Riferimento\nTensione', 'lightyellow')
    draw_block(ax, 9, 2.5, 2, 1, 'Clock\nOscillatore', 'lightyellow')

    # Frecce
    draw_arrow(ax, 2, 5, 2.4, 5)
    draw_arrow(ax, 4.6, 5.5, 4.9, 5.2)
    draw_arrow(ax, 4.6, 4.5, 4.9, 4.8)
    draw_arrow(ax, 7.1, 5, 7.9, 5)
    draw_arrow(ax, 10.1, 5, 10.9, 5)
    draw_arrow(ax, 12, 4.3, 12, 3.3)

    draw_arrow(ax, 7.1, 2.5, 7.9, 4.4)
    draw_arrow(ax, 10.1, 2.5, 10.9, 4.4)

    # Input simboli
    ax.plot([0.2, 0.2], [5.3, 4.7], 'r-', linewidth=3)
    ax.text(0.2, 5.6, 'V/Ω/+', ha='center', fontsize=9, color='red')
    ax.text(0.2, 4.4, 'COM', ha='center', fontsize=9)
    ax.plot([0.2, 0.2], [5.3, 5.7], 'r-', linewidth=2)
    ax.plot([0.2, 0.5], [5, 5], 'r-', linewidth=2)

    # Titolo e note
    ax.set_title('Schema a Blocchi - Multimetro Digitale', fontsize=14, fontweight='bold', pad=15)

    ax.text(7, 7, 'Flusso segnale: Ingresso → Condizionamento → Conversione → Elaborazione → Display',
            fontsize=10, ha='center', style='italic')

    ax.set_xlim(-0.5, 14)
    ax.set_ylim(1, 8)
    ax.set_aspect('equal')
    ax.axis('off')

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'schema_multimetro.png', dpi=150, bbox_inches='tight')
    plt.close()
    print(f"✓ Salvato: {OUTPUT_DIR / 'schema_multimetro.png'}")


def schema_oscilloscopio():
    """Schema a blocchi oscilloscopio digitale."""
    fig, ax = plt.subplots(figsize=(14, 10))

    # Sezione ingresso (2 canali)
    draw_block(ax, 1.5, 7, 1.5, 1, 'CH1\nInput', 'lightyellow')
    draw_block(ax, 1.5, 5, 1.5, 1, 'CH2\nInput', 'lightyellow')

    draw_block(ax, 3.5, 7, 1.8, 1, 'Attenuatore\nV/div', 'lightgreen')
    draw_block(ax, 3.5, 5, 1.8, 1, 'Attenuatore\nV/div', 'lightgreen')

    draw_block(ax, 5.8, 7, 1.8, 1, 'Amplificatore\nVerticale', 'lightblue')
    draw_block(ax, 5.8, 5, 1.8, 1, 'Amplificatore\nVerticale', 'lightblue')

    # ADC
    draw_block(ax, 8.2, 6, 1.8, 2.5, 'ADC\n8-12 bit\n1-10 GS/s', 'lightsalmon')

    # Memoria e processore
    draw_block(ax, 10.5, 6, 2, 1.5, 'Memoria\nAcquisizione', 'plum')
    draw_block(ax, 10.5, 3.5, 2, 1.5, 'DSP\nProcessore', 'plum')

    # Display
    draw_block(ax, 13, 5, 2.2, 3, 'Display\nLCD/LED\nTraccia', 'lightgray')

    # Trigger
    draw_block(ax, 5.8, 2.5, 2, 1.2, 'Circuito\nTrigger', 'lightcoral')
    draw_block(ax, 3, 2.5, 1.8, 1, 'Trigger\nEsterno', 'lightyellow')

    # Base tempi
    draw_block(ax, 8.2, 2.5, 2, 1.2, 'Base Tempi\ns/div', 'lightgreen')

    # Frecce canali
    draw_arrow(ax, 2.3, 7, 2.5, 7)
    draw_arrow(ax, 2.3, 5, 2.5, 5)
    draw_arrow(ax, 4.5, 7, 4.8, 7)
    draw_arrow(ax, 4.5, 5, 4.8, 5)
    draw_arrow(ax, 6.8, 7, 7.2, 6.5)
    draw_arrow(ax, 6.8, 5, 7.2, 5.5)
    draw_arrow(ax, 9.2, 6, 9.4, 6)
    draw_arrow(ax, 11.6, 6, 11.9, 5.5)
    draw_arrow(ax, 11.6, 4, 11.9, 4.5)
    draw_arrow(ax, 10.5, 5.2, 10.5, 4.3)

    # Frecce trigger
    draw_arrow(ax, 6.8, 5.5, 6.8, 3.2)
    draw_arrow(ax, 4, 2.5, 4.7, 2.5)
    draw_arrow(ax, 6.9, 2.5, 7.1, 2.5)
    draw_arrow(ax, 9.3, 2.5, 9.4, 3.5)

    # Controlli utente
    ax.text(3.5, 8.3, 'Controlli Utente', fontsize=10, ha='center', fontweight='bold')
    ax.add_patch(Rectangle((2.5, 8), 2, 0.5, fill=False, edgecolor='gray', linestyle='--'))

    # Titolo
    ax.set_title('Schema a Blocchi - Oscilloscopio Digitale (DSO)', fontsize=14, fontweight='bold', pad=15)

    ax.set_xlim(0, 15)
    ax.set_ylim(1, 9)
    ax.set_aspect('equal')
    ax.axis('off')

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'schema_oscilloscopio.png', dpi=150, bbox_inches='tight')
    plt.close()
    print(f"✓ Salvato: {OUTPUT_DIR / 'schema_oscilloscopio.png'}")


def schema_analizzatore_spettro():
    """Schema a blocchi analizzatore di spettro."""
    fig, ax = plt.subplots(figsize=(14, 8))

    # Ingresso RF
    draw_block(ax, 1.5, 5, 1.5, 1, 'Ingresso\nRF', 'lightyellow')
    draw_block(ax, 3.5, 5, 1.8, 1, 'Attenuatore\nRF', 'lightgreen')
    draw_block(ax, 5.8, 5, 1.8, 1, 'Filtro\nPassa-basso', 'lightblue')

    # Mixer e IF
    draw_block(ax, 8, 5, 1.5, 1.2, 'Mixer', 'lightsalmon')
    draw_block(ax, 8, 3, 1.8, 1, 'Oscillatore\nLocale (LO)', 'plum')
    draw_block(ax, 10.2, 5, 1.8, 1, 'Filtro IF\n(RBW)', 'lightblue')

    # Rivelatore e elaborazione
    draw_block(ax, 12.5, 5, 1.5, 1, 'Rivelatore\nLogaritmico', 'lightsalmon')
    draw_block(ax, 12.5, 3, 1.8, 1, 'Video\nFilter', 'lightgreen')

    # Display
    draw_block(ax, 12.5, 7, 2.5, 1.5, 'Display\nSpettro\ndBm vs MHz', 'lightgray')

    # Sweep generator
    draw_block(ax, 5, 2, 2, 1, 'Generatore\nSweep', 'plum')

    # Frecce
    draw_arrow(ax, 2.3, 5, 2.5, 5)
    draw_arrow(ax, 4.5, 5, 4.8, 5)
    draw_arrow(ax, 6.8, 5, 7.2, 5)
    draw_arrow(ax, 8.8, 5, 9.2, 5)
    draw_arrow(ax, 11.2, 5, 11.7, 5)
    draw_arrow(ax, 12.5, 5.6, 12.5, 6.2)
    draw_arrow(ax, 12.5, 4.4, 12.5, 3.6)

    # Sweep e LO
    draw_arrow(ax, 8, 3.6, 8, 4.3)
    draw_arrow(ax, 6.1, 2, 7, 3)
    draw_arrow(ax, 6.1, 2, 11.5, 7)

    # Annotazioni
    ax.text(8, 6.5, 'f_IF = f_RF - f_LO', fontsize=9, ha='center',
            bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

    ax.text(10.2, 6.3, 'RBW\nRisoluzione', fontsize=8, ha='center', color='gray')

    # Simbolo antenna ingresso
    ax.plot([0.5, 0.5], [5.3, 4.7], 'k-', linewidth=2)
    ax.plot([0.3, 0.7], [5.3, 5.3], 'k-', linewidth=2)
    ax.plot([0.5, 0.9], [5, 5], 'k-', linewidth=2)

    # Titolo
    ax.set_title('Schema a Blocchi - Analizzatore di Spettro', fontsize=14, fontweight='bold', pad=15)

    ax.set_xlim(0, 15)
    ax.set_ylim(1, 8.5)
    ax.set_aspect('equal')
    ax.axis('off')

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'schema_analizzatore_spettro.png', dpi=150, bbox_inches='tight')
    plt.close()
    print(f"✓ Salvato: {OUTPUT_DIR / 'schema_analizzatore_spettro.png'}")


def schema_rosmetro():
    """Schema ROSmetro (ponte riflettometrico direzionale)."""
    fig, ax = plt.subplots(figsize=(12, 8))

    # Linea principale
    ax.plot([1, 11], [5, 5], 'b-', linewidth=4)
    ax.text(6, 5.5, 'Linea di trasmissione 50Ω', ha='center', fontsize=10)

    # TX e Antenna
    draw_block(ax, 1, 5, 1.5, 1.2, 'TX\n50Ω', 'lightyellow')
    draw_block(ax, 11, 5, 1.5, 1.2, 'Antenna\nZ_L', 'lightgreen')

    # Accoppiatore direzionale
    ax.add_patch(Rectangle((4, 3.5), 4, 3, fill=True, facecolor='lightblue',
                            edgecolor='black', linewidth=2))
    ax.text(6, 6.2, 'Accoppiatore Direzionale', ha='center', fontsize=10, fontweight='bold')

    # Porte accoppiatore
    draw_block(ax, 4.5, 3, 1.2, 0.8, 'FWD', 'lightsalmon', fontsize=8)
    draw_block(ax, 7.5, 3, 1.2, 0.8, 'REV', 'lightcoral', fontsize=8)

    # Rivelatori
    draw_block(ax, 4.5, 1.5, 1.5, 0.8, 'Rivelatore\nDiodo', 'plum', fontsize=8)
    draw_block(ax, 7.5, 1.5, 1.5, 0.8, 'Rivelatore\nDiodo', 'plum', fontsize=8)

    # Frecce accoppiamento
    draw_arrow(ax, 4.5, 3.5, 4.5, 2.6)
    draw_arrow(ax, 7.5, 3.5, 7.5, 2.6)
    draw_arrow(ax, 4.5, 2, 4.5, 1.2)
    draw_arrow(ax, 7.5, 2, 7.5, 1.2)

    # Meter
    ax.add_patch(mpatches.Wedge((6, 0.3), 1.5, 30, 150, facecolor='white', edgecolor='black', linewidth=2))
    ax.plot([6, 6.8], [0.3, 1.2], 'r-', linewidth=2)  # Ago
    ax.text(6, -0.5, 'SWR Meter', ha='center', fontsize=10, fontweight='bold')

    # Frecce ai meter
    draw_arrow(ax, 4.5, 1.1, 5.3, 0.5)
    draw_arrow(ax, 7.5, 1.1, 6.7, 0.5)

    # Formule
    formula_box = dict(boxstyle='round', facecolor='lightyellow', alpha=0.9)
    ax.text(10, 2, 'SWR = (FWD + REV)/(FWD - REV)\n\nρ = REV/FWD\n\nSWR = (1+ρ)/(1-ρ)',
            fontsize=9, ha='left', va='top', bbox=formula_box, family='monospace')

    # Direzioni potenza
    ax.annotate('', xy=(3, 5.8), xytext=(2, 5.8),
                arrowprops=dict(arrowstyle='->', color='green', lw=2))
    ax.text(2.5, 6.2, 'P_fwd', fontsize=9, color='green', ha='center')

    ax.annotate('', xy=(9, 4.2), xytext=(10, 4.2),
                arrowprops=dict(arrowstyle='->', color='red', lw=2))
    ax.text(9.5, 3.8, 'P_rev', fontsize=9, color='red', ha='center')

    # Titolo
    ax.set_title('Schema ROSmetro - Ponte Riflettometrico Direzionale', fontsize=14, fontweight='bold', pad=15)

    ax.set_xlim(0, 13)
    ax.set_ylim(-1, 7.5)
    ax.set_aspect('equal')
    ax.axis('off')

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'schema_rosmetro.png', dpi=150, bbox_inches='tight')
    plt.close()
    print(f"✓ Salvato: {OUTPUT_DIR / 'schema_rosmetro.png'}")


def schema_wattmetro():
    """Schema wattmetro a termocoppia/bolometro."""
    fig, ax = plt.subplots(figsize=(12, 7))

    # Ingresso RF
    draw_block(ax, 1.5, 4, 1.5, 1, 'Ingresso\nRF', 'lightyellow')
    draw_block(ax, 3.5, 4, 1.8, 1, 'Attenuatore\nCalibrato', 'lightgreen')

    # Carico e sensore
    draw_block(ax, 6, 4, 2, 1.5, 'Carico\nTermico\n50Ω', 'lightsalmon')

    # Sensore termico
    draw_block(ax, 6, 2, 2, 1, 'Termocoppia\no Termistore', 'plum')

    # Amplificatore e display
    draw_block(ax, 9, 3, 2, 1, 'Amplificatore\nDC', 'lightblue')
    draw_block(ax, 11.5, 3, 2, 1.5, 'Display\nPotenza\nWatt/dBm', 'lightgray')

    # Calibrazione
    draw_block(ax, 9, 5.5, 2, 1, 'Riferimento\nCalibrazione', 'lightyellow')

    # Frecce
    draw_arrow(ax, 2.3, 4, 2.5, 4)
    draw_arrow(ax, 4.5, 4, 4.9, 4)
    draw_arrow(ax, 6, 3.2, 6, 2.6)
    draw_arrow(ax, 7.1, 2, 7.9, 2.8)
    draw_arrow(ax, 10.1, 3, 10.4, 3)
    draw_arrow(ax, 9, 5, 9, 3.6)

    # Simboli termici
    ax.plot([5.5, 6.5], [3.8, 3.8], 'r-', linewidth=3)
    ax.text(6, 3.5, '~', fontsize=20, ha='center', va='center', color='red')

    # Formula
    formula_box = dict(boxstyle='round', facecolor='lightyellow', alpha=0.9)
    ax.text(3, 1, 'P = V²/R = I²R\n\nΔT ∝ P\n\nV_termo = k × ΔT',
            fontsize=9, ha='left', va='top', bbox=formula_box, family='monospace')

    # Annotazioni
    ax.text(6, 5.5, 'Energia RF → Calore → Tensione DC', fontsize=10, ha='center', style='italic')

    # Titolo
    ax.set_title('Schema Wattmetro a Termocoppia', fontsize=14, fontweight='bold', pad=15)

    ax.set_xlim(0, 14)
    ax.set_ylim(0, 7)
    ax.set_aspect('equal')
    ax.axis('off')

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'schema_wattmetro.png', dpi=150, bbox_inches='tight')
    plt.close()
    print(f"✓ Salvato: {OUTPUT_DIR / 'schema_wattmetro.png'}")


def main():
    """Genera tutti gli schemi strumenti di misura."""
    print("Generazione schemi strumenti di misura...")
    print(f"Directory output: {OUTPUT_DIR}\n")

    schema_multimetro()
    schema_oscilloscopio()
    schema_analizzatore_spettro()
    schema_rosmetro()
    schema_wattmetro()

    print("\n✅ Tutti gli schemi sono stati generati con successo!")


if __name__ == "__main__":
    main()
