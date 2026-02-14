---
id: task-32
title: Correzione errori nel documento Regolamento Radiocomunicazioni UIT
status: Done
assignee:
  - '@claude'
created_date: '2026-02-14 17:06'
updated_date: '2026-02-14 17:09'
labels:
  - docs
  - fix
  - ITU
dependencies: []
priority: high
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Correggere gli errori e le imprecisioni trovati nel confronto tra il contenuto del sito (C.1 Regolamento delle Radiocomunicazioni dell'UIT) e le fonti ufficiali ITU (Radio Regulations, edizione 2024). Gli errori includono: numero paesi membri, limiti di potenza attribuiti erroneamente all'UIT, statuti bande invertiti, nome articolo S25 vs 25, bande mancanti, definizioni imprecise, quiz con risposte errate.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [x] #1 Numero paesi membri UIT corretto a 193
- [x] #2 Tabella limiti di potenza rimossa o corretta per indicare che l'UIT non fissa limiti (Art. 25.7)
- [x] #3 Statuti bande HF corretti (160m e 80m sono primarie in Regione 1)
- [x] #4 Articolo S25 rinominato in Articolo 25 in tutto il documento
- [x] #5 Contenuto Articolo 25 completato con tutti i punti fondamentali (25.1-25.11)
- [x] #6 Definizione stazione Art. 1.81 corretta per riflettere il testo ITU
- [x] #7 Regioni UIT con definizioni geografiche corrette e acronimo CEPT
- [x] #8 Bande HF mancanti aggiunte (2200m, 630m, 60m, 30m, 17m, 12m)
- [x] #9 Quiz corretto (domande 2 e 5)
- [x] #10 Tabella bande HF completa con dati da fonte ufficiale ITU
<!-- AC:END -->

## Implementation Plan

<!-- SECTION:PLAN:BEGIN -->
1. Correggere numero paesi membri (186 → 193)
2. Rinominare "Articolo S25" in "Articolo 25" ovunque nel documento
3. Riscrivere sezione Articolo 25 con tutti i punti ufficiali (25.1-25.11)
4. Sostituire tabella limiti di potenza con nota che l'UIT delega alle amministrazioni nazionali
5. Correggere definizione Art. 1.81 (testo minimalista ITU + spiegazione componenti come approfondimento)
6. Correggere tabella bande HF: statuti corretti + aggiungere bande mancanti
7. Aggiornare diagramma bande HF
8. Correggere sezione Regioni UIT con definizioni geografiche precise e acronimo CEPT
9. Correggere quiz domande 2 e 5
10. Correggere definizione "statuto primario" vs "esclusivo"
<!-- SECTION:PLAN:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
Corretto il documento C.1 Regolamento delle Radiocomunicazioni dell'UIT allineandolo alle fonti ufficiali ITU (Radio Regulations, edizione 2024).\n\nCorrezioni applicate:\n- Numero stati membri UIT: 186 → 193\n- Articolo S25 → Articolo 25 (prefisso S eliminato dal 2004)\n- Sezione Articolo 25 completamente riscritta con tutti i punti ufficiali (25.1–25.11), divisa in Sezione I (Servizio di Radioamatore) e Sezione II (Servizio Satellite)\n- Rimossa tabella limiti di potenza errata (attribuita all'UIT ma in realtà nazionale); sostituita con spiegazione corretta dell'Art. 25.7\n- Definizione stazione Art. 1.81 corretta con testo ufficiale ITU + componenti come approfondimento pratico\n- Tabella bande HF: corretti statuti (160m e 80m sono primarie, non secondarie), aggiunte 6 bande mancanti (2200m, 630m, 60m, 30m, 17m, 12m)\n- Definizione statuto primario corretta (non significa esclusivo)\n- Regioni UIT: aggiunte definizioni geografiche precise con Linee A/B/C, corretto acronimo ECA → CEPT, aggiunta CSI e Mongolia in Regione 1\n- Quiz: corrette domande 2 (potenza), 4 (primario vs esclusivo) e 5 (articolo 25)\n- Diagramma mermaid bande aggiornato con tutte le 12 bande\n\nFile modificato: website/docs/C_Regolamentazione/1_Regolamento_Radiocomunicazioni_UIT.md\nBuild Docusaurus verificata: compilazione OK senza errori.
<!-- SECTION:NOTES:END -->
