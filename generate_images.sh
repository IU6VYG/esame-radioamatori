#!/bin/bash

# Script per generare tutte le immagini dai grafici Python
# Attiva automaticamente il venv se esiste

# Controlla se il venv esiste (prova .venv o venv)
if [ ! -d ".venv" ] && [ ! -d "venv" ]; then
    echo "Errore: Virtual environment '.venv' o 'venv' non trovato. Crealo con 'python3 -m venv .venv' o 'python3 -m venv venv'."
    exit 1
fi

# Determina quale venv usare
if [ -d ".venv" ]; then
    VENV_DIR=".venv"
elif [ -d "venv" ]; then
    VENV_DIR="venv"
fi

# Attiva il venv
echo "Attivando virtual environment in $VENV_DIR..."
source "$VENV_DIR/bin/activate"

# Verifica se l'attivazione è riuscita
if [ "$VIRTUAL_ENV" != "" ]; then
    echo "Virtual environment attivato: $VIRTUAL_ENV"
else
    echo "Errore: Impossibile attivare il venv."
    exit 1
fi

echo "Generando immagini dai grafici..."

# Esegui tutti gli script Python nella cartella scripts/
for script in scripts/*.py; do
    if [ -f "$script" ]; then
        echo "Eseguendo $script..."
        python "$script"
    fi
done

echo "Tutte le immagini generate in images!"