#!/usr/bin/env python3
"""
Script per generare diagrammi di rivelatori per il Capitolo 3 (versione corretta)
"""

import schemdraw
import schemdraw.elements as elm
import os

def setup_output_directory():
    """Crea la directory images se non esiste"""
    if not os.path.exists('../images'):
        os.makedirs('../images')
    print("Directory images pronta")

def draw_am_detectors():
    """Disegna rivelatori AM"""
    
    # Rivelatore AM a diodo
    d1 = schemdraw.Drawing(unit=3)
    d1 += elm.SourceSin().label('RF Input')
    d1 += elm.Capacitor().label('C_c').right()
    d1 += elm.Diode().label('D1').right()
    d1 += elm.Capacitor().label('C').down()
    d1 += elm.Ground()
    d1 += elm.Line().right()
    d1 += elm.Label('Audio Output')
    d1 += elm.Resistor().label('R_L').down()
    d1 += elm.Ground()
    d1.save('../images/rivelatore_am_diodo.svg')
    
    # Rivelatore AM a prodotto (usando op-amp come moltiplicatore)
    d2 = schemdraw.Drawing(unit=3)
    d2 += elm.SourceSin().label('RF Input')
    d2 += elm.Capacitor().label('C_in').right()
    d2 += elm.Opamp().label('Mixer').right()
    d2 += elm.SourceSin().label('LO Ref').down()
    d2 += elm.Ground()
    d2 += elm.Capacitor().label('C_out').right()
    d2 += elm.Label('Audio Output')
    d2 += elm.Resistor().label('R_L').down()
    d2 += elm.Ground()
    d2.save('../images/rivelatore_am_prodotto.svg')
    
    print("Rivelatori AM generati")

def draw_fm_detectors():
    """Disegna rivelatori FM"""
    
    # Rivelatore FM a pendenza (slope detector)
    d1 = schemdraw.Drawing(unit=3)
    d1 += elm.SourceSin().label('RF Input')
    d1 += elm.Capacitor().label('C_c').right()
    d1 += elm.Inductor().label('L').right()
    d1 += elm.Capacitor().label('C').down()
    d1 += elm.Ground()
    d1 += elm.Diode().label('D1').right()
    d1 += elm.Capacitor().label('C_out').down()
    d1 += elm.Ground()
    d1 += elm.Line().right()
    d1 += elm.Label('Audio Output')
    d1 += elm.Resistor().label('R_L').down()
    d1 += elm.Ground()
    d1.save('../images/rivelatore_fm_pendenza.svg')
    
    # Rivelatore Foster-Seeley semplificato
    d2 = schemdraw.Drawing(unit=3)
    d2 += elm.SourceSin().label('RF Input')
    d2 += elm.Transformer().label('T1').right()
    d2 += elm.Capacitor().label('C1').down()
    d2 += elm.Ground()
    d2 += elm.Capacitor().label('C2').right()
    d2 += elm.Ground()
    d2 += elm.Diode().label('D1').right()
    d2 += elm.Diode().label('D2').down()
    d2 += elm.Ground()
    d2 += elm.Resistor().label('R1').right()
    d2 += elm.Resistor().label('R2').down()
    d2 += elm.Ground()
    d2 += elm.Line().right()
    d2 += elm.Label('Audio Output')
    d2 += elm.Capacitor().label('C_out').down()
    d2 += elm.Ground()
    d2.save('../images/rivelatore_foster_seeley.svg')
    
    print("Rivelatori FM generati")

def draw_ssb_detectors():
    """Disegna rivelatori SSB/CW"""
    
    # Rivelatore SSB con BFO
    d1 = schemdraw.Drawing(unit=3)
    d1 += elm.SourceSin().label('SSB Input')
    d1 += elm.Capacitor().label('C_in').right()
    d1 += elm.Opamp().label('Mixer').right()
    d1 += elm.SourceSin().label('BFO').down()
    d1 += elm.Ground()
    d1 += elm.Capacitor().label('C_out').right()
    d1 += elm.Label('Audio Output')
    d1 += elm.Resistor().label('R_L').down()
    d1 += elm.Ground()
    d1.save('../images/rivelatore_ssb_bfo.svg')
    
    # Rivelatore CW con beat
    d2 = schemdraw.Drawing(unit=3)
    d2 += elm.SourceSin().label('CW Input')
    d2 += elm.Capacitor().label('C_in').right()
    d2 += elm.Opamp().label('Beat Detector').right()
    d2 += elm.SourceSin().label('BFO').down()
    d2 += elm.Ground()
    d2 += elm.Capacitor().label('C_out').right()
    d2 += elm.Label('Audio Output')
    d2 += elm.Resistor().label('R_L').down()
    d2 += elm.Ground()
    d2.save('../images/rivelatore_cw_beat.svg')
    
    print("Rivelatori SSB/CW generati")

def draw_receiver_block():
    """Disegna diagramma a blocchi di ricevitore"""
    
    # Ricevitore completo semplificato
    d1 = schemdraw.Drawing(unit=2.5)
    d1 += elm.Antenna().label('Antenna')
    d1 += elm.Capacitor().label('C_rf').right()
    d1 += elm.Ic().label('RF Amp').right()
    d1 += elm.Capacitor().label('C_if').right()
    d1 += elm.Ic().label('Detector').right()
    d1 += elm.Capacitor().label('C_af').right()
    d1 += elm.Ic().label('Audio Amp').right()
    d1 += elm.Speaker().label('Speaker').down()
    d1 += elm.Ground()
    d1.save('../images/ricevitore_blocchi.svg')
    
    print("Diagramma a blocchi generato")

def main():
    """Funzione principale che genera tutti i diagrammi di rivelatori"""
    print("Inizio generazione diagrammi di rivelatori...")
    
    setup_output_directory()
    draw_am_detectors()
    draw_fm_detectors()
    draw_ssb_detectors()
    draw_receiver_block()
    
    print("Tutti i diagrammi di rivelatori sono stati generati con successo!")

if __name__ == "__main__":
    main()