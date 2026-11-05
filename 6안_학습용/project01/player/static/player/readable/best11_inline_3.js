/* 공부 지도: learning/files/player/static/player/readable/best11_inline_3.js.md
 * 화면 동작을 담당합니다. ID·전역 함수 이름·실행 순서는 유지합니다. */

document.addEventListener('DOMContentLoaded', function () {
  const tabs = document.querySelectorAll('.ranking-tab');
  const panels = document.querySelectorAll('.ranking-panel');

  tabs.forEach(function (tab) {
    tab.addEventListener('click', function () {
      const position = this.dataset.position;

      tabs.forEach(function (item) {
        item.classList.remove('active');
      });

      panels.forEach(function (panel) {
        panel.classList.remove('active');
      });

      this.classList.add('active');

      const target = document.getElementById('ranking-' + position);
      if (target) {
        target.classList.add('active');
      }
    });
  });
});
