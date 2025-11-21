#!/usr/bin/env python3
"""
Script per generare diagrammi di alimentazioni per il Capitolo 3 (versione corretta)
"""

import schemdraw
import schemdraw.elements as elm
import os

def setup_output_directory():
    """Crea la directory images se non esiste"""
    if not os.path.exists('../images'):
        os.makedirs('../images')
    print("Directory images pronta")

def draw_power_supply_circuits():
    """Disegna circuiti di alimentazione"""
    
    # Raddrizzatore a semionda con filtro
    d1 = schemdraw.Drawing(unit=3)
    d1 += elm.SourceV().label('AC')
    d1 += elm.Transformer().label('T1').right()
    d1 += elm.Diode().label('D1').right()
    d1 += elm.Capacitor().label('C1').down()
    d1 += elm.Ground()
    d1 += elm.Line().right()
    d1 += elm.Label('V_out')
    d1 += elm.Resistor().label('R_L').down()
    d1 += elm.Ground()
    d1.save('../images/raddrizzatore_semionda_filtro.svg')
    
    # Alimentatore lineare completo
    d2 = schemdraw.Drawing(unit=3)
    d2 += elm.SourceV().label('AC 230V')
    d2 += elm.Transformer().label('T1').right()
    d2 += elm.Diode().label('D1').right()
    d2 += elm.Diode().label('D2').down()
    d2 += elm.Ground()
    d2 += elm.Diode().up().label('D3')
    d2 += elm.Diode().right().label('D4')
    d2 += elm.Capacitor().label('C_filter').down()
    d2 += elm.Ground()
    d2 += elm.Line().right()
    d2 += elm.Ic().label('REG').right()
    d2 += elm.Capacitor().label('C_out').down()
    d2 += elm.Ground()
    d2 += elm.Line().right()
    d2 += elm.Label('V_out')
    d2 += elm.Resistor().label('R_L').down()
    d2 += elm.Ground()
    d2.save('../images/alimentatore_lineare_completo.svg')
    
    # Regolatore lineare serie
    d3 = schemdraw.Drawing(unit=3)
    d3 += elm.SourceV().label('V_in')
    d3 += elm.Resistor().label('R_s').right()
    d3 += elm.BjtNpn().label('Q1').right()
    d3 += elm.Zener().label('D_z').down()
    d3 += elm.Ground()
    d3 += elm.Line().right()
    d3 += elm.Label('V_out')
    d3 += elm.Resistor().label('R_L').down()
    d3 += elm.Ground()
    d3 += elm.Capacitor().label('C_out').down()
    d3 += elm.Ground()
    d3.save('../images/regolatore_lineare_serie.svg')
    
    print("Circuiti di alimentazione generati")

def draw_switching_power_supply():
    """Disegna alimentatore switching"""
    
    # Convertitore buck (step-down)
    d1 = schemdraw.Drawing(unit=3)
    d1 += elm.SourceV().label('V_in')
    d1 += elm.NMos().label('Q1').right()
    d1 += elm.Diode().label('D1').down()
    d1 += elm.Ground()
    d1 += elm.Inductor().label('L1').right()
    d1 += elm.Capacitor().label('C1').down()
    d1 += elm.Ground()
    d1 += elm.Line().right()
    d1 += elm.Label('V_out')
    d1 += elm.Resistor().label('R_L').down()
    d1 += elm.Ground()
    d1.save('../images/convertitore_buck.svg')
    
    # Convertitore boost (step-up)
    d2 = schemdraw.Drawing(unit=3)
    d2 += elm.SourceV().label('V_in')
    d2 += elm.Inductor().label('L1').right()
    d2 += elm.NMos().label('Q1').down()
    d2 += elm.Ground()
    d2 += elm.Diode().label('D1').right()
    d2 += elm.Capacitor().label('C1').down()
    d2 += elm.Ground()
    d2 += elm.Line().right()
    d2 += elm.Label('V_out')
    d2 += elm.Resistor().label('R_L').down()
    d2 += elm.Ground()
    d2.save('../images/convertitore_boost.svg')
    
    print("Circuiti switching generati")

def draw_protection_circuits():
    """Disegna circuiti di protezione"""
    
    # Protezione sovratensione con fusibile e Zener
    d1 = schemdraw.Drawing(unit=3)
    d1 += elm.SourceV().label('V_in')
    d1 += elm.Fuse().label('F1').right()
    d1 += elm.Zener().label('D_z').down()
    d1 += elm.Ground()
    d1 += elm.Line().right()
    d1 += elm.Label('V_out_protected')
    d1 += elm.Resistor().label('R_L').down()
    d1 += elm.Ground()
    d1.save('../images/protezione_sovratensione.svg')
    
    # Limitatore di corrente
    d2 = schemdraw.Drawing(unit=3)
    d2 += elm.SourceV().label('V_in')
    d2 += elm.Resistor().label('R_sense').right()
    d2 += elm.BjtNpn().label('Q_limit').down()
    d2 += elm.Ground()
    d2 += elm.Line().right()
    d2 += elm.Label('V_out')
    d2 += elm.Resistor().label('R_load').down()
    d2 += elm.Ground()
    d2.save('../images/limitatore_corrente.svg')
    
    print("Circuiti di protezione generati")

def draw_battery_charger():
    """Disegna circuito di caricabatterie"""
    
    # Caricabatterie Li-ion lineare
    d1 = schemdraw.Drawing(unit=3)
    d1 += elm.SourceV().label('V_in')
    d1 += elm.Ic().label(' Charger ').right()
    d1 += elm.Resistor().label('R_sense').right()
    d1 += elm.Battery().label('Battery').down()
    d1 += elm.Ground()
    d1 += elm.Line().right()
    d1 += elm.Label('V_out')
    d1 += elm.Capacitor().label('C_out').down()
    d1 += elm.Ground()
    d1.save('../images/caricabatterie_liion.svg')
    
    # Caricabatterie CC-CV semplificato
    d2 = schemdraw.Drawing(unit=3)
    d2 += elm.SourceV().label('V_in')
    d2 += elm.Opamp().label('U1').right()
    d2 += elm.NMos().label('Q1').down()
    d2 += elm.Ground()
    d2 += elm.Line().right()
    d2 += elm.Resistor().label('R_sense').right()
    d2 += elm.Battery().label('Battery').down()
    d2 += elm.Ground()
    d2 += elm.Line().right()
    d2 += elm.Label('V_out')
    d2.save('../images/caricabatterie_cc_cv.svg')
    
    print("Circuiti di caricabatterie generati")

def main():
    """Funzione principale che genera tutti i diagrammi di alimentazione"""
    print("Inizio generazione diagrammi di alimentazione...")
    
    setup_output_directory()
    draw_power_supply_circuits()
    draw_switching_power_supply()
    draw_protection_circuits()
    draw_battery_charger()
    
    print("Tutti i diagrammi di alimentazione sono stati generati con successo!")

if __name__ == "__main__":
    main()