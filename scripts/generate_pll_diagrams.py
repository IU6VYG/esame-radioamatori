#!/usr/bin/env python3
"""
Generazione diagrammi PLL (Phase-Locked Loop) semplificati e didattici.
Schema a blocchi con annotazioni flusso segnale e valori tipici.
"""

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle
import numpy as np
from pathlib import Path

from utils import get_output_dir, run_with_error_handling, COLORS_BLOCK_DIAGRAM


# Directory di output
OUTPUT_DIR = get_output_dir('03_circuiti')

# Configurazione stile
plt.rcParams['font.size'] = 10
plt.rcParams['axes.titlesize'] = 12
plt.rcParams['figure.facecolor'] = 'white'


def plot_pll_basic():
    """Schema PLL base semplificato con annotazioni didattiche."""
    fig, ax = plt.subplots(figsize=(14, 9))
    ax.set_facecolor('#f0f9ff')

    # Titolo
    ax.text(0.5, 0.94, 'PLL - Phase-Locked Loop', fontsize=18, fontweight='bold',
            ha='center', transform=ax.transAxes, color='#1e40af')
    ax.text(0.5, 0.89, 'Anello ad aggancio di fase - Schema base', fontsize=11,
            ha='center', transform=ax.transAxes, color='#4a5568')

    colors = {
        'input': '#dbeafe',
        'detector': '#fecaca',
        'filter': '#fef08a',
        'vco': '#bbf7d0',
        'divider': '#ddd6fe',
        'border': '#374151',
        'shadow': '#94a3b8',
    }

    block_w = 0.14
    block_h = 0.10

    def draw_block(x, y, label, sublabel, color):
        shadow = FancyBboxPatch((x - block_w/2 + 0.003, y - block_h/2 - 0.003),
                                block_w, block_h, boxstyle="round,pad=0.008,rounding_size=0.015",
                                facecolor=colors['shadow'], edgecolor='none', zorder=1)
        ax.add_patch(shadow)
        rect = FancyBboxPatch((x - block_w/2, y - block_h/2), block_w, block_h,
                              boxstyle="round,pad=0.008,rounding_size=0.015",
                              facecolor=color, edgecolor=colors['border'], linewidth=2, zorder=2)
        ax.add_patch(rect)
        ax.text(x, y + 0.02, label, ha='center', va='center', fontsize=10,
                fontweight='bold', color='#1e293b', zorder=3)
        ax.text(x, y - 0.025, sublabel, ha='center', va='center', fontsize=8,
                color='#475569', zorder=3)

    # Posizioni
    y_main = 0.55
    y_fb = 0.28

    x_ref = 0.12
    x_pd = 0.32
    x_lf = 0.52
    x_vco = 0.72
    x_out = 0.88
    x_div = 0.52

    # Ingresso riferimento
    ax.text(x_ref - 0.06, y_main, 'f_ref', fontsize=11, ha='center', va='center',
            fontweight='bold', color='#1e40af')
    ax.annotate('', xy=(x_pd - block_w/2 - 0.01, y_main), xytext=(x_ref, y_main),
                arrowprops=dict(arrowstyle='-|>', color='#3b82f6', lw=2.5, mutation_scale=15))

    # Blocchi principali
    draw_block(x_pd, y_main, 'RIVELATORE', 'di Fase (PD)', colors['detector'])
    draw_block(x_lf, y_main, 'FILTRO', 'di Anello (LF)', colors['filter'])
    draw_block(x_vco, y_main, 'VCO', 'Osc. Controllato', colors['vco'])

    # Frecce catena principale
    for x1, x2 in [(x_pd, x_lf), (x_lf, x_vco)]:
        ax.annotate('', xy=(x2 - block_w/2 - 0.01, y_main), xytext=(x1 + block_w/2 + 0.01, y_main),
                    arrowprops=dict(arrowstyle='-|>', color='#22c55e', lw=2, mutation_scale=12))

    # Uscita
    ax.annotate('', xy=(x_out, y_main), xytext=(x_vco + block_w/2 + 0.01, y_main),
                arrowprops=dict(arrowstyle='-|>', color='#22c55e', lw=2.5, mutation_scale=15))
    ax.text(x_out + 0.04, y_main, 'f_out', fontsize=11, ha='center', va='center',
            fontweight='bold', color='#166534')

    # Divisore di frequenza (feedback)
    draw_block(x_div, y_fb, 'DIVISORE', ':N', colors['divider'])

    # Linee feedback
    ax.plot([x_vco, x_vco], [y_main - block_h/2 - 0.01, y_fb + 0.06], color='#8b5cf6', lw=2)
    ax.plot([x_vco, x_div + block_w/2 + 0.01], [y_fb + 0.06, y_fb + 0.06], color='#8b5cf6', lw=2)
    ax.annotate('', xy=(x_div + block_w/2 + 0.01, y_fb), xytext=(x_div + block_w/2 + 0.01, y_fb + 0.06),
                arrowprops=dict(arrowstyle='-|>', color='#8b5cf6', lw=2, mutation_scale=12))

    ax.plot([x_div - block_w/2 - 0.01, x_pd - 0.02], [y_fb, y_fb], color='#8b5cf6', lw=2)
    ax.plot([x_pd - 0.02, x_pd - 0.02], [y_fb, y_main - block_h/2 - 0.01], color='#8b5cf6', lw=2)
    ax.annotate('', xy=(x_pd - 0.02, y_main - block_h/2 - 0.01), xytext=(x_pd - 0.02, y_fb),
                arrowprops=dict(arrowstyle='-|>', color='#8b5cf6', lw=2, mutation_scale=12))

    # Annotazioni segnali
    signals = [
        (x_pd + 0.08, y_main + 0.08, 'Errore fase', '#dc2626'),
        (x_lf + 0.08, y_main + 0.08, 'V_ctrl', '#ca8a04'),
        (x_div, y_fb - 0.07, 'f_out / N', '#7c3aed'),
    ]
    for x, y, text, color in signals:
        ax.text(x, y, text, fontsize=8, ha='center', fontweight='bold', color=color,
                bbox=dict(boxstyle='round,pad=0.2', facecolor='white', edgecolor=color, alpha=0.9))

    # Box formula
    formula = 'Formula: f_out = N x f_ref\nEsempio: N=100, f_ref=10kHz -> f_out=1MHz'
    ax.text(0.15, 0.75, formula, fontsize=9, ha='left', va='center',
            color='#1e40af', linespacing=1.5,
            bbox=dict(boxstyle='round,pad=0.5', facecolor='white', edgecolor='#3b82f6', linewidth=2))

    # Box vantaggi
    vantaggi = 'Vantaggi PLL:\n- Stabilita del quarzo\n- Frequenza variabile\n- Basso rumore di fase'
    ax.text(0.85, 0.28, vantaggi, fontsize=8, ha='center', va='center',
            color='#166534', linespacing=1.4,
            bbox=dict(boxstyle='round,pad=0.4', facecolor='white', edgecolor='#22c55e', linewidth=1.5))

    # Legenda
    legend_items = [
        (colors['detector'], 'Rivelatore'),
        (colors['filter'], 'Filtro'),
        (colors['vco'], 'VCO'),
        (colors['divider'], 'Divisore'),
    ]
    ax.text(0.30, 0.12, 'Legenda:', fontsize=9, fontweight='bold', va='center')
    x_leg = 0.38
    for color, label in legend_items:
        ax.add_patch(Rectangle((x_leg, 0.108), 0.02, 0.025, facecolor=color, edgecolor='#374151', linewidth=1))
        ax.text(x_leg + 0.025, 0.12, label, fontsize=8, va='center')
        x_leg += 0.12

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

    plt.savefig(OUTPUT_DIR / 'pll_schema_base.png', dpi=150, bbox_inches='tight',
                facecolor='#f0f9ff', edgecolor='none')
    plt.close()
    print("[OK] Salvato: pll_schema_base.png")


