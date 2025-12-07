#!/usr/bin/env python3
"""
Generazione schemi circuitali per reti di adattamento impedenza.
Genera L-match, Pi-match, T-match e balun usando schemdraw.
"""

import schemdraw
import schemdraw.elements as elm
from pathlib import Path

# Directory di output
OUTPUT_DIR = Path(__file__).parent.parent / "images" / "06_antenne"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def draw_l_match_lowpass():
    """
    Rete L-match passa-basso: L serie + C parallelo.
    Usata per trasformare impedenza alta in bassa.
    """
    d = schemdraw.Drawing(unit=3)

    # Ingresso
    d += elm.Dot().label('IN\n50Ω', loc='left', fontsize=11)
    d += elm.Line().right().length(0.5)

    # Induttore serie
    d += elm.Inductor().right().label('L', loc='top', fontsize=12)

    # Nodo
    d.push()
    d += elm.Line().right().length(0.5)
    d += elm.Dot().label('OUT\nZ_L', loc='right', fontsize=11)

    # Condensatore parallelo
    d.pop()
    d += elm.Capacitor().down().label('C', loc='right', fontsize=12)
    d += elm.Ground()

    # Linea di massa
    d += elm.Line().left().length(2.5).at((0, -3))
    d += elm.Ground().at((0, -3))

    d.save(OUTPUT_DIR / 'rete_l_match_lowpass.svg')
    print(f"✓ Salvato: {OUTPUT_DIR / 'rete_l_match_lowpass.svg'}")


def draw_l_match_highpass():
    """
    Rete L-match passa-alto: C serie + L parallelo.
    Usata per trasformare impedenza bassa in alta.
    """
    d = schemdraw.Drawing(unit=3)

    # Ingresso
    d += elm.Dot().label('IN\n50Ω', loc='left', fontsize=11)
    d += elm.Line().right().length(0.5)

    # Condensatore serie
    d += elm.Capacitor().right().label('C', loc='top', fontsize=12)

    # Nodo
    d.push()
    d += elm.Line().right().length(0.5)
    d += elm.Dot().label('OUT\nZ_L', loc='right', fontsize=11)

    # Induttore parallelo
    d.pop()
    d += elm.Inductor().down().label('L', loc='right', fontsize=12)
    d += elm.Ground()

    d.save(OUTPUT_DIR / 'rete_l_match_highpass.svg')
    print(f"✓ Salvato: {OUTPUT_DIR / 'rete_l_match_highpass.svg'}")


def draw_pi_match():
    """
    Rete Pi-match: C parallelo - L serie - C parallelo.
    Configurazione classica per accordatori d'antenna.
    """
    d = schemdraw.Drawing(unit=3)

    # Ingresso
    d += elm.Dot().label('IN\n50Ω', loc='left', fontsize=11)
    d.push()
    d += elm.Line().right().length(0.3)

    # C1 parallelo
    d.push()
    d += elm.Capacitor().down().label('C1', loc='right', fontsize=12)
    d += elm.Ground()
    d.pop()

    # L serie
    d += elm.Inductor().right().label('L', loc='top', fontsize=12).length(3)

    # C2 parallelo
    d.push()
    d += elm.Capacitor().down().label('C2', loc='right', fontsize=12)
    d += elm.Ground()
    d.pop()

    # Uscita
    d += elm.Line().right().length(0.3)
    d += elm.Dot().label('OUT\nAntenna', loc='right', fontsize=11)

    # Linea massa
    d.pop()
    d += elm.Line().down().length(3)
    d += elm.Ground()

    d.save(OUTPUT_DIR / 'rete_pi_match.svg')
    print(f"✓ Salvato: {OUTPUT_DIR / 'rete_pi_match.svg'}")


def draw_t_match():
    """
    Rete T-match: L serie - C parallelo - L serie.
    Alternativa al Pi-match con caratteristiche diverse.
    """
    d = schemdraw.Drawing(unit=3)

    # Ingresso
    d += elm.Dot().label('IN\n50Ω', loc='left', fontsize=11)
    d += elm.Line().right().length(0.3)

    # L1 serie
    d += elm.Inductor().right().label('L1', loc='top', fontsize=12)

    # C parallelo centrale
    d.push()
    d += elm.Capacitor().down().label('C', loc='right', fontsize=12)
    d += elm.Ground()
    d.pop()

    # L2 serie
    d += elm.Inductor().right().label('L2', loc='top', fontsize=12)

    # Uscita
    d += elm.Line().right().length(0.3)
    d += elm.Dot().label('OUT\nAntenna', loc='right', fontsize=11)

    d.save(OUTPUT_DIR / 'rete_t_match.svg')
    print(f"✓ Salvato: {OUTPUT_DIR / 'rete_t_match.svg'}")


def draw_balun_1_1():
    """
    Balun 1:1 - bilanciamento senza trasformazione impedenza.
    Connette coassiale sbilanciato ad antenna bilanciata.
    """
    d = schemdraw.Drawing(unit=3)

    # Titolo
    d += elm.Label().at((3, 2)).label('Balun 1:1', fontsize=14)

    # Ingresso coassiale (sbilanciato)
    d += elm.Dot().at((0, 0)).label('Coax\n50Ω', loc='left', fontsize=10)
    d += elm.Line().right().length(0.5)

    # Trasformatore 1:1
    xf = d.add(elm.Transformer(t1=4, t2=4).right())

    # Uscita bilanciata
    d += elm.Line().right().length(0.5).at(xf.s1)
    d += elm.Dot().label('Ant+', loc='right', fontsize=10)

    d += elm.Line().right().length(0.5).at(xf.s2)
    d += elm.Dot().label('Ant-', loc='right', fontsize=10)

    # Massa ingresso
    d += elm.Ground().at(xf.p2)

    # Etichette
    d += elm.Label().at((1.5, -0.5)).label('1:1', fontsize=12)

    d.save(OUTPUT_DIR / 'balun_1_1.svg')
    print(f"✓ Salvato: {OUTPUT_DIR / 'balun_1_1.svg'}")


