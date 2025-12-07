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


def setup_misura_potenza_tx():
    """Setup per misura potenza in uscita trasmettitore."""
    fig, ax = plt.subplots(figsize=(14, 7))

    # Trasmettitore
    draw_block(ax, 1.5, 4, 2, 1.5, 'Trasmettitore\nTX', 'lightyellow')

    # Cavo coassiale 1
    ax.plot([2.6, 4], [4, 4], 'b-', linewidth=4)
    ax.text(3.3, 4.5, '50Ω', ha='center', fontsize=9)

    # Wattmetro passante
    ax.add_patch(Rectangle((4, 3), 2.5, 2, fill=True, facecolor='lightblue',
                            edgecolor='black', linewidth=2))
    ax.text(5.25, 4, 'Wattmetro\nPassante', ha='center', va='center', fontsize=10, fontweight='bold')
    ax.text(5.25, 3.3, 'Bird 43', ha='center', fontsize=8, style='italic')

    # Cavo coassiale 2
    ax.plot([6.5, 8], [4, 4], 'b-', linewidth=4)
    ax.text(7.25, 4.5, '50Ω', ha='center', fontsize=9)

    # Carico fittizio
    draw_block(ax, 9, 4, 2, 1.5, 'Carico\nFittizio\n50Ω', 'lightsalmon')

    # Display wattmetro
    draw_block(ax, 5.25, 6.5, 2, 1, 'Display\n100W', 'lightgray')
    draw_arrow(ax, 5.25, 5.1, 5.25, 5.9)

    # Dissipazione calore
    ax.annotate('', xy=(10.5, 5), xytext=(10.5, 3),
                arrowprops=dict(arrowstyle='->', color='red', lw=2))
    ax.text(11, 4, 'Calore', fontsize=9, color='red')

    # Note setup
    note_box = dict(boxstyle='round', facecolor='lightyellow', alpha=0.9)
    ax.text(1, 1.5, 'Setup Misura Potenza TX:\n'
                    '1. Collegare TX → Wattmetro → Carico 50Ω\n'
                    '2. Selezionare scala appropriata\n'
                    '3. Trasmettere in CW o FM\n'
                    '4. Leggere potenza diretta (FWD)\n'
                    '5. Verificare assenza riflessa (REV)',
            fontsize=9, ha='left', va='top', bbox=note_box)

    # Freccia flusso RF
    ax.annotate('', xy=(9, 3), xytext=(2, 3),
                arrowprops=dict(arrowstyle='->', color='green', lw=2, ls='--'))
    ax.text(5.5, 2.5, 'Flusso RF', fontsize=9, color='green', ha='center')

    ax.set_title('Setup Misura Potenza in Uscita TX', fontsize=14, fontweight='bold', pad=15)
    ax.set_xlim(0, 12)
    ax.set_ylim(0.5, 8)
    ax.set_aspect('equal')
    ax.axis('off')

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'setup_misura_potenza.png', dpi=150, bbox_inches='tight')
    plt.close()
    print(f"✓ Salvato: {OUTPUT_DIR / 'setup_misura_potenza.png'}")


