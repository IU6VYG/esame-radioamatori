#!/usr/bin/env python3
"""
Generazione diagrammi sicurezza elettrica.
Curva IEC, messa a terra, differenziale, scaricatore antenna.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Rectangle, Circle, FancyArrowPatch, Polygon
import numpy as np
from pathlib import Path

# Directory di output
OUTPUT_DIR = Path(__file__).parent.parent / "images" / "10_protezione"
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


def plot_curva_iec():
    """Curva IEC 60479-1 effetti fisiologici corrente vs tempo."""
    fig, ax = plt.subplots(figsize=(12, 9))

    # Scale logaritmiche
    ax.set_xscale('log')
    ax.set_yscale('log')

    # Zone IEC (approssimate)
    # AC-1: Nessuna reazione
    t_ac1 = np.array([10, 10000])
    i_ac1 = np.array([0.5, 0.5])

    # AC-2: Nessun effetto fisiologico pericoloso
    t_ac2 = np.array([10, 10000])
    i_ac2_low = np.array([0.5, 0.5])
    i_ac2_high = np.array([10, 10])

    # AC-3: Effetti reversibili
    t_ac3 = np.logspace(1, 4, 50)
    i_ac3_low = np.ones_like(t_ac3) * 10
    i_ac3_high = 500 / np.sqrt(t_ac3 / 10)
    i_ac3_high = np.clip(i_ac3_high, 30, 500)

    # AC-4: Fibrillazione ventricolare possibile
    # Limiti c1, c2, c3 della curva IEC
    t_c1 = np.array([10, 30, 100, 300, 1000, 3000, 10000])
    i_c1 = np.array([500, 300, 150, 90, 50, 35, 30])

    t_c2 = np.array([10, 30, 100, 300, 1000, 3000, 10000])
    i_c2 = np.array([1000, 500, 250, 130, 80, 50, 40])

    t_c3 = np.array([10, 30, 100, 300, 1000, 3000, 10000])
    i_c3 = np.array([2000, 1000, 500, 250, 150, 80, 60])

    # Riempi le zone
    ax.fill_between([10, 10000], 0.1, 0.5, color='green', alpha=0.3, label='AC-1: Percezione')
    ax.fill_between([10, 10000], 0.5, 10, color='yellow', alpha=0.3, label='AC-2: Reazioni muscolari')
    ax.fill_betweenx([30, 500], 10, 10000, color='orange', alpha=0.2)

    # Curve limite
    ax.plot(t_c1, i_c1, 'r-', linewidth=2.5, label='c1: Fibrillazione 0%')
    ax.plot(t_c2, i_c2, 'r--', linewidth=2, label='c2: Fibrillazione 5%')
    ax.plot(t_c3, i_c3, 'r:', linewidth=2, label='c3: Fibrillazione 50%')

    # Linea soglia percezione
    ax.axhline(y=0.5, color='green', linestyle='-', linewidth=2, label='Soglia percezione')

    # Linea soglia "let-go"
    ax.axhline(y=10, color='orange', linestyle='-', linewidth=2, label='Soglia "let-go"')

    # Zone
    ax.text(100, 0.25, 'AC-1\nNessuna reazione', ha='center', fontsize=10, color='darkgreen')
    ax.text(100, 3, 'AC-2\nEffetti non pericolosi', ha='center', fontsize=10, color='olive')
    ax.text(100, 50, 'AC-3\nEffetti reversibili', ha='center', fontsize=10, color='darkorange')
    ax.text(1000, 200, 'AC-4\nFibrillazione\nventricolare', ha='center', fontsize=10, color='darkred')

    # Punti di riferimento
    ax.plot([100], [30], 'ko', markersize=10)
    ax.annotate('Soglia fibrillazione\n(100ms, 30mA)', xy=(100, 30), xytext=(300, 100),
                arrowprops=dict(arrowstyle='->', color='black'),
                fontsize=9, ha='center')

    ax.set_xlabel('Tempo di esposizione (ms)', fontsize=12)
    ax.set_ylabel('Corrente attraverso il corpo (mA)', fontsize=12)
    ax.set_title('Curva IEC 60479-1: Effetti della Corrente sul Corpo Umano\n(Corrente Alternata 50/60 Hz, percorso mano-mano)',
                 fontsize=13, fontweight='bold')

    ax.set_xlim(10, 10000)
    ax.set_ylim(0.1, 5000)
    ax.grid(True, which='both', linestyle='--', alpha=0.5)
    ax.legend(loc='upper right', fontsize=9)

    # Note
    note_box = dict(boxstyle='round', facecolor='lightyellow', alpha=0.9)
    ax.text(15, 0.15, 'Note:\n• Corrente AC 50/60 Hz più pericolosa di DC\n• Resistenza corpo: 1000-5000Ω (pelle umida)\n• Percorso mano-piedi più pericoloso',
            fontsize=8, va='bottom', bbox=note_box)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'curva_iec_corrente.png', dpi=150, bbox_inches='tight')
    plt.close()
    print(f"✓ Salvato: {OUTPUT_DIR / 'curva_iec_corrente.png'}")


def schema_messa_terra():
    """Schema impianto messa a terra stazione radioamatore."""
    fig, ax = plt.subplots(figsize=(14, 10))

    # Edificio
    ax.add_patch(Rectangle((1, 2), 8, 6, fill=True, facecolor='lightyellow',
                            edgecolor='black', linewidth=2))
    ax.text(5, 7.5, 'Stazione Radioamatore', ha='center', fontsize=12, fontweight='bold')

    # Quadro elettrico
    draw_block(ax, 2, 6.5, 1.8, 1, 'Quadro\nElettrico', 'lightgray')

    # Trasformatore/Alimentatore
    draw_block(ax, 4.5, 6.5, 1.8, 1, 'Alimentatore\n13.8V', 'lightblue')

    # Radio
    draw_block(ax, 7, 6.5, 1.5, 1, 'Radio\nTX/RX', 'lightgreen')

    # Lineare
    draw_block(ax, 7, 4.5, 1.5, 1, 'Amplif.\nLineare', 'lightsalmon')

    # Barra equipotenziale
    ax.plot([1.5, 8.5], [3, 3], 'g-', linewidth=6)
    ax.text(5, 3.4, 'Barra Equipotenziale di Terra', ha='center', fontsize=10, fontweight='bold', color='darkgreen')

    # Connessioni a barra equipotenziale
    ax.plot([2, 2], [6, 3], 'g-', linewidth=2)  # Quadro
    ax.plot([4.5, 4.5], [6, 3], 'g-', linewidth=2)  # Alimentatore
    ax.plot([7, 7], [6, 3], 'g-', linewidth=2)  # Radio
    ax.plot([7, 7], [4, 3], 'g-', linewidth=2)  # Lineare

    # Antenna e traliccio
    ax.plot([11, 11], [0, 8], 'k-', linewidth=4)  # Traliccio
    ax.text(11, 8.5, 'Traliccio', ha='center', fontsize=10)

    # Dipolo stilizzato
    ax.plot([10, 12], [7.5, 7.5], 'k-', linewidth=3)
    ax.plot([9.5, 10], [7.7, 7.5], 'k-', linewidth=2)
    ax.plot([12, 12.5], [7.5, 7.7], 'k-', linewidth=2)
    ax.text(11, 8, 'Antenna', ha='center', fontsize=9)

    # Cavo coassiale
    ax.plot([8.5, 10.5], [6.5, 6.5], 'b-', linewidth=2)
    ax.plot([10.5, 10.5], [6.5, 7.5], 'b-', linewidth=2)
    ax.text(9.5, 6.8, 'Coax', ha='center', fontsize=8, color='blue')

    # Scaricatore
    draw_block(ax, 10.5, 5.5, 1, 0.8, 'Scaric.', 'plum', fontsize=8)
    ax.plot([10.5, 10.5], [6, 6.5], 'b-', linewidth=2)
    ax.plot([10.5, 10.5], [5, 3], 'g-', linewidth=2)

    # Terra traliccio
    ax.plot([11, 11], [0, 0], 'g-', linewidth=3)
    ax.plot([11, 11], [0, -0.5], 'g-', linewidth=3)

    # Picchetti di terra
    picchetti_x = [3, 5, 7, 11]
    for x in picchetti_x:
        # Picchetto
        ax.add_patch(Rectangle((x-0.15, -1.5), 0.3, 1.5, facecolor='brown', edgecolor='black'))
        ax.plot([x, x], [0, -0.3], 'g-', linewidth=2)

    # Conduttore di terra
    ax.plot([1.5, 11.5], [0, 0], 'g-', linewidth=4)
    ax.text(6.5, 0.3, 'Conduttore di Terra (Cu 16mm²)', ha='center', fontsize=9, color='darkgreen')

    # Collegamento da barra a conduttore
    ax.plot([5, 5], [3, 0], 'g-', linewidth=3)

    # Terreno
    ax.fill_between([0, 13], -2, 0, color='saddlebrown', alpha=0.3)
    ax.plot([0, 13], [0, 0], 'k-', linewidth=1)
    ax.text(1, -1, 'Terreno', fontsize=9, color='brown')

    # Simboli terra
    for x in picchetti_x:
        ax.plot([x-0.3, x+0.3], [-1.7, -1.7], 'k-', linewidth=1)
        ax.plot([x-0.2, x+0.2], [-1.85, -1.85], 'k-', linewidth=1)
        ax.plot([x-0.1, x+0.1], [-2, -2], 'k-', linewidth=1)

    # Legenda
    legend_box = dict(boxstyle='round', facecolor='white', alpha=0.9)
    ax.text(0.5, 9, 'Componenti chiave:\n'
                    '• Barra equipotenziale: collega tutte le masse\n'
                    '• Picchetti: dispersione nel terreno\n'
                    '• Scaricatore: protegge da sovratensioni\n'
                    '• Resistenza terra: < 10Ω',
            fontsize=9, va='top', bbox=legend_box)

    ax.set_title('Schema Impianto di Messa a Terra - Stazione Radioamatore', fontsize=14, fontweight='bold', pad=15)
    ax.set_xlim(0, 13)
    ax.set_ylim(-2.5, 10)
    ax.set_aspect('equal')
    ax.axis('off')

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'schema_messa_terra.png', dpi=150, bbox_inches='tight')
    plt.close()
    print(f"✓ Salvato: {OUTPUT_DIR / 'schema_messa_terra.png'}")


def schema_differenziale():
    """Schema principio funzionamento interruttore differenziale."""
    fig, ax = plt.subplots(figsize=(14, 10))

    # Titolo
    ax.text(7, 9.5, 'Principio di Funzionamento - Interruttore Differenziale (ID)',
            ha='center', fontsize=14, fontweight='bold')

    # === PARTE SINISTRA: Funzionamento normale ===
    ax.text(3.5, 8.5, 'Funzionamento Normale', ha='center', fontsize=11, fontweight='bold', color='green')

    # Linee L e N
    ax.plot([1, 6], [7, 7], 'r-', linewidth=2, label='Fase (L)')  # Fase
    ax.plot([1, 6], [5, 5], 'b-', linewidth=2, label='Neutro (N)')  # Neutro
    ax.text(0.5, 7, 'L', ha='center', fontsize=10, color='red')
    ax.text(0.5, 5, 'N', ha='center', fontsize=10, color='blue')

    # Toroide (nucleo ferromagnetico)
    circle1 = Circle((3.5, 6), 0.8, fill=False, edgecolor='orange', linewidth=3)
    ax.add_patch(circle1)
    ax.text(3.5, 6, 'Toroide', ha='center', fontsize=8)

    # Avvolgimento differenziale
    ax.plot([3.5, 3.5], [6.8, 7.5], 'orange', linewidth=2)
    ax.plot([3.5, 4.5], [7.5, 7.5], 'orange', linewidth=2)
    draw_block(ax, 4.5, 7.5, 0.8, 0.5, 'Relè', 'lightyellow', fontsize=7)

    # Carico
    draw_block(ax, 6, 6, 1.2, 1.5, 'Carico\n(R)', 'lightgreen')
    ax.plot([6, 6], [6.75, 7], 'r-', linewidth=2)
    ax.plot([6, 6], [5.25, 5], 'b-', linewidth=2)

    # Frecce corrente (uguali)
    ax.annotate('', xy=(2.5, 7.3), xytext=(1.5, 7.3),
                arrowprops=dict(arrowstyle='->', color='red', lw=2))
    ax.text(2, 7.6, 'I₁', fontsize=10, color='red')
    ax.annotate('', xy=(1.5, 4.7), xytext=(2.5, 4.7),
                arrowprops=dict(arrowstyle='->', color='blue', lw=2))
    ax.text(2, 4.3, 'I₂', fontsize=10, color='blue')

    # Formula
    ax.text(3.5, 4, 'I₁ = I₂ → ΣΦ = 0\nNessun intervento', ha='center', fontsize=9,
            bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.8))

    # === PARTE DESTRA: Guasto a terra ===
    ax.text(10.5, 8.5, 'Guasto a Terra', ha='center', fontsize=11, fontweight='bold', color='red')

    # Linee L e N
    ax.plot([8, 13], [7, 7], 'r-', linewidth=2)  # Fase
    ax.plot([8, 13], [5, 5], 'b-', linewidth=2)  # Neutro
    ax.text(7.5, 7, 'L', ha='center', fontsize=10, color='red')
    ax.text(7.5, 5, 'N', ha='center', fontsize=10, color='blue')

    # Toroide
    circle2 = Circle((10.5, 6), 0.8, fill=False, edgecolor='orange', linewidth=3)
    ax.add_patch(circle2)

    # Avvolgimento + relè (scattato)
    ax.plot([10.5, 10.5], [6.8, 7.5], 'orange', linewidth=2)
    ax.plot([10.5, 11.5], [7.5, 7.5], 'orange', linewidth=2)
    draw_block(ax, 11.5, 7.5, 0.8, 0.5, 'Relè', 'lightsalmon', fontsize=7)

    # Carico con guasto
    draw_block(ax, 13, 6, 1.2, 1.5, 'Carico\n(guasto)', 'lightcoral')
    ax.plot([13, 13], [6.75, 7], 'r-', linewidth=2)
    ax.plot([13, 13], [5.25, 5], 'b-', linewidth=2)

    # Corrente di dispersione verso terra
    ax.plot([12.5, 12.5], [6, 3.5], 'g-', linewidth=2)
    ax.annotate('', xy=(12.5, 3.5), xytext=(12.5, 5),
                arrowprops=dict(arrowstyle='->', color='green', lw=2))
    ax.text(13, 4.2, 'I_guasto', fontsize=9, color='green')

    # Simbolo terra
    ax.plot([12.2, 12.8], [3.5, 3.5], 'k-', linewidth=2)
    ax.plot([12.3, 12.7], [3.3, 3.3], 'k-', linewidth=1.5)
    ax.plot([12.4, 12.6], [3.1, 3.1], 'k-', linewidth=1)
    ax.text(12.5, 2.8, 'Terra', ha='center', fontsize=8)

    # Frecce corrente (diverse!)
    ax.annotate('', xy=(9.5, 7.3), xytext=(8.5, 7.3),
                arrowprops=dict(arrowstyle='->', color='red', lw=2))
    ax.text(9, 7.6, 'I₁', fontsize=10, color='red')
    ax.annotate('', xy=(8.5, 4.7), xytext=(9.5, 4.7),
                arrowprops=dict(arrowstyle='->', color='blue', lw=2))
    ax.text(9, 4.3, 'I₂ < I₁', fontsize=10, color='blue')

    # Formula guasto
    ax.text(10.5, 4, 'I₁ ≠ I₂ → ΣΦ ≠ 0\nINTERVENTO!', ha='center', fontsize=9,
            bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.8))

    # Persona (stilizzata) che tocca il guasto
    # Testa
    ax.add_patch(Circle((11.5, 5), 0.3, facecolor='peachpuff', edgecolor='black'))
    # Corpo
    ax.plot([11.5, 11.5], [4.7, 3.8], 'k-', linewidth=2)
    # Braccia
    ax.plot([11.5, 12.3], [4.5, 5.5], 'k-', linewidth=2)
    ax.plot([11.5, 10.8], [4.5, 4.2], 'k-', linewidth=2)
    # Gambe
    ax.plot([11.5, 11.2], [3.8, 3], 'k-', linewidth=2)
    ax.plot([11.5, 11.8], [3.8, 3], 'k-', linewidth=2)

    # Nota esplicativa
    note_box = dict(boxstyle='round', facecolor='lightyellow', alpha=0.9)
    ax.text(7, 1.5, 'L\'interruttore differenziale confronta la corrente entrante (I₁) con quella uscente (I₂).\n'
                    'Se la differenza supera la soglia (tipicamente 30mA), il relè sgancia il circuito\n'
                    'in meno di 30ms, proteggendo da contatti diretti e indiretti.',
            ha='center', fontsize=10, bbox=note_box)

    # Specifiche tipiche
    specs_box = dict(boxstyle='round', facecolor='lightblue', alpha=0.9)
    ax.text(1, 2.5, 'Tipi di ID:\n• 30mA: protezione persone\n• 300mA: protezione incendio\n• Classe AC/A/B: tipo corrente',
            fontsize=9, va='top', bbox=specs_box)

    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.set_aspect('equal')
    ax.axis('off')

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'schema_differenziale.png', dpi=150, bbox_inches='tight')
    plt.close()
    print(f"✓ Salvato: {OUTPUT_DIR / 'schema_differenziale.png'}")


def schema_scaricatore():
    """Schema scaricatore antenna (gas discharge tube)."""
    fig, ax = plt.subplots(figsize=(14, 9))

    # Titolo
    ax.text(7, 8.5, 'Scaricatore per Protezione Antenna (Gas Discharge Tube)',
            ha='center', fontsize=14, fontweight='bold')

    # Antenna
    ax.plot([2, 2], [6, 8], 'k-', linewidth=3)
    ax.plot([1, 3], [8, 8], 'k-', linewidth=3)
    ax.plot([0.5, 1], [8.2, 8], 'k-', linewidth=2)
    ax.plot([3, 3.5], [8, 8.2], 'k-', linewidth=2)
    ax.text(2, 8.5, 'Antenna', ha='center', fontsize=10)

    # Cavo coassiale in entrata
    ax.plot([2, 2], [6, 5], 'b-', linewidth=3)
    ax.text(2.5, 5.5, 'Coax', fontsize=9, color='blue')

    # Scaricatore (dettagliato)
    ax.add_patch(Rectangle((1, 2), 2, 3, fill=True, facecolor='lightgray',
                            edgecolor='black', linewidth=2))
    ax.text(2, 4.5, 'Scaricatore', ha='center', fontsize=10, fontweight='bold')

    # Interno scaricatore
    # Connettore ingresso (N/SO-239)
    ax.add_patch(Circle((2, 4.8), 0.2, facecolor='silver', edgecolor='black'))
    ax.text(2, 5.2, 'IN', ha='center', fontsize=8)

    # Gas discharge tube simbolico
    ax.add_patch(Rectangle((1.5, 3.2), 1, 0.8, fill=True, facecolor='lightyellow',
                            edgecolor='orange', linewidth=2))
    ax.text(2, 3.6, 'GDT', ha='center', fontsize=9, fontweight='bold')

    # Elettrodi
    ax.plot([1.7, 1.7], [3.2, 2.8], 'k-', linewidth=3)
    ax.plot([2.3, 2.3], [3.2, 2.8], 'k-', linewidth=3)

    # Gap simbolico
    ax.plot([1.9, 2.1], [3.5, 3.5], 'orange', linewidth=2)

    # Connettore uscita
    ax.add_patch(Circle((2, 2.2), 0.2, facecolor='silver', edgecolor='black'))
    ax.text(2, 1.8, 'OUT', ha='center', fontsize=8)

    # Collegamento a terra
    ax.plot([0.8, 0.8], [3.5, 1], 'g-', linewidth=3)
    ax.plot([0.5, 1.1], [1, 1], 'k-', linewidth=2)
    ax.plot([0.6, 1], [0.8, 0.8], 'k-', linewidth=1.5)
    ax.plot([0.7, 0.9], [0.6, 0.6], 'k-', linewidth=1)
    ax.text(0.8, 0.3, 'Terra', ha='center', fontsize=9)

    # Freccia verso terra dal GDT
    ax.plot([1.5, 0.8], [3.5, 3.5], 'g-', linewidth=2)

    # Cavo verso radio
    ax.plot([2, 2], [2, 1], 'b-', linewidth=3)
    ax.plot([2, 5], [1, 1], 'b-', linewidth=3)

    # Radio
    draw_block(ax, 6, 1, 1.5, 1.2, 'Radio\nTX/RX', 'lightgreen')
    ax.plot([5, 5.2], [1, 1], 'b-', linewidth=3)

    # === Diagramma funzionamento ===
    ax.text(10, 7.5, 'Principio di Funzionamento', ha='center', fontsize=11, fontweight='bold')

    # Stato normale
    ax.add_patch(Rectangle((8, 5.5), 4, 1.5, fill=True, facecolor='lightgreen',
                            edgecolor='black', linewidth=1.5))
    ax.text(10, 6.5, 'Stato Normale', ha='center', fontsize=10, fontweight='bold')
    ax.text(10, 5.8, 'Gas isolante - Segnale RF passa', ha='center', fontsize=9)

    # Stato sovratensione
    ax.add_patch(Rectangle((8, 3.5), 4, 1.5, fill=True, facecolor='lightsalmon',
                            edgecolor='black', linewidth=1.5))
    ax.text(10, 4.5, 'Sovratensione/Fulmine', ha='center', fontsize=10, fontweight='bold')
    ax.text(10, 3.8, 'Gas ionizzato - Scarica a terra', ha='center', fontsize=9)

    # Freccia fulmine
    ax.annotate('', xy=(5, 7), xytext=(4, 8),
                arrowprops=dict(arrowstyle='->', color='yellow', lw=4))
    ax.text(4.5, 7.8, 'Fulmine', fontsize=9, color='darkorange', fontweight='bold')

    # Caratteristiche tecniche
    specs_box = dict(boxstyle='round', facecolor='lightyellow', alpha=0.9)
    ax.text(10, 2, 'Caratteristiche tipiche:\n'
                   '• Tensione innesco: 75-90V DC\n'
                   '• Corrente di scarica: 5-20 kA\n'
                   '• Tempo risposta: < 1 μs\n'
                   '• Frequenza: DC - 2.5 GHz\n'
                   '• Connettori: N, SO-239, BNC',
            ha='center', fontsize=9, va='top', bbox=specs_box)

    # Note installazione
    install_box = dict(boxstyle='round', facecolor='lightblue', alpha=0.9)
    ax.text(5, 4, 'Installazione:\n'
                  '• Montare vicino\n  all\'ingresso antenna\n'
                  '• Terra corta e robusta\n'
                  '• Proteggere anche\n  linee di controllo',
            ha='left', fontsize=9, va='top', bbox=install_box)

    ax.set_xlim(-0.5, 13)
    ax.set_ylim(-0.5, 9)
    ax.set_aspect('equal')
    ax.axis('off')

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'schema_scaricatore.png', dpi=150, bbox_inches='tight')
    plt.close()
    print(f"✓ Salvato: {OUTPUT_DIR / 'schema_scaricatore.png'}")


def main():
    """Genera tutti i diagrammi di sicurezza elettrica."""
    print("Generazione diagrammi sicurezza elettrica...")
    print(f"Directory output: {OUTPUT_DIR}\n")

    plot_curva_iec()
    schema_messa_terra()
    schema_differenziale()
    schema_scaricatore()

    print("\n✅ Tutti i diagrammi sono stati generati con successo!")


if __name__ == "__main__":
    main()
