#!/usr/bin/env python3
"""
Script per generare diagrammi di PLL per il Capitolo 3 (versione corretta)
"""

import schemdraw
import schemdraw.elements as elm
import os

def setup_output_directory():
    """Crea la directory images se non esiste"""
    if not os.path.exists('../images'):
        os.makedirs('../images')
    print("Directory images pronta")

def draw_simple_pll():
    """Disegna PLL base senza riferimenti complessi"""
    
    # PLL base
    d1 = schemdraw.Drawing(unit=3)
    d1 += elm.SourceSin().label('Reference')
    d1 += elm.Ic().label('Phase Detector').right()
    d1 += elm.Ic().label('Loop Filter').right()
    d1 += elm.Ic().label('VCO').right()
    d1 += elm.Label('RF Output')
    d1 += elm.Ic().label('Frequency Divider').down()
    d1 += elm.Line().left()
    d1 += elm.Line().down()
    d1 += elm.Ground()
    d1.save('../images/pll_base.svg')
    
    # PLL con VCO
    d2 = schemdraw.Drawing(unit=3)
    d2 += elm.SourceSin().label('Reference')
    d2 += elm.Ic().label('Phase Detector').right()
    d2 += elm.Ic().label('Loop Filter').right()
    d2 += elm.SourceV().label('V_control').down()
    d2 += elm.Ground()
    d2 += elm.Ic().label('VCO').right()
    d2 += elm.Label('RF Output')
    d2 += elm.Ic().label('Frequency Divider').down()
    d2 += elm.Line().left()
    d2 += elm.Line().down()
    d2 += elm.Ground()
    d2.save('../images/pll_vco.svg')
    
    print("PLL base generati")

def draw_pll_components():
    """Disegna componenti individuali del PLL"""
    
    # Phase detector (usando op-amp come moltiplicatore)
    d1 = schemdraw.Drawing(unit=3)
    d1 += elm.SourceSin().label('Reference')
    d1 += elm.Capacitor().label('C_in').right()
    d1 += elm.Opamp().label('Mixer').right()
    d1 += elm.SourceSin().label('VCO Feedback').down()
    d1 += elm.Ground()
    d1 += elm.Capacitor().label('C_out').right()
    d1 += elm.Label('Error Output')
    d1 += elm.Resistor().label('R_out').down()
    d1 += elm.Ground()
    d1.save('../images/phase_detector_pll.svg')
    
    # VCO base
    d2 = schemdraw.Drawing(unit=3)
    d2 += elm.SourceV().label('V_control')
    d2 += elm.Varactor().label('D_v').right()
    d2 += elm.Inductor().label('L').right()
    d2 += elm.Capacitor().label('C').down()
    d2 += elm.Ground()
    d2 += elm.Line().right()
    d2 += elm.Label('VCO Output')
    d2 += elm.Resistor().label('R_L').down()
    d2 += elm.Ground()
    d2.save('../images/vco_pll.svg')
    
    # Loop filter
    d3 = schemdraw.Drawing(unit=3)
    d3 += elm.SourceSin().label('Error Input')
    d3 += elm.Resistor().label('R1').right()
    d3 += elm.Capacitor().label('C1').down()
    d3 += elm.Ground()
    d3 += elm.Resistor().label('R2').right()
    d3 += elm.Capacitor().label('C2').down()
    d3 += elm.Ground()
    d3 += elm.Line().right()
    d3 += elm.Label('Control Output')
    d3 += elm.Resistor().label('R_out').down()
    d3 += elm.Ground()
    d3.save('../images/loop_filter_pll.svg')
    
    print("Componenti PLL generati")

def draw_pll_applications():
    """Disegna applicazioni PLL"""
    
    # Sintetizzatore con PLL
    d1 = schemdraw.Drawing(unit=3)
    d1 += elm.SourceSin().label('Reference')
    d1 += elm.Ic().label('Reference PLL').right()
    d1 += elm.Label('Base Frequency')
    d1 += elm.Ic().label('RF Synthesizer').right()
    d1 += elm.Label('RF Output')
    d1 += elm.Ic().label('IF PLL').right()
    d1 += elm.Label('IF Output')
    d1 += elm.Ic().label('Baseband PLL').right()
    d1 += elm.Label('Baseband Output')
    d1.save('../images/sintetizzatore_pll.svg')
    
    # Clock generator
    d2 = schemdraw.Drawing(unit=3)
    d2 += elm.SourceSin().label('Reference')
    d2 += elm.Ic().label('Clock PLL').right()
    d2 += elm.Label('System Clock')
    d2 += elm.Ic().label('CPU Clock').right()
    d2 += elm.Label('CPU Clock')
    d2 += elm.Ic().label('Memory Clock').right()
    d2 += elm.Label('Memory Clock')
    d2 += elm.Ic().label('Peripheral Clock').right()
    d2 += elm.Label('Peripheral Clock')
    d2.save('../images/clock_generator_pll.svg')
    
    print("Applicazioni PLL generate")

def main():
    """Funzione principale che genera tutti i diagrammi di PLL"""
    print("Inizio generazione diagrammi di PLL...")
    
    setup_output_directory()
    draw_simple_pll()
    draw_pll_components()
    draw_pll_applications()
    
    print("Tutti i diagrammi di PLL sono stati generati con successo!")

if __name__ == "__main__":
    main()