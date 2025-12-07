---
id: task-27
title: Consolidare e ottimizzare script Python
status: To Do
assignee: []
created_date: '2025-12-07 16:23'
labels:
  - scripts
  - maintenance
dependencies: []
priority: low
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Migliorare la manutenibilità degli script Python: standardizzare i path, aggiungere gestione errori, creare funzioni riutilizzabili e documentare i parametri configurabili.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Standardizzare tutti i path usando pathlib (eliminare path relativi ../images)
- [ ] #2 Aggiungere try-except con logging per gestione errori
- [ ] #3 Creare modulo utils.py con funzioni comuni (salvataggio, stile grafico)
- [ ] #4 Aggiungere docstring a tutte le funzioni
- [ ] #5 Aggiornare generate_images.sh per eseguire tutti gli script in ordine
- [ ] #6 Verificare che tutti gli script funzionino correttamente
<!-- AC:END -->
