from pathlib import Path
from datetime import datetime
import shutil


root = Path.cwd()
source = root / "6안 수정" / "6안 수정" / "project01"
target = root / "6안" / "6안" / "project01"

files = """data/virtual/2026_virtual_stats.json
player/scoring.py
team/management/commands/make_virtual_stats.py
team/virtual_stats.py
manager/config.py
manager/templates/manager/scoring.html
manager/views.py
player/lab/reports.py
player/lab/service.py
player/services.py
player/static/player/best11_edit.js
player/static/player/lab.css
team/lineup_simulation.py
team/simulation_views.py
team/static/team/lineup_simulation.css
team/static/team/lineup_simulation.js
team/templates/team/lineup_simulation.html""".splitlines()

if (
    not (source / "manage.py").is_file()
    or not (target / "simulation/models.py").is_file()
):
    raise SystemExit(
        "aix_web_1007 폴더에서 실행하세요. "
        "6안과 6안 수정 폴더가 모두 있어야 합니다."
    )

# 먼저 모든 수정 내용을 준비합니다.
plan = {
    name: (source / name).read_text(encoding="utf-8-sig")
    for name in files
}


def replace(name, old, new):
    if plan[name].count(old) != 1:
        raise SystemExit(
            f"수정본 내용이 예상과 다릅니다: {name}. "
            "파일은 아직 변경하지 않았습니다."
        )

    plan[name] = plan[name].replace(old, new, 1)


# 범주 비율 합과 관계없이 점수 범위를 유지합니다.
name = "player/scoring.py"

replace(
    name,
    "PER90 = 'per90'",
    "import math\n\nPER90 = 'per90'",
)

start = plan[name].index("def metric_weights(")
end = plan[name].index("def metric_values(", start)

plan[name] = plan[name][:start] + '''def metric_weights(pos, groups=None):
    """범주 비율 합을 100으로 환산한 뒤 컬럼별로 나눕니다."""
    groups = group_weights(pos) if groups is None else groups
    values = {g: float(groups.get(g, 0.0)) for g, *_ in GROUPS[pos]}

    if any(not math.isfinite(v) or v < 0 for v in values.values()):
        raise ValueError('범주 비율은 유한한 0 이상의 숫자여야 합니다.')

    total = sum(values.values())

    if not math.isfinite(total) or total <= 0:
        raise ValueError('범주 비율 합은 유한한 양수여야 합니다.')

    return {
        k: values[g] / total * 100 / len(keys)
        for g, label, weight, keys in GROUPS[pos]
        for k in keys
    }


''' + plan[name][end:]


# 관리자 입력에서 잘못된 숫자를 차단합니다.
name = "manager/views.py"

replace(
    name,
    "import json\n",
    "import json\nimport math\n",
)

replace(
    name,
    "if v < 0:",
    "if not math.isfinite(v) or v < 0:",
)

replace(
    name,
    "if not errors and sum(out['groups'][p].values()) <= 0:",
    "if not errors and "
    "(not math.isfinite(sum(out['groups'][p].values())) "
    "or sum(out['groups'][p].values()) <= 0):",
)


name = "manager/templates/manager/scoring.html"

replace(
    name,
    "포지션별 합을 100으로 맞추기",
    "저장할 비율 합을 100으로 맞추기 "
    "(계산 시에는 항상 합계 100으로 환산)",
)


# 새 계산과 맞지 않는 화면 설명을 수정합니다.
name = "team/static/team/lineup_simulation.js"

replace(
    name,
    "['전력', '기본', '변경 후', '변화', '가정 비중']",
    "['포지션 평균점수', '기본', '변경 후', '변화']",
)

replace(name, "                    `${p.weight}%`,\n", "")
replace(name, "Math.abs(b.contribution)", "Math.abs(b.change)")
replace(name, "Math.abs(a.contribution)", "Math.abs(a.change)")

replace(
    name,
    "가장 크게 반영된 전력 변화:",
    "평균점수 변화가 가장 큰 포지션:",
)

replace(
    name,
    "교체·컨디션 보정은 이 평가에 포함되지 않았으며 "
    "실제 승률 효과를 검증한 값이 아닙니다.",
    "선수 능력치 혼합·케미·컨디션·가상 최근 경기 보정은 "
    "이 평가에 포함되지 않았습니다.",
)


name = "team/templates/team/lineup_simulation.html"

start = plan[name].index(
    "<ul>",
    plan[name].index("<!-- 계산 기준 -->"),
)
end = plan[name].index("</ul>", start) + len("</ul>")

plan[name] = plan[name][:start] + """<ul>
<li>선수·컨디션 효과는 실제 경기에서 학습한 효과가 아닌 시뮬레이션 가정입니다.</li>
<li>동일 포지션의 지표별 최저·최고를 비교하며, 부족한 기록과 출전 경험을 보정합니다.</li>
<li>컨디션은 안 좋음 0.9배, 보통 1.0배, 좋음 1.1배입니다. 기록이 없으면 중립값 50을 사용합니다.</li>
<li>공격 지수는 공격수·미드필더 평균, 수비 지수는 수비수 평균 60%와 골키퍼 40%입니다.</li>
<li>필드 선수를 다른 역할에 배치하면 0.9배를 적용합니다. GK는 GK 자리에만 배치합니다.</li>
<li>기본 혼합은 팀 기록 70%와 선수 능력치 30%이며, 관리자에서 선수 비중을 0~60%로 설정합니다.</li>
<li>활동량·스프린트와 일부 골키퍼 지표는 별도 가상 값이며 GPS 누적 기록에서 가져온 값이 아닙니다.</li>
<li>내 BEST11 최근 5경기는 가상 결과입니다. 해당 모드에서는 홈팀 예상 득점에 가정에 따른 보정을 적용합니다.</li>
<li>기존 모델 평가 성적은 새 혼합 방식의 성능을 의미하지 않습니다. 과거 경기 예측에 현재 시즌 최종 기록을 사용하면 안 됩니다.</li>
</ul>""" + plan[name][end:]


# 파이썬 문법을 검사한 다음 백업합니다.
for name, text in plan.items():
    if name.endswith(".py"):
        compile(text, name, "exec")

backup = root.parent / (
    "v6_merge_backup_"
    + datetime.now().strftime("%Y%m%d_%H%M%S_%f")
)
backup.mkdir(parents=True)

backup_files = files + [
    "player/static/player/data/player_reports.json",
    "db.sqlite3",
]

for name in backup_files:
    old = target / name

    if old.is_file():
        saved = backup / name
        saved.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(old, saved)


# 준비된 기능 파일만 적용합니다.
for name, text in plan.items():
    destination = target / name
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(text, encoding="utf-8")

print("병합 완료:", len(plan), "개 기능 파일")
print("백업 위치:", backup)
print("기존 DB와 GPS 앱은 변경하지 않았습니다.")