def plot_pll_synthesizer():
    """Schema sintetizzatore di frequenza con PLL."""
    fig, ax = plt.subplots(figsize=(14, 8))
    ax.set_facecolor('#fef3c7')

    ax.text(0.5, 0.94, 'Sintetizzatore di Frequenza', fontsize=18, fontweight='bold',
            ha='center', transform=ax.transAxes, color='#92400e')
    ax.text(0.5, 0.89, 'Applicazione tipica PLL per ricetrasmettitori', fontsize=11,
            ha='center', transform=ax.transAxes, color='#4a5568')

    colors = {
        'xtal': '#dbeafe',
        'pll': '#bbf7d0',
        'vco': '#fecaca',
        'mix': '#ddd6fe',
        'border': '#374151',
        'shadow': '#94a3b8',
    }

    block_w = 0.12
    block_h = 0.09

    def draw_block(x, y, label, sublabel, color, w=None):
        w = w or block_w
        shadow = FancyBboxPatch((x - w/2 + 0.002, y - block_h/2 - 0.002),
                                w, block_h, boxstyle="round,pad=0.006,rounding_size=0.012",
                                facecolor=colors['shadow'], edgecolor='none', zorder=1)
        ax.add_patch(shadow)
        rect = FancyBboxPatch((x - w/2, y - block_h/2), w, block_h,
                              boxstyle="round,pad=0.006,rounding_size=0.012",
                              facecolor=color, edgecolor=colors['border'], linewidth=1.5, zorder=2)
        ax.add_patch(rect)
        ax.text(x, y + 0.018, label, ha='center', va='center', fontsize=9,
                fontweight='bold', color='#1e293b', zorder=3)
        ax.text(x, y - 0.018, sublabel, ha='center', va='center', fontsize=7,
                color='#475569', zorder=3)

    y_main = 0.55
    y_pll = 0.30

    # Blocchi
    draw_block(0.12, y_main, 'XTAL', '10 MHz', colors['xtal'])
    draw_block(0.30, y_main, 'PLL 1', 'x10', colors['pll'])
    draw_block(0.50, y_main, 'VCO', '90-110 MHz', colors['vco'], w=0.14)
    draw_block(0.70, y_main, 'MIXER', 'Upconv.', colors['mix'])
    draw_block(0.88, y_main, 'OUT', '144 MHz', colors['pll'])

    # PLL programmabile
    draw_block(0.50, y_pll, 'PLL 2', 'Programm.', colors['pll'])
    draw_block(0.30, y_pll, 'uC', 'Controllo', colors['xtal'])

    # Frecce
    for x1, x2 in [(0.12, 0.30), (0.30, 0.50), (0.50, 0.70), (0.70, 0.88)]:
        ax.annotate('', xy=(x2 - block_w/2 - 0.01, y_main), xytext=(x1 + block_w/2 + 0.01, y_main),
                    arrowprops=dict(arrowstyle='-|>', color='#22c55e', lw=2, mutation_scale=12))

    # Feedback PLL2
    ax.plot([0.50, 0.50], [y_main - block_h/2 - 0.01, y_pll + block_h/2 + 0.01], color='#8b5cf6', lw=1.5)
    ax.annotate('', xy=(0.30 + block_w/2 + 0.01, y_pll), xytext=(0.50 - block_w/2 - 0.01, y_pll),
                arrowprops=dict(arrowstyle='<|-', color='#ef4444', lw=1.5, mutation_scale=10))

    # Frequenze
    freqs = [
        (0.12, y_main + 0.07, '10 MHz'),
        (0.30, y_main + 0.07, '100 MHz'),
        (0.50, y_main + 0.07, '90-110 MHz'),
        (0.88, y_main + 0.07, '144 MHz'),
    ]
    for x, y, text in freqs:
        ax.text(x, y, text, fontsize=8, ha='center', fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.15', facecolor='#dcfce7', edgecolor='#16a34a', linewidth=0.8))

    # Info box
    info = 'Sintesi indiretta:\nVCO controllato da PLL\nRisoluzione = f_ref / N\nTipico: 1-10 kHz step'
    ax.text(0.15, 0.72, info, fontsize=8, ha='left', va='center',
            color='#92400e', linespacing=1.4,
            bbox=dict(boxstyle='round,pad=0.4', facecolor='white', edgecolor='#d97706', linewidth=1.5))

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

    plt.savefig(OUTPUT_DIR / 'pll_sintetizzatore.png', dpi=150, bbox_inches='tight',
                facecolor='#fef3c7', edgecolor='none')
    plt.close()
    print("[OK] Salvato: pll_sintetizzatore.png")


def plot_vco_detail():
    """Schema VCO con varactor e valori tipici."""
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.set_facecolor('#f0fdf4')

    ax.text(0.5, 0.94, 'VCO - Oscillatore Controllato in Tensione', fontsize=16, fontweight='bold',
            ha='center', transform=ax.transAxes, color='#166534')
    ax.text(0.5, 0.89, 'Con diodo varactor per variazione frequenza', fontsize=10,
            ha='center', transform=ax.transAxes, color='#4a5568')

    colors = {
        'input': '#dbeafe',
        'varactor': '#fecaca',
        'lc': '#fef08a',
        'output': '#bbf7d0',
        'border': '#374151',
    }

    # Schema semplificato VCO
    y_main = 0.50

    # V_ctrl input
    ax.text(0.08, y_main, 'V_ctrl', fontsize=11, fontweight='bold', color='#1e40af')
    ax.text(0.08, y_main - 0.06, '0-10V', fontsize=9, color='#64748b')

    # Freccia input
    ax.annotate('', xy=(0.20, y_main), xytext=(0.12, y_main),
                arrowprops=dict(arrowstyle='-|>', color='#3b82f6', lw=2, mutation_scale=12))

    # Varactor block
    rect = FancyBboxPatch((0.20, y_main - 0.06), 0.15, 0.12,
                          boxstyle="round,pad=0.01", facecolor=colors['varactor'],
                          edgecolor=colors['border'], linewidth=1.5)
    ax.add_patch(rect)
    ax.text(0.275, y_main + 0.02, 'VARACTOR', fontsize=9, fontweight='bold', ha='center')
    ax.text(0.275, y_main - 0.025, 'C = f(V)', fontsize=8, ha='center', color='#475569')

    # LC tank
    rect2 = FancyBboxPatch((0.42, y_main - 0.06), 0.15, 0.12,
                           boxstyle="round,pad=0.01", facecolor=colors['lc'],
                           edgecolor=colors['border'], linewidth=1.5)
    ax.add_patch(rect2)
    ax.text(0.495, y_main + 0.02, 'TANK LC', fontsize=9, fontweight='bold', ha='center')
    ax.text(0.495, y_main - 0.025, 'Risonanza', fontsize=8, ha='center', color='#475569')

    # Amplificatore
    rect3 = FancyBboxPatch((0.64, y_main - 0.06), 0.15, 0.12,
                           boxstyle="round,pad=0.01", facecolor=colors['output'],
                           edgecolor=colors['border'], linewidth=1.5)
    ax.add_patch(rect3)
    ax.text(0.715, y_main + 0.02, 'AMPLIF.', fontsize=9, fontweight='bold', ha='center')
    ax.text(0.715, y_main - 0.025, 'Buffer', fontsize=8, ha='center', color='#475569')

    # Frecce
    ax.annotate('', xy=(0.42, y_main), xytext=(0.35, y_main),
                arrowprops=dict(arrowstyle='-|>', color='#22c55e', lw=2, mutation_scale=12))
    ax.annotate('', xy=(0.64, y_main), xytext=(0.57, y_main),
                arrowprops=dict(arrowstyle='-|>', color='#22c55e', lw=2, mutation_scale=12))
    ax.annotate('', xy=(0.88, y_main), xytext=(0.79, y_main),
                arrowprops=dict(arrowstyle='-|>', color='#22c55e', lw=2, mutation_scale=12))

    # Output
    ax.text(0.92, y_main, 'f_out', fontsize=11, fontweight='bold', color='#166534')

    # Valori tipici box
    valori = 'Valori tipici VHF:\nL = 100 nH\nC_var = 5-20 pF\nf = 100-150 MHz\nK_vco = 10 MHz/V'
    ax.text(0.20, 0.25, valori, fontsize=9, ha='left', va='center',
            color='#166534', linespacing=1.4,
            bbox=dict(boxstyle='round,pad=0.5', facecolor='white', edgecolor='#22c55e', linewidth=2))

    # Formula
    formula = 'Frequenza:\nf = 1 / (2pi x sqrt(L x C))\n\nVariazione:\nDelta_f = K_vco x Delta_V'
    ax.text(0.70, 0.25, formula, fontsize=9, ha='center', va='center',
            color='#1e40af', linespacing=1.4,
            bbox=dict(boxstyle='round,pad=0.5', facecolor='white', edgecolor='#3b82f6', linewidth=2))

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

    plt.savefig(OUTPUT_DIR / 'vco_dettaglio.png', dpi=150, bbox_inches='tight',
                facecolor='#f0fdf4', edgecolor='none')
    plt.close()
    print("[OK] Salvato: vco_dettaglio.png")


def main():
    """Genera tutti i diagrammi PLL semplificati."""
    print(f"Generazione diagrammi PLL in: {OUTPUT_DIR}\n")

    plot_pll_basic()
    plot_pll_synthesizer()
    plot_vco_detail()

    print(f"\nTutti i diagrammi PLL salvati in: {OUTPUT_DIR}")


if __name__ == "__main__":
    exit(run_with_error_handling(main, "generate_pll_diagrams"))