def setup_misura_ros():
    """Setup per misura ROS/SWR antenna."""
    fig, ax = plt.subplots(figsize=(14, 8))

    # Trasmettitore
    draw_block(ax, 1.5, 5, 2, 1.5, 'Trasmettitore\nTX\n(bassa pot.)', 'lightyellow')

    # Cavo coassiale 1
    ax.plot([2.6, 4], [5, 5], 'b-', linewidth=4)

    # ROSmetro
    ax.add_patch(Rectangle((4, 3.8), 2.5, 2.4, fill=True, facecolor='lightblue',
                            edgecolor='black', linewidth=2))
    ax.text(5.25, 5, 'ROSmetro', ha='center', va='center', fontsize=11, fontweight='bold')

    # Indicatore FWD/REV
    ax.add_patch(mpatches.Wedge((5.25, 4.3), 0.6, 30, 150, facecolor='white', edgecolor='black', linewidth=1.5))
    ax.text(5.25, 4.3, 'SWR', ha='center', fontsize=7)

    # Cavo coassiale 2 (verso antenna)
    ax.plot([6.5, 9], [5, 5], 'b-', linewidth=4)
    ax.text(7.75, 5.5, 'Cavo coassiale', ha='center', fontsize=9)

    # Antenna
    # Dipolo stilizzato
    ax.plot([10, 10], [5, 6.5], 'k-', linewidth=3)
    ax.plot([9, 11], [6.5, 6.5], 'k-', linewidth=3)
    ax.plot([8.5, 9], [6.8, 6.5], 'k-', linewidth=2)
    ax.plot([11, 11.5], [6.5, 6.8], 'k-', linewidth=2)
    ax.text(10, 7.3, 'Antenna\n(Dipolo)', ha='center', fontsize=10)

    # Frecce potenze
    ax.annotate('', xy=(5.5, 6.5), xytext=(4.5, 6.5),
                arrowprops=dict(arrowstyle='->', color='green', lw=2))
    ax.text(5, 7, 'FWD', fontsize=9, color='green', ha='center')

    ax.annotate('', xy=(4.5, 3.3), xytext=(5.5, 3.3),
                arrowprops=dict(arrowstyle='->', color='red', lw=2))
    ax.text(5, 2.9, 'REV', fontsize=9, color='red', ha='center')

    # Letture tipiche
    readings_box = dict(boxstyle='round', facecolor='lightgreen', alpha=0.9)
    ax.text(11.5, 5, 'Letture tipiche:\n'
                      'SWR 1.0 = perfetto\n'
                      'SWR 1.5 = buono\n'
                      'SWR 2.0 = accettabile\n'
                      'SWR 3.0+ = problema',
            fontsize=9, ha='left', va='center', bbox=readings_box)

    # Note procedura
    note_box = dict(boxstyle='round', facecolor='lightyellow', alpha=0.9)
    ax.text(1, 2, 'Procedura:\n'
                   '1. Collegare TX → ROSmetro → Antenna\n'
                   '2. Impostare bassa potenza (5-10W)\n'
                   '3. Calibrare FWD a fondo scala\n'
                   '4. Commutare su SWR e leggere\n'
                   '5. Se SWR alto: regolare antenna',
            fontsize=9, ha='left', va='top', bbox=note_box)

    ax.set_title('Setup Misura ROS (SWR) Antenna', fontsize=14, fontweight='bold', pad=15)
    ax.set_xlim(0, 14)
    ax.set_ylim(1, 8)
    ax.set_aspect('equal')
    ax.axis('off')

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'setup_misura_ros.png', dpi=150, bbox_inches='tight')
    plt.close()
    print(f"✓ Salvato: {OUTPUT_DIR / 'setup_misura_ros.png'}")


