import logging
import logging.config

# Logging configuration function
def setup_logging():
    logging.config.dictConfig({
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'detailed': {
                'format': '%(asctime)s [%(levelname)s] %(name)s %(filename)s:%(lineno)d - %(message)s'
            },
        },
        'handlers': {
            'console': {
                'level': 'DEBUG',
                'formatter': 'detailed',
                'class': 'logging.StreamHandler',
            },
            'file': {
                'level': 'DEBUG',
                'formatter': 'detailed',
                'class': 'logging.FileHandler',
                'filename': 'application.log',
                'mode': 'a',
            }
        },
        'loggers': {
            '': {
                'handlers': ['console', 'file'],
                'level': 'DEBUG',
                'propagate': True
            }
        }
    })

# Initialize logging when the module is imported
setup_logging()
