import logging
from logging.config import dictConfig

logging_config = {
    "version": 1,
    "disable_existing_loggers": True,
    "formatters": {
        "default": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "default",
            "level": "DEBUG",
        },
    },
    "loggers": {
        "yp": { 
            "handlers": ["console"],
            "level": "DEBUG",
            "propagate": False,
        },
    },
}

def setup_logging():
    """
    setup logging configuration
    """
    dictConfig(logging_config)
