# `manager/importer.py`

업로드 자료 분석·항목 변환·검토·실제 반영



[실제 코드 열기](../../../manager/importer.py)



## 이 파일을 읽을 때

1. 입력을 어디서 받는지 찾습니다.

2. 값을 바꾸는 계산과 DB를 읽거나 쓰는 부분을 구분합니다.

3. 마지막 `return` 또는 화면/이벤트 연결을 확인합니다.



## 연결된 Python 모듈

```python

import hashlib

import io

import json

import re

import zipfile

import datetime as dt

import pandas as pd

```

## 함수·클래스 안내

### `norm` — 25행

입력 이름: `text`

읽을 때 따라갈 호출(중복 제외): `re.sub('[\\s_\\-\\(\\)（）\\[\\]/·.]', '', str(text)).lower`, `re.sub`, `str`



### `lev1` — 177행

두 문자열이 글자 하나(바꿈/빠짐/끼움)만 다른가

입력 이름: `a`, `b`

읽을 때 따라갈 호출(중복 제외): `any`, `len`, `abs`, `sum`, `range`, `zip`



### `sub1` — 187행

길이가 같고 글자 하나만 다른가 (오타 판정용 — 글자가 빠지거나 늘어난 건 다른 항목으로 본다)

입력 이름: `a`, `b`

읽을 때 따라갈 호출(중복 제외): `len`, `sum`, `zip`



### `TeamResolver` — 197행

클래스 안의 작업: `__init__`, `resolve`, `find_in_text`, `strip_suffix`



### `ReadError` — 261행



### `_decode` — 265행

입력 이름: `data`

읽을 때 따라갈 호출(중복 제외): `ReadError`, `data.decode`



### `_image_kind` — 274행

입력 이름: `head`



### `sniff_format` — 286행

입력 이름: `filename`, `data`

읽을 때 따라갈 호출(중복 제외): `filename.lower`, `_image_kind`, `data[:2000].lstrip`, `low.endswith`, `any`, `zipfile.ZipFile(io.BytesIO(data)).namelist`, `zipfile.ZipFile`, `n.startswith`, `io.BytesIO`



### `_zip_name` — 318행

입력 이름: `info`

읽을 때 따라갈 호출(중복 제외): `name.encode('cp437').decode`, `name.encode`



### `expand_inputs` — 330행

zip 묶음을 풀어서 [(경로, bytes)] 로 펼침. 엑셀(xlsx)은 풀지 않음.

입력 이름: `files`, `notes`

읽을 때 따라갈 호출(중복 제외): `sniff_format`, `zf.infolist`, `notes.append`, `out.append`, `zipfile.ZipFile`, `info.is_dir`, `_zip_name`, `io.BytesIO`, `name.rsplit`, `name.startswith`, `base.startswith`, `base.lower`, `zf.read`



### `_flatten_columns` — 360행

입력 이름: `cols`

읽을 때 따라갈 호출(중복 제외): `isinstance`, `out.append`, `str(p).strip`, `' '.join`, `str(c).strip`, `parts.append`, `str`, `p.lower().startswith`, `p.lower`



### `_known` — 375행

입력 이름: `v`

읽을 때 따라갈 호출(중복 제외): `norm`, `any`, `len`, `sub1`



### `_find_header_row` — 382행

입력 이름: `raw`

읽을 때 따라갈 호출(중복 제외): `range`, `min`, `sum`, `len`, `raw.iloc[i].tolist`, `isinstance`, `_known`



### `_from_raw` — 391행

입력 이름: `raw`

읽을 때 따라갈 호출(중복 제외): `raw.dropna(how='all').dropna(how='all', axis=1).reset_index`, `_find_header_row`, `raw.iloc[h + 1:].reset_index`, `raw.copy`, `str(v).strip`, `raw.dropna(how='all').dropna`, `raw.iloc[h].tolist`, `range`, `str`, `raw.dropna`



### `_rows_to_table` — 403행

입력 이름: `rows`

읽을 때 따라갈 호출(중복 제외): `max`, `pd.DataFrame([r + [None] * (width - len(r)) for r in rows]).astype`, `len`, `pd.DataFrame`



### `_read_pdf` — 408행

입력 이름: `data`, `notes`

