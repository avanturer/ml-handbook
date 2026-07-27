// Рендерит формулы через KaTeX — ровно тот движок, которым GitHub рисует математику
// в markdown. Если KaTeX бросает исключение, на странице вместо формулы будет сырой LaTeX.
//
// Вход:  JSON-массив [{id, tex, display}] на stdin.
// Выход: JSON-массив [{id, error}] на stdout — только для тех, что не отрендерились.
//
// Вызывается из tools/check_katex.py, руками запускать не нужно.

const path = require('path');
const Module = require('module');

// KaTeX может лежать в node_modules репозитория или в каталоге, указанном в KATEX_PATH.
const extraPaths = [];
if (process.env.KATEX_PATH) extraPaths.push(process.env.KATEX_PATH);
extraPaths.push(path.join(__dirname, '..', 'node_modules'));
Module.globalPaths.push(...extraPaths);

let katex;
try {
  katex = require('katex');
} catch (e) {
  try {
    katex = require(path.join(extraPaths[extraPaths.length - 1], 'katex'));
  } catch (e2) {
    process.stderr.write('KATEX_NOT_FOUND\n');
    process.exit(2);
  }
}

let input = '';
process.stdin.on('data', (chunk) => { input += chunk; });
process.stdin.on('end', () => {
  const items = JSON.parse(input);
  const failures = [];
  for (const item of items) {
    try {
      katex.renderToString(item.tex, {
        throwOnError: true,
        displayMode: item.display,
        // GitHub не подключает пользовательские макросы, поэтому и мы не подключаем:
        // формула должна быть самодостаточной.
        macros: {},
        strict: false,
      });
    } catch (err) {
      failures.push({ id: item.id, error: String(err.message || err).slice(0, 200) });
    }
  }
  process.stdout.write(JSON.stringify(failures));
});
