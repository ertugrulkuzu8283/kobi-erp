import os
import logging
from logging.handlers import RotatingFileHandler

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)


def setup_logging() -> None:
    """Proje genelinde application.log, error.log ve audit.log altyapısını kurar."""
    
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    app_handler = RotatingFileHandler(
        os.path.join(LOG_DIR, "application.log"),
        maxBytes=10 * 1024 * 1024,
        backupCount=5,
        encoding="utf-8"
    )
    app_handler.setLevel(logging.INFO)
    app_handler.setFormatter(formatter)
    root_logger.addHandler(app_handler)

    error_handler = RotatingFileHandler(
        os.path.join(LOG_DIR, "error.log"),
        maxBytes=10 * 1024 * 1024,
        backupCount=5,
        encoding="utf-8"
    )
    error_handler.setLevel(logging.ERROR)
    error_handler.setFormatter(formatter)
    root_logger.addHandler(error_handler)

    audit_logger = logging.getLogger("erp.audit")
    audit_logger.setLevel(logging.INFO)
    audit_logger.propagate = False

    audit_handler = RotatingFileHandler(
        os.path.join(LOG_DIR, "audit.log"),
        maxBytes=10 * 1024 * 1024,
        backupCount=10,
        encoding="utf-8"
    )
    audit_handler.setLevel(logging.INFO)
    audit_formatter = logging.Formatter(
        "%(asctime)s | AUDIT | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    audit_handler.setFormatter(audit_formatter)
    audit_logger.addHandler(audit_handler)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)
    root_logger.addHandler(console_handler)