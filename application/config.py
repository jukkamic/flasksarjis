class Config():
    FLASK_APP="application/app.py"
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            'file': {
                'level': 'DEBUG',
                'class': 'logging.FileHandler',
                'filename': 'debug-sarjis.log',
            },
            'console': {
                'class': 'logging.StreamHandler',
            },
        },
        'loggers': {
            'sarjis': {
                'handlers': ['file','console'],
                'level': 'DEBUG',
                'propagate': True,
            },
        },
    }
