# `team/train_prediction.py`

팀 기록 모델을 시간 순서로 학습·평가하는 명령 코드



[실제 코드 열기](../../../team/train_prediction.py)



## 이 파일을 읽을 때

1. 입력을 어디서 받는지 찾습니다.

2. 값을 바꾸는 계산과 DB를 읽거나 쓰는 부분을 구분합니다.

3. 마지막 `return` 또는 화면/이벤트 연결을 확인합니다.



## 연결된 Python 모듈

```python

from collections import Counter

from datetime import datetime, timezone

import json

import math

from pathlib import Path

from team.match_prediction import FEATURE_NAMES, MODEL_VERSION, chronological_split, load_matches, model_path, predict_probabilities, training_rows

```

## 함수·클래스 안내

### `train_model` — 22행

입력 이름: `output`

찾아볼 반환 사전 키(분기·내부 함수 포함): `accuracy`, `precision_macro`, `recall_macro`, `f1_macro`, `log_loss`, `confusion_matrix`, `prediction_counts`

읽을 때 따라갈 호출(중복 제외): `load_matches`, `training_rows`, `chronological_split`, `sorted`, `range`, `min`, `probabilities`, `Counter`, `max`, `fit`, `target.parent.mkdir`, `target.with_suffix`, `temporary.write_text`, `temporary.replace`, `make_pipeline`, `pipeline.fit`, `fitted.predict_proba`, `precision_recall_fscore_support`, `len`, `ValueError`, `summarize`, `dict`, `math.log`, `np.zeros`, `np.ones`, `datetime.now(timezone.utc).isoformat`, `np.allclose`, `RuntimeError`