def draw_balun_4_1():
    """
    Balun 4:1 - trasformazione impedenza 200Ω → 50Ω.
    Tipico per dipolo ripiegato.
    """
    d = schemdraw.Drawing(unit=3)

    # Titolo
    d += elm.Label().at((3, 2)).label('Balun 4:1', fontsize=14)

    # Ingresso coassiale
    d += elm.Dot().at((0, 0)).label('Coax\n50Ω', loc='left', fontsize=10)
    d += elm.Line().right().length(0.5)

    # Trasformatore 4:1 (n1=2, n2=4 per rapporto 1:4 impedenza)
    xf = d.add(elm.Transformer(t1=2, t2=4).right())

    # Uscita bilanciata alta impedenza
    d += elm.Line().right().length(0.5).at(xf.s1)
    d += elm.Dot().label('Ant+\n200Ω', loc='right', fontsize=10)

    d += elm.Line().right().length(0.5).at(xf.s2)
    d += elm.Dot().label('Ant-', loc='right', fontsize=10)

    # Massa ingresso
    d += elm.Ground().at(xf.p2)

    # Etichetta rapporto
    d += elm.Label().at((1.5, -0.5)).label('1:4 (Z)', fontsize=12)

    d.save(OUTPUT_DIR / 'balun_4_1.svg')
    print(f"✓ Salvato: {OUTPUT_DIR / 'balun_4_1.svg'}")


def draw_balun_current():
    """
    Balun a corrente (choke balun) con ferrite.
    Blocca le correnti di modo comune.
    """
    d = schemdraw.Drawing(unit=3)

    # Ingresso
    d += elm.Dot().at((0, 1)).label('Coax\ncentro', loc='left', fontsize=10)
    d += elm.Line().right().length(0.5)

    # Rappresentazione avvolgimento su ferrite (due induttori accoppiati)
    d += elm.Inductor().right().label('', fontsize=12)
    d += elm.Line().right().length(0.5)
    d += elm.Dot().label('Ant+', loc='right', fontsize=10)

    # Seconda linea (schermo)
    d += elm.Dot().at((0, -1)).label('Coax\nschermo', loc='left', fontsize=10)
    d += elm.Line().right().length(0.5)
    d += elm.Inductor().right()
    d += elm.Line().right().length(0.5)
    d += elm.Dot().label('Ant-', loc='right', fontsize=10)

    # Nucleo ferrite (simbolo)
    d += elm.Line().down().at((2.2, 1.5)).length(3).linewidth(3).color('gray')
    d += elm.Line().down().at((2.4, 1.5)).length(3).linewidth(3).color('gray')

    # Etichetta
    d += elm.Label().at((2.3, 2)).label('Ferrite\nCore', fontsize=10)

    d.save(OUTPUT_DIR / 'balun_corrente.svg')
    print(f"✓ Salvato: {OUTPUT_DIR / 'balun_corrente.svg'}")


def draw_antenna_tuner_complete():
    """
    Accordatore d'antenna completo tipo T con indicatori.
    Schema didattico con etichette.
    """
    d = schemdraw.Drawing(unit=2.5)

    # Ingresso da radio
    d += elm.Dot().at((0, 0)).label('TX\n50Ω', loc='left', fontsize=10)
    d += elm.Line().right().length(0.5)

    # C1 variabile (ingresso)
    d.push()
    c1 = d.add(elm.Capacitor().down().label('C1\nvar', loc='right', fontsize=10))
    d += elm.Ground()
    d.pop()

    # L variabile (serie) - roller inductor
    d += elm.Inductor().right().label('L var\n(roller)', loc='top', fontsize=10).length(2.5)

    # C2 variabile (uscita)
    d.push()
    d += elm.Capacitor().down().label('C2\nvar', loc='right', fontsize=10)
    d += elm.Ground()
    d.pop()

    # Uscita antenna
    d += elm.Line().right().length(0.5)
    d += elm.Dot().label('ANT', loc='right', fontsize=11)

    # Titolo
    d += elm.Label().at((2, 2.5)).label('Accordatore T', fontsize=14)

    d.save(OUTPUT_DIR / 'accordatore_t_completo.svg')
    print(f"✓ Salvato: {OUTPUT_DIR / 'accordatore_t_completo.svg'}")


def main():
    """Genera tutti i diagrammi delle reti di adattamento."""
    print("Generazione schemi reti di adattamento impedenza...")
    print(f"Directory output: {OUTPUT_DIR}\n")

    draw_l_match_lowpass()
    draw_l_match_highpass()
    draw_pi_match()
    draw_t_match()
    draw_balun_1_1()
    draw_balun_4_1()
    draw_balun_current()
    draw_antenna_tuner_complete()

    print("\n✅ Tutti gli schemi sono stati generati con successo!")


if __name__ == "__main__":
    main()
