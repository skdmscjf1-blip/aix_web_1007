"""학습용 검증은 DB를 읽기 전용으로 엽니다."""
from project01.settings import *
DATABASES = {'default': {'ENGINE': 'django.db.backends.sqlite3', 'NAME': f'file:{BASE_DIR / "db.sqlite3"}?mode=ro', 'OPTIONS': {'uri': True}}}
