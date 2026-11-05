/* 공부 지도: learning/files/board/static/board/readable/form_inline_1.js.md
 * 화면 동작을 담당합니다. ID·전역 함수 이름·실행 순서는 유지합니다. */

(function () {
  var t = document.getElementById('id_content'),
    c = document.getElementById('cnt');
  function u() {
    c.textContent = t.value.length;
  }
  t.addEventListener('input', u);
  u();
})();
