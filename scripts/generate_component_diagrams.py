#!/usr/bin/env python3
"""
Script per generare diagrammi elettrici dei componenti usando schemdraw.
Genera simboli di resistori, condensatori, induttori, diodi, transistor, etc.
"""

import schemdraw
import schemdraw.elements as elm
from schemdraw import flow

from utils import get_output_dir, setup_logging, run_with_error_handling


# Directory di output
OUTPUT_DIR = get_output_dir('02_componenti')
OUTPUT_DIR_CIRCUITI = get_output_dir('03_circuiti')


def draw_resistor():
    """Disegna un resistore con simbolo europeo e americano."""
    # Simbolo europeo (rettangolo)
    d = schemdraw.Drawing(unit=2.5)
    d += elm.Resistor().label('R')
    d += elm.Line().length(1).right()
    d.save(OUTPUT_DIR / 'simbolo_resistore_europeo.svg')

    # Simbolo americano (zigzag)
    d2 = schemdraw.Drawing(unit=2.5)
    d2 += elm.ResistorIEEE().label('R')
    d2 += elm.Line().length(1).right()
    d2.save(OUTPUT_DIR / 'simbolo_resistore_americano.svg')

    print("[OK] Resistore generato")


def draw_capacitor():
    """Disegna un condensatore non polarizzato e polarizzato."""
    # Condensatore non polarizzato
    d = schemdraw.Drawing(unit=2.5)
    d += elm.Capacitor().label('C')
    d += elm.Line().length(1).right()
    d.save(OUTPUT_DIR / 'simbolo_condensatore.svg')

    # Condensatore polarizzato
    d2 = schemdraw.Drawing(unit=2.5)
    d2 += elm.Capacitor().label('C+')
    d2 += elm.Line().length(1).right()
    d2.save(OUTPUT_DIR / 'simbolo_condensatore_polarizzato.svg')

    print("[OK] Condensatore generato")


def draw_inductor():
    """Disegna un induttore."""
    d = schemdraw.Drawing(unit=2.5)
    d += elm.Inductor().label('L')
    d += elm.Line().length(1).right()
    d.save(OUTPUT_DIR / 'simbolo_induttore.svg')

    print("[OK] Induttore generato")


def draw_diode():
    """Disegna un diodo e LED."""
    # Diodo standard
    d = schemdraw.Drawing(unit=2.5)
    d += elm.Diode().label('D')
    d += elm.Line().length(1).right()
    d.save(OUTPUT_DIR / 'simbolo_diodo.svg')

    # LED
    d2 = schemdraw.Drawing(unit=2.5)
    d2 += elm.LED().label('LED')
    d2 += elm.Line().length(1).right()
    d2.save(OUTPUT_DIR / 'simbolo_led.svg')

    print("[OK] Diodo generato")


def draw_transistor_bjt():
    """Disegna transistor BJT NPN e PNP."""
    d = schemdraw.Drawing(unit=2.5)
    d += elm.BjtNpn().label('Q')
    d += elm.Line().length(1).right()
    d.save(OUTPUT_DIR / 'simbolo_transistor_npn.svg')

    print("[OK] Transistor BJT generato")


def draw_transistor_mosfet():
    """Disegna transistor MOSFET."""
    d = schemdraw.Drawing(unit=2.5)
    d += elm.NMos().label('Q')
    d += elm.Line().length(1).right()
    d.save(OUTPUT_DIR / 'simbolo_transistor_mosfet.svg')

    print("[OK] Transistor MOSFET generato")


def draw_transformer():
    """Disegna un trasformatore."""
    d = schemdraw.Drawing(unit=3)
    d += elm.Transformer().label('T')
    d += elm.Line().length(1).right()
    d.save(OUTPUT_DIR / 'simbolo_trasformatore.svg')

    print("[OK] Trasformatore generato")


def draw_valve():
    """Disegna una valvola termoionica (triodo)."""
    d = schemdraw.Drawing(unit=3)
    d += elm.Ic().label('V').label('TRIODE', loc='bottom')
    d += elm.Line().length(1).right()
    d.save(OUTPUT_DIR / 'simbolo_valvola_triodo.svg')

    print("[OK] Valvola generata")


def draw_circuit_examples():
    """Disegna circuiti di esempio."""
    # Circuito serie RC
    d = schemdraw.Drawing(unit=3)
    d += elm.SourceV().label('V')
    d += elm.Resistor().label('R').right()
    d += elm.Capacitor().label('C').down()
    d += elm.Line().left()
    d += elm.Line().up()
    d.save(OUTPUT_DIR_CIRCUITI / 'circuito_serie_rc.svg')

    # Circuito raddrizzatore a ponte
    d2 = schemdraw.Drawing(unit=2.5)
    d2 += elm.SourceV().label('AC')
    d2.push()
    d2 += elm.Diode().right().label('D1')
    d2 += elm.Diode().down().label('D2')
    d2 += elm.Line().left()
    d2 += elm.Diode().up().label('D3')
    d2 += elm.Diode().right().label('D4')
    d2.pop()
    d2 += elm.Line().down()
    d2 += elm.Line().right()
    d2 += elm.Resistor().label('Load').down()
    d2 += elm.Line().left()
    d2.save(OUTPUT_DIR_CIRCUITI / 'circuito_ponte_raddrizzatore.svg')

    print("[OK] Circuiti di esempio generati")


def main():
    """Funzione principale che genera tutti i diagrammi."""
    print(f"Generazione diagrammi in: {OUTPUT_DIR}\n")

    # Simboli dei componenti
    draw_resistor()
    draw_capacitor()
    draw_inductor()
    draw_diode()
    draw_transistor_bjt()
    draw_transistor_mosfet()
    draw_transformer()
    draw_valve()

    # Circuiti di esempio
    draw_circuit_examples()

    print(f"\nTutti i diagrammi salvati in: {OUTPUT_DIR}")


if __name__ == "__main__":
    exit(run_with_error_handling(main, "generate_component_diagrams"))
