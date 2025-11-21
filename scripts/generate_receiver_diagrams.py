import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, ConnectionPatch

def create_directories():
    """Create necessary directories for Chapter 4 diagrams"""
    dirs = [
        'images/04_ricevitori'
    ]
    for dir_path in dirs:
        os.makedirs(dir_path, exist_ok=True)
        print(f"Directory {dir_path} pronta")

def draw_block_diagram(ax, blocks, connections, title):
    """Draw a block diagram with matplotlib"""
    ax.set_xlim(0, 15)
    ax.set_ylim(-2, 3)
    ax.axis('off')
    ax.set_title(title, fontsize=14, fontweight='bold', pad=20)

    # Draw blocks
    for block in blocks:
        x, y, w, h, label, color = block
        rect = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.1",
                             facecolor=color, edgecolor='black', linewidth=2)
        ax.add_patch(rect)
        ax.text(x + w/2, y + h/2, label, ha='center', va='center',
               fontsize=10, fontweight='bold')

    # Draw connections
    for conn in connections:
        x1, y1, x2, y2 = conn
        ax.arrow(x1, y1, x2-x1, y2-y1, head_width=0.1, head_length=0.1,
                fc='black', ec='black', length_includes_head=True)

def generate_receiver_diagrams():
    """Generate all receiver block diagrams for Chapter 4"""

    print("Generazione diagrammi ricevitori...")

    # 1. Superheterodyne Single Conversion
    fig, ax = plt.subplots(figsize=(15, 6))

    blocks = [
        (0.5, 0.5, 1.5, 1, 'Antenna\n📡', '#e6f3ff'),
        (2.5, 0.5, 1.5, 1, 'RF\nFilter\n🎛️', '#fff2e6'),
        (4.5, 0.5, 1.5, 1, 'RF\nAmp\n📈', '#e6ffe6'),
        (6.5, 0.5, 1.5, 1, 'Mixer\n🔄', '#ffe6e6'),
        (8.5, 0.5, 1.5, 1, 'IF\nFilter\n🎛️', '#fff2e6'),
        (10.5, 0.5, 1.5, 1, 'IF\nAmp\n📈', '#e6ffe6'),
        (12.5, 0.5, 1.5, 1, 'Detector\n🎯', '#ffffe6'),
        (2.5, 2, 1.5, 0.8, 'LO\n🔄', '#f0f0f0')
    ]

    connections = [
        (2, 1, 2.5, 1), (4, 1, 4.5, 1), (6, 1, 6.5, 1), (8, 1, 8.5, 1),
        (10, 1, 10.5, 1), (12, 1, 12.5, 1), (14, 1, 15, 1),
        (4, 2.4, 4, 1.5), (4, 1.5, 6.5, 1.5)
    ]

    draw_block_diagram(ax, blocks, connections, 'Ricevitore Supereterodina Semplice')
    plt.tight_layout()
    plt.savefig('images/04_ricevitori/superheterodyne_single.svg', dpi=150, bbox_inches='tight')
    plt.close()
    print("Superheterodyne single generato")

    # 2. Superheterodyne Double Conversion
    fig, ax = plt.subplots(figsize=(18, 6))

    blocks = [
        (0.5, 0.5, 1.2, 1, 'Antenna\n📡', '#e6f3ff'),
        (2.2, 0.5, 1.2, 1, 'RF\nFilter', '#fff2e6'),
        (3.9, 0.5, 1.2, 1, 'RF\nAmp', '#e6ffe6'),
        (5.6, 0.5, 1.2, 1, 'Mixer 1\n🔄', '#ffe6e6'),
        (7.3, 0.5, 1.2, 1, 'IF1\nFilter', '#fff2e6'),
        (9.0, 0.5, 1.2, 1, 'IF1\nAmp', '#e6ffe6'),
        (10.7, 0.5, 1.2, 1, 'Mixer 2\n🔄', '#ffe6e6'),
        (12.4, 0.5, 1.2, 1, 'IF2\nFilter', '#fff2e6'),
        (14.1, 0.5, 1.2, 1, 'IF2\nAmp', '#e6ffe6'),
        (15.8, 0.5, 1.2, 1, 'Detector\n🎯', '#ffffe6'),
        (2.2, 2, 1.2, 0.8, 'LO1\n🔄', '#f0f0f0'),
        (10.7, 2, 1.2, 0.8, 'LO2\n🔄', '#f0f0f0')
    ]

    connections = [
        (1.7, 1, 2.2, 1), (3.5, 1, 3.9, 1), (5.2, 1, 5.6, 1), (6.9, 1, 7.3, 1),
        (8.6, 1, 9.0, 1), (10.3, 1, 10.7, 1), (11.9, 1, 12.4, 1),
        (13.6, 1, 14.1, 1), (15.3, 1, 15.8, 1), (17.0, 1, 18, 1),
        (3.5, 2.4, 3.5, 1.5), (3.5, 1.5, 5.6, 1.5),
        (12.0, 2.4, 12.0, 1.5), (12.0, 1.5, 10.7, 1.5)
    ]

    draw_block_diagram(ax, blocks, connections, 'Ricevitore Supereterodina Doppia')
    plt.tight_layout()
    plt.savefig('images/04_ricevitori/superheterodyne_double.svg', dpi=150, bbox_inches='tight')
    plt.close()
    print("Superheterodyne double generato")

    # 3. AM Receiver Block Diagram
    fig, ax = plt.subplots(figsize=(16, 6))

    blocks = [
        (0.5, 0.5, 1.2, 1, 'Antenna\n📡', '#e6f3ff'),
        (2.2, 0.5, 1.2, 1, 'RF\nFilter', '#fff2e6'),
        (3.9, 0.5, 1.2, 1, 'RF\nAmp', '#e6ffe6'),
        (5.6, 0.5, 1.2, 1, 'Mixer\n🔄', '#ffe6e6'),
        (7.3, 0.5, 1.2, 1, 'IF\nFilter', '#fff2e6'),
        (9.0, 0.5, 1.2, 1, 'IF\nAmp', '#e6ffe6'),
        (10.7, 0.5, 1.2, 1, 'Limiter\n📏', '#ffcccc'),
        (12.4, 0.5, 1.2, 1, 'AM\nDetector\n🎯', '#ffffe6'),
        (14.1, 0.5, 1.2, 1, 'AGC\n📊', '#ccffcc'),
        (2.2, 2, 1.2, 0.8, 'LO\n🔄', '#f0f0f0'),
        (12.4, -1, 1.2, 0.8, 'S-Meter\n📊', '#e6e6ff')
    ]

    connections = [
        (1.7, 1, 2.2, 1), (3.5, 1, 3.9, 1), (5.2, 1, 5.6, 1), (6.9, 1, 7.3, 1),
        (8.6, 1, 9.0, 1), (10.3, 1, 10.7, 1), (11.9, 1, 12.4, 1),
        (13.6, 1, 14.1, 1), (15.3, 1, 16, 1),
        (3.5, 2.4, 3.5, 1.5), (3.5, 1.5, 5.6, 1.5),
        (13.0, 0, 13.0, -0.5), (13.0, -0.5, 12.4, -0.5)
    ]

    draw_block_diagram(ax, blocks, connections, 'Schema a Blocchi Ricevitore AM (A3E)')
    plt.tight_layout()
    plt.savefig('images/04_ricevitori/am_receiver_blocks.svg', dpi=150, bbox_inches='tight')
    plt.close()
    print("AM receiver blocks generato")

    # 4. SSB Receiver Block Diagram
    fig, ax = plt.subplots(figsize=(16, 6))

    blocks = [
        (0.5, 0.5, 1.2, 1, 'Antenna\n📡', '#e6f3ff'),
        (2.2, 0.5, 1.2, 1, 'RF\nFilter', '#fff2e6'),
        (3.9, 0.5, 1.2, 1, 'RF\nAmp', '#e6ffe6'),
        (5.6, 0.5, 1.2, 1, 'Mixer\n🔄', '#ffe6e6'),
        (7.3, 0.5, 1.2, 1, 'IF\nFilter', '#fff2e6'),
        (9.0, 0.5, 1.2, 1, 'IF\nAmp', '#e6ffe6'),
        (10.7, 0.5, 1.2, 1, 'SSB\nFilter\n🎛️', '#ffcccc'),
        (12.4, 0.5, 1.2, 1, 'Product\nDetector\n🔄', '#ffffe6'),
        (14.1, 0.5, 1.2, 1, 'AF\nFilter', '#fff2e6'),
        (2.2, 2, 1.2, 0.8, 'LO\n🔄', '#f0f0f0'),
        (10.7, 2, 1.2, 0.8, 'BFO\n±1.5kHz\n🔄', '#f0f0f0')
    ]

    connections = [
        (1.7, 1, 2.2, 1), (3.5, 1, 3.9, 1), (5.2, 1, 5.6, 1), (6.9, 1, 7.3, 1),
        (8.6, 1, 9.0, 1), (10.3, 1, 10.7, 1), (11.9, 1, 12.4, 1),
        (13.6, 1, 14.1, 1), (15.3, 1, 16, 1),
        (3.5, 2.4, 3.5, 1.5), (3.5, 1.5, 5.6, 1.5),
        (12.0, 2.4, 12.0, 1.5), (12.0, 1.5, 10.7, 1.5)
    ]

    draw_block_diagram(ax, blocks, connections, 'Schema a Blocchi Ricevitore SSB (J3E)')
    plt.tight_layout()
    plt.savefig('images/04_ricevitori/ssb_receiver_blocks.svg', dpi=150, bbox_inches='tight')
    plt.close()
    print("SSB receiver blocks generato")

    # 5. CW Receiver with BFO
    fig, ax = plt.subplots(figsize=(14, 6))

    blocks = [
        (0.5, 0.5, 1.2, 1, 'Antenna\n📡', '#e6f3ff'),
        (2.2, 0.5, 1.2, 1, 'RF\nFilter', '#fff2e6'),
        (3.9, 0.5, 1.2, 1, 'RF\nAmp', '#e6ffe6'),
        (5.6, 0.5, 1.2, 1, 'Mixer\n🔄', '#ffe6e6'),
        (7.3, 0.5, 1.2, 1, 'IF\nFilter', '#fff2e6'),
        (9.0, 0.5, 1.2, 1, 'IF\nAmp', '#e6ffe6'),
        (10.7, 0.5, 1.2, 1, 'BFO\nMixer\n🔄', '#ffffe6'),
        (12.4, 0.5, 1.2, 1, 'AF\nFilter', '#fff2e6'),
        (2.2, 2, 1.2, 0.8, 'LO\n🔄', '#f0f0f0'),
        (7.3, 2, 1.2, 0.8, 'BFO\n±800Hz\n🔄', '#f0f0f0')
    ]

    connections = [
        (1.7, 1, 2.2, 1), (3.5, 1, 3.9, 1), (5.2, 1, 5.6, 1), (6.9, 1, 7.3, 1),
        (8.6, 1, 9.0, 1), (10.3, 1, 10.7, 1), (11.9, 1, 12.4, 1), (13.6, 1, 14, 1),
        (3.5, 2.4, 3.5, 1.5), (3.5, 1.5, 5.6, 1.5),
        (8.6, 2.4, 8.6, 1.5), (8.6, 1.5, 7.3, 1.5)
    ]

    draw_block_diagram(ax, blocks, connections, 'Schema a Blocchi Ricevitore CW (A1A) con BFO')
    plt.tight_layout()
    plt.savefig('images/04_ricevitori/cw_receiver_blocks.svg', dpi=150, bbox_inches='tight')
    plt.close()
    print("CW receiver blocks generato")

    print("Tutti i diagrammi ricevitori generati con successo!")

if __name__ == "__main__":
    create_directories()
    generate_receiver_diagrams()