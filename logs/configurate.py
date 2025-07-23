import os
from logging.config import dictConfig

conf = {
    'version': 1,
    'formatters': {
        'standart': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        },
        'debug': {
            'format': '%(asctime)s - %(levelname)s - %(module)s:%(lineno)d - %(message)s'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'standart',
            'level': 'INFO',
            'stream': 'ext://sys.stdout'
        },
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'debug',
            'level': 'DEBUG',
            'filename': os.path.join('file_logs', 'debug.log'),
            'encoding': 'UTF-8',
            'maxBytes': 1024*1024*10,
            'backupCount': 3
        }
    },
    'loggers': {
        '': {
            'level': 'DEBUG',
            'handlers': ['console', 'file'],
            'propagate': False
        }
    }
}