def setup_test_due_toni():
    """Setup test due toni per linearità amplificatore."""
    fig, ax = plt.subplots(figsize=(14, 9))

    # Generatori
    draw_block(ax, 1.5, 6, 2, 1.2, 'Generatore\nf1 = 1000 Hz', 'lightyellow')
    draw_block(ax, 1.5, 4, 2, 1.2, 'Generatore\nf2 = 1700 Hz', 'lightyellow')

    # Sommatore
    draw_block(ax, 4.5, 5, 1.5, 2, 'Σ\nMixer\nAudio', 'lightgreen')

    # Frecce ai sommatore
    draw_arrow(ax, 2.6, 6, 3.7, 5.5)
    draw_arrow(ax, 2.6, 4, 3.7, 4.5)

    # Trasmettitore SSB
    draw_block(ax, 7, 5, 2.2, 1.5, 'TX SSB\nAmplificatore\nLineare', 'lightblue')
    draw_arrow(ax, 5.3, 5, 5.8, 5)

    # Carico
    draw_block(ax, 10, 5, 1.8, 1.2, 'Carico\n50Ω', 'lightsalmon')
    draw_arrow(ax, 8.2, 5, 9, 5)

    # Accoppiatore
    ax.add_patch(Rectangle((9.3, 3.5), 1.5, 1, fill=True, facecolor='plum',
                            edgecolor='black', linewidth=1.5))
    ax.text(10.05, 4, 'Accop.', ha='center', fontsize=8)
    ax.plot([10, 10], [4.4, 5], 'k-', linewidth=2)

    # Analizzatore di spettro
    draw_block(ax, 10, 2, 2.5, 1.5, 'Analizzatore\ndi Spettro', 'lightgray')
    draw_arrow(ax, 10, 3.4, 10, 2.8)

    # Spettro ideale
    ax.add_patch(Rectangle((0.5, 0.3), 5.5, 2.2, fill=True, facecolor='white',
                            edgecolor='black', linewidth=1.5))
    ax.text(3.25, 2.3, 'Spettro Ideale (lineare)', ha='center', fontsize=9, fontweight='bold')

    # Barre spettro ideale
    bar_x = [1.5, 2.5]
    bar_h = [1.5, 1.5]
    for x, h in zip(bar_x, bar_h):
        ax.add_patch(Rectangle((x, 0.5), 0.3, h, facecolor='green', edgecolor='black'))
    ax.text(1.65, 0.3, 'f1', ha='center', fontsize=8)
    ax.text(2.65, 0.3, 'f2', ha='center', fontsize=8)

    # Spettro con IMD
    ax.add_patch(Rectangle((6.5, 0.3), 6, 2.2, fill=True, facecolor='white',
                            edgecolor='black', linewidth=1.5))
    ax.text(9.5, 2.3, 'Spettro con Distorsione (IMD)', ha='center', fontsize=9, fontweight='bold')

    # Barre spettro distorto
    imd_x = [7.2, 8, 9, 10, 10.8, 11.6]
    imd_h = [0.3, 0.6, 1.5, 1.5, 0.6, 0.3]
    imd_c = ['red', 'red', 'green', 'green', 'red', 'red']
    labels = ['2f1-f2', 'f1', 'f1', 'f2', 'f2', '2f2-f1']
    for i, (x, h, c) in enumerate(zip(imd_x, imd_h, imd_c)):
        ax.add_patch(Rectangle((x, 0.5), 0.3, h, facecolor=c, edgecolor='black'))

    ax.text(7.35, 0.3, 'IMD3', ha='center', fontsize=7, color='red')
    ax.text(9.15, 0.3, 'f1', ha='center', fontsize=7)
    ax.text(10.15, 0.3, 'f2', ha='center', fontsize=7)
    ax.text(11.75, 0.3, 'IMD3', ha='center', fontsize=7, color='red')

    # Annotazione IMD
    ax.annotate('', xy=(7.35, 1.3), xytext=(9.15, 1.8),
                arrowprops=dict(arrowstyle='->', color='red', lw=1.5))
    ax.text(8, 1.7, 'IMD3\n-30dB', ha='center', fontsize=8, color='red')

    # Formula
    formula_box = dict(boxstyle='round', facecolor='lightyellow', alpha=0.9)
    ax.text(4, 7.5, 'IMD3 = Pf1 - P(2f1-f2) [dB]\n'
                     'Tipico TX lineare: IMD3 > 25-30 dB',
            fontsize=9, ha='left', bbox=formula_box)

    ax.set_title('Setup Test Due Toni - Verifica Linearità Amplificatore', fontsize=14, fontweight='bold', pad=15)
    ax.set_xlim(0, 13)
    ax.set_ylim(-0.2, 8.5)
    ax.set_aspect('equal')
    ax.axis('off')

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'setup_test_due_toni.png', dpi=150, bbox_inches='tight')
    plt.close()
    print(f"✓ Salvato: {OUTPUT_DIR / 'setup_test_due_toni.png'}")


