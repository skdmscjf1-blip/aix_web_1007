# `install_site_navigation.py`

프로젝트 실행 도구



[실제 코드 열기](../../install_site_navigation.py)



## 이 파일을 읽을 때

1. 입력을 어디서 받는지 찾습니다.

2. 값을 바꾸는 계산과 DB를 읽거나 쓰는 부분을 구분합니다.

3. 마지막 `return` 또는 화면/이벤트 연결을 확인합니다.



## 연결된 Python 모듈

```python

from datetime import datetime

from pathlib import Path

import re

```

## 함수·클래스 안내

### `transform` — 567행

입력 이름: `relative`, `text`, `active`

읽을 때 따라갈 호출(중복 제외): `text.replace`, `text.count`, `ValueError`, `re.subn`, `re.sub`



### `main` — 669행

입력 이름: 

읽을 때 따라갈 호출(중복 제외): `dict`, `PAGES.items`, `planned.items`, `datetime.now().strftime`, `originals.items`, `print`, `(ROOT / 'manage.py').is_file`, `SystemExit`, `transform`, `text.encode`, `changed.items`, `path.is_file`, `path.read_text`, `path.exists`, `path.read_bytes`, `datetime.now`, `target.parent.mkdir`, `target.write_bytes`, `path.parent.mkdir`, `path.write_bytes`, `written.append`, `reversed`, `len`, `path.unlink`

