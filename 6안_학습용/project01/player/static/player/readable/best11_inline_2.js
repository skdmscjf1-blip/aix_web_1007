/* 공부 지도: learning/files/player/static/player/readable/best11_inline_2.js.md
 * 화면 동작을 담당합니다. ID·전역 함수 이름·실행 순서는 유지합니다. */

// =====================================================
// 현재 육각형 그래프
//
// 다른 선수를 클릭했을 때
// 기존 그래프를 삭제하기 위해 저장
// =====================================================

// =====================================================
// 구단 / 포메이션은 "적용" 버튼을 눌러야 반영된다.
// (예전에는 고르는 순간 바로 제출되어 적용 버튼이 쓸모없었음)
// =====================================================

let playerRadarChart = null;

// =====================================================
// 선수 클릭
// =====================================================

function openPlayerModal(playerId) {
  // -------------------------------------------------
  // Django에 선수 정보 요청
  //
  // 예:
  // /player/info/245/
  // -------------------------------------------------

  fetch('/player/info/' + playerId + '/')
    // -------------------------------------------------
    // Django 응답을 JSON으로 변환
    // -------------------------------------------------

    .then(function (response) {
      if (!response.ok) {
        throw new Error('HTTP 오류 : ' + response.status);
      }

      return response.json();
    })

    // -------------------------------------------------
    // JSON을 성공적으로 받은 경우
    // -------------------------------------------------

    .then(function (data) {
      // 데이터가 없는 경우
      if (data.success == false) {
        alert(data.message);

        return;
      }

      // =================================================
      // 선수 이름
      // =================================================

      document.getElementById('modalPlayerName').innerText = data.player.name;

      // =================================================
      // 구단 / 포지션 / 등번호
      // =================================================

      document.getElementById('modalPlayerTeam').innerText =
        data.player.team + ' · ' + data.player.position + ' · #' + data.player.number;

      // =================================================
      // 선수 사진
      // =================================================

      const photo = document.getElementById('modalPlayerPhoto');

      const noPhoto = document.getElementById('modalNoPhoto');

      if (data.player.photo) {
        photo.src = data.player.photo;

        photo.style.display = 'block';

        noPhoto.style.display = 'none';
      } else {
        photo.removeAttribute('src');

        photo.style.display = 'none';

        noPhoto.style.display = 'flex';
      }

      // =================================================
      // 기본 기록
      // =================================================

      document.getElementById('modalGames').innerText = data.stats.games + '경기';

      document.getElementById('modalMinutes').innerText = data.stats.minutes + '분';

      document.getElementById('modalGoals').innerText = data.stats.goals;

      document.getElementById('modalAssists').innerText = data.stats.assists;

      // =================================================
      // BEST11 점수 / 순위
      // =================================================

      const scoreArea = document.getElementById('modalBest11Score');

      if (data.best11.score != null) {
        scoreArea.innerText =
          'BEST11 ' +
          data.best11.score +
          '점' +
          ' · ' +
          data.player.position +
          ' ' +
          data.best11.rank +
          '위 / ' +
          data.best11.candidate_count +
          '명';
      } else {
        scoreArea.innerText = '600분 미만 · ' + 'BEST11 순위 미산정';
      }

      // =================================================
      // 90분당 기록
      // =================================================

      document.getElementById('per90Goals').innerText = data.per90.goals;

      document.getElementById('per90Assists').innerText = data.per90.assists;

      document.getElementById('per90Shots').innerText = data.per90.shots;

      document.getElementById('per90ShotsTarget').innerText =
        data.per90.shots_on_target;

      document.getElementById('per90KeyPasses').innerText = data.per90.key_passes;

      document.getElementById('per90PassRate').innerText = data.per90.pass_rate;

      document.getElementById('per90Dribble').innerText = data.per90.dribble;

      document.getElementById('per90Interceptions').innerText =
        data.per90.interceptions;

      document.getElementById('per90Clearances').innerText = data.per90.clearances;

      document.getElementById('per90Recoveries').innerText = data.per90.recoveries;

      // =================================================
      // 기존 육각형 그래프 삭제
      //
      // 이 부분이 없으면
      // 선수 A 클릭 → 선수 B 클릭 시
      // 그래프가 중복될 수 있음
      // =================================================

      if (playerRadarChart != null) {
        playerRadarChart.destroy();

        playerRadarChart = null;
      }

      // =================================================
      // 육각형 그래프
      // =================================================

      const ctx = document.getElementById('playerRadarChart');

      playerRadarChart = new Chart(
        ctx,

        {
          // 레이더 그래프
          type: 'radar',

          data: {
            // =================================================
            // 포지션별 육각형 6개 항목
            //
            // FW
            // 득점력 / 슈팅 / 찬스메이킹 / 드리블 / 패스 / 경합
            //
            // MF
            // 공격포인트 / 찬스메이킹 / 패스 / 드리블 / 볼회수 / 경합
            //
            // DF
            // 수비 / 태클 / 인터셉트 / 경합 / 빌드업 / 활동량
            //
            // GK
            // 패스 / 롱패스 / 볼회수 / 클리어링 / 출전시간 / 평점
            //
            // 항목 이름은 services.py에서 계산
            // → views.py JSON
            // → 여기에서 그대로 사용
            // =================================================
            labels: data.radar_labels,

            datasets: [
              {
                // 선수명
                label: data.player.name,

                // 포지션별 백분위 점수 6개
                data: data.radar_scores,

                borderWidth: 2,

                fill: true,

                // 점 크기
                pointRadius: 4,

                pointHoverRadius: 6,
              },
            ],
          },

          options: {
            responsive: true,

            maintainAspectRatio: true,

            plugins: {
              legend: {
                display: true,
              },
            },

            scales: {
              r: {
                // 최소값
                min: 0,

                // 최대값
                max: 100,

                // 20점 간격
                ticks: {
                  stepSize: 20,
                },

                // 항목 글씨
                pointLabels: {
                  font: {
                    size: 14,
                  },
                },
              },
            },
          },
        },
      );

      // =================================================
      // 팝업 열기
      // =================================================

      document.getElementById('playerModal').style.display = 'block';

      // =================================================
      // 뒤쪽 페이지 스크롤 막기
      // =================================================

      document.body.style.overflow = 'hidden';
    })

    // -------------------------------------------------
    // 오류
    // -------------------------------------------------

    .catch(function (error) {
      console.log('선수정보 오류 : ', error);

      alert('선수 정보를 불러오지 못했습니다.');
    });
}

// =====================================================
// 팝업 닫기
// =====================================================

function closePlayerModal() {
  document.getElementById('playerModal').style.display = 'none';

  document.body.style.overflow = 'auto';
}

// =====================================================
// 검은 배경 클릭 → 팝업 닫기
// =====================================================

document.getElementById('playerModal').addEventListener(
  'click',

  function (event) {
    if (event.target.id == 'playerModal') {
      closePlayerModal();
    }
  },
);

// =====================================================
// ESC → 팝업 닫기
// =====================================================

document.addEventListener(
  'keydown',

  function (event) {
    if (event.key == 'Escape') {
      closePlayerModal();
    }
  },
);
