#!/usr/bin/env python3
"""
Script per generare diagrammi aggiuntivi: circuiti (cap. 3) e tipologie componenti (cap. 2)
"""

import schemdraw
import schemdraw.elements as elm
from utils import get_output_dir, run_with_error_handling

# Directory di output per le diverse sezioni
OUTPUT_DIR_CIRCUITI = get_output_dir("03_circuiti")
OUTPUT_DIR_COMPONENTI = get_output_dir("02_componenti")

def draw_simple_circuits():
    """Disegna circuiti semplici"""
    
    # Partitore di tensione
    d1 = schemdraw.Drawing(unit=3)
    d1 += elm.SourceV().label('V_in')
    d1 += elm.Resistor().label('R1').right()
    d1 += elm.Resistor().label('R2').down()
    d1 += elm.Line().left()
    d1 += elm.Line().up()
    d1.save(OUTPUT_DIR_CIRCUITI / 'circuito_partitore_tensione.svg')
    
    # Filtro RC passa-basso
    d2 = schemdraw.Drawing(unit=3)
    d2 += elm.SourceSin().label('V_in')
    d2 += elm.Resistor().label('R').right()
    d2 += elm.Capacitor().label('C').down()
    d2 += elm.Ground()
    d2 += elm.Line().right()
    d2 += elm.Label('V_out')
    d2.save(OUTPUT_DIR_CIRCUITI / 'filtro_passa_basso_rc.svg')
    
    # Stabilizzatore Zener
    d3 = schemdraw.Drawing(unit=3)
    d3 += elm.SourceV().label('V_in')
    d3 += elm.Resistor().label('R_s').right()
    d3 += elm.Zener().label('D_z').down()
    d3 += elm.Ground()
    d3 += elm.Line().right()
    d3 += elm.Label('V_out')
    d3 += elm.Resistor().label('R_L').down()
    d3 += elm.Ground()
    d3.save(OUTPUT_DIR_CIRCUITI / 'circuito_stabilizzatore_zener.svg')
    
    print("Circuiti semplici generati")

def draw_component_variations():
    """Disegna variazioni dei componenti"""
    
    # Resistori diversi
    d1 = schemdraw.Drawing(unit=2)
    d1 += elm.Resistor().label('Standard')
    d1 += elm.ResistorVar().label('Variabile').right()
    d1 += elm.Potentiometer().label('Potenziometro').right()
    d1.save(OUTPUT_DIR_COMPONENTI / 'tipologie_resistori.svg')
    
    # Condensatori diversi
    d2 = schemdraw.Drawing(unit=2)
    d2 += elm.Capacitor().label('Fisso')
    d2 += elm.CapacitorVar().label('Variabile').right()
    d2 += elm.CapacitorTrim().label('Trim').right()
    d2.save(OUTPUT_DIR_COMPONENTI / 'tipologie_condensatori.svg')
    
    # Diodi diversi
    d3 = schemdraw.Drawing(unit=2)
    d3 += elm.Diode().label('Standard')
    d3 += elm.Zener().label('Zener').right()
    d3 += elm.LED().label('LED').right()
    d3 += elm.Schottky().label('Schottky').right()
    d3.save(OUTPUT_DIR_COMPONENTI / 'tipologie_diodi.svg')
    
    print("Variazioni componenti generate")

def draw_basic_circuits():
    """Disegna circuiti base di esempio"""
    
    # Circuito RL serie
    d1 = schemdraw.Drawing(unit=3)
    d1 += elm.SourceSin().label('V_in')
    d1 += elm.Resistor().label('R').right()
    d1 += elm.Inductor().label('L').right()
    d1 += elm.Line().down()
    d1 += elm.Line().left()
    d1.save(OUTPUT_DIR_CIRCUITI / 'circuito_serie_rl.svg')
    
    # Circuito RLC serie
    d2 = schemdraw.Drawing(unit=3)
    d2 += elm.SourceSin().label('V_in')
    d2 += elm.Resistor().label('R').right()
    d2 += elm.Inductor().label('L').right()
    d2 += elm.Capacitor().label('C').right()
    d2 += elm.Line().down()
    d2 += elm.Line().left()
    d2.save(OUTPUT_DIR_CIRCUITI / 'circuito_serie_rlc.svg')
    
    # Circuito con diodo di protezione
    d3 = schemdraw.Drawing(unit=3)
    d3 += elm.SourceV().label('V_in')
    d3 += elm.Resistor().label('R').right()
    d3 += elm.Diode().label('D_protezione').down()
    d3 += elm.Line().left()
    d3 += elm.Line().up()
    d3 += elm.Line().right()
    d3 += elm.Label('V_out')
    d3 += elm.Resistor().label('R_load').down()
    d3 += elm.Ground()
    d3.save(OUTPUT_DIR_CIRCUITI / 'circuito_protezione_diodo.svg')
    
    print("Circuiti base generati")

def main():
    """Funzione principale che genera diagrammi aggiuntivi"""
    print("Inizio generazione diagrammi aggiuntivi...")
    
    draw_simple_circuits()
    draw_component_variations()
    draw_basic_circuits()
    
    print("Tutti i diagrammi aggiuntivi sono stati generati con successo!")

if __name__ == "__main__":
    main()