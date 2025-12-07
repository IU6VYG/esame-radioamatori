---
id: task-31
title: Aggiungere diagrammi linee di trasmissione
status: Done
assignee:
  - '@claude'
created_date: '2025-12-07 16:23'
updated_date: '2025-12-07 17:18'
labels:
  - diagrams
  - chapter6
  - matplotlib
dependencies: []
priority: high
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Creare visualizzazioni per le linee di trasmissione: onde stazionarie, impedenza caratteristica, velocità di propagazione e perdite.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [x] #1 Creare script plot_transmission_lines.py
- [x] #2 Generare visualizzazione onde stazionarie (ROS)
- [x] #3 Generare grafico impedenza vs posizione su linea
- [x] #4 Creare diagramma carta di Smith semplificata
- [x] #5 Generare confronto attenuazione cavi (RG-58, RG-213, etc.)
- [x] #6 Integrare in 06_Antenne_Linee_Trasmissioni/
<!-- AC:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
Implementato script plot_transmission_lines.py con 5 funzioni:
- plot_onde_stazionarie(): onde stazionarie per SWR 1:1, 1.5:1, 2:1, 3:1
- plot_impedenza_linea(): impedenza normalizzata lungo la linea
- plot_carta_smith(): carta di Smith semplificata con esempi
- plot_attenuazione_cavi(): confronto RG-174, RG-58, RG-213, LMR-400, Heliax
- plot_velocita_propagazione(): velocità per diversi dielettrici

Generate 5 immagini PNG in images/06_antenne/.
Integrate in 6.3_Linee_di_trasmissione.md con nuove sezioni per Smith chart, onde stazionarie e confronti cavi.
<!-- SECTION:NOTES:END -->
