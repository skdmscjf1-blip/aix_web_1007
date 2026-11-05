# `manager/views.py`

관리자 입력 검토·반영·백업·기본 설정 — 요청 처리와 응답 연결



[실제 코드 열기](../../../manager/views.py)



## 이 파일을 읽을 때

1. 입력을 어디서 받는지 찾습니다.

2. 값을 바꾸는 계산과 DB를 읽거나 쓰는 부분을 구분합니다.

3. 마지막 `return` 또는 화면/이벤트 연결을 확인합니다.



## 연결된 Python 모듈

```python

import json

import math

from datetime import datetime

from pathlib import Path

from django.conf import settings

from django.contrib import messages

from django.contrib.auth.decorators import user_passes_test

from django.core.files.base import ContentFile

from django.core.files.storage import default_storage

from django.db import connections

from django.db.models import Count, Q

from django.core.exceptions import TooManyFilesSent

from django.http import Http404

from django.shortcuts import get_object_or_404, redirect, render

from django.utils import timezone

from django.views.decorators.http import require_POST

from player.models import Player, PlayerStats

from team.models import Team

from . import backup as bk

from . import config

from .importer import STAT_FIELDS, apply_plan, build_plan

from .models import BestExclusion, ImportBatch, ScoreConfig, ScoreConfigLog, StatColumn

```

## 함수·클래스 안내

### `db_path` — 31행

입력 이름: 



### `backup_dir` — 35행

입력 이름: 

읽을 때 따라갈 호출(중복 제외): `Path`



### `is_admin` — 39행

입력 이름: `user`



### `dashboard` — 47행

입력 이름: `request`

읽을 때 따라갈 호출(중복 제외): `Team.objects.annotate(total=Count('player', distinct=True), with_stats=Count('player', filter=Q(player__playerstats__season=2026), distinct=True), no_photo=Count('player', filter=Q(player__photo=''), distinct=True), no_birth=Count('player', filter=Q(player__birth_date__isnull=True), distinct=True)).order_by`, `render`, `rows.append`, `sum`, `Team.objects.annotate`, `StatColumn.objects.all`, `getattr`, `Count`, `Q`



### `build_existing` — 73행

DB의 선수 + 현재 값 (파일과 비교해서 '변경 전'을 보여주기 위함)

입력 이름: `season`

읽을 때 따라갈 호출(중복 제외): `Player.objects.select_related`, `stats.get`, `out.append`, `PlayerStats.objects.filter(season=season).values`, `p.birth_date.isoformat`, `dict`, `PlayerStats.objects.filter`, `bool`, `str`, `s.items`



### `import_upload` — 113행

입력 이름: `request`

읽을 때 따라갈 호출(중복 제외): `render`, `enumerate`, `list`, `build_plan`, `ImportBatch.objects.create`, `blobs.items`, `redirect`, `request.FILES.getlist`, `messages.error`, `json.loads`, `'/'.join`, `names.append`, `int`, `StatColumn.objects.values_list`, `build_existing`, `default_storage.save`, `Team.objects.values_list`, `request.user.get_username`, `ContentFile`, `request.POST.get`, `isinstance`, `f.read`, `zip`, `', '.join`, `len`, `p.replace('\\', '/').split`, `p.replace`



### `import_report` — 167행

입력 이름: `request`, `pk`

읽을 때 따라갈 호출(중복 제외): `get_object_or_404`, `list`, `render`, `StatColumn.objects.values_list`, `len`, `any`, `plan.get`



### `write_schema_file` — 189행

입력 이름: `batch`, `approved`, `plan`, `registered`

읽을 때 따라갈 호출(중복 제외): `folder.mkdir`, `datetime.now().strftime`, `path.write_text`, `str`, `datetime.now().isoformat`, `json.dumps`, `path.relative_to`, `Path`, `datetime.now`, `plan.get`, `list`



### `import_apply` — 211행

입력 이름: `request`, `pk`

읽을 때 따라갈 호출(중복 제외): `get_object_or_404`, `messages.success`, `redirect`, `messages.error`, `ImportBatch.objects.filter(pk=pk, status='검토중').update`, `list`, `apply_plan`, `batch.save`, `bk.make_backup`, `StatColumn.objects.values_list`, `StatColumn.objects.get_or_create`, `write_schema_file`, `ImportBatch.objects.filter(pk=pk).update`, `ImportBatch.objects.filter`, `db_path`, `backup_dir`, `batch.plan.get`, `request.POST.getlist`, `bool`, `len`, `request.user.get_username`, `default_storage.open`, `f.read`, `request.POST.get`, `dict`



### `history` — 282행

입력 이름: `request`

읽을 때 따라갈 호출(중복 제외): `render`, `ImportBatch.objects.all`



