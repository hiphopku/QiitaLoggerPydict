import os
from logging import getLogger
from logging.config import dictConfig


APP_NAME = os.getenv('APP_NAME', default='app_with_pydict')
CONFIG = {
    'version': 1, 
    'disable_existing_loggers': False,
    'formatters': {
        'basic': {
            'format': '%(asctime)s  [%(name)s][%(levelname)s]  %(message)s  (%(module)s:%(filename)s:%(funcName)s:%(lineno)d)', 
            'datefmt': '%Y-%m-%d %H:%M:%S'
            }
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler', 
                'level': 'DEBUG', 
                'formatter': 'basic', 
                'stream': 'ext://sys.stdout'
            }, 
            'file': {
                'class': 'logging.handlers.TimedRotatingFileHandler', 
                'formatter': 'basic', 
                'filename': os.path.join(os.path.pardir, 'log', 'application.log'), 
                'when': 'D', 
                'interval': 1, 
                'backupCount': 31
            }, 
            'error': {
                'class': 'logging.handlers.TimedRotatingFileHandler', 
                'level': 'ERROR', 
                'formatter': 'basic', 
                'filename': os.path.join(os.path.pardir, 'log', 'error.log'), 
                'when': 'D', 
                'interval': 1, 
                'backupCount': 31
            }
        }, 
        'loggers': {
            APP_NAME: {
                'level': 'INFO', 
                'handlers': [
                    'console', 
                    'file', 
                    'error'
                ], 
                'propagate': False
            }
        }, 
        'root': {
            'level': 'INFO', 
            'handlers': [
                'console', 
                'file', 
                'error'
            ] 
        }
    }


def init_logger():
    dictConfig(CONFIG)


def get_logger():
    return getLogger(APP_NAME)