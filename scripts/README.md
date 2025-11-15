# Scripts per Generare Grafici

Questo repository contiene script Python per generare grafici utilizzati nelle pagine Markdown.

## Come Usare
1. Assicurati che il venv sia creato: `python3 -m venv venv` (se non esiste)
2. Installa dipendenze: `pip install -r requirements.txt` (con venv attivato)
3. Esegui tutti gli script: `./generate_images.sh` (attiva automaticamente il venv)
4. Le immagini verranno salvate in `images/`

## Script Disponibili
- `plot_campo_elettrico.py`: Genera il grafico del campo elettrico vs distanza.
- `plot_campo_magnetico.py`: Genera il grafico del campo magnetico attorno a un conduttore.
- `plot_polarizzazioni.py`: Genera i grafici delle polarizzazioni (lineare, circolare destra/sinistra, ellittica).