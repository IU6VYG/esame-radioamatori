#!/usr/bin/env python3
"""
Script per generare diagrammi di oscillatori per il Capitolo 3 (versione minimale)
"""

import schemdraw
import schemdraw.elements as elm
import os

def setup_output_directory():
    """Crea la directory images se non esiste"""
    if not os.path.exists('../images'):
        os.makedirs('../images')
    print("Directory images pronta")

def draw_basic_oscillators():
    """Disegna oscillatori base senza riferimenti complessi"""
    
    # Oscillatore LC base
    d1 = schemdraw.Drawing(unit=3)
    d1 += elm.SourceV().label('V_cc')
    d1 += elm.Resistor().label('R_c').right()
    d1 += elm.BjtNpn().label('Q1').right()
    d1 += elm.Capacitor().label('C').down()
    d1 += elm.Ground()
    d1 += elm.Line().right()
    d1 += elm.Label('Output')
    d1 += elm.Resistor().label('R_L').down()
    d1 += elm.Ground()
    d1 += elm.Line().down()
    d1 += elm.Inductor().label('L').right()
    d1 += elm.Ground()
    d1.save('../images/oscillatore_lc_base.svg')
    
    # Oscillatore a quarzo
    d2 = schemdraw.Drawing(unit=3)
    d2 += elm.SourceV().label('V_in')
    d2 += elm.Resistor().label('R_f').right()
    d2 += elm.Ic().label('XTAL').right()
    d2 += elm.Capacitor().label('C1').down()
    d2 += elm.Ground()
    d2 += elm.Line().right()
    d2 += elm.Label('Output')
    d2 += elm.Resistor().label('R_L').down()
    d2 += elm.Ground()
    d2.save('../images/oscillatore_quarzo_base.svg')
    
    # VCO base
    d3 = schemdraw.Drawing(unit=3)
    d3 += elm.SourceV().label('V_control')
    d3 += elm.Varactor().label('D_v').right()
    d3 += elm.Inductor().label('L').right()
    d3 += elm.Capacitor().label('C').down()
    d3 += elm.Ground()
    d3 += elm.Line().right()
    d3 += elm.Label('VCO Output')
    d3 += elm.Resistor().label('R_L').down()
    d3 += elm.Ground()
    d3.save('../images/oscillatore_vco_base.svg')
    
    print("Oscillatori base generati")

def draw_resonant_circuits():
    """Disegna circuiti risonanti"""
    
    # Circuito LC risonante
    d1 = schemdraw.Drawing(unit=3)
    d1 += elm.Inductor().label('L').right()
    d1 += elm.Capacitor().label('C').down()
    d1 += elm.Ground()
    d1 += elm.Line().right()
    d1 += elm.Label('f₀ = 1/(2π√LC)')
    d1 += elm.Resistor().label('R').down()
    d1 += elm.Ground()
    d1.save('../images/circuito_risonante_lc.svg')
    
    # Circuito cristallo
    d2 = schemdraw.Drawing(unit=3)
    d2 += elm.Capacitor().label('C_p').right()
    d2 += elm.Inductor().label('L_m').right()
    d2 += elm.Capacitor().label('C_m').down()
    d2 += elm.Ground()
    d2 += elm.Resistor().label('R_m').right()
    d2 += elm.Line().down()
    d2 += elm.Line().left()
    d2 += elm.Label('f₀ = 1/(2π√L_mC_m)')
    d2.save('../images/circuito_cristallo.svg')
    
    print("Circuiti risonanti generati")

def main():
    """Funzione principale che genera tutti i diagrammi di oscillatori"""
    print("Inizio generazione diagrammi di oscillatori...")
    
    setup_output_directory()
    draw_basic_oscillators()
    draw_resonant_circuits()
    
    print("Tutti i diagrammi di oscillatori sono stati generati con successo!")

if __name__ == "__main__":
    main()