def setup_sonde_oscilloscopio():
    """Posizionamento sonde oscilloscopio per misure RF."""
    fig, ax = plt.subplots(figsize=(14, 9))

    # Oscilloscopio
    ax.add_patch(Rectangle((9, 2), 4, 5, fill=True, facecolor='lightgray',
                            edgecolor='black', linewidth=2))
    ax.text(11, 6.5, 'Oscilloscopio', ha='center', fontsize=11, fontweight='bold')

    # Schermo
    ax.add_patch(Rectangle((9.5, 3.5), 3, 2.5, fill=True, facecolor='black',
                            edgecolor='gray', linewidth=1.5))
    # Traccia sinusoidale
    t = np.linspace(0, 2*np.pi, 100)
    y = np.sin(3*t)
    ax.plot(9.5 + 3*t/(2*np.pi), 4.75 + 0.8*y, 'lime', linewidth=2)

    # Controlli
    ax.add_patch(Rectangle((10, 2.3), 0.5, 0.5, fill=True, facecolor='yellow', edgecolor='black'))
    ax.add_patch(Rectangle((11, 2.3), 0.5, 0.5, fill=True, facecolor='cyan', edgecolor='black'))
    ax.text(10.25, 2.1, 'CH1', ha='center', fontsize=7)
    ax.text(11.25, 2.1, 'CH2', ha='center', fontsize=7)

    # BNC inputs
    ax.add_patch(mpatches.Circle((10.25, 1.7), 0.2, facecolor='white', edgecolor='black'))
    ax.add_patch(mpatches.Circle((11.25, 1.7), 0.2, facecolor='white', edgecolor='black'))

    # Circuito sotto test
    ax.add_patch(Rectangle((1, 3), 6, 3, fill=True, facecolor='lightgreen',
                            edgecolor='black', linewidth=2))
    ax.text(4, 5.5, 'Circuito Sotto Test', ha='center', fontsize=11, fontweight='bold')

    # Componenti interni
    draw_block(ax, 2.5, 4.5, 1.2, 0.8, 'Stadio\nIngresso', 'lightyellow', fontsize=7)
    draw_block(ax, 4, 4.5, 1.2, 0.8, 'Filtro', 'lightblue', fontsize=7)
    draw_block(ax, 5.5, 4.5, 1.2, 0.8, 'Amplif.', 'lightsalmon', fontsize=7)

    ax.plot([3.2, 3.3], [4.5, 4.5], 'k-', linewidth=2)
    ax.plot([4.7, 4.8], [4.5, 4.5], 'k-', linewidth=2)

    # Sonda CH1 (ingresso)
    ax.plot([2.5, 2.5, 8, 10.25], [4, 2, 2, 1.7], 'y-', linewidth=2.5)
    ax.add_patch(mpatches.Circle((2.5, 4), 0.15, facecolor='yellow', edgecolor='black'))
    ax.text(2.5, 3.5, 'Sonda\nCH1', ha='center', fontsize=8, color='darkgoldenrod')

    # Sonda CH2 (uscita)
    ax.plot([5.5, 5.5, 8.5, 11.25], [4, 1.2, 1.2, 1.7], 'c-', linewidth=2.5)
    ax.add_patch(mpatches.Circle((5.5, 4), 0.15, facecolor='cyan', edgecolor='black'))
    ax.text(5.5, 3.5, 'Sonda\nCH2', ha='center', fontsize=8, color='darkcyan')

    # Massa comune
    ax.plot([1.5, 1.5], [3, 1], 'k-', linewidth=2)
    ax.plot([1.2, 1.8], [1, 1], 'k-', linewidth=2)
    ax.plot([1.3, 1.7], [0.8, 0.8], 'k-', linewidth=1.5)
    ax.plot([1.4, 1.6], [0.6, 0.6], 'k-', linewidth=1)
    ax.text(1.5, 0.3, 'GND', ha='center', fontsize=8)

    # Clip massa sonde
    ax.plot([2.2, 1.5], [3.8, 2], 'y--', linewidth=1.5)
    ax.plot([5.2, 1.5], [3.8, 2], 'c--', linewidth=1.5)
    ax.add_patch(mpatches.Circle((2.2, 3.8), 0.1, facecolor='yellow', edgecolor='black'))
    ax.add_patch(mpatches.Circle((5.2, 3.8), 0.1, facecolor='cyan', edgecolor='black'))

    # Note
    note_box = dict(boxstyle='round', facecolor='lightyellow', alpha=0.9)
    ax.text(1, 7.5, 'Regole posizionamento sonde:\n'
                     '• Masse corte (< loop induttivi)\n'
                     '• Sonda 10:1 per alta frequenza\n'
                     '• Compensare la sonda (onda quadra)\n'
                     '• Non superare Vmax sonda\n'
                     '• Collegare massa vicino al punto di misura',
            fontsize=9, ha='left', va='top', bbox=note_box)

    # Specifiche sonde
    probe_box = dict(boxstyle='round', facecolor='lightblue', alpha=0.9)
    ax.text(9, 8, 'Sonde tipiche:\n'
                   '• 1:1 - DC-10MHz, 300V\n'
                   '• 10:1 - DC-200MHz, 600V\n'
                   '• 100:1 - alte tensioni',
            fontsize=8, ha='left', va='top', bbox=probe_box)

    ax.set_title('Posizionamento Sonde Oscilloscopio', fontsize=14, fontweight='bold', pad=15)
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 9)
    ax.set_aspect('equal')
    ax.axis('off')

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'setup_sonde_oscilloscopio.png', dpi=150, bbox_inches='tight')
    plt.close()
    print(f"✓ Salvato: {OUTPUT_DIR / 'setup_sonde_oscilloscopio.png'}")


def main():
    """Genera tutti gli schemi strumenti di misura."""
    print("Generazione schemi strumenti di misura...")
    print(f"Directory output: {OUTPUT_DIR}\n")

    schema_multimetro()
    schema_oscilloscopio()
    schema_analizzatore_spettro()
    schema_rosmetro()
    schema_wattmetro()

    # Configurazioni di misura
    setup_misura_potenza_tx()
    setup_misura_ros()
    setup_test_due_toni()
    setup_sonde_oscilloscopio()

    print("\n✅ Tutti gli schemi sono stati generati con successo!")


if __name__ == "__main__":
    main()
