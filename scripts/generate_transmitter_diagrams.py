#!/usr/bin/env python3
"""
Generazione diagrammi dettagliati trasmettitori radio.
SSB con mixer bilanciato, amplificatore finale, modulatore FM, ALC.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Rectangle, FancyBboxPatch, FancyArrowPatch, Circle
import numpy as np
from pathlib import Path

# Directory di output
OUTPUT_DIR = Path(__file__).parent.parent / "images" / "05_trasmettitori"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Configurazione stile
plt.rcParams['font.size'] = 10
plt.rcParams['axes.titlesize'] = 12
plt.rcParams['figure.facecolor'] = 'white'


def plot_ssb_transmitter():
    """Schema trasmettitore SSB con mixer bilanciato dettagliato."""
    fig, ax = plt.subplots(figsize=(16, 11))
    ax.set_facecolor('#f8fafc')

    # Titolo
    ax.text(0.5, 0.96, 'Trasmettitore SSB (J3E)', fontsize=20, fontweight='bold',
            ha='center', transform=ax.transAxes, color='#1a365d')
    ax.text(0.5, 0.92, 'Schema a blocchi con mixer bilanciato', fontsize=12,
            ha='center', transform=ax.transAxes, color='#4a5568')

    # Colori
    colors = {
        'audio': '#fef08a',
        'osc': '#fecaca',
        'mixer': '#bfdbfe',
        'filter': '#ddd6fe',
        'amp': '#bbf7d0',
        'output': '#fed7aa',
        'border': '#374151',
    }

    block_w = 0.11
    block_h = 0.08

    def draw_block(x, y, label, sublabel, color):
        shadow = FancyBboxPatch((x - block_w/2 + 0.002, y - block_h/2 - 0.002),
                                block_w, block_h, boxstyle="round,pad=0.005,rounding_size=0.01",
                                facecolor='#94a3b8', edgecolor='none', zorder=1)
        ax.add_patch(shadow)
        rect = FancyBboxPatch((x - block_w/2, y - block_h/2), block_w, block_h,
                              boxstyle="round,pad=0.005,rounding_size=0.01",
                              facecolor=color, edgecolor=colors['border'], linewidth=1.5, zorder=2)
        ax.add_patch(rect)
        ax.text(x, y + 0.015, label, ha='center', va='center', fontsize=9,
                fontweight='bold', color='#1e293b', zorder=3)
        ax.text(x, y - 0.015, sublabel, ha='center', va='center', fontsize=7,
                color='#475569', zorder=3)

    y_audio = 0.75
    y_main = 0.55
    y_osc = 0.35

    x_mic = 0.08
    x_preamp = 0.20
    x_mixer = 0.35
    x_filter = 0.50
    x_amp1 = 0.65
    x_pa = 0.80
    x_ant = 0.94

    # Blocchi audio
    draw_block(x_mic, y_audio, 'MIC', 'Microfono', colors['audio'])
    draw_block(x_preamp, y_audio, 'PREAMP', 'AF +40dB', colors['audio'])

    ax.annotate('', xy=(x_preamp - block_w/2 - 0.005, y_audio), xytext=(x_mic + block_w/2 + 0.005, y_audio),
                arrowprops=dict(arrowstyle='-|>', color='#3b82f6', lw=2, mutation_scale=12))

    ax.plot([x_preamp + block_w/2 + 0.01, x_preamp + 0.08, x_preamp + 0.08],
            [y_audio, y_audio, y_main + 0.02], color='#3b82f6', lw=2)
    ax.annotate('', xy=(x_mixer - block_w/2 - 0.005, y_main + 0.02),
                xytext=(x_preamp + 0.08, y_main + 0.02),
                arrowprops=dict(arrowstyle='-|>', color='#3b82f6', lw=2, mutation_scale=12))

    # Catena principale
    draw_block(x_mixer, y_main, 'MIXER', 'Bilanciato', colors['mixer'])
    draw_block(x_filter, y_main, 'FILTRO SSB', '2.4 kHz', colors['filter'])
    draw_block(x_amp1, y_main, 'AMP IF', 'Lineare', colors['amp'])
    draw_block(x_pa, y_main, 'PA', '100W', colors['amp'])
    draw_block(x_ant, y_main, 'ANTENNA', '50 ohm', colors['output'])

    for x1, x2 in [(x_mixer, x_filter), (x_filter, x_amp1), (x_amp1, x_pa), (x_pa, x_ant)]:
        ax.annotate('', xy=(x2 - block_w/2 - 0.005, y_main), xytext=(x1 + block_w/2 + 0.005, y_main),
                    arrowprops=dict(arrowstyle='-|>', color='#3b82f6', lw=2, mutation_scale=12))

    # Oscillatori
    # Oscillatori - spaziati per evitare sovrapposizioni
    draw_block(x_mixer, y_osc, 'BFO', '9 MHz', colors['osc'])

    ax.annotate('', xy=(x_mixer, y_main - block_h/2 - 0.01), xytext=(x_mixer, y_osc + block_h/2 + 0.01),
                arrowprops=dict(arrowstyle='-|>', color='#ef4444', lw=2, mutation_scale=10))

    # MIXER 2 e VFO/PLL ben distanziati
    x_mixer2 = 0.58
    x_vfo = 0.73
    draw_block(x_mixer2, y_osc, 'MIXER 2', 'Upconvert', colors['mixer'])
    draw_block(x_vfo, y_osc, 'VFO/PLL', 'Sintonia', colors['osc'])

    ax.annotate('', xy=(x_amp1, y_main - block_h/2 - 0.01), xytext=(x_mixer2, y_osc + block_h/2 + 0.01),
                arrowprops=dict(arrowstyle='-|>', color='#ef4444', lw=2, mutation_scale=10))
    ax.annotate('', xy=(x_mixer2 - block_w/2 - 0.005, y_osc), xytext=(x_vfo + block_w/2 + 0.005, y_osc),
                arrowprops=dict(arrowstyle='<|-', color='#ef4444', lw=2, mutation_scale=10))

    freq_labels = [
        (x_preamp, y_audio + 0.06, '300-3400 Hz'),
        (x_mixer + 0.07, y_main + 0.06, '9 MHz SSB'),
        (x_amp1 + 0.07, y_main + 0.06, 'f_TX'),
        (x_pa, y_main + 0.06, 'RF'),
    ]
    for x, y, text in freq_labels:
        ax.text(x, y, text, fontsize=8, ha='center', fontweight='bold',
               bbox=dict(boxstyle='round,pad=0.2', facecolor='#fef3c7', edgecolor='#d4a574', linewidth=0.8))

    # Info box
    mixer_text = 'Mixer Bilanciato:\n- Sopprime portante\n- Genera USB + LSB\n- Richiede bilanciamento'
    ax.text(0.18, 0.25, mixer_text, fontsize=9, ha='center', va='center',
            color='#1e40af', linespacing=1.4,
            bbox=dict(boxstyle='round,pad=0.4', facecolor='white', edgecolor='#3b82f6', linewidth=2))

    legend_y = 0.08
    legend_items = [
        (colors['audio'], 'Audio'),
        (colors['mixer'], 'Mixer'),
        (colors['filter'], 'Filtro'),
        (colors['amp'], 'Amplificatore'),
        (colors['osc'], 'Oscillatore'),
    ]
    ax.text(0.50, legend_y, 'Legenda:', fontsize=9, fontweight='bold', va='center')
    x_leg = 0.57
    for color, label in legend_items:
        ax.add_patch(Rectangle((x_leg, legend_y - 0.012), 0.018, 0.024, facecolor=color,
                               edgecolor='#374151', linewidth=1))
        ax.text(x_leg + 0.022, legend_y, label, fontsize=8, va='center')
        x_leg += 0.08

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

    plt.savefig(OUTPUT_DIR / 'trasmettitore_ssb.png', dpi=150, bbox_inches='tight',
                facecolor='#f8fafc', edgecolor='none')
    plt.close()
    print(f"[OK] Salvato: {OUTPUT_DIR / 'trasmettitore_ssb.png'}")


def plot_power_amplifier():
    """Schema amplificatore finale con rete di adattamento."""
    fig, ax = plt.subplots(figsize=(16, 11))
    ax.set_facecolor('#f0fdf4')

    ax.text(0.5, 0.96, 'Amplificatore di Potenza (PA)', fontsize=20, fontweight='bold',
            ha='center', transform=ax.transAxes, color='#166534')
    ax.text(0.5, 0.92, 'Con rete di adattamento e protezioni', fontsize=12,
            ha='center', transform=ax.transAxes, color='#4a5568')

    colors = {
        'input': '#dbeafe',
        'driver': '#bbf7d0',
        'pa': '#fef08a',
        'match': '#ddd6fe',
        'filter': '#fecaca',
        'protect': '#fed7aa',
        'border': '#374151',
    }

    block_w = 0.12
    block_h = 0.09

    def draw_block(x, y, label, sublabel, color, w=None, h=None):
        w = w or block_w
        h = h or block_h
        shadow = FancyBboxPatch((x - w/2 + 0.002, y - h/2 - 0.002),
                                w, h, boxstyle="round,pad=0.005,rounding_size=0.01",
                                facecolor='#94a3b8', edgecolor='none', zorder=1)
        ax.add_patch(shadow)
        rect = FancyBboxPatch((x - w/2, y - h/2), w, h,
                              boxstyle="round,pad=0.005,rounding_size=0.01",
                              facecolor=color, edgecolor=colors['border'], linewidth=1.5, zorder=2)
        ax.add_patch(rect)
        ax.text(x, y + 0.018, label, ha='center', va='center', fontsize=9,
                fontweight='bold', color='#1e293b', zorder=3)
        ax.text(x, y - 0.018, sublabel, ha='center', va='center', fontsize=7,
                color='#475569', zorder=3)

    y_main = 0.55
    y_prot = 0.30

    x_in = 0.08
    x_driver = 0.22
    x_pa = 0.40
    x_match = 0.58
    x_lpf = 0.76
    x_ant = 0.92

    draw_block(x_in, y_main, 'RF IN', '1-10 mW', colors['input'])
    draw_block(x_driver, y_main, 'DRIVER', '+20 dB', colors['driver'])
    draw_block(x_pa, y_main, 'PA FINALE', 'LDMOS 100W', colors['pa'], w=0.14, h=0.11)
    draw_block(x_match, y_main, 'RETE PI', 'Adattamento', colors['match'])
    draw_block(x_lpf, y_main, 'LPF', 'Armoniche', colors['filter'])
    draw_block(x_ant, y_main, 'ANTENNA', '50 ohm', colors['protect'])

    for x1, x2 in [(x_in, x_driver), (x_driver, x_pa), (x_pa, x_match), (x_match, x_lpf), (x_lpf, x_ant)]:
        ax.annotate('', xy=(x2 - block_w/2 - 0.01, y_main), xytext=(x1 + block_w/2 + 0.01, y_main),
                    arrowprops=dict(arrowstyle='-|>', color='#22c55e', lw=2, mutation_scale=12))

    power_labels = [
        (x_in, y_main + 0.08, '10 mW'),
        (x_driver, y_main + 0.08, '1 W'),
        (x_pa + 0.08, y_main + 0.08, '100 W'),
        (x_lpf, y_main + 0.08, '95 W'),
    ]
    for x, y, text in power_labels:
        ax.text(x, y, text, fontsize=9, ha='center', fontweight='bold',
               bbox=dict(boxstyle='round,pad=0.2', facecolor='#dcfce7', edgecolor='#16a34a', linewidth=1))

    # Blocchi protezione - spaziati per evitare sovrapposizioni
    y_prot_row1 = 0.32
    y_prot_row2 = 0.18
    draw_block(x_pa - 0.07, y_prot_row1, 'BIAS', 'Classe AB', colors['protect'])
    draw_block(x_pa + 0.07, y_prot_row1, 'TEMP', 'Sensore', colors['protect'])
    draw_block(x_match, y_prot_row2, 'SWR', 'Protezione', colors['filter'])
    draw_block(x_lpf, y_prot_row2, 'ALC', 'Feedback', colors['match'])

    # Connessioni protezioni
    ax.annotate('', xy=(x_pa - 0.05, y_main - block_h/2 - 0.02), xytext=(x_pa - 0.07, y_prot_row1 + block_h/2 + 0.01),
                arrowprops=dict(arrowstyle='-|>', color='#ef4444', lw=1.5, mutation_scale=10))
    ax.annotate('', xy=(x_pa + 0.05, y_main - block_h/2 - 0.02), xytext=(x_pa + 0.07, y_prot_row1 + block_h/2 + 0.01),
                arrowprops=dict(arrowstyle='-|>', color='#ef4444', lw=1.5, mutation_scale=10))

    ax.plot([x_match, x_match], [y_prot_row2 + block_h/2 + 0.01, y_main - block_h/2 - 0.02], color='#8b5cf6', lw=1.5)
    ax.plot([x_lpf, x_lpf], [y_prot_row2 + block_h/2 + 0.01, y_main - block_h/2 - 0.02], color='#8b5cf6', lw=1.5, ls='--')

    # Alimentazione a sinistra
    y_psu = 0.25
    draw_block(0.08, y_psu, 'PSU', '13.8V 25A', colors['pa'])
    ax.plot([0.08 + block_w/2 + 0.01, x_pa - 0.07], [y_psu, y_psu], color='#dc2626', lw=2)
    ax.annotate('', xy=(x_pa - 0.07, y_prot_row1 - block_h/2 - 0.01), xytext=(x_pa - 0.07, y_psu),
                arrowprops=dict(arrowstyle='-|>', color='#dc2626', lw=2, mutation_scale=10))

    info_text = 'Rete PI (L-C-L):\n- Adatta 50 ohm\n- Q variabile\n- Banda selezionabile'
    ax.text(0.58, 0.78, info_text, fontsize=9, ha='center', va='center',
            color='#7c3aed', linespacing=1.4,
            bbox=dict(boxstyle='round,pad=0.4', facecolor='white', edgecolor='#8b5cf6', linewidth=2))

    eff_text = 'Efficienza PA:\nClasse A: 25%\nClasse AB: 50%\nClasse C: 70%'
    ax.text(0.15, 0.78, eff_text, fontsize=9, ha='center', va='center',
            color='#166534', linespacing=1.4,
            bbox=dict(boxstyle='round,pad=0.4', facecolor='white', edgecolor='#22c55e', linewidth=2))

    legend_y = 0.10
    legend_items = [
        (colors['driver'], 'Driver'),
        (colors['pa'], 'PA'),
        (colors['match'], 'Matching'),
        (colors['filter'], 'Filtro/Prot.'),
    ]
    ax.text(0.55, legend_y, 'Legenda:', fontsize=9, fontweight='bold', va='center')
    x_leg = 0.62
    for color, label in legend_items:
        ax.add_patch(Rectangle((x_leg, legend_y - 0.012), 0.018, 0.024, facecolor=color,
                               edgecolor='#374151', linewidth=1))
        ax.text(x_leg + 0.022, legend_y, label, fontsize=8, va='center')
        x_leg += 0.09

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

    plt.savefig(OUTPUT_DIR / 'amplificatore_potenza.png', dpi=150, bbox_inches='tight',
                facecolor='#f0fdf4', edgecolor='none')
    plt.close()
    print(f"[OK] Salvato: {OUTPUT_DIR / 'amplificatore_potenza.png'}")


def plot_fm_modulator():
    """Schema modulatore FM con VCO."""
    fig, ax = plt.subplots(figsize=(16, 11))
    ax.set_facecolor('#fef3c7')

    ax.text(0.5, 0.96, 'Modulatore FM con VCO', fontsize=20, fontweight='bold',
            ha='center', transform=ax.transAxes, color='#92400e')
    ax.text(0.5, 0.92, 'Trasmettitore FM (F3E) - Deviazione +/- 5 kHz', fontsize=12,
            ha='center', transform=ax.transAxes, color='#4a5568')

    colors = {
        'audio': '#dbeafe',
        'vco': '#fecaca',
        'pll': '#ddd6fe',
        'mult': '#bbf7d0',
        'amp': '#fef08a',
        'filter': '#fed7aa',
        'border': '#374151',
    }

    block_w = 0.11
    block_h = 0.08

    def draw_block(x, y, label, sublabel, color, w=None, h=None):
        w = w or block_w
        h = h or block_h
        shadow = FancyBboxPatch((x - w/2 + 0.002, y - h/2 - 0.002),
                                w, h, boxstyle="round,pad=0.005,rounding_size=0.01",
                                facecolor='#94a3b8', edgecolor='none', zorder=1)
        ax.add_patch(shadow)
        rect = FancyBboxPatch((x - w/2, y - h/2), w, h,
                              boxstyle="round,pad=0.005,rounding_size=0.01",
                              facecolor=color, edgecolor=colors['border'], linewidth=1.5, zorder=2)
        ax.add_patch(rect)
        ax.text(x, y + 0.015, label, ha='center', va='center', fontsize=9,
                fontweight='bold', color='#1e293b', zorder=3)
        ax.text(x, y - 0.015, sublabel, ha='center', va='center', fontsize=7,
                color='#475569', zorder=3)

    y_audio = 0.75
    y_main = 0.55
    y_pll = 0.35

    x_mic = 0.06
    x_preamp = 0.18
    x_preemph = 0.30
    x_vco = 0.45
    x_mult = 0.60
    x_pa = 0.75
    x_lpf = 0.88

    draw_block(x_mic, y_audio, 'MIC', 'Audio IN', colors['audio'])
    draw_block(x_preamp, y_audio, 'PREAMP', 'Gain', colors['audio'])
    draw_block(x_preemph, y_audio, 'PRE-ENFASI', '50 us', colors['audio'])

    for x1, x2 in [(x_mic, x_preamp), (x_preamp, x_preemph)]:
        ax.annotate('', xy=(x2 - block_w/2 - 0.005, y_audio), xytext=(x1 + block_w/2 + 0.005, y_audio),
                    arrowprops=dict(arrowstyle='-|>', color='#3b82f6', lw=2, mutation_scale=12))

    ax.plot([x_preemph + block_w/2 + 0.01, x_preemph + 0.08, x_preemph + 0.08],
            [y_audio, y_audio, y_main], color='#3b82f6', lw=2)
    ax.annotate('', xy=(x_vco - block_w/2 - 0.01, y_main), xytext=(x_preemph + 0.08, y_main),
                arrowprops=dict(arrowstyle='-|>', color='#3b82f6', lw=2, mutation_scale=12))

    draw_block(x_vco, y_main, 'VCO', 'Varactor', colors['vco'], w=0.13)
    draw_block(x_mult, y_main, 'x3 MULT', 'Triplicatore', colors['mult'])
    draw_block(x_pa, y_main, 'PA', '25W', colors['amp'])
    draw_block(x_lpf, y_main, 'LPF/ANT', '144 MHz', colors['filter'])

    for x1, x2 in [(x_vco, x_mult), (x_mult, x_pa), (x_pa, x_lpf)]:
        ax.annotate('', xy=(x2 - block_w/2 - 0.01, y_main), xytext=(x1 + block_w/2 + 0.01, y_main),
                    arrowprops=dict(arrowstyle='-|>', color='#22c55e', lw=2, mutation_scale=12))

    # PLL - blocchi spaziati per evitare sovrapposizioni
    x_xtal = 0.35
    x_pfd = 0.52
    x_loopf = 0.69

    draw_block(x_xtal, y_pll, 'XTAL REF', '12.8 MHz', colors['pll'])
    draw_block(x_pfd, y_pll, 'PFD', 'Phase Det', colors['pll'])
    draw_block(x_loopf, y_pll, 'LOOP FILTER', 'LPF', colors['pll'])

    ax.annotate('', xy=(x_pfd - block_w/2 - 0.005, y_pll), xytext=(x_xtal + block_w/2 + 0.005, y_pll),
                arrowprops=dict(arrowstyle='-|>', color='#8b5cf6', lw=1.5, mutation_scale=10))
    ax.annotate('', xy=(x_loopf - block_w/2 - 0.005, y_pll), xytext=(x_pfd + block_w/2 + 0.005, y_pll),
                arrowprops=dict(arrowstyle='-|>', color='#8b5cf6', lw=1.5, mutation_scale=10))

    # Feedback dal VCO al PFD
    ax.plot([x_vco + 0.04, x_vco + 0.04], [y_main - block_h/2 - 0.01, y_pll + 0.06], color='#8b5cf6', lw=1.5, ls='--')
    ax.annotate('', xy=(x_pfd, y_pll + block_h/2 + 0.01), xytext=(x_vco + 0.04, y_pll + 0.06),
                arrowprops=dict(arrowstyle='-|>', color='#8b5cf6', lw=1.5, mutation_scale=10))

    # Loop filter torna al VCO
    ax.plot([x_loopf, x_loopf], [y_pll + block_h/2 + 0.01, y_pll + 0.10], color='#ef4444', lw=2)
    ax.plot([x_loopf, x_vco], [y_pll + 0.10, y_pll + 0.10], color='#ef4444', lw=2)
    ax.annotate('', xy=(x_vco, y_main - block_h/2 - 0.01), xytext=(x_vco, y_pll + 0.10),
                arrowprops=dict(arrowstyle='-|>', color='#ef4444', lw=2, mutation_scale=10))

    freq_labels = [
        (x_vco, y_main + 0.07, '48 MHz'),
        (x_mult, y_main + 0.07, '144 MHz'),
        (x_lpf, y_main + 0.07, 'VHF OUT'),
    ]
    for x, y, text in freq_labels:
        ax.text(x, y, text, fontsize=8, ha='center', fontweight='bold',
               bbox=dict(boxstyle='round,pad=0.2', facecolor='#fef3c7', edgecolor='#d97706', linewidth=0.8))

    vco_text = 'VCO con Varactor:\n- Audio modula capacita\n- Deviazione +/- 5 kHz\n- Frequenza base / 3'
    ax.text(0.18, 0.35, vco_text, fontsize=9, ha='center', va='center',
            color='#dc2626', linespacing=1.4,
            bbox=dict(boxstyle='round,pad=0.4', facecolor='white', edgecolor='#ef4444', linewidth=2))

    preemph_text = 'Pre-enfasi:\n+6 dB/ottava\nsopra 3 kHz'
    ax.text(x_preemph, y_audio - 0.12, preemph_text, fontsize=8, ha='center', va='center',
            color='#1d4ed8', linespacing=1.3,
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='#3b82f6', linewidth=1.5))

    legend_y = 0.12
    legend_items = [
        (colors['audio'], 'Audio'),
        (colors['vco'], 'VCO'),
        (colors['pll'], 'PLL'),
        (colors['mult'], 'Moltipl.'),
        (colors['amp'], 'PA'),
    ]
    ax.text(0.50, legend_y, 'Legenda:', fontsize=9, fontweight='bold', va='center')
    x_leg = 0.57
    for color, label in legend_items:
        ax.add_patch(Rectangle((x_leg, legend_y - 0.012), 0.018, 0.024, facecolor=color,
                               edgecolor='#374151', linewidth=1))
        ax.text(x_leg + 0.022, legend_y, label, fontsize=8, va='center')
        x_leg += 0.08

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

    plt.savefig(OUTPUT_DIR / 'modulatore_fm_vco.png', dpi=150, bbox_inches='tight',
                facecolor='#fef3c7', edgecolor='none')
    plt.close()
    print(f"[OK] Salvato: {OUTPUT_DIR / 'modulatore_fm_vco.png'}")


def plot_alc_system():
    """Schema ALC (Automatic Level Control)."""
    fig, ax = plt.subplots(figsize=(16, 10))
    ax.set_facecolor('#f0f9ff')

    ax.text(0.5, 0.96, 'Sistema ALC - Automatic Level Control', fontsize=20, fontweight='bold',
            ha='center', transform=ax.transAxes, color='#1e40af')
    ax.text(0.5, 0.92, 'Controllo automatico del livello di modulazione', fontsize=12,
            ha='center', transform=ax.transAxes, color='#4a5568')

    colors = {
        'audio': '#dbeafe',
        'amp': '#bbf7d0',
        'detector': '#fecaca',
        'control': '#fef08a',
        'output': '#ddd6fe',
        'border': '#374151',
    }

    block_w = 0.12
    block_h = 0.09

    def draw_block(x, y, label, sublabel, color, w=None):
        w = w or block_w
        shadow = FancyBboxPatch((x - w/2 + 0.002, y - block_h/2 - 0.002),
                                w, block_h, boxstyle="round,pad=0.005,rounding_size=0.01",
                                facecolor='#94a3b8', edgecolor='none', zorder=1)
        ax.add_patch(shadow)
        rect = FancyBboxPatch((x - w/2, y - block_h/2), w, block_h,
                              boxstyle="round,pad=0.005,rounding_size=0.01",
                              facecolor=color, edgecolor=colors['border'], linewidth=1.5, zorder=2)
        ax.add_patch(rect)
        ax.text(x, y + 0.018, label, ha='center', va='center', fontsize=9,
                fontweight='bold', color='#1e293b', zorder=3)
        ax.text(x, y - 0.018, sublabel, ha='center', va='center', fontsize=7,
                color='#475569', zorder=3)

    y_main = 0.60
    y_feedback = 0.35

    x_in = 0.10
    x_vca = 0.28
    x_preamp = 0.46
    x_pa = 0.64
    x_out = 0.82

    draw_block(x_in, y_main, 'AUDIO IN', 'MIC/LINE', colors['audio'])
    draw_block(x_vca, y_main, 'VCA', 'Guadagno var.', colors['control'])
    draw_block(x_preamp, y_main, 'PREAMP', 'Driver', colors['amp'])
    draw_block(x_pa, y_main, 'PA', 'Finale', colors['amp'])
    draw_block(x_out, y_main, 'RF OUT', 'Antenna', colors['output'])

    for x1, x2 in [(x_in, x_vca), (x_vca, x_preamp), (x_preamp, x_pa), (x_pa, x_out)]:
        ax.annotate('', xy=(x2 - block_w/2 - 0.01, y_main), xytext=(x1 + block_w/2 + 0.01, y_main),
                    arrowprops=dict(arrowstyle='-|>', color='#3b82f6', lw=2, mutation_scale=12))

    draw_block(x_pa, y_feedback, 'DETECTOR', 'Picco RF', colors['detector'])
    draw_block(x_preamp, y_feedback, 'COMPARATORE', 'Soglia', colors['control'])
    draw_block(x_vca, y_feedback, 'INTEGRATORE', 'Tempo att.', colors['control'])

    ax.plot([x_pa, x_pa], [y_main - block_h/2 - 0.01, y_feedback + block_h/2 + 0.01], color='#ef4444', lw=2)

    ax.annotate('', xy=(x_preamp + block_w/2 + 0.01, y_feedback), xytext=(x_pa - block_w/2 - 0.01, y_feedback),
                arrowprops=dict(arrowstyle='-|>', color='#ef4444', lw=2, mutation_scale=12))

    ax.annotate('', xy=(x_vca + block_w/2 + 0.01, y_feedback), xytext=(x_preamp - block_w/2 - 0.01, y_feedback),
                arrowprops=dict(arrowstyle='-|>', color='#ef4444', lw=2, mutation_scale=12))

    ax.annotate('', xy=(x_vca, y_main - block_h/2 - 0.01), xytext=(x_vca, y_feedback + block_h/2 + 0.01),
                arrowprops=dict(arrowstyle='-|>', color='#22c55e', lw=2.5, mutation_scale=12))

    ax.text(x_preamp + 0.08, y_feedback + 0.06, 'Soglia\nALC', fontsize=8, ha='center',
            color='#dc2626', fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.2', facecolor='white', edgecolor='#ef4444'))

    info_text = 'Funzionamento ALC:\n1. Rileva picchi RF in uscita\n2. Confronta con soglia\n3. Riduce guadagno se > soglia\n4. Previene sovramodulazione'
    ax.text(0.18, 0.78, info_text, fontsize=9, ha='left', va='center',
            color='#1e40af', linespacing=1.4,
            bbox=dict(boxstyle='round,pad=0.5', facecolor='white', edgecolor='#3b82f6', linewidth=2))

    ax_inset = fig.add_axes([0.62, 0.70, 0.25, 0.18])
    t = np.linspace(0, 1, 100)
    input_signal = np.clip(1.5 * np.sin(2 * np.pi * 3 * t) + 0.5, 0, 2)
    output_signal = np.clip(input_signal, 0, 1.2)
    ax_inset.plot(t, input_signal, 'b-', lw=1.5, label='Ingresso')
    ax_inset.plot(t, output_signal, 'g-', lw=2, label='Uscita ALC')
    ax_inset.axhline(y=1.2, color='r', ls='--', lw=1, label='Soglia')
    ax_inset.set_xlim(0, 1)
    ax_inset.set_ylim(0, 2.2)
    ax_inset.set_xlabel('Tempo', fontsize=8)
    ax_inset.set_ylabel('Livello', fontsize=8)
    ax_inset.legend(fontsize=7, loc='upper right')
    ax_inset.set_title('Risposta ALC', fontsize=9, fontweight='bold')
    ax_inset.tick_params(labelsize=7)

    vantaggi_text = 'Vantaggi ALC:\n- Previene splatter\n- Protegge PA\n- Audio consistente'
    ax.text(0.85, 0.25, vantaggi_text, fontsize=9, ha='center', va='center',
            color='#166534', linespacing=1.4,
            bbox=dict(boxstyle='round,pad=0.4', facecolor='white', edgecolor='#22c55e', linewidth=2))

    legend_y = 0.12
    legend_items = [
        (colors['audio'], 'Audio'),
        (colors['control'], 'Controllo'),
        (colors['detector'], 'Rilevatore'),
        (colors['amp'], 'Amplif.'),
    ]
    ax.text(0.35, legend_y, 'Legenda:', fontsize=9, fontweight='bold', va='center')
    x_leg = 0.42
    for color, label in legend_items:
        ax.add_patch(Rectangle((x_leg, legend_y - 0.012), 0.018, 0.024, facecolor=color,
                               edgecolor='#374151', linewidth=1))
        ax.text(x_leg + 0.022, legend_y, label, fontsize=8, va='center')
        x_leg += 0.09

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

    plt.savefig(OUTPUT_DIR / 'sistema_alc.png', dpi=150, bbox_inches='tight',
                facecolor='#f0f9ff', edgecolor='none')
    plt.close()
    print(f"[OK] Salvato: {OUTPUT_DIR / 'sistema_alc.png'}")


def plot_transmitter_comparison():
    """Tabella confronto architetture trasmettitori."""
    fig, ax = plt.subplots(figsize=(16, 10))
    ax.set_facecolor('white')

    ax.text(0.5, 0.95, 'Confronto Architetture Trasmettitori', fontsize=18, fontweight='bold',
            ha='center', transform=ax.transAxes, color='#1e293b')

    transmitters = [
        ('CW (A1A)', 'On/Off keying', 'Semplice', '100-500 Hz', 'Alta', 'DX, QRP', '#dcfce7'),
        ('AM (A3E)', 'Ampiezza', 'Media', '9 kHz', 'Bassa', 'Broadcast', '#fef9c3'),
        ('SSB (J3E)', 'Banda laterale', 'Alta', '2.4-3 kHz', 'Alta', 'HF voce', '#dbeafe'),
        ('FM (F3E)', 'Frequenza', 'Media', '16 kHz', 'Media', 'VHF/UHF', '#fce7f3'),
        ('PSK31', 'Fase digitale', 'Alta', '31 Hz', 'Alta', 'Digitale HF', '#e0e7ff'),
    ]

    headers = ['Tipo', 'Modulazione', 'Complessita', 'Banda', 'Efficienza', 'Uso']
    col_widths = [0.12, 0.14, 0.12, 0.12, 0.12, 0.14]
    x_starts = [0.10]
    for w in col_widths[:-1]:
        x_starts.append(x_starts[-1] + w + 0.02)

    y = 0.85
    for x, header, width in zip(x_starts, headers, col_widths):
        ax.add_patch(Rectangle((x, y - 0.025), width, 0.05, facecolor='#1e293b',
                               edgecolor='black', linewidth=1, transform=ax.transAxes))
        ax.text(x + width/2, y, header, ha='center', va='center', fontsize=11,
               fontweight='bold', color='white', transform=ax.transAxes)

    row_height = 0.10
    for i, (tipo, mod, compl, banda, eff, uso, color) in enumerate(transmitters):
        y = 0.78 - i * row_height

        ax.add_patch(Rectangle((0.09, y - row_height/2 + 0.01), 0.82, row_height - 0.02,
                               facecolor=color, edgecolor='#ccc', linewidth=0.5,
                               transform=ax.transAxes))

        values = [tipo, mod, compl, banda, eff, uso]
        for x, val, width in zip(x_starts, values, col_widths):
            fontweight = 'bold' if x == x_starts[0] else 'normal'
            ax.text(x + width/2, y, val, ha='center', va='center', fontsize=10,
                   fontweight=fontweight, transform=ax.transAxes)

    ax.text(0.5, 0.20, 'SSB = Single Side Band | FM = Frequency Modulation | PSK = Phase Shift Keying',
           ha='center', fontsize=10, style='italic', transform=ax.transAxes, color='gray')

    rec_text = 'Raccomandazioni:\n- CW: Massima efficienza per DX\n- SSB: Standard per comunicazioni HF\n- FM: Ideale per comunicazioni locali VHF/UHF'
    ax.text(0.50, 0.12, rec_text, fontsize=9, ha='center', va='center',
            color='#374151', linespacing=1.5,
            bbox=dict(boxstyle='round,pad=0.5', facecolor='#f8fafc', edgecolor='#94a3b8', linewidth=1))

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

    plt.savefig(OUTPUT_DIR / 'confronto_trasmettitori.png', dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print(f"[OK] Salvato: {OUTPUT_DIR / 'confronto_trasmettitori.png'}")


def main():
    """Genera tutti i diagrammi trasmettitori."""
    print("Generazione diagrammi trasmettitori...")
    print(f"Directory output: {OUTPUT_DIR}\n")

    plot_ssb_transmitter()
    plot_power_amplifier()
    plot_fm_modulator()
    plot_alc_system()
    plot_transmitter_comparison()

    print("\n[OK] Tutti i diagrammi trasmettitori sono stati generati!")


if __name__ == "__main__":
    main()
