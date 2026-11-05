# 6안 전체 실행 코드 학습용 버전

기준: GitHub `82f2862`의 `6안/6안/project01`. 기존 프로그램을 복사해 계산과 화면 연결을 유지하면서 공부하기 쉽게 정리했습니다. 원본 폴더나 GitHub에는 적용하지 않았습니다.

## 무엇을 정리했나요?

- Python 실행 파일 141개: 역할 설명, 중요한 처리 순서, 한 줄에 몰린 코드와 들여쓰기 정리
- JavaScript 20개: 조건문·객체·함수 표현을 펼치고 주요 동작에 설명 추가
- CSS 11개: 규칙과 값을 보존하며 읽기 쉬운 배치로 정리
- HTML 33개: 역할 안내와 연결된 파일 안내, 독립 코드 11개를 정적 파일로 분리
- 파일별 공부 안내 205개: 입력·함수·참조·모델 필드·화면 연결·수정 시 확인점

특히 BEST11 HTML은 4,760행에서 1,317행으로 줄였습니다. 사라진 기능이 아니라 장식과 조작 코드가 별도 파일로 옮겨졌습니다. 연구실의 비중 적용·경험 보정과 스코어 확률은 계산 단계별로 풀어 썼습니다. 모든 함수를 새 알고리즘으로 교체한 것은 아닙니다.

DB와 모델 필드·관계·URL·선수 ID·기본 가중치는 유지했습니다. migration과 과거 백업/참고 코드도 원본을 보존했습니다. 과거 참고 파일의 문법 오류는 현재 실행 코드의 오류와 구분해 기록했습니다.

## 먼저 실행하기

새 폴더의 `manage.py`가 있는 곳에서 기존 6안을 실행하던 Python 가상환경을 사용합니다. 이번 작업은 실행용 패키지를 추가하지 않았습니다.

```powershell
python manage.py check
python manage.py runserver
```

새 환경은 Python 버전을 먼저 맞추고 Django 5.2.18과 `prediction_requirements.txt`의 패키지가 필요합니다. 이번 비교 환경은 Linux Python 3.12 / Django 5.2.18이며 Windows Python 3.13 전체 검증을 대신하지 않습니다.

모델 변경이 없으므로 이번 정리를 적용하기 위해 `makemigrations`나 DB 초기화를 할 필요는 없습니다.

## 공부 순서

1. [문법과 데이터 흐름](02_문법과데이터흐름.md): result, filter, return, round
2. [DB 모델 지도](06_DB모델지도.md)와 `player/models.py`: 선수와 시즌 기록 관계
3. `player/views.py`의 `plist` / `pview`: 검색 조건 → 조회 → 화면
4. `player/scoring.py`: 지표·범주·비중·정규화
5. `player/services.py`: 점수와 구단별 BEST11
6. `player/lab/service.py`: 내 설정·경험·케미·분석
7. `team/match_prediction.py`와 `lineup_simulation.py`: 팀 기록과 선수 구성 확률
8. `simulation/tracking_metrics.py`와 `event_metrics.py`: 좌표와 행동을 컬럼으로 바꾸기
9. `soccer_game/static/js/script.js`: 현재 6안 게임의 공·선수·프레임 흐름
10. `manager`·`board`: 입력 검사와 안전한 저장

모든 폴더의 `STUDY.md`에서 개별 파일 안내로 이동할 수 있습니다. [전체 실행 코드 지도](01_전체파일지도.md)와 [수정 위치 찾기](07_수정위치찾기.md)를 함께 보세요.

## 세 가지 언어를 따로 읽기

- **HTML**: 무엇이 화면에 있는가? 입력·표·카드·Django 표시 값
- **CSS**: 어디에 어떤 모습으로 놓이는가? 색·크기·배치·반응형 규칙
- **JavaScript**: 클릭하면 무엇을 하는가? 선택·요청·저장·화면 갱신
- **Python**: 서버에서 무엇을 조회·계산·저장하는가?

`player/static/player/readable/` 등에는 HTML에서 분리한 코드가 있습니다. 기존 파일명이 가리키는 기능을 유지하기 위해 전체 폴더 이름을 새로 바꾸지는 않았습니다.

## 수정·추가 연습

[수정과 추가 연습](03_수정과추가연습.md)에서 가중치 수정, 기존 기록으로 새 지표 만들기, 진짜 DB 컬럼 추가를 구분합니다. [초보 문법 사전](08_초보문법사전.md)에는 용어와 사용 이유가 있습니다.

## 검증하기

```powershell
python manage.py test learning.tests
python learning/verify_results.py
```

첫 명령은 중요한 계산 의미를 확인하는 10개 검사입니다. DB를 쓰지 않습니다. 두 번째는 원래 DB·설정 기준의 점수·명단·GPS 결과와 비교합니다. 112가지 입력을 계산하므로 시간이 걸릴 수 있습니다. 실제 자료나 비중을 바꿨다면 기존 기준과 달라질 수 있습니다.

[정리 전후 검증](05_정리전후검증.md)에서 확인 범위와 아직 검증하지 않은 작업을 구분해 보세요.
