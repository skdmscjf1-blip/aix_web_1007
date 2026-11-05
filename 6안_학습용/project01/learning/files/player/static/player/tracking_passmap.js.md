# `player/static/player/tracking_passmap.js`

선수 조회·공통 평가·BEST11·연구실



[실제 코드 열기](../../../../../player/static/player/tracking_passmap.js)



## 이 파일을 읽을 때

1. 입력을 어디서 받는지 찾습니다.

2. 값을 바꾸는 계산과 DB를 읽거나 쓰는 부분을 구분합니다.

3. 마지막 `return` 또는 화면/이벤트 연결을 확인합니다.



## 처음 읽는 순서

1. 위쪽 DOM 조회: `getElementById` / `querySelector`

2. 작은 도구: 숫자 표시·요청·저장

3. 사용자 조작: `click` / `change` / `addEventListener`

4. 데이터 요청: `fetch` → URL → View

5. 표시: `textContent`, class, Canvas 그리기

## 이름이 있는 함수

- `screen`

- `drawField`

- `drawPass`

- `draw`

- `tick`

## 수정 기준

브라우저 이벤트 순서·전역 함수·DOM id·저장 키는 유지했습니다. `var`를 무조건 `let`으로 바꾸거나 함수를 다른 파일로 옮기면 범위와 실행 시점이 달라질 수 있습니다. 같은 로직이라도 변수 이름 변경은 참조 관계부터 확인하세요.