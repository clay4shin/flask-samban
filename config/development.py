from config.default import *

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'samban1.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'F\x1cg\x88\xb3\x0b1C\x1e\xd0I>\x93XG\xd3'