### `backups` — 290행

입력 이름: `request`

읽을 때 따라갈 호출(중복 제외): `render`, `bk.list_backups`, `backup_dir`



### `backup_now` — 300행

입력 이름: `request`

읽을 때 따라갈 호출(중복 제외): `redirect`, `bk.make_backup`, `messages.success`, `db_path`, `backup_dir`, `messages.error`, `request.POST.get('reason', '').strip`, `request.user.get_username`, `request.POST.get`



### `backup_restore` — 315행

입력 이름: `request`, `name`

읽을 때 따라갈 호출(중복 제외): `bk.get_backup`, `list`, `render`, `backup_dir`, `Http404`, `ImportBatch.objects.filter`, `connections.all`, `messages.success`, `messages.info`, `redirect`, `bk.list_backups`, `request.POST.get`, `messages.error`, `bk.restore_backup`, `c.close`, `call_command`, `_parse`, `db_path`, `messages.warning`, `item.get`, `request.user.get_username`



### `_parse` — 366행

입력 이름: `s`

읽을 때 따라갈 호출(중복 제외): `timezone.make_aware`, `datetime.strptime`, `datetime`



### `_svc` — 374행

입력 이름: 



### `_defaults` — 380행

입력 이름: 

찾아볼 반환 사전 키(분기·내부 함수 포함): `min`, `groups`, `player_weight`

읽을 때 따라갈 호출(중복 제외): `_svc`, `SC.default_group_weights`



### `_current` — 391행

입력 이름: 

읽을 때 따라갈 호출(중복 제외): `cur['min'].update`, `config.player_weight`, `_defaults`, `config.load_saved`, `dict`, `SC.group_weights`, `int`, `saved.get('min', {}).items`, `saved.get`



### `_parse_form` — 404행

폼 → 설정. (설정, 오류목록)

입력 이름: `post`, `base`

읽을 때 따라갈 호출(중복 제외): `str(post.get('player_weight', '')).strip`, `errors.append`, `float`, `post.get`, `int`, `post.get(f'g_{p}_{g}', '').strip`, `str`, `sum`, `out['groups'][p].values`, `round`, `math.isfinite`, `out['groups'][p].items`



### `_best11_names` — 465행

입력 이름: `cfg`, `formation`

읽을 때 따라갈 호출(중복 제외): `_svc`, `config.load_saved().get`, `config.override`, `svc.get_filtered_best11`, `r['best11'].items`, `config.load_saved`



### `_diff_best11` — 490행

입력 이름: `before`, `after`

읽을 때 따라갈 호출(중복 제외): `out.append`, `dict`, `before.get`, `after.get`, `a.items`, `b.items`



### `scoring` — 510행

입력 이름: `request`

읽을 때 따라갈 호출(중복 제외): `dict`, `render`, `_defaults`, `_current`, `request.POST.get`, `request.GET.get`, `_parse_form`, `list`, `config.load_saved`, `ScoreConfig.objects.first`, `ScoreConfigLog.objects.create`, `messages.success`, `redirect`, `_best11_names`, `_diff_best11`, `_svc().FORMATIONS.keys`, `ScoreConfigLog.objects.all`, `obj.save`, `form.get`, `sum`, `request.user.get_username`, `ScoreConfig`, `form['groups'][p].values`, `obj.data.items`, `form['groups'].get`, `_svc`, `config.load_saved().items`, `form['groups'][p].items`



### `_snap` — 619행

입력 이름: `p`



### `exclusions` — 624행

입력 이름: `request`

읽을 때 따라갈 호출(중복 제외): `config.exclusions_initialized`, `request.GET.get('q', '').strip`, `config.excluded_ids`, `set`, `render`, `redirect`, `list`, `dict`, `request.POST.get`, `request.user.get_username`, `Player.objects.filter(id__in=ids).select_related`, `obj.save`, `messages.success`, `request.GET.get`, `_svc`, `BestExclusion.objects.select_related`, `BestExclusion.objects.get_or_create`, `ScoreConfig.objects.first`, `ScoreConfig`, `messages.error`, `Player.objects.filter(name__contains=q).select_related('team').exclude(bestexclusion__isnull=False).order_by`, `Player.objects.filter(playerstats__season=2026, birth_date__isnull=True, photo='').select_related('team').distinct`, `Player.objects.filter`, `Player.objects.filter(pk=request.POST.get('player') or 0).select_related('team').first`, `_snap`, `BestExclusion.objects.filter(pk=request.POST.get('pk') or 0).delete`, `Player.objects.filter(name__contains=q).select_related('team').exclude`, `Player.objects.filter(playerstats__season=2026, birth_date__isnull=True, photo='').select_related`

