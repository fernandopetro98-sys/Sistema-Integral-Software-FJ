
# Configuración del registro de eventos y errores
# Sistema Integral de Gestión Software FJ.

import logging
from pathlib import Path

# Ubicación del archivo de registro.
RUTA_LOG = Path(__file__).parent / "sistema.log"

# Configuración del sistema de logs.
logging.basicConfig(
    filename=RUTA_LOG,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%d/%m/%Y %H:%M:%S",
    encoding="utf-8",
    force=True
)

# Registrador general del sistema.
logger = logging.getLogger("SoftwareFJ")


def registrar_evento(mensaje):
    """Registra un evento normal del sistema."""
    logger.info(mensaje)


def registrar_error(mensaje):
    """Registra un error del sistema."""
    logger.error(mensaje)
