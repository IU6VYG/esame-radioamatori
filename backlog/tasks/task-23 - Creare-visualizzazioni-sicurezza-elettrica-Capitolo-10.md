---
id: task-23
title: Creare visualizzazioni sicurezza elettrica - Capitolo 10
status: Done
assignee:
  - '@claude'
created_date: '2025-12-07 16:19'
updated_date: '2025-12-07 17:29'
labels:
  - diagrams
  - chapter10
  - schemdraw
  - matplotlib
dependencies: []
priority: medium
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Creare diagrammi per illustrare i concetti di sicurezza elettrica: effetti della corrente sul corpo umano, impianto di messa a terra, protezione differenziale e scaricatori.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [x] #1 Creare script generate_safety_diagrams.py
- [x] #2 Generare grafico corrente vs tempo effetti fisiologici (curva IEC)
- [x] #3 Generare schema impianto messa a terra stazione radio
- [x] #4 Generare schema principio funzionamento differenziale
- [x] #5 Generare schema scaricatore antenna (gas discharge)
- [x] #6 Integrare diagrammi in 10_Protezione_Elettrica/
<!-- AC:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
Creato script generate_safety_diagrams.py con 4 funzioni:
- plot_curva_iec(): curva IEC 60479-1 effetti corrente vs tempo (zone AC-1/2/3/4)
- schema_messa_terra(): impianto completo stazione con barra equipotenziale e picchetti
- schema_differenziale(): principio funzionamento ID con confronto normale/guasto
- schema_scaricatore(): gas discharge tube per protezione antenna da fulmini

Generate 4 immagini PNG in images/10_protezione/.
Integrate in 10_Protezione_Elettrica.md nelle sezioni appropriate.
<!-- SECTION:NOTES:END -->
