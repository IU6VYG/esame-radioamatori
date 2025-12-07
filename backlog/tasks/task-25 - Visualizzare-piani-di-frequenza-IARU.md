---
id: task-25
title: Visualizzare piani di frequenza IARU
status: Done
assignee:
  - '@claude'
created_date: '2025-12-07 16:20'
updated_date: '2025-12-07 17:48'
labels:
  - diagrams
  - operativa
  - matplotlib
dependencies: []
priority: medium
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Creare visualizzazioni grafiche per i piani di frequenza IARU: allocazione bande HF/VHF/UHF, segmenti per modo di emissione e limiti di potenza.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [x] #1 Creare script plot_frequency_plans.py
- [x] #2 Generare grafico allocazione bande HF radioamatore (1.8-30 MHz)
- [x] #3 Generare grafico allocazione bande VHF/UHF (144, 432, 1296 MHz)
- [x] #4 Generare legenda modi di emissione per segmento
- [x] #5 Creare tabella visuale potenze massime per banda (Italia)
- [x] #6 Integrare visualizzazioni in B_Operativa/5_Piani_Frequenze_IARU.md
<!-- AC:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
Creato script plot_frequency_plans.py con 7 visualizzazioni:
- allocazione_bande_hf.png: Panoramica bande HF con segmenti per modo
- allocazione_bande_vhf_uhf.png: Bande 2m, 70cm, 23cm
- legenda_modi_emissione.png: Tabella completa modi con designatori
- potenze_massime_italia.png: Limiti potenza classe A Italia
- frequenze_per_modulazione.png: Raggruppamento per CW/SSB/FM/Digi
- frequenze_per_applicazione.png: Raggruppamento per DX/Locale/Contest/etc.
- panoramica_normativa_italia.png: Status primario/secondario bande

Risolti problemi matplotlib (axhline, emoji glyph warnings).
Immagini integrate in B_Operativa/5_Piani_Frequenze_IARU.md.
<!-- SECTION:NOTES:END -->
