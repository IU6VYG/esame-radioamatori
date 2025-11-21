#!/usr/bin/env python3
"""
Script per generare diagrammi di amplificatori per il Capitolo 3 (versione ultra semplificata)
"""

import schemdraw
import schemdraw.elements as elm
import os

def setup_output_directory():
    """Crea la directory images se non esiste"""
    if not os.path.exists('../images'):
        os.makedirs('../images')
    print("Directory images pronta")

def draw_simple_amplifiers():
    """Disegna circuiti di amplificatori molto semplici"""
    
    # Amplificatore base con transistor
    d1 = schemdraw.Drawing(unit=3)
    d1 += elm.SourceV().label('V_cc')
    d1 += elm.Resistor().label('R_c').right()
    d1 += elm.BjtNpn().label('Q1').right()
    d1 += elm.Resistor().label('R_e').down()
    d1 += elm.Ground()
    d1 += elm.Line().right()
    d1 += elm.Label('V_out')
    d1 += elm.Resistor().label('R_L').down()
    d1 += elm.Ground()
    d1.save('../images/amplificatore_base_transistor.svg')
    
    # Amplificatore con op-amp
    d2 = schemdraw.Drawing(unit=3)
    d2 += elm.Opamp().label('U1').right()
    d2 += elm.Resistor().label('R_in').left()
    d2 += elm.Line().right()
    d2 += elm.Label('V_out')
    d2 += elm.Resistor().label('R_f').up()
    d2 += elm.Line().left()
    d2 += elm.Ground()
    d2.save('../images/amplificatore_opamp.svg')
    
    # Amplificatore RF
    d3 = schemdraw.Drawing(unit=3)
    d3 += elm.SourceSin().label('V_in')
    d3 += elm.Capacitor().label('C_in').right()
    d3 += elm.BjtNpn().label('Q_RF').right()
    d3 += elm.Capacitor().label('C_out').right()
    d3 += elm.Label('V_out')
    d3 += elm.Resistor().label('R_L').down()
    d3 += elm.Ground()
    d3.save('../images/amplificatore_rf.svg')
    
    print("Amplificatori semplici generati")

def draw_amplifier_configurations():
    """Disegna configurazioni di amplificatori"""
    
    # Amplificatore differenziale
    d1 = schemdraw.Drawing(unit=3)
    d1 += elm.Opamp().label('U1').right()
    d1 += elm.Resistor().label('R1').left()
    d1 += elm.Line().up()
    d1 += elm.SourceSin().label('V_in+').left()
    d1 += elm.Resistor().label('R2').down()
    d1 += elm.Ground()
    d1 += elm.Line().right()
    d1 += elm.Label('V_out')
    d1 += elm.Resistor().label('R_L').down()
    d1 += elm.Ground()
    d1.save('../images/amplificatore_differenziale.svg')
    
    # Amplificatore push-pull
    d2 = schemdraw.Drawing(unit=3)
    d2 += elm.SourceV().label('V_in')
    d2 += elm.BjtNpn().label('Q1').right()
    d2 += elm.BjtPnp().label('Q2').down()
    d2 += elm.Line().right()
    d2 += elm.Label('V_out')
    d2 += elm.Resistor().label('R_L').down()
    d2 += elm.Ground()
    d2.save('../images/amplificatore_push_pull.svg')
    
    print("Configurazioni di amplificatori generate")

def main():
    """Funzione principale che genera tutti i diagrammi di amplificatori"""
    print("Inizio generazione diagrammi di amplificatori...")
    
    setup_output_directory()
    draw_simple_amplifiers()
    draw_amplifier_configurations()
    
    print("Tutti i diagrammi di amplificatori sono stati generati con successo!")

if __name__ == "__main__":
    main()