읽을 때 따라갈 호출(중복 제외): `pdfplumber.open`, `enumerate`, `ReadError`, `io.BytesIO`, `page.extract_tables`, `len`, `page.extract_text`, `text.strip`, `_from_raw`, `tables.append`, `notes.append`, `pd.DataFrame(rows).replace('', pd.NA).astype`, `re.split`, `_rows_to_table`, `pytesseract.image_to_string`, `ValueError`, `(c or '').replace('\n', ' ').strip`, `ln.strip`, `text.splitlines`, `page.to_image`, `pd.DataFrame(rows).replace`, `txt.splitlines`, `(c or '').replace`, `pd.DataFrame`, `type`



### `read_tables` — 474행

-> (표 목록 [(이름, DataFrame, 머리글 찾음)], 알림 목록)

입력 이름: `filename`, `data`

읽을 때 따라갈 호출(중복 제외): `sniff_format`, `ReadError`, `sheets.items`, `pd.read_excel`, `_from_raw`, `tables.append`, `_decode`, `enumerate`, `notes.append`, `io.BytesIO`, `pd.read_html`, `_flatten_columns`, `isinstance`, `io.StringIO`, `sum`, `json.loads`, `_read_pdf`, `max`, `t.astype`, `lists.items`, `pd.read_csv`, `obj.items`, `all`, `_known`, `pd.DataFrame`, `text[:3000].count`, `obj.values`, `list`



### `to_number` — 578행

-> (숫자 또는 None, 고친 경우 '원래값 → 고친값'). 실패하면 ValueError

입력 이름: `value`, `as_float`

읽을 때 따라갈 호출(중복 제외): `str(value).strip`, `re.sub('(?i)(cm|kg|%|분|회|명|원|세)$', '', s.replace(',', '')).strip`, `float`, `s.lower`, `re.fullmatch`, `re.search`, `isinstance`, `pd.isna`, `str`, `body.translate`, `re.sub`, `int`, `unit.group`, `s.replace`, `round`, `unit.start`



### `to_date` — 601행

입력 이름: `value`

읽을 때 따라갈 호출(중복 제외): `isinstance`, `str(value).strip`, `re.match`, `dt.date`, `value.date`, `s.lower`, `ValueError`, `int`, `pd.isna`, `str`



### `clean_text` — 617행

입력 이름: `v`

읽을 때 따라갈 호출(중복 제외): `re.sub('\\s+', ' ', str(v)).strip`, `isinstance`, `pd.isna`, `re.sub`, `str`



### `add_issue` — 623행

입력 이름: `issues`, `level`, `where`, `column`, `value`, `message`, `action`

읽을 때 따라갈 호출(중복 제외): `issues.append`, `dict`, `str`



### `map_columns` — 641행

컬럼 → (종류, 필드). 오타는 고치고, 모르는 컬럼은 원래 이름 그대로 유지

입력 이름: `df`, `registered`, `where`, `issues`

읽을 때 따라갈 호출(중복 제외): `norm`, `set`, `str(col).strip`, `used.add`, `str`, `add_issue`, `len`, `k.startswith`, `re.fullmatch`, `cands.pop`, `next`, `sub1`, `iter`



### `infer_name_column` — 719행

'성면'처럼 이름 컬럼의 머리글이 틀렸을 때, 값의 모양(한글 이름)으로 추정

입력 이름: `df`, `colmap`, `where`, `issues`

읽을 때 따라갈 호출(중복 제외): `colmap.items`, `add_issue`, `clean_text`, `len`, `str`, `df[c].tolist`, `re.fullmatch`, `set`



### `classify` — 760행

입력 이름: `colmap`, `has_fused_rank`

읽을 때 따라갈 호출(중복 제외): `colmap.values`



### `analyze_table` — 776행

입력 이름: `label`, `df`, `header_ok`, `filename`, `resolver`, `season_default`, `registered`, `issues`, `rep`, `unmatched`

읽을 때 따라갈 호출(중복 제외): `resolver.find_in_text`, `next`, `map_columns`, `any`, `classify`, `rep['tables'].append`, `df.iterrows`, `bool`, `dict`, `add_issue`, `re.search`, `rows_out.append`, `len`, `df[fused].astype(str).str.match('^\\d+\\D').mean`, `colmap.items`, `', '.join`, `re.match`, `resolver.strip_suffix`, `name.endswith`, `resolver.resolve`, `unmatched.append`, `colmap.values`, `infer_name_column`, `clean_text`, `int`, `name.lower`, `to_number`, `norm`



