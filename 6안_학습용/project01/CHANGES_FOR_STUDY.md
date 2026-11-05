# 전체 코드 정리 변경 내역

Python 141 · JavaScript 20 · CSS 11 · HTML 33 / 파일별 안내 205개

## 실행 결과를 유지하며 읽기 쉽게 정리한 핵심
- 1차 공통 점수·BEST11·GPS 정리를 유지
- 연구실의 비중 우선순위와 경험 보정을 단계별로 풀어쓰기
- 예상 득점에서 승무패 확률을 구하는 반복문을 조건문으로 풀어쓰기
- 모든 실행 Python의 역할·주소·입력·계산·저장 경계를 안내
- 독립 인라인 CSS/JS 11개를 정적 파일로 분리
- 기존 함수·DOM id·CSS 선택자·DB 관계·가중치 유지

## HTML에서 분리한 파일
- `board/templates/board/form.html` → `board/static/board/readable/form_inline_1.js`
- `board/templates/board/login.html` → `board/static/board/readable/login_inline_1.js`
- `home/templates/index.html` → `home/static/home/readable/index_inline_1.css`
- `manager/templates/manager/base.html` → `manager/static/manager/readable/base_inline_1.css`
- `manager/templates/manager/upload.html` → `manager/static/manager/readable/upload_inline_1.css`
- `manager/templates/manager/upload.html` → `manager/static/manager/readable/upload_inline_2.js`
- `player/templates/player/best11.html` → `player/static/player/readable/best11_inline_1.css`
- `player/templates/player/best11.html` → `player/static/player/readable/best11_inline_2.js`
- `player/templates/player/best11.html` → `player/static/player/readable/best11_inline_3.js`
- `player/templates/player/tracking_demo.html` → `player/static/player/readable/tracking_demo_inline_1.css`
- `team/templates/team/predict_match.html` → `team/static/team/readable/predict_match_inline_1.css`

## 확인
DB·JSON·CSV·이미지·migration은 원본 해시와 일치합니다. 학습 문서는 실행에 필요하지 않으며 바로 열어 볼 수 있습니다. 이번 버전은 GitHub에 푸시하지 않았습니다.