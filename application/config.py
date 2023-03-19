import uuid

class Config:
    FLASK_APP="application/app.py"
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
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

class DevelopmentConfig(Config):
    SECRET_KEY='dev'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///sarjis.sqlite'
    MAX_CONTENT_LENGTH = 1 * 1000 * 1000

class ProductionConfig(Config):
    SECRET_KEY=uuid.uuid4().hex
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:secret@database'
    MAX_CONTENT_LENGTH = 1 * 1000 * 1000
    # username = 'flaskr_admin'
    # password = 'postgres'
    # database = 'flaskr'
    # SQLALCHEMY_DATABASE_URI = f'postgresql+psycopg2://{username}:{password}@localhost:5432/{database}'
