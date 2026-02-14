# esame-radioamatori

> [!WARNING]
> Questi sono **appunti personali** e possono contenere errori o imprecisioni.
> Non sostituiscono libri di testo o fonti ufficiali.
> Il materiale è soggetto a revisione continua grazie al contributo volontario della comunità.
> [Contribuisci su GitHub](https://github.com/IU6VYG/esame-radioamatori)

Questo repository contiene materiali di studio organizzati per preparare l'esame di radioamatore. I contenuti sono estratti e strutturati dal programma ufficiale (Sub_Allegato_D_All.26.pdf), divisi in macroargomenti e argomenti specifici per facilitare lo studio.

## Sito Web

I materiali sono disponibili come sito navigabile: **[Esame Radioamatori](https://iu6vyg.github.io/esame-radioamatori/)**

## Struttura del Progetto

I documenti si trovano in `website/docs/`, organizzati in tre sezioni:

- **A. Tecnica** (Capitoli 1-10): Elettricita, componenti, circuiti, ricevitori, trasmettitori, antenne, propagazione, misure, disturbi, protezione elettrica
- **B. Operativa**: Alfabeto fonetico, codice Q, abbreviazioni, segnali di soccorso, indicativi, piani frequenze IARU
- **C. Regolamentazione**: Regolamento UIT, CEPT, legislazione nazionale

## Sviluppo Locale

### Sito Docusaurus

```bash
cd website
npm install
npm start        # Server di sviluppo
npm run build    # Build di produzione
```

### Generare Immagini

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
./generate_images.sh
```

## Deploy

Il sito viene automaticamente pubblicato su GitHub Pages ad ogni push su `main` tramite GitHub Actions.

Buono studio per l'esame di radioamatore!
