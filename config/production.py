from config.default import *
from logging.config import dictConfig
from dotenv import load_dotenv

load_dotenv(os.path.join(BASE_DIR, '.env'))

SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(
    user=os.getenv('DB_USER'),
    pw=os.getenv('DB_PASSWORD'),
    url=os.getenv('DB_HOST'),
    db=os.getenv('DB_NAME'))

SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'F\x1cg\x88\xb3\x0b1C\x1e\xd0I>\x93XG\xd3'

dictConfig({
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
        }
    },
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/samban.log'),
            'maxBytes': 1024 * 1024 * 5,  # 5 MB
            'backupCount': 5,
            'formatter': 'default',
        },
    },
    'root': {
        'level': 'INFO',
        'handlers': ['file']
    }
})
