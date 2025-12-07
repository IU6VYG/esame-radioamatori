#!/usr/bin/env python3
"""
Generazione diagrammi dettagliati ricevitori radio.
Supereterodina, SDR, flusso segnale con livelli dBm, mixer.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Rectangle, FancyBboxPatch, FancyArrowPatch, Circle
import numpy as np
from pathlib import Path

# Directory di output
OUTPUT_DIR = Path(__file__).parent.parent / "images" / "04_ricevitori"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Configurazione stile
plt.rcParams['font.size'] = 10
plt.rcParams['axes.titlesize'] = 12
plt.rcParams['figure.facecolor'] = 'white'


def draw_block(ax, x, y, width, height, label, sublabel='', color='lightblue', fontsize=10):
    """Disegna un blocco con etichetta."""
    rect = FancyBboxPatch((x - width/2, y - height/2), width, height,
                          boxstyle="round,pad=0.02,rounding_size=0.1",
                          facecolor=color, edgecolor='black', linewidth=1.5)
    ax.add_patch(rect)

    if sublabel:
        ax.text(x, y + 0.15, label, ha='center', va='center', fontsize=fontsize, fontweight='bold')
        ax.text(x, y - 0.2, sublabel, ha='center', va='center', fontsize=fontsize-2, color='#555')
    else:
        ax.text(x, y, label, ha='center', va='center', fontsize=fontsize, fontweight='bold')


def draw_arrow(ax, x1, y1, x2, y2, color='black'):
    """Disegna una freccia."""
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='->', color=color, lw=1.5))


def plot_superheterodyne_detailed():
    """Schema dettagliato ricevitore supereterodina con layout ottimizzato."""
    fig, ax = plt.subplots(figsize=(16, 12))

    # Sfondo
    ax.set_facecolor('#f8fafc')

    # Titolo
    ax.text(0.5, 0.96, 'Ricevitore Supereterodina', fontsize=20, fontweight='bold',
            ha='center', transform=ax.transAxes, color='#1a365d')
    ax.text(0.5, 0.92, 'Schema a blocchi - Banda 40m (7 MHz)', fontsize=12,
            ha='center', transform=ax.transAxes, color='#4a5568')

    # Colori
    colors = {
        'antenna': '#fed7aa',
        'rf': '#bbf7d0',
        'mixer': '#bfdbfe',
        'if': '#ddd6fe',
        'audio': '#fef08a',
        'osc': '#fecaca',
        'border': '#374151',
    }

    # Dimensioni blocchi
    block_w = 0.11
    block_h = 0.08

    def draw_block(x, y, label, sublabel, color):
        # Ombra
        shadow = FancyBboxPatch((x - block_w/2 + 0.002, y - block_h/2 - 0.002),
                                block_w, block_h, boxstyle="round,pad=0.005,rounding_size=0.01",
                                facecolor='#94a3b8', edgecolor='none', zorder=1)
        ax.add_patch(shadow)
        # Blocco
        rect = FancyBboxPatch((x - block_w/2, y - block_h/2), block_w, block_h,
                              boxstyle="round,pad=0.005,rounding_size=0.01",
                              facecolor=color, edgecolor=colors['border'], linewidth=1.5, zorder=2)
        ax.add_patch(rect)
        ax.text(x, y + 0.015, label, ha='center', va='center', fontsize=10,
                fontweight='bold', color='#1e293b', zorder=3)
        ax.text(x, y - 0.015, sublabel, ha='center', va='center', fontsize=7,
                color='#475569', zorder=3)

    # Layout a 3 righe:
    # Riga 1: ANTENNA (centrata sopra PRESEL)
    # Riga 2: PRESEL -> LNA -> MIXER -> FILTRO IF -> AMP IF -> DEMOD -> AUDIO
    # Riga 3: OSC. LOCALE (sotto MIXER), BFO (sotto DEMOD)

    y_top = 0.78    # Antenna
    y_main = 0.62   # Catena principale
    y_osc = 0.42    # Oscillatori

    # Posizioni X della catena principale
    x_presel = 0.12
    x_lna = 0.26
    x_mixer = 0.40
    x_filtro = 0.54
    x_amp = 0.68
    x_demod = 0.82
    x_audio = 0.94

    # ANTENNA (sopra PRESEL)
    draw_block(x_presel, y_top, 'ANTENNA', '7.0 MHz', colors['antenna'])

    # Freccia da ANTENNA a PRESEL
    ax.annotate('', xy=(x_presel, y_main + block_h/2 + 0.01), xytext=(x_presel, y_top - block_h/2 - 0.01),
                arrowprops=dict(arrowstyle='-|>', color='#3b82f6', lw=2, mutation_scale=12))

    # Catena principale
    main_blocks = [
        (x_presel, y_main, 'PRESEL.', 'BPF 6.5-7.5', colors['rf']),
        (x_lna, y_main, 'LNA', '+15dB NF=2dB', colors['rf']),
        (x_mixer, y_main, 'MIXER', 'Conversione', colors['mixer']),
        (x_filtro, y_main, 'FILTRO IF', '455 kHz', colors['if']),
        (x_amp, y_main, 'AMP IF', '+60dB AGC', colors['if']),
        (x_demod, y_main, 'DEMOD', 'AM/SSB/CW', colors['audio']),
        (x_audio, y_main, 'AUDIO', '+20dB', colors['audio']),
    ]

    for x, y, label, sublabel, color in main_blocks:
        draw_block(x, y, label, sublabel, color)

    # Frecce tra blocchi catena principale
    x_positions = [x_presel, x_lna, x_mixer, x_filtro, x_amp, x_demod, x_audio]
    for i in range(len(x_positions) - 1):
        x1 = x_positions[i] + block_w/2 + 0.005
        x2 = x_positions[i+1] - block_w/2 - 0.005
        ax.annotate('', xy=(x2, y_main), xytext=(x1, y_main),
                    arrowprops=dict(arrowstyle='-|>', color='#3b82f6', lw=2, mutation_scale=12))

    # OSC. LOCALE (sotto MIXER)
    draw_block(x_mixer, y_osc, 'OSC. LOCALE', 'VFO 6.545 MHz', colors['osc'])
    ax.annotate('', xy=(x_mixer, y_main - block_h/2 - 0.01), xytext=(x_mixer, y_osc + block_h/2 + 0.01),
                arrowprops=dict(arrowstyle='-|>', color='#ef4444', lw=2, mutation_scale=10))

    # BFO (sotto DEMOD)
    draw_block(x_demod, y_osc, 'BFO', '455 kHz ±1.5k', colors['osc'])
    ax.annotate('', xy=(x_demod, y_main - block_h/2 - 0.01), xytext=(x_demod, y_osc + block_h/2 + 0.01),
                arrowprops=dict(arrowstyle='-|>', color='#ef4444', lw=2, mutation_scale=10))

    # AGC feedback
    ax.annotate('', xy=(x_amp, y_main + block_h/2 + 0.015), xytext=(x_demod, y_main + block_h/2 + 0.015),
                arrowprops=dict(arrowstyle='<-', color='#22c55e', lw=2, connectionstyle='arc3,rad=0.25'))
    ax.text((x_amp + x_demod)/2, y_main + 0.09, 'AGC', fontsize=9, fontweight='bold', color='#22c55e', ha='center')

    # Etichette frequenze sul percorso
    freq_labels = [
        (x_presel, y_main + 0.07, '7.0 MHz'),
        ((x_lna + x_mixer)/2, y_main + 0.07, '7.0 MHz'),
        ((x_mixer + x_filtro)/2, y_main + 0.07, '455 kHz'),
        ((x_amp + x_demod)/2 - 0.02, y_main + 0.07, '455 kHz'),
        (x_audio, y_main + 0.07, '0.3-3 kHz'),
    ]
    for x, y, text in freq_labels:
        ax.text(x, y, text, fontsize=8, ha='center', va='center', fontweight='bold',
               bbox=dict(boxstyle='round,pad=0.2', facecolor='#fef3c7', edgecolor='#d4a574', linewidth=0.8))

    # Formula conversione (usando text con bbox)
    formula_text = 'f_IF = f_RF - f_LO\n455 = 7000 - 6545 kHz'
    ax.text(0.40, 0.24, formula_text, fontsize=10, ha='center', va='center',
            color='#1e40af', fontweight='bold', linespacing=1.5,
            bbox=dict(boxstyle='round,pad=0.5', facecolor='white',
                     edgecolor='#3b82f6', linewidth=2))

    # Legenda
    legend_y = 0.08
    legend_items = [
        (colors['rf'], 'RF'),
        (colors['mixer'], 'Mixer'),
        (colors['if'], 'IF'),
        (colors['audio'], 'Audio'),
        (colors['osc'], 'Oscillatori'),
    ]
    ax.text(0.55, legend_y, 'Legenda:', fontsize=9, fontweight='bold', va='center')
    x_leg = 0.62
    for color, label in legend_items:
        ax.add_patch(Rectangle((x_leg, legend_y - 0.012), 0.018, 0.024, facecolor=color,
                               edgecolor='#374151', linewidth=1))
        ax.text(x_leg + 0.022, legend_y, label, fontsize=8, va='center')
        x_leg += 0.07

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

    plt.savefig(OUTPUT_DIR / 'supereterodina_dettagliato.png', dpi=150, bbox_inches='tight',
                facecolor='#f8fafc', edgecolor='none')
    plt.close()
    print(f"✓ Salvato: {OUTPUT_DIR / 'supereterodina_dettagliato.png'}")


def plot_sdr_receiver():
    """Schema ricevitore SDR con layout ottimizzato - antenna sopra."""
    fig, ax = plt.subplots(figsize=(16, 12))

    # Sfondo
    ax.set_facecolor('#f0f9ff')

    # Titolo
    ax.text(0.5, 0.96, 'Ricevitore SDR - Software Defined Radio', fontsize=20, fontweight='bold',
            ha='center', transform=ax.transAxes, color='#1e3a5f')
    ax.text(0.5, 0.92, 'Architettura I/Q a Conversione Diretta', fontsize=12,
            ha='center', transform=ax.transAxes, color='#4a5568')

    # Colori
    colors = {
        'antenna': '#fed7aa',
        'analog': '#a7f3d0',
        'mixer': '#93c5fd',
        'digital': '#c4b5fd',
        'osc': '#fca5a5',
        'dsp': '#fcd34d',
        'border': '#374151',
    }

    # Dimensioni blocchi
    block_w = 0.10
    block_h = 0.07

    def draw_block(x, y, label, sublabel, color):
        shadow = FancyBboxPatch((x - block_w/2 + 0.002, y - block_h/2 - 0.002),
                                block_w, block_h, boxstyle="round,pad=0.005,rounding_size=0.01",
                                facecolor='#94a3b8', edgecolor='none', zorder=1)
        ax.add_patch(shadow)
        rect = FancyBboxPatch((x - block_w/2, y - block_h/2), block_w, block_h,
                              boxstyle="round,pad=0.005,rounding_size=0.01",
                              facecolor=color, edgecolor=colors['border'], linewidth=1.5, zorder=2)
        ax.add_patch(rect)
        ax.text(x, y + 0.012, label, ha='center', va='center', fontsize=9,
                fontweight='bold', color='#1f2937', zorder=3)
        if sublabel:
            ax.text(x, y - 0.012, sublabel, ha='center', va='center', fontsize=7,
                    color='#4b5563', zorder=3)

    # Layout:
    # Riga 1: ANTENNA (sopra LNA)
    # Riga 2: LNA -> BPF -> split -> MIXER I -> LPF -> ADC -> DSP -> OUTPUT
    # Riga 3:                     -> MIXER Q -> LPF -> ADC -/
    # Sotto: LO (tra i mixer)

    y_top = 0.80      # Antenna
    y_i = 0.65        # Canale I
    y_q = 0.45        # Canale Q
    y_osc = 0.55      # LO (tra I e Q)

    # Posizioni X
    x_lna = 0.10
    x_bpf = 0.22
    x_split = 0.30
    x_mixer = 0.40
    x_lpf = 0.52
    x_adc = 0.64
    x_dsp = 0.80
    x_out = 0.94

    # ANTENNA (sopra LNA)
    draw_block(x_lna, y_top, 'ANTENNA', 'RF IN', colors['antenna'])
    ax.annotate('', xy=(x_lna, y_i + block_h/2 + 0.01), xytext=(x_lna, y_top - block_h/2 - 0.01),
                arrowprops=dict(arrowstyle='-|>', color='#3b82f6', lw=2, mutation_scale=12))

    # LNA e BPF (comuni)
    draw_block(x_lna, y_i, 'LNA', '+20dB', colors['analog'])
    draw_block(x_bpf, y_i, 'BPF', 'Anti-alias', colors['analog'])

    # Freccia LNA -> BPF
    ax.annotate('', xy=(x_bpf - block_w/2 - 0.005, y_i), xytext=(x_lna + block_w/2 + 0.005, y_i),
                arrowprops=dict(arrowstyle='-|>', color='#3b82f6', lw=2, mutation_scale=12))

    # Splitter (biforcazione verso I e Q)
    ax.plot([x_bpf + block_w/2 + 0.01, x_split, x_split], [y_i, y_i, y_i], color='#3b82f6', lw=2)
    ax.plot([x_split, x_split], [y_i, y_q], color='#3b82f6', lw=2)
    ax.annotate('', xy=(x_mixer - block_w/2 - 0.005, y_i), xytext=(x_split + 0.01, y_i),
                arrowprops=dict(arrowstyle='-|>', color='#3b82f6', lw=2, mutation_scale=12))
    ax.annotate('', xy=(x_mixer - block_w/2 - 0.005, y_q), xytext=(x_split + 0.01, y_q),
                arrowprops=dict(arrowstyle='-|>', color='#3b82f6', lw=2, mutation_scale=12))

    # Canale I
    draw_block(x_mixer, y_i, 'MIXER I', '0 deg', colors['mixer'])
    draw_block(x_lpf, y_i, 'LPF', 'Baseband', colors['analog'])
    draw_block(x_adc, y_i, 'ADC', '16-bit', colors['digital'])

    # Canale Q
    draw_block(x_mixer, y_q, 'MIXER Q', '90 deg', colors['mixer'])
    draw_block(x_lpf, y_q, 'LPF', 'Baseband', colors['analog'])
    draw_block(x_adc, y_q, 'ADC', '16-bit', colors['digital'])

    # Frecce canali I e Q (MIXER -> LPF -> ADC)
    for y_ch in [y_i, y_q]:
        for x1, x2 in [(x_mixer, x_lpf), (x_lpf, x_adc)]:
            ax.annotate('', xy=(x2 - block_w/2 - 0.005, y_ch), xytext=(x1 + block_w/2 + 0.005, y_ch),
                        arrowprops=dict(arrowstyle='-|>', color='#3b82f6', lw=2, mutation_scale=12))

    # Oscillatore locale (tra i due mixer)
    draw_block(x_mixer, y_osc, 'LO', 'DDS/PLL', colors['osc'])

    # Connessioni LO ai mixer
    ax.annotate('', xy=(x_mixer, y_i - block_h/2 - 0.005), xytext=(x_mixer, y_osc + block_h/2 + 0.005),
                arrowprops=dict(arrowstyle='-|>', color='#ef4444', lw=1.5, mutation_scale=10))
    ax.annotate('', xy=(x_mixer, y_q + block_h/2 + 0.005), xytext=(x_mixer, y_osc - block_h/2 - 0.005),
                arrowprops=dict(arrowstyle='-|>', color='#ef4444', lw=1.5, mutation_scale=10))

    # 90° phase shift label
    ax.text(x_mixer + 0.06, y_osc, '90°', fontsize=9, fontweight='bold', color='#ef4444',
            bbox=dict(boxstyle='circle,pad=0.2', facecolor='white', edgecolor='#ef4444'))

    # DSP Block (grande, riceve entrambi i canali)
    dsp_w, dsp_h = 0.12, 0.28
    shadow = FancyBboxPatch((x_dsp - dsp_w/2 + 0.002, y_osc - dsp_h/2 - 0.002), dsp_w, dsp_h,
                            boxstyle="round,pad=0.01,rounding_size=0.015",
                            facecolor='#94a3b8', edgecolor='none', zorder=1)
    ax.add_patch(shadow)
    rect = FancyBboxPatch((x_dsp - dsp_w/2, y_osc - dsp_h/2), dsp_w, dsp_h,
                          boxstyle="round,pad=0.01,rounding_size=0.015",
                          facecolor=colors['dsp'], edgecolor=colors['border'], linewidth=2, zorder=2)
    ax.add_patch(rect)
    ax.text(x_dsp, y_osc + 0.09, 'DSP', ha='center', fontsize=12, fontweight='bold', color='#1f2937', zorder=3)
    dsp_features = ['Filtri digitali', 'Demodulazione', 'FFT/Spettro', 'AGC software']
    for i, feat in enumerate(dsp_features):
        ax.text(x_dsp, y_osc + 0.04 - i*0.04, feat, ha='center', fontsize=8, color='#374151', zorder=3)

    # Frecce da ADC a DSP
    ax.annotate('', xy=(x_dsp - dsp_w/2 - 0.005, y_i), xytext=(x_adc + block_w/2 + 0.01, y_i),
                arrowprops=dict(arrowstyle='-|>', color='#8b5cf6', lw=2, mutation_scale=12))
    ax.annotate('', xy=(x_dsp - dsp_w/2 - 0.005, y_q), xytext=(x_adc + block_w/2 + 0.01, y_q),
                arrowprops=dict(arrowstyle='-|>', color='#8b5cf6', lw=2, mutation_scale=12))

    # Etichette I e Q
    ax.text(x_adc + 0.08, y_i + 0.02, 'I', fontsize=11, fontweight='bold', color='#2563eb')
    ax.text(x_adc + 0.08, y_q + 0.02, 'Q', fontsize=11, fontweight='bold', color='#dc2626')

    # Output
    ax.text(x_out, y_osc, 'USB\nAudio\nDisplay', fontsize=9, ha='center', va='center',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#e5e7eb', edgecolor='#374151', linewidth=1.5))
    ax.annotate('', xy=(x_out - 0.045, y_osc), xytext=(x_dsp + dsp_w/2 + 0.01, y_osc),
                arrowprops=dict(arrowstyle='-|>', color='#3b82f6', lw=2, mutation_scale=12))

    # Etichette canali (a sinistra)
    ax.text(x_split + 0.02, y_i + 0.045, 'Canale I (In-Phase)', fontsize=8, color='#2563eb', fontweight='bold')
    ax.text(x_split + 0.02, y_q - 0.045, 'Canale Q (Quadrature)', fontsize=8, color='#dc2626', fontweight='bold')

    # Box vantaggi SDR (usando text con bbox)
    vantaggi_text = 'Vantaggi SDR:\n• Flessibilita software\n• Filtri digitali\n• FFT/Spettro\n• Basso costo'
    ax.text(0.16, 0.16, vantaggi_text, fontsize=8, ha='center', va='center',
            color='#166534', linespacing=1.4,
            bbox=dict(boxstyle='round,pad=0.5', facecolor='white',
                     edgecolor='#22c55e', linewidth=2))

    # Legenda
    legend_x, legend_y = 0.55, 0.12
    ax.text(legend_x, legend_y, 'Legenda:', fontsize=9, fontweight='bold')
    legend_items = [
        (colors['analog'], 'Analogico'),
        (colors['mixer'], 'Mixer'),
        (colors['digital'], 'Digitale'),
        (colors['dsp'], 'DSP'),
    ]
    x_leg = legend_x + 0.06
    for color, label in legend_items:
        ax.add_patch(Rectangle((x_leg, legend_y - 0.012), 0.016, 0.024, facecolor=color,
                               edgecolor='#374151', linewidth=1))
        ax.text(x_leg + 0.020, legend_y, label, fontsize=8, va='center')
        x_leg += 0.08

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

    plt.savefig(OUTPUT_DIR / 'ricevitore_sdr.png', dpi=150, bbox_inches='tight',
                facecolor='#f0f9ff', edgecolor='none')
    plt.close()
    print(f"✓ Salvato: {OUTPUT_DIR / 'ricevitore_sdr.png'}")


def plot_signal_flow_dbm():
    """Diagramma flusso segnale con livelli dBm."""
    fig, ax = plt.subplots(figsize=(16, 10))

    # Titolo
    ax.text(0.5, 0.96, 'Flusso Segnale nel Ricevitore - Livelli dBm',
            fontsize=18, fontweight='bold', ha='center', transform=ax.transAxes)
    ax.text(0.5, 0.92, 'Esempio: segnale debole S5 (-93 dBm) su banda 20m',
            fontsize=12, ha='center', transform=ax.transAxes, color='gray')

    # Stadi e livelli
    stages = [
        ('Antenna', -93, 0, 'Segnale S5'),
        ('Presel.', -94, -1, 'Perdita 1dB'),
        ('LNA', -74, 20, 'Guadagno 20dB'),
        ('Mixer', -80, -6, 'Perdita 6dB'),
        ('Filtro IF', -83, -3, 'Perdita 3dB'),
        ('Amp IF 1', -43, 40, 'Guadagno 40dB'),
        ('Amp IF 2', -23, 20, 'Guadagno 20dB'),
        ('Rivelatore', -25, -2, 'Perdita 2dB'),
        ('Amp AF', -5, 20, 'Guadagno 20dB'),
    ]

    # Grafico livelli
    x_positions = np.arange(len(stages))
    levels = [s[1] for s in stages]
    gains = [s[2] for s in stages]

    # Barre livello segnale
    colors = ['green' if g > 0 else 'red' if g < 0 else 'gray' for g in gains]
    bars = ax.bar(x_positions, levels, color='lightblue', edgecolor='black', width=0.6, zorder=2)

    # Linea livello
    ax.plot(x_positions, levels, 'b-o', linewidth=2, markersize=8, zorder=3)

    # Etichette
    ax.set_xticks(x_positions)
    ax.set_xticklabels([s[0] for s in stages], rotation=45, ha='right', fontsize=10)
    ax.set_ylabel('Livello (dBm)', fontsize=12)
    ax.set_xlabel('Stadio', fontsize=12)

    # Annotazioni guadagno/perdita
    for i, (name, level, gain, desc) in enumerate(stages):
        color = 'green' if gain > 0 else 'red' if gain < 0 else 'gray'
        sign = '+' if gain > 0 else ''
        ax.text(i, level + 3, f'{sign}{gain}dB', ha='center', fontsize=9,
               fontweight='bold', color=color)
        ax.text(i, -100, desc, ha='center', fontsize=8, rotation=45, color='gray')

    # Livelli di riferimento
    ax.axhline(y=-93, color='orange', linestyle='--', alpha=0.7, label='Sensibilita tipica')
    ax.axhline(y=-10, color='red', linestyle='--', alpha=0.7, label='Saturazione')
    ax.axhline(y=0, color='purple', linestyle='--', alpha=0.7, label='1 mW (0 dBm)')

    # Range dinamico
    ax.fill_between(x_positions, -120, levels, alpha=0.2, color='blue')

    ax.set_ylim(-110, 10)
    ax.set_xlim(-0.5, len(stages) - 0.5)
    ax.grid(True, alpha=0.3, axis='y')
    ax.legend(loc='lower right', fontsize=9)

    # Tabella riassuntiva
    table_data = [
        ['Parametro', 'Valore'],
        ['Segnale ingresso', '-93 dBm (S5)'],
        ['Guadagno totale', '88 dB'],
        ['Segnale uscita', '-5 dBm'],
        ['Floor rumore', '-120 dBm'],
        ['SNR uscita', '115 dB'],
    ]

    table_ax = fig.add_axes([0.72, 0.55, 0.22, 0.25])
    table_ax.axis('off')
    table = table_ax.table(cellText=table_data, loc='center', cellLoc='center',
                          colWidths=[0.5, 0.5])
    table.auto_set_font_size(False)
    table.set_fontsize(9)
    table.scale(1, 1.5)
    for i in range(len(table_data)):
        for j in range(2):
            cell = table[(i, j)]
            if i == 0:
                cell.set_facecolor('#2c3e50')
                cell.set_text_props(color='white', fontweight='bold')
            else:
                cell.set_facecolor('#f8f9fa' if i % 2 else 'white')

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'flusso_segnale_dbm.png', dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print(f"✓ Salvato: {OUTPUT_DIR / 'flusso_segnale_dbm.png'}")


def plot_mixer_oscillator():
    """Schema dettagliato mixer e oscillatore locale."""
    fig, axes = plt.subplots(1, 2, figsize=(16, 8))

    # === MIXER ===
    ax = axes[0]
    ax.set_title('Mixer a Diodi (Doppio Bilanciato)', fontsize=14, fontweight='bold')

    # Schema semplificato mixer
    # Ingresso RF
    ax.text(0.05, 0.5, 'RF IN\n7.0 MHz', fontsize=10, ha='center', va='center',
           bbox=dict(boxstyle='round', facecolor='#CCFFCC'))
    ax.annotate('', xy=(0.18, 0.5), xytext=(0.12, 0.5),
                arrowprops=dict(arrowstyle='->', lw=1.5))

    # Trasformatore ingresso
    ax.add_patch(Rectangle((0.18, 0.4), 0.08, 0.2, facecolor='#FFE5CC', edgecolor='black'))
    ax.text(0.22, 0.5, 'T1', fontsize=9, ha='center', va='center')

    # Anello diodi
    center_x, center_y = 0.45, 0.5
    radius = 0.12
    for i, angle in enumerate([45, 135, 225, 315]):
        rad = np.radians(angle)
        x = center_x + radius * np.cos(rad)
        y = center_y + radius * np.sin(rad)
        ax.plot(x, y, 'ko', markersize=10)
        ax.text(x, y, f'D{i+1}', fontsize=8, ha='center', va='bottom')

    # Connessioni diodi (cerchio)
    theta = np.linspace(0, 2*np.pi, 100)
    ax.plot(center_x + radius * np.cos(theta), center_y + radius * np.sin(theta),
            'b-', linewidth=1)

    ax.text(center_x, center_y, 'Anello\nDiodi', fontsize=9, ha='center', va='center')

    # Connessioni
    ax.plot([0.26, 0.33], [0.5, 0.5], 'k-', lw=1.5)
    ax.plot([0.57, 0.64], [0.5, 0.5], 'k-', lw=1.5)

    # Trasformatore uscita
    ax.add_patch(Rectangle((0.64, 0.4), 0.08, 0.2, facecolor='#FFE5CC', edgecolor='black'))
    ax.text(0.68, 0.5, 'T2', fontsize=9, ha='center', va='center')

    # LO input
    ax.text(center_x, 0.15, 'LO IN\n6.545 MHz', fontsize=10, ha='center', va='center',
           bbox=dict(boxstyle='round', facecolor='#FFCCCC'))
    ax.annotate('', xy=(center_x, 0.38), xytext=(center_x, 0.22),
                arrowprops=dict(arrowstyle='->', lw=1.5))

    # IF output
    ax.text(0.85, 0.5, 'IF OUT\n455 kHz', fontsize=10, ha='center', va='center',
           bbox=dict(boxstyle='round', facecolor='#E5CCFF'))
    ax.annotate('', xy=(0.78, 0.5), xytext=(0.72, 0.5),
                arrowprops=dict(arrowstyle='->', lw=1.5))

    # Formula
    ax.text(0.5, 0.85, 'f_IF = |f_RF - f_LO| = |7000 - 6545| = 455 kHz',
           fontsize=10, ha='center', va='center',
           bbox=dict(boxstyle='round', facecolor='lightyellow'))

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

    # === OSCILLATORE LOCALE ===
    ax = axes[1]
    ax.set_title('Oscillatore Locale (VFO)', fontsize=14, fontweight='bold')

    # Schema VFO
    # Cristallo/VFO
    ax.add_patch(Rectangle((0.1, 0.4), 0.15, 0.2, facecolor='#CCFFCC', edgecolor='black', lw=2))
    ax.text(0.175, 0.5, 'VFO\no TCXO', fontsize=10, ha='center', va='center')
    ax.text(0.175, 0.35, '5-5.5 MHz', fontsize=8, ha='center', color='gray')

    # Buffer
    ax.add_patch(Rectangle((0.35, 0.4), 0.12, 0.2, facecolor='#CCE5FF', edgecolor='black', lw=2))
    ax.text(0.41, 0.5, 'Buffer\nAmp', fontsize=9, ha='center', va='center')

    # Moltiplicatore (opzionale)
    ax.add_patch(Rectangle((0.55, 0.4), 0.12, 0.2, facecolor='#FFFFCC', edgecolor='black', lw=2))
    ax.text(0.61, 0.5, 'PLL\nSynth', fontsize=9, ha='center', va='center')

    # Output buffer
    ax.add_patch(Rectangle((0.75, 0.4), 0.12, 0.2, facecolor='#CCE5FF', edgecolor='black', lw=2))
    ax.text(0.81, 0.5, 'Output\nBuffer', fontsize=9, ha='center', va='center')

    # Frecce
    ax.annotate('', xy=(0.33, 0.5), xytext=(0.25, 0.5),
                arrowprops=dict(arrowstyle='->', lw=1.5))
    ax.annotate('', xy=(0.53, 0.5), xytext=(0.47, 0.5),
                arrowprops=dict(arrowstyle='->', lw=1.5))
    ax.annotate('', xy=(0.73, 0.5), xytext=(0.67, 0.5),
                arrowprops=dict(arrowstyle='->', lw=1.5))

    # Output
    ax.text(0.95, 0.5, 'LO\n6.545 MHz\n+7 dBm', fontsize=10, ha='center', va='center',
           bbox=dict(boxstyle='round', facecolor='#FFCCCC'))
    ax.annotate('', xy=(0.90, 0.5), xytext=(0.87, 0.5),
                arrowprops=dict(arrowstyle='->', lw=1.5))

    # Caratteristiche
    specs = [
        'Specifiche tipiche VFO/PLL:',
        '• Stabilita: <10 ppm',
        '• Rumore fase: -110 dBc/Hz @10kHz',
        '• Spurie: <-60 dBc',
        '• Potenza uscita: +7 dBm',
    ]
    y_spec = 0.25
    for line in specs:
        fontweight = 'bold' if 'Specifiche' in line else 'normal'
        ax.text(0.1, y_spec, line, fontsize=9, fontweight=fontweight)
        y_spec -= 0.045

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

    plt.suptitle('Componenti Chiave del Ricevitore Supereterodina', fontsize=16, fontweight='bold', y=1.02)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'mixer_oscillatore.png', dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print(f"✓ Salvato: {OUTPUT_DIR / 'mixer_oscillatore.png'}")


def plot_receiver_comparison():
    """Tabella confronto architetture ricevitori."""
    fig, ax = plt.subplots(figsize=(16, 10))

    # Titolo
    ax.text(0.5, 0.96, 'Confronto Architetture Ricevitori', fontsize=18, fontweight='bold',
            ha='center', transform=ax.transAxes)

    # Dati
    receivers = [
        ('Supereterodina\nsingola conv.', 'Analogico', 'Buona', 'Media', 'Buona', 'HF classico', '#CCFFCC'),
        ('Supereterodina\ndoppia conv.', 'Analogico', 'Ottima', 'Alta', 'Eccellente', 'HF/VHF pro', '#CCFFCC'),
        ('Conversione\ndiretta', 'Misto', 'Buona', 'Bassa', 'Limitata', 'SDR entry', '#CCE5FF'),
        ('SDR I/Q', 'Digitale', 'Ottima', 'Media', 'Eccellente', 'SDR moderno', '#CCE5FF'),
        ('Campionamento\ndiretto', 'Digitale', 'Ottima', 'Alta', 'Eccellente', 'SDR high-end', '#E5CCFF'),
    ]

    headers = ['Architettura', 'Tipo', 'Sensibilita', 'Complessita', 'Selettivita', 'Uso tipico']
    col_widths = [0.15, 0.10, 0.12, 0.12, 0.12, 0.14]
    x_starts = [0.08]
    for w in col_widths[:-1]:
        x_starts.append(x_starts[-1] + w + 0.02)

    # Header
    y = 0.88
    for x, header, width in zip(x_starts, headers, col_widths):
        ax.add_patch(Rectangle((x, y - 0.025), width, 0.045, facecolor='#2c3e50',
                               edgecolor='black', linewidth=1, transform=ax.transAxes))
        ax.text(x + width/2, y, header, ha='center', va='center', fontsize=11,
               fontweight='bold', color='white', transform=ax.transAxes)

    # Dati
    row_height = 0.10
    for i, (arch, tipo, sens, compl, selet, uso, color) in enumerate(receivers):
        y = 0.80 - i * row_height

        ax.add_patch(Rectangle((0.07, y - row_height/2 + 0.01), 0.86, row_height - 0.02,
                               facecolor=color, edgecolor='#ccc', linewidth=0.5,
                               transform=ax.transAxes))

        values = [arch, tipo, sens, compl, selet, uso]
        for x, val, width in zip(x_starts, values, col_widths):
            fontweight = 'bold' if x == x_starts[0] else 'normal'
            ax.text(x + width/2, y, val, ha='center', va='center', fontsize=10,
                   fontweight=fontweight, transform=ax.transAxes)

    # Note
    ax.text(0.5, 0.15, 'SDR = Software Defined Radio | I/Q = In-phase/Quadrature',
           ha='center', fontsize=10, style='italic', transform=ax.transAxes, color='gray')

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'confronto_architetture_rx.png', dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print(f"✓ Salvato: {OUTPUT_DIR / 'confronto_architetture_rx.png'}")


def main():
    """Genera tutti i diagrammi ricevitori."""
    print("Generazione diagrammi ricevitori...")
    print(f"Directory output: {OUTPUT_DIR}\n")

    plot_superheterodyne_detailed()
    plot_sdr_receiver()
    plot_signal_flow_dbm()
    plot_mixer_oscillator()
    plot_receiver_comparison()

    print("\n✅ Tutti i diagrammi ricevitori sono stati generati!")


if __name__ == "__main__":
    main()
