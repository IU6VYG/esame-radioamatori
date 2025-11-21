#!/usr/bin/env python3
"""
Script per generare diagrammi di filtri per il Capitolo 3 (versione semplificata)
"""

import schemdraw
import schemdraw.elements as elm
import os

def setup_output_directory():
    """Crea la directory images se non esiste"""
    if not os.path.exists('../images'):
        os.makedirs('../images')
    print("Directory images pronta")

def draw_filter_circuits():
    """Disegna circuiti di filtri specifici"""
    
    # Filtro passa-basso LC di secondo ordine
    d1 = schemdraw.Drawing(unit=3)
    d1 += elm.SourceSin().label('V_in')
    d1 += elm.Inductor().label('L1').right()
    d1 += elm.Capacitor().label('C1').down()
    d1 += elm.Ground()
    d1 += elm.Inductor().label('L2').right()
    d1 += elm.Capacitor().label('C2').down()
    d1 += elm.Ground()
    d1 += elm.Line().right()
    d1 += elm.Label('V_out')
    d1 += elm.Resistor().label('R_L').down()
    d1 += elm.Ground()
    d1.save('../images/filtro_passa_basso_lc_secondo.svg')
    
    # Filtro passa-alto LC di secondo ordine
    d2 = schemdraw.Drawing(unit=3)
    d2 += elm.SourceSin().label('V_in')
    d2 += elm.Capacitor().label('C1').right()
    d2 += elm.Inductor().label('L1').down()
    d2 += elm.Ground()
    d2 += elm.Capacitor().label('C2').right()
    d2 += elm.Inductor().label('L2').down()
    d2 += elm.Ground()
    d2 += elm.Line().right()
    d2 += elm.Label('V_out')
    d2 += elm.Resistor().label('R_L').down()
    d2 += elm.Ground()
    d2.save('../images/filtro_passa_alto_lc_secondo.svg')
    
    # Filtro a π
    d3 = schemdraw.Drawing(unit=3)
    d3 += elm.SourceSin().label('V_in')
    d3.push()
    d3 += elm.Inductor().label('L_p1').down()
    d3 += elm.Ground()
    d3.pop()
    d3 += elm.Capacitor().label('C_s').right()
    d3 += elm.Inductor().label('L_s').right()
    d3.push()
    d3 += elm.Inductor().label('L_p2').down()
    d3 += elm.Ground()
    d3.pop()
    d3 += elm.Line().right()
    d3 += elm.Label('V_out')
    d3 += elm.Resistor().label('R_L').down()
    d3 += elm.Ground()
    d3.save('../images/filtro_pi.svg')
    
    print("Circuiti di filtri generati")

def draw_crystal_filter():
    """Disegna circuiti con cristalli di quarzo"""
    
    # Circuito equivalente del cristallo
    d1 = schemdraw.Drawing(unit=3)
    d1 += elm.Capacitor().label('C_p').right()
    d1.push()
    d1 += elm.Inductor().label('L_m').right()
    d1 += elm.Capacitor().label('C_m').down()
    d1 += elm.Ground()
    d1.pop()
    d1 += elm.Resistor().label('R_m').right()
    d1 += elm.Line().down()
    d1 += elm.Line().left()
    d1.save('../images/circuito_cristallo_quarzo.svg')
    
    # Filtro a cristallo singolo
    d2 = schemdraw.Drawing(unit=3)
    d2 += elm.SourceSin().label('V_in')
    d2 += elm.Resistor().label('R_s').right()
    d2 += elm.Ic().label('XTAL').right()
    d2 += elm.Resistor().label('R_L').down()
    d2 += elm.Ground()
    d2 += elm.Line().right()
    d2 += elm.Label('V_out')
    d2 += elm.Capacitor().label('C_L').down()
    d2 += elm.Ground()
    d2.save('../images/filtro_cristallo_singolo.svg')
    
    print("Circuiti a cristallo generati")

def draw_special_filters():
    """Disegna filtri speciali"""
    
    # Filtro Crossover (per audio)
    d1 = schemdraw.Drawing(unit=3)
    d1 += elm.SourceSin().label('V_in')
    d1.push()
    # Via passa-alto (tweeter)
    d1 += elm.Capacitor().label('C_high').right()
    d1 += elm.Resistor().label('R_high').down()
    d1 += elm.Ground()
    d1 += elm.Line().right()
    d1 += elm.Label('V_out_high')
    d1.pop()
    # Via passa-basso (woofer)
    d1 += elm.Inductor().label('L_low').right()
    d1 += elm.Resistor().label('R_low').down()
    d1 += elm.Ground()
    d1 += elm.Line().right()
    d1 += elm.Label('V_out_low')
    d1.save('../images/filtro_crossover_audio.svg')
    
    # Filtro anti-aliasing
    d2 = schemdraw.Drawing(unit=3)
    d2 += elm.SourceSin().label('Analog In')
    d2 += elm.Resistor().label('R1').right()
    d2 += elm.Capacitor().label('C1').down()
    d2 += elm.Ground()
    d2 += elm.Resistor().label('R2').right()
    d2 += elm.Capacitor().label('C2').down()
    d2 += elm.Ground()
    d2 += elm.Line().right()
    d2 += elm.Ic().label('ADC').right()
    d2 += elm.Line().down()
    d2 += elm.Ground()
    d2.save('../images/filtro_antialiasing.svg')
    
    print("Filtri speciali generati")

def main():
    """Funzione principale che genera tutti i diagrammi di filtri"""
    print("Inizio generazione diagrammi di filtri...")
    
    setup_output_directory()
    draw_filter_circuits()
    draw_crystal_filter()
    draw_special_filters()
    
    print("Tutti i diagrammi di filtri sono stati generati con successo!")

if __name__ == "__main__":
    main()