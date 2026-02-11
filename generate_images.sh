#!/bin/bash
#
# Script per generare tutte le immagini dai grafici Python.
# Attiva automaticamente il venv e esegue tutti gli script in ordine.
#
# Uso: ./generate_images.sh [--verbose] [--script nome_script.py]
#

set -e  # Esce su errori

# Colori per output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Contatori
TOTAL=0
SUCCESS=0
FAILED=0

# Opzioni
VERBOSE=false
SINGLE_SCRIPT=""

# Parse argomenti
while [[ $# -gt 0 ]]; do
    case $1 in
        --verbose|-v)
            VERBOSE=true
            shift
            ;;
        --script|-s)
            SINGLE_SCRIPT="$2"
            shift 2
            ;;
        *)
            echo "Uso: $0 [--verbose] [--script nome_script.py]"
            exit 1
            ;;
    esac
done

# Funzione per stampare messaggi
log_info() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

log_warn() {
    echo -e "${YELLOW}[WARN]${NC} $1"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Controlla se il venv esiste
if [ ! -d ".venv" ] && [ ! -d "venv" ]; then
    log_error "Virtual environment '.venv' o 'venv' non trovato."
    echo "Crealo con: python3 -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt"
    exit 1
fi

# Determina quale venv usare
if [ -d ".venv" ]; then
    VENV_DIR=".venv"
elif [ -d "venv" ]; then
    VENV_DIR="venv"
fi

# Attiva il venv
log_info "Attivando virtual environment in $VENV_DIR..."
source "$VENV_DIR/bin/activate"

# Verifica se l'attivazione e' riuscita
if [ "$VIRTUAL_ENV" = "" ]; then
    log_error "Impossibile attivare il venv."
    exit 1
fi

log_info "Virtual environment attivato: $VIRTUAL_ENV"
echo ""

# Crea symlink images -> website/static/images per compatibilita' con gli script
if [ ! -e "images" ]; then
    ln -s website/static/images images
    log_info "Creato symlink images -> website/static/images"
fi

# Esegui uno script singolo se specificato
if [ -n "$SINGLE_SCRIPT" ]; then
    if [ -f "scripts/$SINGLE_SCRIPT" ]; then
        log_info "Eseguendo scripts/$SINGLE_SCRIPT..."
        python "scripts/$SINGLE_SCRIPT"
        exit $?
    else
        log_error "Script non trovato: scripts/$SINGLE_SCRIPT"
        exit 1
    fi
fi

# Ordine consigliato degli script (dipendenze)
ORDERED_SCRIPTS=(
    # Capitolo 1: Elettronica base
    "plot_segnale_sinusoidale.py"
    "plot_segnale_quadra.py"
    "plot_campo_elettrico.py"
    "plot_campo_magnetico.py"
    "plot_modulazione_am.py"
    "plot_modulazione_fm.py"
    "plot_polarizzazioni.py"

    # Capitolo 2: Componenti
    "plot_resistore_vi.py"
    "plot_condensatore_carica.py"
    "plot_reattanza_frequenza.py"
    "generate_component_diagrams.py"
    "generate_diagrams.py"
    "generate_additional_diagrams.py"

    # Capitolo 3: Circuiti
    "generate_circuits_chapter3.py"
    "generate_filter_diagrams.py"
    "generate_power_supply_diagrams.py"
    "generate_amplifier_diagrams.py"
    "generate_detector_diagrams.py"
    "generate_oscillator_diagrams.py"
    "generate_pll_diagrams.py"
    "plot_bode_diagrams.py"

    # Capitolo 4: Ricevitori
    "generate_receiver_diagrams.py"

    # Capitolo 5: Trasmettitori
    "generate_transmitter_diagrams.py"

    # Capitolo 6: Antenne
    "plot_antenna_patterns.py"
    "generate_matching_networks.py"
    "plot_transmission_lines.py"

    # Capitolo 7: Propagazione
    "plot_ionosphere.py"

    # Capitolo 8-9: Misure e Interferenze
    "generate_measurement_diagrams.py"
    "generate_interference_diagrams.py"

    # Capitolo 10: Sicurezza
    "generate_safety_diagrams.py"

    # Operativa
    "plot_frequency_plans.py"
    "plot_modulation_comparison.py"
)

log_info "Generazione immagini in corso..."
echo ""

# Esegui script in ordine
for script in "${ORDERED_SCRIPTS[@]}"; do
    if [ -f "scripts/$script" ]; then
        TOTAL=$((TOTAL + 1))

        if [ "$VERBOSE" = true ]; then
            echo "----------------------------------------"
            echo "Eseguendo: $script"
            echo "----------------------------------------"
            if python "scripts/$script"; then
                SUCCESS=$((SUCCESS + 1))
                log_info "$script completato"
            else
                FAILED=$((FAILED + 1))
                log_error "$script FALLITO"
            fi
            echo ""
        else
            printf "%-45s" "Eseguendo $script..."
            if python "scripts/$script" > /dev/null 2>&1; then
                SUCCESS=$((SUCCESS + 1))
                echo -e "${GREEN}OK${NC}"
            else
                FAILED=$((FAILED + 1))
                echo -e "${RED}ERRORE${NC}"
            fi
        fi
    fi
done

# Esegui eventuali script non in lista
for script in scripts/*.py; do
    if [ -f "$script" ]; then
        basename_script=$(basename "$script")

        # Salta utils.py e check_elements.py
        if [[ "$basename_script" == "utils.py" ]] || [[ "$basename_script" == "check_elements.py" ]]; then
            continue
        fi

        # Salta se gia' eseguito
        if [[ " ${ORDERED_SCRIPTS[*]} " =~ " ${basename_script} " ]]; then
            continue
        fi

        TOTAL=$((TOTAL + 1))
        printf "%-45s" "Eseguendo $basename_script..."
        if python "$script" > /dev/null 2>&1; then
            SUCCESS=$((SUCCESS + 1))
            echo -e "${GREEN}OK${NC}"
        else
            FAILED=$((FAILED + 1))
            echo -e "${RED}ERRORE${NC}"
        fi
    fi
done

# Riepilogo
echo ""
echo "========================================"
log_info "Generazione completata!"
echo "  Totale:    $TOTAL script"
echo -e "  ${GREEN}Successo:${NC}  $SUCCESS"
if [ $FAILED -gt 0 ]; then
    echo -e "  ${RED}Falliti:${NC}   $FAILED"
fi
echo "========================================"
echo ""
log_info "Immagini salvate in: website/static/images/"

# Exit con errore se ci sono stati fallimenti
if [ $FAILED -gt 0 ]; then
    exit 1
fi
