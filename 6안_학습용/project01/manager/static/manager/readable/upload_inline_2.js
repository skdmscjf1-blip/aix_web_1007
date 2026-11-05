/* 공부 지도: learning/files/manager/static/manager/readable/upload_inline_2.js.md
 * 화면 동작을 담당합니다. ID·전역 함수 이름·실행 순서는 유지합니다. */

(function () {
  var items = []; // {file, path}
  var $ = function (i) {
    return document.getElementById(i);
  };
  var seen = {};
  function add(file, path) {
    path = (path || file.name).replace(/^\/+/, '');
    var k = path + '|' + file.size;
    if (seen[k]) return;
    seen[k] = 1;
    items.push({ file: file, path: path });
  }
  /* 받은 결과를 화면에 표시합니다. */
  function render() {
    var tot = items.reduce(function (a, x) {
      return a + x.file.size;
    }, 0);
    $('summary').innerHTML = items.length
      ? '<b>' + items.length + '개 파일</b>, ' + (tot / 1048576).toFixed(1) + ' MB'
      : '<small>선택된 파일이 없습니다.</small>';
    var h = '';
    items.slice(0, 300).forEach(function (x) {
      h +=
        '<div><span></span><small>' +
        (x.file.size / 1024).toFixed(0) +
        ' KB</small></div>';
    });
    $('list').innerHTML = h;
    var spans = $('list').getElementsByTagName('span');
    items.slice(0, 300).forEach(function (x, i) {
      spans[i].textContent = x.path;
    });
    if (items.length > 300) {
      var d = document.createElement('div');
      d.textContent = '… 외 ' + (items.length - 300) + '개';
      $('list').appendChild(d);
    }
    $('go').disabled = !items.length;
  }
  function fromInput(inp) {
    Array.prototype.forEach.call(inp.files, function (f) {
      add(f, f.webkitRelativePath || f.name);
    });
    inp.value = '';
    render();
  }
  $('pickFiles').onclick = function () {
    $('inFiles').click();
  };
  $('pickDir').onclick = function () {
    $('inDir').click();
  };
  $('inFiles').onchange = function () {
    fromInput(this);
  };
  $('inDir').onchange = function () {
    fromInput(this);
  };
  $('clear').onclick = function () {
    items = [];
    seen = {};
    render();
  };
  function walk(entry, prefix) {
    return new Promise(function (res) {
      if (entry.isFile) {
        entry.file(
          function (f) {
            add(f, prefix + entry.name);
            res();
          },
          function () {
            res();
          },
        );
      } else if (entry.isDirectory) {
        var r = entry.createReader(),
          all = [];
        (function read() {
          r.readEntries(
            function (es) {
              if (!es.length) {
                Promise.all(
                  all.map(function (e) {
                    return walk(e, prefix + entry.name + '/');
                  }),
                ).then(res);
                return;
              }
              all = all.concat(Array.prototype.slice.call(es));
              read();
            },
            function () {
              res();
            },
          );
        })();
      } else res();
    });
  }
  var drop = $('drop');
  ['dragenter', 'dragover'].forEach(function (ev) {
    drop.addEventListener(ev, function (e) {
      e.preventDefault();
      drop.classList.add('over');
    });
  });
  ['dragleave', 'drop'].forEach(function (ev) {
    drop.addEventListener(ev, function (e) {
      e.preventDefault();
      drop.classList.remove('over');
    });
  });
  drop.addEventListener('drop', function (e) {
    var its = e.dataTransfer.items,
      jobs = [];
    if (its && its.length && its[0].webkitGetAsEntry) {
      var ents = [];
      for (var i = 0; i < its.length; i++) {
        var en = its[i].webkitGetAsEntry();
        if (en) ents.push(en);
      }
      jobs = ents.map(function (en) {
        return walk(en, '');
      });
    } else {
      Array.prototype.forEach.call(e.dataTransfer.files, function (f) {
        add(f, f.name);
      });
    }
    Promise.all(jobs).then(render);
  });
  document.addEventListener('dragover', function (e) {
    e.preventDefault();
  });
  document.addEventListener('drop', function (e) {
    if (!drop.contains(e.target)) e.preventDefault();
  });
  $('f').addEventListener('submit', function (e) {
    e.preventDefault();
    if (!items.length) return;
    var fd = new FormData();
    fd.append(
      'csrfmiddlewaretoken',
      document.querySelector('[name=csrfmiddlewaretoken]').value,
    );
    fd.append('season', document.querySelector('[name=season]').value);
    fd.append(
      'paths',
      JSON.stringify(
        items.map(function (x) {
          return x.path;
        }),
      ),
    );
    items.forEach(function (x) {
      fd.append('files', x.file, x.file.name);
    });
    $('go').disabled = true;
    $('busy').style.display = 'inline';
    fetch(location.href, { method: 'POST', body: fd, credentials: 'same-origin' })
      .then(function (r) {
        window.location.href = r.url; // 서버가 보내준 점검 결과 화면(또는 오류 시 이 화면)으로 이동
      })
      .catch(function () {
        $('go').disabled = false;
        $('busy').style.display = 'none';
        alert('업로드에 실패했습니다. 다시 시도해주세요.');
      });
  });
  render();
})();
