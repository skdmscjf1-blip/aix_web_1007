# `manager/templates/manager/exclusions.html`

관리자 입력 검토·반영·백업·기본 설정



[실제 코드 열기](../../../../../manager/templates/manager/exclusions.html)



## 이 파일을 읽을 때

1. 입력을 어디서 받는지 찾습니다.

2. 값을 바꾸는 계산과 DB를 읽거나 쓰는 부분을 구분합니다.

3. 마지막 `return` 또는 화면/이벤트 연결을 확인합니다.



## Template 문법

- `{{ 이름 }}`: View가 넘긴 값을 표시합니다.

- `{% if %}`: 조건에 맞는 부분만 표시합니다.

- `{% for %}`: 목록을 반복 표시합니다.

- `{% include %}` / `{% extends %}`: 공통 화면을 연결합니다.

- `{% static %}`: CSS·JavaScript의 주소를 만듭니다.

## 이 화면에서 사용하는 연결

- `{% extends 'manager/base.html' %}`

## 수정 기준

class·id·name은 JavaScript와 CSS가 함께 참조할 수 있습니다. 이름을 바꾸기 전에 프로젝트 전체 검색으로 사용처를 확인하세요. Django 변수를 쓰는 인라인 코드는 무리하게 정적 파일로 옮기지 않았습니다.