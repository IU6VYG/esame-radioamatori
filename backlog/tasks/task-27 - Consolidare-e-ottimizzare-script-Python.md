---
id: task-27
title: Consolidare e ottimizzare script Python
status: Done
assignee:
  - '@claude'
created_date: '2025-12-07 16:23'
updated_date: '2025-12-07 22:59'
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
- [x] #1 Standardizzare tutti i path usando pathlib (eliminare path relativi ../images)
- [x] #2 Aggiungere try-except con logging per gestione errori
- [x] #3 Creare modulo utils.py con funzioni comuni (salvataggio, stile grafico)
- [x] #4 Aggiungere docstring a tutte le funzioni
- [x] #5 Aggiornare generate_images.sh per eseguire tutti gli script in ordine
- [x] #6 Verificare che tutti gli script funzionino correttamente
<!-- AC:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
Implementato modulo utils.py con:
- Path management con pathlib
- Logging configurabile
- Stili matplotlib comuni
- Palette colori per diagrammi
- Utility di disegno (draw_block_with_shadow, etc.)
- Wrapper error handling

Aggiornati 11 script per usare utils.
Migliorato generate_images.sh con opzioni --verbose e --script.
Tutti 32 script verificati con successo.
<!-- SECTION:NOTES:END -->
