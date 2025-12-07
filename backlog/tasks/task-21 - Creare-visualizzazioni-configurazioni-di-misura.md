---
id: task-21
title: Creare visualizzazioni configurazioni di misura
status: Done
assignee:
  - '@claude'
created_date: '2025-12-07 16:19'
updated_date: '2025-12-07 17:23'
labels:
  - diagrams
  - chapter8
  - schemdraw
dependencies: []
priority: medium
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Creare diagrammi per le configurazioni tipiche di misura: setup per misura di potenza, misura ROS, calibrazione antenna, test di linearità amplificatore.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [x] #1 Aggiungere funzioni a generate_measurement_diagrams.py
- [x] #2 Generare schema setup misura potenza in uscita TX
- [x] #3 Generare schema setup misura ROS antenna
- [x] #4 Generare schema setup test due toni per linearità
- [x] #5 Generare schema posizionamento sonde oscilloscopio
- [x] #6 Integrare diagrammi in 08_Misure/2_Tecniche_Misura.md
<!-- AC:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
Aggiunte 4 funzioni a generate_measurement_diagrams.py:
- setup_misura_potenza_tx(): TX → Wattmetro → Carico 50Ω
- setup_misura_ros(): TX → ROSmetro → Antenna con letture SWR
- setup_test_due_toni(): generatori audio → TX SSB → analizzatore spettro IMD
- setup_sonde_oscilloscopio(): posizionamento sonde CH1/CH2 su circuito

Generate 4 immagini PNG in images/08_misure/.
Integrate in 8.2_Strumenti_di_misura.md nella nuova sezione "Configurazioni di Misura".
<!-- SECTION:NOTES:END -->
