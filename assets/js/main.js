(function () {
  var root = document.documentElement;

  // Тема (світла / темна)
  try {
    var saved = localStorage.getItem('theme');
    if (saved) root.setAttribute('data-theme', saved);
  } catch (e) {}
  var themeBtn = document.getElementById('themeToggle');
  if (themeBtn) {
    themeBtn.addEventListener('click', function () {
      var current = root.getAttribute('data-theme');
      if (!current) {
        current = window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
      }
      var next = current === 'dark' ? 'light' : 'dark';
      root.setAttribute('data-theme', next);
      try { localStorage.setItem('theme', next); } catch (e) {}
    });
  }

  // Мобільне меню
  var sidebar = document.getElementById('sidebar');
  var toggle = document.getElementById('menuToggle');
  var backdrop = document.getElementById('backdrop');
  function setMenu(open) {
    document.body.classList.toggle('menu-open', open);
    if (toggle) toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
  }
  if (toggle) toggle.addEventListener('click', function () {
    setMenu(!document.body.classList.contains('menu-open'));
  });
  if (backdrop) backdrop.addEventListener('click', function () { setMenu(false); });

  // Прокрутити бокове меню до активного уроку
  var active = sidebar && sidebar.querySelector('a.active');
  if (active) active.scrollIntoView({ block: 'center' });

  // Пошук у меню
  var search = document.getElementById('navSearch');
  if (search) {
    search.addEventListener('input', function () {
      var q = search.value.trim().toLowerCase();
      sidebar.querySelectorAll('.nav-section').forEach(function (sec) {
        var visible = 0;
        sec.querySelectorAll('li').forEach(function (li) {
          var match = !q || li.textContent.toLowerCase().indexOf(q) !== -1;
          li.style.display = match ? '' : 'none';
          if (match) visible++;
        });
        sec.style.display = visible ? '' : 'none';
      });
    });
  }

  // Кнопка "Копіювати" для блоків коду
  document.querySelectorAll('.lesson div.highlighter-rouge').forEach(function (block) {
    var btn = document.createElement('button');
    btn.className = 'copy-btn';
    btn.type = 'button';
    btn.textContent = 'Копіювати';
    btn.addEventListener('click', function () {
      var code = block.querySelector('code');
      var text = code ? code.innerText : '';
      var done = function () {
        btn.textContent = 'Скопійовано ✓';
        setTimeout(function () { btn.textContent = 'Копіювати'; }, 1500);
      };
      if (navigator.clipboard) {
        navigator.clipboard.writeText(text).then(done, function () {});
      }
    });
    block.appendChild(btn);
  });
})();
