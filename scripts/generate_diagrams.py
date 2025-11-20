import schemdraw
import schemdraw.elements as elm
import matplotlib.pyplot as plt
import numpy as np
import os

# Ensure images directory exists
os.makedirs('images', exist_ok=True)

def generate_transformer():
    print("Generating Transformer diagram...")
    with schemdraw.Drawing(file='images/grafico_trasformatore.svg', show=False) as d:
        d.config(fontsize=12)
        
        # Primary side
        d += elm.SourceSin().up().label('Vp', loc='bottom')
        d += elm.Line().right().length(1)
        trans = elm.Transformer().right().anchor('p1').label('Avvolgimento\nPrimario', loc='bottom', ofst=1).label('Avvolgimento\nSecondario', loc='bottom', ofst=1, halign='left')
        d += trans
        
        # Secondary side
        d += elm.Line().right().at(trans.s1).length(1)
        d += elm.Resistor().down().label('Carico')
        d += elm.Line().left().to(trans.s2)
        
        # Labels for currents/voltages: draw the figure then add text via the figure API
        d.draw(show=False)
        # schemdraw Figure.text expects signature text(s, x, y, ...)
        d.fig.text('Ip ->', 0.5, 0, color='blue', halign='left', valign='center')
        d.fig.text('-> Is', 5.5, 0, color='blue', halign='right', valign='center')
        d.fig.text('Tensione\nIngresso', 0, 2, halign='right', valign='center')
        d.fig.text('Tensione\nUscita', 6, 2, halign='left', valign='center')

def generate_transistor_amp():
    print("Generating Transistor Amplifier diagram...")
    with schemdraw.Drawing(file='images/grafico_transistor_amplificatore.svg', show=False) as d:
        d.config(fontsize=12)
        
        # Power rails
        d += elm.Line().right().length(6).label('Vcc', loc='right')
        
        # Voltage divider
        d += elm.Resistor().down().at((2, 0)).label('R1')
        base_node = d.here
        d += elm.Resistor().down().label('R2')
        d += elm.Ground()
        
        # Input
        d += elm.Capacitor().left().at(base_node).label('Cin')
        d += elm.SourceSin().down().label('Vin\n(Segnale Ingresso)')
        d += elm.Ground()
        
        # Transistor
        t = elm.BjtNpn().right().at(base_node).anchor('base').label('Q1')
        d += t
        # Try to obtain emitter/collector pin coordinates from the element instance.
        # Different schemdraw versions expose pins with different attribute names,
        # so try several common ones and fall back to the current drawing position.
        emitter_node = getattr(t, 'emitter', None) or getattr(t, 'E', None) or getattr(t, 'e', None) or d.here
        collector_node = getattr(t, 'collector', None) or getattr(t, 'C', None) or getattr(t, 'c', None) or d.here
        
        # Emitter
        d += elm.Resistor().down().at(emitter_node).label('Re')
        d += elm.Ground()
        # Emitter bypass capacitor
        d += elm.Line().right().at(emitter_node).length(1)
        d += elm.Capacitor().down().label('Ce')
        d += elm.Ground()
        
        # Collector
        d += elm.Resistor().up().at(collector_node).to((collector_node[0], 0)).label('Rc')
        
        # Output
        d += elm.Capacitor().right().at(collector_node).label('Cout')
        d += elm.Resistor().down().label('RL')
        d += elm.Ground()
        d += elm.Line().right().at(collector_node).length(0.5).label('Vout\n(Segnale Uscita)', loc='right')

def generate_diode_curve():
    print("Generating Diode I-V Curve...")
    plt.figure(figsize=(8, 6))
    
    # Data
    v = np.linspace(-2, 1, 500)
    i = np.zeros_like(v)
    
    # Shockley diode equation approximation
    is_sat = 1e-9  # Saturation current
    vt = 0.026     # Thermal voltage
    n = 1.5        # Ideality factor
    
    # Forward bias
    mask_fwd = v > 0
    i[mask_fwd] = is_sat * (np.exp(v[mask_fwd] / (n * vt)) - 1)
    
    # Reverse breakdown (simplified)
    v_breakdown = -1.5
    mask_rev = v < v_breakdown
    i[mask_rev] = -1e-3 * (np.exp(-(v[mask_rev] - v_breakdown) * 10)) 

    # Plot
    plt.plot(v, i * 1000, 'b-', linewidth=2) # Current in mA
    
    # Styling
    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(0, color='black', linewidth=1)
    plt.grid(True, which='both', linestyle='--', alpha=0.7)
    
    plt.title('Curva Caratteristica I-V del Diodo', fontsize=14)
    plt.xlabel('Tensione (V)', fontsize=12)
    plt.ylabel('Corrente (mA)', fontsize=12)
    
    # Annotations
    plt.annotate('Polarizzazione\nDiretta', xy=(0.7, 5), xytext=(0.2, 10),
                 arrowprops={'facecolor': 'black', 'shrink': 0.05})
    plt.annotate('Soglia ~0.7V', xy=(0.7, 0), xytext=(0.8, -5),
                 arrowprops={'facecolor': 'black', 'shrink': 0.05})
    plt.annotate('Polarizzazione\nInversa', xy=(-1, 0), xytext=(-1.5, 5),
                 arrowprops={'facecolor': 'black', 'shrink': 0.05})
    
    plt.ylim(-10, 20)
    plt.xlim(-2, 1)
    
    plt.savefig('images/grafico_curva_diodo.svg')
    plt.close()

def generate_capacitor_charge():
    print("Generating Capacitor Charge Curve...")
    plt.figure(figsize=(8, 6))
    
    # Data
    t = np.linspace(0, 5, 500) # Time in units of tau
    v_max = 10
    v = v_max * (1 - np.exp(-t))
    
    # Plot
    plt.plot(t, v, 'b-', linewidth=2)
    
    # Styling
    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(0, color='black', linewidth=1)
    plt.grid(True, which='both', linestyle='--', alpha=0.7)
    plt.axhline(v_max, color='r', linestyle='--', label='Vmax')
    
    plt.title('Curva di Carica Esponenziale', fontsize=14)
    plt.xlabel('Tempo (t / τ)', fontsize=12)
    plt.ylabel('Tensione (V)', fontsize=12)
    
    # Tau marker
    tau_val = v_max * 0.632
    plt.plot([1, 1], [0, tau_val], 'g--')
    plt.plot([0, 1], [tau_val, tau_val], 'g--')
    plt.plot(1, tau_val, 'go')
    
    plt.annotate('63.2% Vmax\n(1 Costante di tempo)', xy=(1, tau_val), xytext=(1.5, tau_val - 2),
                 arrowprops=dict(facecolor='black', shrink=0.05))
    
    plt.xticks([0, 1, 2, 3, 4, 5], ['0', 'τ', '2τ', '3τ', '4τ', '5τ'])
    plt.legend()
    
    plt.savefig('images/grafico_carica_condensatore.svg')
    plt.close()

if __name__ == "__main__":
    generate_transformer()
    generate_transistor_amp()
    generate_diode_curve()
    generate_capacitor_charge()
    print("All diagrams generated successfully.")
