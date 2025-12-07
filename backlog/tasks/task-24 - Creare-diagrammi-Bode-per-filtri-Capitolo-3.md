---
id: task-24
title: Creare diagrammi Bode per filtri - Capitolo 3
status: Done
assignee:
  - '@claude'
created_date: '2025-12-07 16:19'
updated_date: '2025-12-07 17:37'
labels:
  - diagrams
  - chapter3
  - matplotlib
dependencies: []
priority: medium
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Arricchire il capitolo filtri con diagrammi di Bode (risposta in frequenza) per i principali tipi di filtro, mostrando modulo e fase.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [x] #1 Creare script plot_bode_diagrams.py
- [x] #2 Generare diagramma Bode filtro passa-basso RC (modulo + fase)
- [x] #3 Generare diagramma Bode filtro passa-alto CR
- [x] #4 Generare diagramma Bode filtro passa-banda RLC
- [x] #5 Generare confronto risposta Butterworth vs Chebyshev
- [x] #6 Integrare diagrammi in 03_Circuiti/3.2_Filtri.md
<!-- AC:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
Creato script plot_bode_diagrams.py con 4 funzioni:
- plot_bode_passa_basso(): modulo e fase filtro RC con asintoti e annotazioni
- plot_bode_passa_alto(): modulo e fase filtro CR con pendenze +20dB/dec
- plot_bode_passa_banda(): risposta RLC con BW e Q visualizzati
- plot_butterworth_vs_chebyshev(): confronto ordini 2/4/6 per entrambi

Generate 4 immagini PNG in images/03_circuiti/.
Integrate in 3.2_Filtri.md nelle sezioni specifiche di ogni filtro.
<!-- SECTION:NOTES:END -->
