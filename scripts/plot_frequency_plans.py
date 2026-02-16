#!/usr/bin/env python3
"""
Generazione visualizzazioni piani di frequenza IARU.
Allocazione bande HF, VHF/UHF, modi di emissione e potenze.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Rectangle
import numpy as np
from pathlib import Path

# Directory di output
OUTPUT_DIR = Path(__file__).parent.parent / "images" / "b_operativa"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Configurazione stile
plt.rcParams['font.size'] = 9
plt.rcParams['axes.titlesize'] = 12
plt.rcParams['figure.facecolor'] = 'white'

# Colori per modi
COLORS = {
    'CW': '#FF6B6B',      # Rosso
    'Digi': '#4ECDC4',    # Ciano
    'SSB': '#45B7D1',     # Blu
    'FM': '#96CEB4',      # Verde
    'Beacon': '#FFEAA7',  # Giallo
    'Satellite': '#DDA0DD', # Viola
    'EME': '#FFB6C1',     # Rosa
}

# Colori per modi digitali specifici
DIGITAL_COLORS = {
    'FT8': '#FF9F43',      # Arancione
    'FT4': '#FFB976',      # Arancione chiaro
    'RTTY': '#00CEC9',     # Teal
    'PSK31': '#6C5CE7',    # Viola
    'JS8': '#A29BFE',      # Lavanda
    'SSTV': '#FD79A8',     # Rosa
    'FAX': '#E17055',      # Corallo
    'Winlink': '#74B9FF',  # Azzurro
    'APRS': '#00B894',     # Verde acqua
    'Packet': '#55E6C1',   # Menta
    'JT65': '#FDA7DF',     # Rosa chiaro
    'WSPR': '#F8B739',     # Oro
}


def plot_hf_bands():
    """Grafico allocazione bande HF radioamatore (1.8-30 MHz) - versione migliorata."""
    fig, ax = plt.subplots(figsize=(16, 14))

    # Dati bande HF (Regione 1 - IARU) con frequenze tipiche
    bands = [
        # (nome, freq_min, freq_max, lambda, segmenti)
        ('160m', 1.810, 1.850, '160m (Top Band)', [
            (1.810, 1.838, 'CW', 'CW/QRP'),
            (1.838, 1.840, 'Digi', 'Digi'),
            (1.840, 1.850, 'SSB', 'Fonia'),
        ]),
        ('80m', 3.5, 3.8, '80m (Notte)', [
            (3.500, 3.570, 'CW', 'CW'),
            (3.570, 3.600, 'Digi', 'Digi'),
            (3.600, 3.650, 'SSB', 'Contest'),
            (3.650, 3.700, 'SSB', 'Fonia'),
            (3.700, 3.800, 'SSB', 'DX/Fonia'),
        ]),
        ('60m', 5.3515, 5.3665, '60m (Canalizzato)', [
            (5.3515, 5.3665, 'SSB', '5 canali'),
        ]),
        ('40m', 7.0, 7.2, '40m (DX 24h)', [
            (7.000, 7.040, 'CW', 'CW/DX'),
            (7.040, 7.060, 'Digi', 'Digi'),
            (7.060, 7.100, 'SSB', 'Contest'),
            (7.100, 7.200, 'SSB', 'Fonia'),
        ]),
        ('30m', 10.1, 10.15, '30m (WARC)', [
            (10.100, 10.130, 'CW', 'CW'),
            (10.130, 10.150, 'Digi', 'Digi'),
        ]),
        ('20m', 14.0, 14.35, '20m (DX principale)', [
            (14.000, 14.070, 'CW', 'CW/DX'),
            (14.070, 14.099, 'Digi', 'Digi/FT8'),
            (14.099, 14.101, 'Beacon', 'IBP'),
            (14.101, 14.125, 'SSB', 'DX'),
            (14.125, 14.300, 'SSB', 'Fonia'),
            (14.300, 14.350, 'SSB', 'Emerg.'),
        ]),
        ('17m', 18.068, 18.168, '17m (WARC)', [
            (18.068, 18.095, 'CW', 'CW'),
            (18.095, 18.109, 'Digi', 'Digi'),
            (18.109, 18.111, 'Beacon', 'IBP'),
            (18.111, 18.168, 'SSB', 'Fonia'),
        ]),
        ('15m', 21.0, 21.45, '15m (Ciclo solare)', [
            (21.000, 21.070, 'CW', 'CW/DX'),
            (21.070, 21.149, 'Digi', 'Digi'),
            (21.149, 21.151, 'Beacon', 'IBP'),
            (21.151, 21.450, 'SSB', 'Fonia/DX'),
        ]),
        ('12m', 24.89, 24.99, '12m (WARC)', [
            (24.890, 24.915, 'CW', 'CW'),
            (24.915, 24.929, 'Digi', 'Digi'),
            (24.929, 24.931, 'Beacon', 'IBP'),
            (24.931, 24.990, 'SSB', 'Fonia'),
        ]),
        ('10m', 28.0, 29.7, '10m (Sporadica)', [
            (28.000, 28.070, 'CW', 'CW'),
            (28.070, 28.190, 'Digi', 'Digi'),
            (28.190, 28.225, 'Beacon', 'IBP'),
            (28.225, 28.300, 'SSB', 'DX'),
            (28.300, 29.100, 'SSB', 'Fonia'),
            (29.100, 29.200, 'FM', 'Simplex'),
            (29.200, 29.700, 'FM', 'Ripetit.'),
        ]),
    ]

    y_pos = len(bands) + 0.5
    bar_height = 0.7
    bar_width = 10

    # Titolo
    ax.text(6, y_pos + 1.5, 'Allocazione Bande HF Radioamatore', fontsize=16, fontweight='bold', ha='center')
    ax.text(6, y_pos + 0.9, 'IARU Regione 1 (Europa/Africa/Medio Oriente)', fontsize=11, ha='center', color='gray')

    for band_name, freq_min, freq_max, description, segments in bands:
        y_pos -= 1

        # Sfondo banda con bordo
        ax.add_patch(Rectangle((-0.2, y_pos - bar_height/2 - 0.1), bar_width + 3.5, bar_height + 0.2,
                               facecolor='#f8f9fa', edgecolor='#dee2e6', linewidth=1, zorder=0))

        # Etichetta banda (grande, a sinistra)
        ax.text(-1.5, y_pos, band_name, ha='right', va='center', fontsize=14, fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='gray', linewidth=1))

        # Frequenze (sotto il nome)
        ax.text(-1.5, y_pos - 0.4, f'{freq_min:.3f}-{freq_max:.3f}', ha='right', va='center',
                fontsize=9, color='#666', family='monospace')

        # Disegna segmenti con etichette
        for seg_min, seg_max, mode, label in segments:
            width = (seg_max - seg_min) / (freq_max - freq_min) * bar_width
            x_start = (seg_min - freq_min) / (freq_max - freq_min) * bar_width

            rect = Rectangle((x_start, y_pos - bar_height/2), width, bar_height,
                            facecolor=COLORS[mode], edgecolor='white', linewidth=1.5, zorder=1)
            ax.add_patch(rect)

            # Etichetta modo (se c'è spazio)
            if width > 0.8:
                ax.text(x_start + width/2, y_pos, label, ha='center', va='center',
                       fontsize=8 if width > 1.5 else 7, fontweight='bold', color='black', zorder=2)

        # Descrizione banda (a destra)
        ax.text(bar_width + 0.3, y_pos, description, ha='left', va='center', fontsize=10, color='#444')

    # Legenda più grande e visibile
    legend_patches = [
        mpatches.Patch(color=COLORS['CW'], label='CW (Telegrafia)'),
        mpatches.Patch(color=COLORS['Digi'], label='Digitale (FT8, RTTY...)'),
        mpatches.Patch(color=COLORS['SSB'], label='SSB (Fonia)'),
        mpatches.Patch(color=COLORS['FM'], label='FM'),
        mpatches.Patch(color=COLORS['Beacon'], label='Beacon IBP'),
    ]
    ax.legend(handles=legend_patches, loc='lower center', fontsize=11, title='Modi di Emissione',
              title_fontsize=12, ncol=5, bbox_to_anchor=(0.45, -0.02),
              frameon=True, fancybox=True, shadow=True)

    # Note
    ax.text(6, -0.8, 'IBP = International Beacon Project | WARC = Bande senza contest',
            ha='center', fontsize=9, style='italic', color='gray')

    ax.set_xlim(-3.5, 15)
    ax.set_ylim(-1.5, len(bands) + 3)
    ax.axis('off')

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'allocazione_bande_hf.png', dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print(f"✓ Salvato: {OUTPUT_DIR / 'allocazione_bande_hf.png'}")


def plot_vhf_uhf_bands():
    """Grafico allocazione bande VHF/UHF (144, 432, 1296 MHz)."""
    fig, axes = plt.subplots(3, 1, figsize=(14, 10))

    # Banda 2m (144 MHz)
    segments_2m = [
        (144.000, 144.025, 'EME'),
        (144.025, 144.110, 'CW'),
        (144.110, 144.150, 'SSB'),
        (144.150, 144.180, 'CW'),
        (144.180, 144.360, 'SSB'),
        (144.360, 144.400, 'CW'),
        (144.400, 144.490, 'Beacon'),
        (144.490, 144.500, 'CW'),
        (144.500, 144.800, 'FM'),
        (144.800, 144.990, 'FM'),
        (144.990, 145.194, 'Satellite'),
        (145.194, 145.806, 'FM'),
        (145.806, 146.000, 'Satellite'),
    ]

    # Banda 70cm (432 MHz)
    segments_70cm = [
        (432.000, 432.025, 'EME'),
        (432.025, 432.100, 'CW'),
        (432.100, 432.400, 'SSB'),
        (432.400, 432.500, 'Beacon'),
        (432.500, 433.000, 'FM'),
        (433.000, 433.400, 'FM'),
        (433.400, 434.000, 'FM'),
        (434.000, 435.000, 'Digi'),
        (435.000, 438.000, 'Satellite'),
    ]

    # Banda 23cm (1296 MHz)
    segments_23cm = [
        (1240.000, 1260.000, 'Digi'),
        (1260.000, 1270.000, 'Satellite'),
        (1270.000, 1290.000, 'FM'),
        (1290.000, 1296.000, 'CW'),
        (1296.000, 1296.150, 'EME'),
        (1296.150, 1296.800, 'SSB'),
        (1296.800, 1297.000, 'Beacon'),
        (1297.000, 1298.000, 'FM'),
        (1298.000, 1300.000, 'Digi'),
    ]

    all_bands = [
        ('2m (144-146 MHz)', 144, 146, segments_2m),
        ('70cm (432-438 MHz)', 432, 438, segments_70cm),
        ('23cm (1240-1300 MHz)', 1240, 1300, segments_23cm),
    ]

    for ax, (band_name, freq_min, freq_max, segments) in zip(axes, all_bands):
        for seg_min, seg_max, mode in segments:
            # Normalizza a 0-1
            x_start = (seg_min - freq_min) / (freq_max - freq_min)
            width = (seg_max - seg_min) / (freq_max - freq_min)

            ax.axvspan(x_start, x_start + width, facecolor=COLORS.get(mode, 'gray'),
                      alpha=0.8, edgecolor='black', linewidth=0.5)

            # Etichetta modo (se abbastanza largo)
            if width > 0.05:
                ax.text(x_start + width/2, 0.5, mode, ha='center', va='center',
                       fontsize=8, rotation=90 if width < 0.1 else 0)

        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.set_title(band_name, fontsize=12, fontweight='bold')

        # Asse X con frequenze
        n_ticks = 6
        tick_positions = np.linspace(0, 1, n_ticks)
        tick_labels = [f'{freq_min + (freq_max-freq_min)*p:.1f}' for p in tick_positions]
        ax.set_xticks(tick_positions)
        ax.set_xticklabels(tick_labels, fontsize=8)
        ax.set_xlabel('Frequenza (MHz)', fontsize=9)
        ax.set_yticks([])

    # Legenda comune
    legend_patches = [mpatches.Patch(color=color, label=mode) for mode, color in COLORS.items()]
    fig.legend(handles=legend_patches, loc='center right', fontsize=9, title='Modi',
              bbox_to_anchor=(1.12, 0.5))

    fig.suptitle('Allocazione Bande VHF/UHF - IARU Regione 1', fontsize=14, fontweight='bold', y=1.02)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'allocazione_bande_vhf_uhf.png', dpi=150, bbox_inches='tight')
    plt.close()
    print(f"✓ Salvato: {OUTPUT_DIR / 'allocazione_bande_vhf_uhf.png'}")


def plot_mode_legend():
    """Legenda modi di emissione per segmento."""
    fig, ax = plt.subplots(figsize=(12, 8))

    modes_info = [
        ('CW', COLORS['CW'], 'Telegrafia Morse', 'A1A', '150-500 Hz', 'DX, Contest'),
        ('SSB', COLORS['SSB'], 'Single Side Band', 'J3E', '2.4-3 kHz', 'Voce, DX'),
        ('FM', COLORS['FM'], 'Frequency Modulation', 'F3E', '12-25 kHz', 'Locale, Ripetitori'),
        ('Digi', COLORS['Digi'], 'Modi Digitali', 'Vari', '0.5-3 kHz', 'FT8, RTTY, PSK'),
        ('Beacon', COLORS['Beacon'], 'Fari di Propagazione', 'A1A/F1A', '100-500 Hz', 'Test propagazione'),
        ('Satellite', COLORS['Satellite'], 'Comunicazioni via Satellite', 'Vari', 'Varia', 'Spazio, ISS'),
        ('EME', COLORS['EME'], 'Earth-Moon-Earth', 'A1A/J3E', '500-3kHz', 'Riflessione lunare'),
    ]

    # Intestazione
    headers = ['Modo', 'Colore', 'Descrizione', 'Designatore', 'Larghezza', 'Uso Tipico']
    col_widths = [0.08, 0.08, 0.22, 0.12, 0.12, 0.22]
    x_positions = [0.02]
    for w in col_widths[:-1]:
        x_positions.append(x_positions[-1] + w)

    # Header row
    y = 0.92
    for x, header, width in zip(x_positions, headers, col_widths):
        ax.text(x + width/2, y, header, ha='center', va='center', fontsize=11,
               fontweight='bold', transform=ax.transAxes)

    ax.plot([0.02, 0.98], [0.88, 0.88], color='black', linewidth=2, transform=ax.transAxes)

    # Data rows
    for i, (mode, color, desc, desig, bw, use) in enumerate(modes_info):
        y = 0.82 - i * 0.1

        # Colore box
        rect = Rectangle((x_positions[0], y - 0.03), col_widths[0] - 0.01, 0.06,
                         facecolor=color, edgecolor='black', linewidth=1,
                         transform=ax.transAxes)
        ax.add_patch(rect)

        # Testo
        texts = [mode, '', desc, desig, bw, use]
        for x, text, width in zip(x_positions, texts, col_widths):
            if text:
                ax.text(x + width/2, y, text, ha='center', va='center', fontsize=9,
                       transform=ax.transAxes)

    # Nota
    ax.text(0.5, 0.05, 'Nota: I segmenti e le larghezze di banda sono indicativi.\n'
                       'Consultare sempre il piano IARU aggiornato della propria regione.',
           ha='center', va='center', fontsize=9, style='italic', transform=ax.transAxes,
           bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    ax.set_title('Legenda Modi di Emissione - Piani Frequenze IARU', fontsize=14, fontweight='bold', pad=20)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'legenda_modi_emissione.png', dpi=150, bbox_inches='tight')
    plt.close()
    print(f"✓ Salvato: {OUTPUT_DIR / 'legenda_modi_emissione.png'}")


def plot_power_limits():
    """Tabella visuale potenze massime per banda (Italia)."""
    fig, ax = plt.subplots(figsize=(12, 10))

    # Dati potenze Italia (classe A)
    power_data = [
        ('160m', '1.830-1.850 kHz', 500, 'PNRF: solo 1830-1850'),
        ('80m', '3.5-3.8 MHz', 500, 'PNRF: secondario'),
        ('60m', '5.3515-5.3665 MHz', 15, 'Canalizzato'),
        ('40m', '7.0-7.2 MHz', 500, 'Si'),
        ('30m', '10.1-10.15 MHz', 500, 'No SSB'),
        ('20m', '14.0-14.35 MHz', 500, 'Si'),
        ('17m', '18.068-18.168 MHz', 500, 'Si'),
        ('15m', '21.0-21.45 MHz', 500, 'Si'),
        ('12m', '24.89-24.99 MHz', 500, 'Si'),
        ('10m', '28.0-29.7 MHz', 500, 'Si'),
        ('6m', '50.0-52.0 MHz', 500, 'Si'),
        ('2m', '144-146 MHz', 500, 'Si'),
        ('70cm', '430-440 MHz', 500, 'Si'),
        ('23cm', '1240-1300 MHz', 500, 'Si'),
    ]

    # Colori per livello potenza
    def get_power_color(power):
        if power >= 500:
            return '#90EE90'  # Verde chiaro
        elif power >= 100:
            return '#FFD700'  # Giallo
        else:
            return '#FFA07A'  # Arancione chiaro

    # Intestazioni
    headers = ['Banda', 'Frequenze', 'P.max (W)', 'Potenza', 'Note']
    col_widths = [0.1, 0.25, 0.12, 0.35, 0.15]
    x_positions = [0.02]
    for w in col_widths[:-1]:
        x_positions.append(x_positions[-1] + w)

    # Header
    y = 0.95
    for x, header, width in zip(x_positions, headers, col_widths):
        ax.text(x + width/2, y, header, ha='center', va='center', fontsize=11,
               fontweight='bold', transform=ax.transAxes)

    ax.plot([0.02, 0.98], [0.92, 0.92], color='black', linewidth=2, transform=ax.transAxes)

    # Dati
    row_height = 0.055
    for i, (band, freq, power, note) in enumerate(power_data):
        y = 0.88 - i * row_height

        # Sfondo alternato
        if i % 2 == 0:
            rect = Rectangle((0.02, y - row_height/2), 0.96, row_height,
                            facecolor='#f0f0f0', edgecolor='none', transform=ax.transAxes)
            ax.add_patch(rect)

        # Testi
        ax.text(x_positions[0] + col_widths[0]/2, y, band, ha='center', va='center',
               fontsize=10, fontweight='bold', transform=ax.transAxes)
        ax.text(x_positions[1] + col_widths[1]/2, y, freq, ha='center', va='center',
               fontsize=9, transform=ax.transAxes)
        ax.text(x_positions[2] + col_widths[2]/2, y, str(power), ha='center', va='center',
               fontsize=10, fontweight='bold', transform=ax.transAxes)

        # Barra potenza
        bar_width = (power / 500) * (col_widths[3] - 0.02)
        bar_rect = Rectangle((x_positions[3] + 0.01, y - 0.015), bar_width, 0.03,
                             facecolor=get_power_color(power), edgecolor='black',
                             linewidth=0.5, transform=ax.transAxes)
        ax.add_patch(bar_rect)

        ax.text(x_positions[4] + col_widths[4]/2, y, note, ha='center', va='center',
               fontsize=8, transform=ax.transAxes)

    # Legenda potenze
    legend_y = 0.08
    ax.text(0.15, legend_y, 'Legenda:', fontsize=10, fontweight='bold', transform=ax.transAxes)
    for color, label, x in [('#90EE90', '500W (Classe A)', 0.25),
                            ('#FFD700', '100-500W', 0.45),
                            ('#FFA07A', '<100W (limitato)', 0.65)]:
        rect = Rectangle((x, legend_y - 0.015), 0.03, 0.03, facecolor=color,
                         edgecolor='black', transform=ax.transAxes)
        ax.add_patch(rect)
        ax.text(x + 0.04, legend_y, label, fontsize=9, va='center', transform=ax.transAxes)

    # Nota
    ax.text(0.5, 0.02, 'Potenze riferite alla patente di classe A in Italia. '
                       'La classe B ha limiti inferiori su alcune bande.',
           ha='center', va='center', fontsize=8, style='italic', transform=ax.transAxes)

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    ax.set_title('Potenze Massime per Banda - Italia (Classe A)', fontsize=14, fontweight='bold', pad=20)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'potenze_massime_italia.png', dpi=150, bbox_inches='tight')
    plt.close()
    print(f"✓ Salvato: {OUTPUT_DIR / 'potenze_massime_italia.png'}")


def plot_bands_by_modulation():
    """Visualizzazione bande raggruppate per tipo di modulazione."""
    fig, ax = plt.subplots(figsize=(14, 10))

    # Raggruppamento per modulazione
    modulations = {
        'CW (A1A)\nTelegrafia': [
            ('160m', 1.810, 1.840),
            ('80m', 3.500, 3.570),
            ('40m', 7.000, 7.040),
            ('30m', 10.100, 10.130),
            ('20m', 14.000, 14.070),
            ('17m', 18.068, 18.095),
            ('15m', 21.000, 21.070),
            ('12m', 24.890, 24.915),
            ('10m', 28.000, 28.070),
            ('2m', 144.000, 144.150),
            ('70cm', 432.000, 432.100),
        ],
        'SSB (J3E)\nVoce': [
            ('160m', 1.840, 1.850),
            ('80m', 3.600, 3.800),
            ('40m', 7.060, 7.200),
            ('20m', 14.101, 14.350),
            ('17m', 18.111, 18.168),
            ('15m', 21.151, 21.450),
            ('12m', 24.931, 24.990),
            ('10m', 28.300, 29.100),
            ('2m', 144.150, 144.400),
            ('70cm', 432.100, 432.400),
        ],
        'FM (F3E)\nLocale/Ripetitori': [
            ('10m', 29.200, 29.700),
            ('6m', 51.400, 52.000),
            ('2m', 145.200, 145.800),
            ('70cm', 433.000, 434.600),
            ('23cm', 1297.000, 1298.000),
        ],
        'Digi\nFT8/RTTY/PSK': [
            ('80m', 3.570, 3.600),
            ('40m', 7.040, 7.060),
            ('30m', 10.130, 10.150),
            ('20m', 14.070, 14.099),
            ('17m', 18.095, 18.109),
            ('15m', 21.070, 21.149),
            ('12m', 24.915, 24.929),
            ('10m', 28.070, 28.190),
        ],
    }

    colors_mod = {
        'CW (A1A)\nTelegrafia': '#FF6B6B',
        'SSB (J3E)\nVoce': '#45B7D1',
        'FM (F3E)\nLocale/Ripetitori': '#96CEB4',
        'Digi\nFT8/RTTY/PSK': '#4ECDC4',
    }

    y_offset = 0
    for mod_name, segments in modulations.items():
        # Intestazione modulazione
        ax.add_patch(Rectangle((-1, y_offset - 0.3), 15, len(segments) * 0.5 + 0.6,
                              facecolor=colors_mod[mod_name], alpha=0.2, edgecolor='none'))
        ax.text(-0.8, y_offset + len(segments) * 0.25, mod_name, ha='left', va='center',
               fontsize=11, fontweight='bold')

        for i, (band, f_min, f_max) in enumerate(segments):
            y = y_offset + i * 0.5

            # Nome banda
            ax.text(1.5, y, band, ha='center', va='center', fontsize=10, fontweight='bold')

            # Barra frequenza
            bar_width = 8
            ax.add_patch(Rectangle((2.5, y - 0.15), bar_width, 0.3,
                                  facecolor=colors_mod[mod_name], edgecolor='black', linewidth=0.5))

            # Frequenze
            ax.text(2.5 + bar_width + 0.3, y, f'{f_min:.3f} - {f_max:.3f} MHz',
                   ha='left', va='center', fontsize=9)

        y_offset += len(segments) * 0.5 + 1

    ax.set_xlim(-1.5, 16)
    ax.set_ylim(-0.5, y_offset + 0.5)
    ax.axis('off')
    ax.set_title('Allocazione Frequenze per Tipo di Modulazione', fontsize=14, fontweight='bold', y=1.02)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'frequenze_per_modulazione.png', dpi=150, bbox_inches='tight')
    plt.close()
    print(f"✓ Salvato: {OUTPUT_DIR / 'frequenze_per_modulazione.png'}")


def plot_bands_by_application():
    """Visualizzazione bande raggruppate per applicazione - versione migliorata."""
    fig, ax = plt.subplots(figsize=(16, 18))

    applications = [
        ('DX (Lunga Distanza)', '#FFCCCC', [
            ('160m', '1.810-1.850 MHz', 'Propagazione notturna, DX difficile'),
            ('80m', '3.5-3.8 MHz', 'DX notturno, regionali'),
            ('40m', '7.0-7.2 MHz', 'DX 24h, ottima per inizio'),
            ('20m', '14.0-14.35 MHz', 'Banda DX per eccellenza'),
            ('17m', '18.068-18.168 MHz', 'DX diurno, meno affollata'),
            ('15m', '21.0-21.45 MHz', 'DX diurno, ciclo solare'),
            ('12m', '24.89-24.99 MHz', 'DX quando aperta'),
            ('10m', '28.0-29.7 MHz', 'DX ciclo solare alto'),
        ]),
        ('Comunicazioni Locali', '#CCFFCC', [
            ('2m FM', '145.2-145.8 MHz', 'Ripetitori, simplex locale'),
            ('70cm FM', '433.0-434.6 MHz', 'Ripetitori, simplex'),
            ('10m FM', '29.2-29.7 MHz', 'FM locale'),
            ('6m', '51.4-52.0 MHz', 'Locale e sporadic-E'),
        ]),
        ('Contest & Pile-up', '#CCCCFF', [
            ('CW 40m', '7.000-7.040 MHz', 'Contest CW'),
            ('CW 20m', '14.000-14.070 MHz', 'Contest CW principale'),
            ('SSB 40m', '7.060-7.200 MHz', 'Contest SSB'),
            ('SSB 20m', '14.150-14.350 MHz', 'Contest SSB principale'),
            ('SSB 15m', '21.200-21.450 MHz', 'Contest SSB'),
        ]),
        ('Modi Digitali (FT8/FT4)', '#FFFFCC', [
            ('FT8 40m', '7.074 MHz', 'Frequenza standard FT8'),
            ('FT8 20m', '14.074 MHz', 'FT8 piu attivo'),
            ('FT8 15m', '21.074 MHz', 'FT8 diurno'),
            ('FT8 10m', '28.074 MHz', 'FT8 quando aperta'),
            ('FT4 20m', '14.080 MHz', 'FT4 contest'),
        ]),
        ('Sperimentazione', '#FFCCFF', [
            ('EME 2m', '144.000-144.025 MHz', 'Riflessione lunare'),
            ('EME 70cm', '432.000-432.025 MHz', 'Moonbounce UHF'),
            ('Satellite', '145.8-146.0 MHz', 'Uplink satelliti'),
            ('Satellite', '435-438 MHz', 'Downlink satelliti'),
            ('Meteor Scatter', '144.360 MHz', 'MSK144'),
        ]),
        ('Emergenza/ARES', '#FFE5CC', [
            ('80m', '3.760 MHz', 'Emergenza Italia'),
            ('40m', '7.110 MHz', 'Emergenza IARU'),
            ('20m', '14.300 MHz', 'Emergenza globale'),
            ('2m', '145.500 MHz', 'Chiamata emergenza'),
        ]),
    ]

    # Titolo
    ax.text(0.5, 0.98, 'Frequenze per Applicazione', fontsize=20, fontweight='bold',
            ha='center', transform=ax.transAxes)
    ax.text(0.5, 0.955, 'Guida rapida per trovare la frequenza giusta', fontsize=12,
            ha='center', transform=ax.transAxes, color='gray')

    y = 0.92
    row_height = 0.022

    for app_name, color, bands in applications:
        # Header categoria
        header_height = 0.035
        ax.add_patch(Rectangle((0.02, y - header_height), 0.96, header_height,
                               facecolor=color, edgecolor='black', linewidth=1.5,
                               transform=ax.transAxes))
        ax.text(0.03, y - header_height/2, app_name, ha='left', va='center',
               fontsize=14, fontweight='bold', transform=ax.transAxes)

        y -= header_height + 0.005

        # Righe della tabella
        for i, (band, freq, desc) in enumerate(bands):
            bg_color = '#f8f9fa' if i % 2 == 0 else 'white'
            ax.add_patch(Rectangle((0.02, y - row_height), 0.96, row_height,
                                   facecolor=bg_color, edgecolor='#e0e0e0', linewidth=0.5,
                                   transform=ax.transAxes))

            # Colonne: Banda | Frequenza | Descrizione
            ax.text(0.05, y - row_height/2, band, ha='left', va='center',
                   fontsize=11, fontweight='bold', color='#2c3e50', transform=ax.transAxes)
            ax.text(0.25, y - row_height/2, freq, ha='left', va='center',
                   fontsize=11, family='monospace', color='#27ae60', transform=ax.transAxes)
            ax.text(0.48, y - row_height/2, desc, ha='left', va='center',
                   fontsize=10, color='#666', transform=ax.transAxes)

            y -= row_height

        y -= 0.02  # Spazio tra categorie

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'frequenze_per_applicazione.png', dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print(f"✓ Salvato: {OUTPUT_DIR / 'frequenze_per_applicazione.png'}")


def plot_regulatory_overview():
    """Panoramica normativa bande radioamatori Italia."""
    fig, ax = plt.subplots(figsize=(14, 10))

    # Dati normativi Italia
    regulatory_data = [
        {'band': '160m', 'freq': '1.830-1.850', 'status': 'Primario', 'power': '500W',
         'notes': 'PNRF: solo 1830-1850 primario', 'color': '#CCFFCC'},
        {'band': '80m', 'freq': '3.500-3.800', 'status': 'Secondario', 'power': '500W',
         'notes': 'PNRF: secondario in Italia', 'color': '#FFCCCC'},
        {'band': '60m', 'freq': '5.3515-5.3665', 'status': 'Secondario', 'power': '15W EIRP',
         'notes': 'Canalizzato, 5 canali', 'color': '#FFCCCC'},
        {'band': '40m', 'freq': '7.000-7.200', 'status': 'Primario', 'power': '500W',
         'notes': 'Banda primaria mondiale', 'color': '#CCFFCC'},
        {'band': '30m', 'freq': '10.100-10.150', 'status': 'Secondario', 'power': '500W',
         'notes': 'Solo CW e Digi, no fonia', 'color': '#FFFFCC'},
        {'band': '20m', 'freq': '14.000-14.350', 'status': 'Primario', 'power': '500W',
         'notes': 'Banda DX principale', 'color': '#CCFFCC'},
        {'band': '17m', 'freq': '18.068-18.168', 'status': 'Primario', 'power': '500W',
         'notes': 'Banda WARC', 'color': '#CCFFCC'},
        {'band': '15m', 'freq': '21.000-21.450', 'status': 'Primario', 'power': '500W',
         'notes': 'Ottima per DX diurno', 'color': '#CCFFCC'},
        {'band': '12m', 'freq': '24.890-24.990', 'status': 'Primario', 'power': '500W',
         'notes': 'Banda WARC', 'color': '#CCFFCC'},
        {'band': '10m', 'freq': '28.000-29.700', 'status': 'Primario', 'power': '500W',
         'notes': 'Propagazione sporadica', 'color': '#CCFFCC'},
        {'band': '6m', 'freq': '50.000-52.000', 'status': 'Secondario', 'power': '500W',
         'notes': '"Magic Band" - sporadic-E', 'color': '#FFCCCC'},
        {'band': '2m', 'freq': '144.000-146.000', 'status': 'Primario', 'power': '500W',
         'notes': 'VHF principale', 'color': '#CCFFCC'},
        {'band': '70cm', 'freq': '430.000-438.000', 'status': 'Misto', 'power': '500W',
         'notes': '430-434 sec, 435-436 pri, 436-438 sec', 'color': '#FFFFCC'},
        {'band': '23cm', 'freq': '1240-1300', 'status': 'Secondario', 'power': '500W',
         'notes': 'Condivisa GNSS', 'color': '#FFCCCC'},
    ]

    # Intestazioni
    headers = ['Banda', 'Frequenze (MHz)', 'Status', 'Potenza', 'Note']
    col_widths = [0.08, 0.18, 0.12, 0.1, 0.35]
    x_starts = [0.05]
    for w in col_widths[:-1]:
        x_starts.append(x_starts[-1] + w + 0.02)

    # Header
    y = 0.95
    for x, header, w in zip(x_starts, headers, col_widths):
        ax.text(x, y, header, ha='left', va='center', fontsize=11,
               fontweight='bold', transform=ax.transAxes)

    # Linea separatrice
    ax.plot([0.03, 0.97], [0.92, 0.92], color='black', linewidth=2, transform=ax.transAxes)

    # Dati
    row_height = 0.055
    for i, data in enumerate(regulatory_data):
        y = 0.88 - i * row_height

        # Sfondo colorato per status
        rect = Rectangle((0.03, y - row_height/2 + 0.005), 0.94, row_height - 0.01,
                         facecolor=data['color'], edgecolor='none', transform=ax.transAxes)
        ax.add_patch(rect)

        # Testi
        ax.text(x_starts[0], y, data['band'], ha='left', va='center', fontsize=10,
               fontweight='bold', transform=ax.transAxes)
        ax.text(x_starts[1], y, data['freq'], ha='left', va='center', fontsize=9,
               family='monospace', transform=ax.transAxes)
        ax.text(x_starts[2], y, data['status'], ha='left', va='center', fontsize=9,
               transform=ax.transAxes)
        ax.text(x_starts[3], y, data['power'], ha='left', va='center', fontsize=9,
               transform=ax.transAxes)
        ax.text(x_starts[4], y, data['notes'], ha='left', va='center', fontsize=8,
               transform=ax.transAxes)

    # Legenda status
    legend_y = 0.06
    ax.text(0.1, legend_y, 'Legenda Status:', fontsize=10, fontweight='bold', transform=ax.transAxes)
    for color, label, x in [('#CCFFCC', 'Primario', 0.28), ('#FFCCCC', 'Secondario', 0.45),
                            ('#FFFFCC', 'Limitazioni', 0.65)]:
        rect = Rectangle((x, legend_y - 0.015), 0.03, 0.03, facecolor=color,
                         edgecolor='black', transform=ax.transAxes)
        ax.add_patch(rect)
        ax.text(x + 0.04, legend_y, label, fontsize=9, va='center', transform=ax.transAxes)

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    ax.set_title('Panoramica Normativa Bande Radioamatori - Italia', fontsize=14, fontweight='bold', pad=15)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'panoramica_normativa_italia.png', dpi=150, bbox_inches='tight')
    plt.close()
    print(f"✓ Salvato: {OUTPUT_DIR / 'panoramica_normativa_italia.png'}")


def plot_digital_modes():
    """Panoramica completa modi digitali radioamatoriali - versione migliorata."""
    fig, ax = plt.subplots(figsize=(16, 20))

    # Categorie modi digitali - struttura lista per ordine
    digital_modes = [
        ('Modi Weak Signal', '#FFE5CC', [
            ('FT8', '#FF9F43', '7.074, 14.074, 21.074 MHz', 'WSJT-X, 15s cicli, -24dB SNR'),
            ('FT4', '#FFB976', '7.047.5, 14.080 MHz', 'FT8 veloce, 7.5s cicli'),
            ('JT65', '#FDA7DF', '14.076, 144.120 MHz', 'EME, segnali deboli'),
            ('WSPR', '#F8B739', '7.040.1, 14.097.1 MHz', 'Beacon propagazione'),
            ('JS8Call', '#A29BFE', '7.078, 14.078 MHz', 'QSO completi'),
        ]),
        ('Modi Telescriventi', '#CCE5FF', [
            ('RTTY', '#00CEC9', '7.040-7.050, 14.080-14.099 MHz', 'FSK 45.45 baud, contest'),
            ('PSK31', '#6C5CE7', '7.040, 14.070 MHz', 'Tastiera, bassa potenza'),
            ('Olivia', '#81ECEC', '14.072, 21.072 MHz', 'Robusto, multipath'),
            ('Hellschreiber', '#00B894', '14.063 MHz', 'Testo come immagine'),
        ]),
        ('Modi Immagine', '#E5CCFF', [
            ('SSTV', '#FD79A8', '14.230, 21.340 MHz', 'Immagini in 1-2 min'),
            ('FAX', '#E17055', '7.880, 14.230 MHz', 'Facsimile meteo'),
            ('ATV', '#E84393', '430-440, 1240-1300 MHz', 'Video tempo reale'),
        ]),
        ('Modi Dati/Packet', '#CCFFCC', [
            ('Packet', '#55E6C1', '144.800, 432.500 MHz', 'AX.25, BBS'),
            ('APRS', '#00B894', '144.800 MHz (EU)', 'GPS, meteo, messaggi'),
            ('Winlink', '#74B9FF', '7.083, 14.112 MHz', 'Email emergenza'),
        ]),
        ('Voce Digitale', '#E5F5FF', [
            ('D-STAR', '#0984E3', '145.670, 438.xxx MHz', 'Icom, rete mondiale'),
            ('DMR', '#6C5CE7', '430-440 MHz', 'Talkgroups mondiali'),
            ('C4FM', '#00CEC9', '144-146, 430-440 MHz', 'Yaesu Fusion'),
        ]),
        ('Modi Speciali', '#FFFFCC', [
            ('MSK144', '#FD79A8', '144.360 MHz', 'Meteor scatter'),
            ('Q65', '#A29BFE', '50.xxx, 144.xxx MHz', 'VHF/EME nuovo'),
            ('FreeDV', '#74B9FF', '14.236, 7.177 MHz', 'Voce open-source'),
        ]),
    ]

    # Titolo
    ax.text(0.5, 0.98, 'Panoramica Modi Digitali Radioamatoriali', fontsize=20, fontweight='bold',
            ha='center', transform=ax.transAxes)
    ax.text(0.5, 0.955, 'Frequenze tipiche e caratteristiche principali', fontsize=12,
            ha='center', transform=ax.transAxes, color='gray')

    y = 0.92
    row_height = 0.028
    header_height = 0.035

    for cat_name, cat_color, modes in digital_modes:
        # Header categoria
        ax.add_patch(Rectangle((0.02, y - header_height), 0.96, header_height,
                               facecolor=cat_color, edgecolor='black', linewidth=1.5,
                               transform=ax.transAxes))
        ax.text(0.03, y - header_height/2, cat_name, ha='left', va='center',
               fontsize=14, fontweight='bold', transform=ax.transAxes)

        y -= header_height + 0.005

        # Righe modi
        for i, (mode, color, freq, desc) in enumerate(modes):
            bg_color = '#f8f9fa' if i % 2 == 0 else 'white'
            ax.add_patch(Rectangle((0.02, y - row_height), 0.96, row_height,
                                   facecolor=bg_color, edgecolor='#e0e0e0', linewidth=0.5,
                                   transform=ax.transAxes))

            # Badge colorato modo
            ax.add_patch(Rectangle((0.03, y - row_height + 0.003), 0.08, row_height - 0.006,
                                   facecolor=color, edgecolor='white', linewidth=1,
                                   transform=ax.transAxes))
            ax.text(0.07, y - row_height/2, mode, ha='center', va='center',
                   fontsize=10, fontweight='bold', color='black', transform=ax.transAxes)

            # Frequenze
            ax.text(0.14, y - row_height/2, freq, ha='left', va='center',
                   fontsize=10, family='monospace', color='#27ae60', transform=ax.transAxes)

            # Descrizione
            ax.text(0.55, y - row_height/2, desc, ha='left', va='center',
                   fontsize=10, color='#555', transform=ax.transAxes)

            y -= row_height

        y -= 0.015  # Spazio tra categorie

    # Note
    ax.text(0.5, 0.02, 'WSJT-X: Software di Joe Taylor K1JT | Le frequenze sono indicative per IARU Reg. 1',
           ha='center', fontsize=9, style='italic', transform=ax.transAxes, color='gray')

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'modi_digitali_panoramica.png', dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print(f"✓ Salvato: {OUTPUT_DIR / 'modi_digitali_panoramica.png'}")


def plot_digital_frequencies():
    """Tabella frequenze standard modi digitali HF."""
    fig, ax = plt.subplots(figsize=(14, 12))

    # Frequenze standard modi digitali per banda HF
    digital_freqs = [
        # (Banda, FT8, FT4, RTTY, PSK, SSTV, WSPR, Note)
        ('160m', '1.840', '1.840', '1.838', '1.838', '-', '1.8366', 'Limitato'),
        ('80m', '3.573', '3.575', '3.580-3.600', '3.580', '3.730', '3.5686', 'Notte'),
        ('60m', '5.357', '-', '-', '-', '-', '5.2872', 'Canalizzato'),
        ('40m', '7.074', '7.047.5', '7.040-7.050', '7.040', '7.171', '7.0386', 'Molto attivo'),
        ('30m', '10.136', '10.140', '10.130-10.145', '10.142', '-', '10.1387', 'CW/Digi'),
        ('20m', '14.074', '14.080', '14.080-14.099', '14.070', '14.230', '14.0956', 'Principale'),
        ('17m', '18.100', '18.104', '18.100-18.105', '18.100', '18.163', '18.1046', 'WARC'),
        ('15m', '21.074', '21.140', '21.080-21.120', '21.070', '21.340', '21.0946', 'Diurno'),
        ('12m', '24.915', '24.919', '24.920-24.925', '24.920', '24.975', '24.9246', 'WARC'),
        ('10m', '28.074', '28.180', '28.080-28.150', '28.120', '28.680', '28.1246', 'Sporadico'),
    ]

    # Intestazioni
    headers = ['Banda', 'FT8', 'FT4', 'RTTY', 'PSK31', 'SSTV', 'WSPR', 'Note']
    col_colors = ['#FFE5CC', DIGITAL_COLORS['FT8'], DIGITAL_COLORS['FT4'],
                  DIGITAL_COLORS['RTTY'], DIGITAL_COLORS['PSK31'], DIGITAL_COLORS['SSTV'],
                  DIGITAL_COLORS['WSPR'], '#f0f0f0']

    col_widths = [0.08, 0.10, 0.10, 0.15, 0.10, 0.10, 0.10, 0.12]
    x_starts = [0.03]
    for w in col_widths[:-1]:
        x_starts.append(x_starts[-1] + w + 0.01)

    # Titolo
    ax.text(0.5, 0.97, 'Frequenze Standard Modi Digitali HF', fontsize=16, fontweight='bold',
            ha='center', transform=ax.transAxes)
    ax.text(0.5, 0.93, 'IARU Regione 1 - Frequenze in MHz', fontsize=11, ha='center',
            transform=ax.transAxes, color='gray')

    # Header row con colori
    y = 0.88
    for x, header, width, color in zip(x_starts, headers, col_widths, col_colors):
        rect = Rectangle((x, y - 0.02), width, 0.04, facecolor=color,
                         edgecolor='black', linewidth=1, transform=ax.transAxes)
        ax.add_patch(rect)
        ax.text(x + width/2, y, header, ha='center', va='center', fontsize=10,
               fontweight='bold', transform=ax.transAxes)

    # Dati
    row_height = 0.065
    for i, row in enumerate(digital_freqs):
        y = 0.82 - i * row_height

        # Sfondo alternato
        if i % 2 == 0:
            rect = Rectangle((0.02, y - row_height/2 + 0.005), 0.96, row_height - 0.01,
                            facecolor='#f8f9fa', edgecolor='none', transform=ax.transAxes)
            ax.add_patch(rect)

        for j, (x, val, width) in enumerate(zip(x_starts, row, col_widths)):
            fontweight = 'bold' if j == 0 else 'normal'
            fontsize = 10 if j == 0 else 9
            color = 'black' if val != '-' else '#ccc'
            ax.text(x + width/2, y, val, ha='center', va='center', fontsize=fontsize,
                   fontweight=fontweight, transform=ax.transAxes, color=color,
                   family='monospace' if j > 0 and j < 7 else None)

    # Legenda colori
    legend_y = 0.08
    ax.text(0.1, legend_y, 'Codice colori:', fontsize=10, fontweight='bold', transform=ax.transAxes)
    legend_items = [
        (DIGITAL_COLORS['FT8'], 'FT8 (Weak signal)'),
        (DIGITAL_COLORS['FT4'], 'FT4 (Contest)'),
        (DIGITAL_COLORS['RTTY'], 'RTTY'),
        (DIGITAL_COLORS['PSK31'], 'PSK31'),
        (DIGITAL_COLORS['SSTV'], 'SSTV'),
        (DIGITAL_COLORS['WSPR'], 'WSPR'),
    ]
    x_leg = 0.22
    for color, label in legend_items:
        rect = Rectangle((x_leg, legend_y - 0.012), 0.025, 0.024, facecolor=color,
                         edgecolor='black', transform=ax.transAxes)
        ax.add_patch(rect)
        ax.text(x_leg + 0.03, legend_y, label, fontsize=8, va='center', transform=ax.transAxes)
        x_leg += 0.13

    # Note
    ax.text(0.5, 0.02, 'WSPR: frequenze dial, la trasmissione avviene 1500 Hz sopra | '
                       'FT8/FT4: frequenze standard WSJT-X',
           ha='center', va='center', fontsize=8, style='italic', transform=ax.transAxes, color='gray')

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'frequenze_modi_digitali.png', dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print(f"✓ Salvato: {OUTPUT_DIR / 'frequenze_modi_digitali.png'}")


def main():
    """Genera tutte le visualizzazioni piani frequenze."""
    print("Generazione visualizzazioni piani frequenze IARU...")
    print(f"Directory output: {OUTPUT_DIR}\n")

    plot_hf_bands()
    plot_vhf_uhf_bands()
    plot_mode_legend()
    plot_power_limits()
    plot_bands_by_modulation()
    plot_bands_by_application()
    plot_regulatory_overview()
    plot_digital_modes()
    plot_digital_frequencies()

    print("\n✅ Tutte le visualizzazioni sono state generate con successo!")


if __name__ == "__main__":
    main()
