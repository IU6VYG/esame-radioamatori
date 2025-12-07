---
id: task-29
title: Arricchire diagrammi ricevitori - Capitolo 4
status: In Progress
assignee:
  - '@claude'
created_date: '2025-12-07 16:23'
updated_date: '2025-12-07 18:20'
labels:
  - diagrams
  - chapter4
  - schemdraw
dependencies: []
priority: medium
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Migliorare i diagrammi a blocchi dei ricevitori con maggior dettaglio: etichette frequenze intermedie, livelli segnale, cifra di rumore per stadio.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [x] #1 Aggiornare schema ricevitore supereterodina con frequenze tipiche
- [x] #2 Aggiungere schema ricevitore a conversione diretta (SDR)
- [x] #3 Creare diagramma flusso segnale con livelli dBm
- [x] #4 Generare schema dettagliato mixer e oscillatore locale
- [x] #5 Integrare miglioramenti in 04_Ricevitori/
<!-- AC:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
Creato script generate_receiver_diagrams.py con 5 visualizzazioni:
- supereterodina_dettagliato.png: Schema con frequenze tipiche HF
- ricevitore_sdr.png: Architettura SDR I/Q moderna
- flusso_segnale_dbm.png: Livelli segnale da antenna a uscita
- mixer_oscillatore.png: Dettaglio mixer diodi e VFO/PLL
- confronto_architetture_rx.png: Tabella confronto architetture

Integrate in 04_Ricevitori/4.2_Schemi_a_blocchi.md
<!-- SECTION:NOTES:END -->