### `age_consistent` — 1074행

DB 선수와 파일 값이 같은 사람인가? True / False / None(판단 근거 없음)

입력 이름: `ex`, `birth`, `age`, `season`

읽을 때 따라갈 호출(중복 제외): `ex.get`, `abs`, `int`



### `diff_changes` — 1088행

입력 이름: `cur`, `new_player`, `cur_stats`, `new_stats`, `season`

읽을 때 따라갈 호출(중복 제외): `new_stats.items`, `cur.get`, `(cur_stats or {}).get`, `out.append`, `dict`, `LABEL.get`



### `parse_photo_name` — 1145행

입력 이름: `path`, `resolver`, `name_index`

읽을 때 따라갈 호출(중복 제외): `reversed`, `re.search`, `parts[-1].rsplit`, `resolver.find_in_text`, `raw.replace`, `re.split`, `int`, `' '.join`, `''.join`



### `match_photos` — 1175행

people: [{'team','name','birth_date','age','id','has_photo'}] (기존 + 이번에 새로 등록될 선수)

입력 이름: `photo_files`, `resolver`, `people`, `season`, `issues`, `unmatched`

읽을 때 따라갈 호출(중복 제외): `by_sha.items`, `name_index.setdefault(p['name'], []).append`, `_image_kind`, `parse_photo_name`, `list`, `dict`, `out.append`, `Image.open(io.BytesIO(data)).verify`, `name_index.get`, `hashlib.sha1(data).hexdigest`, `len`, `ent.update`, `c.get`, `by_sha.setdefault(sha, []).append`, `add_issue`, `name_index.setdefault`, `unmatched.append`, `IMAGE_EXT.get`, `', '.join`, `Image.open`, `f.append`, `hashlib.sha1`, `by_sha.setdefault`, `io.BytesIO`, `int`, `age_consistent`, `sorted`



### `propose_columns` — 1323행

입력 이름: `players`, `registered`

읽을 때 따라갈 호출(중복 제외): `len`, `cols.items`, `norm`, `p['extra'].items`, `out.append`, `vals.items`, `problems.append`, `dict`, `cols.setdefault(name, []).append`, `isinstance`, `any`, `min`, `max`, `name.strip().endswith`, `cols.setdefault`, `name.strip`, `set`



### `build_plan` — 1383행

files            : [(파일이름, bytes)]
existing_players : [{'id','team','name','birth_date','age','has_photo','cur':{...},'stats':{'2026':{...}}}]
registered_columns : 이미 승인된 추가 컬럼 이름들
반환: (plan, blobs)   blobs = {사진 key: bytes}  (plan 은 JSON 으로 저장 가능)

입력 이름: `files`, `team_names`, `existing_players`, `default_season`, `registered_columns`

읽을 때 따라갈 호출(중복 제외): `TeamResolver`, `expand_inputs`, `dict`, `merged.items`, `match_photos`, `propose_columns`, `list`, `issues.sort`, `report.append`, `report.insert`, `merged.setdefault`, `r['player'].items`, `m['seasons'].setdefault`, `r['stats'].items`, `m['sources'].append`, `by_key.setdefault((p['team'], p['name']), []).append`, `by_name.setdefault(p['name'], []).append`, `next`, `', '.join`, `by_key.get`, `plan_players.append`, `uniq.values`, `sniff_format`, `photo_files.append`, `read_tables`, `analyze_table`, `m['extra'].setdefault(str(r['season']), {}).update`, `m['player'].get`



### `apply_plan` — 1693행

입력 이름: `plan`, `allow_transfer`, `approved_columns`, `registered_columns`, `read_blob`

읽을 때 따라갈 호출(중복 제외): `dict`, `norm`, `transaction.atomic`, `plan.get`, `Team.objects.all`, `teams.get`, `p['seasons'].items`, `p['extra'].items`, `done.get`, `read_blob`, `SHORT_OF.get`, `player.photo.save`, `list`, `dt.date.fromisoformat`, `Player.objects.create`, `PlayerStats.objects.get_or_create`, `values.items`, `stats.save`, `ExtraStat.objects.get_or_create`, `obj.save`, `ph.get`, `Player.objects.filter(id=ph['player_id']).first`, `Player.objects.filter(team__team_name=ph['player_team'], name=ph['name']).first`, `ContentFile`, `Player.objects.get`, `fields.items`, `player.save`, `setattr`

