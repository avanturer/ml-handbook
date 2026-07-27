#!/usr/bin/env bash
# Финальная сборка хендбука: пересобрать навигацию и библиографию, прогнать все проверки.
#
# Запуск:  bash tools/finalize.sh
# Код возврата 0 означает, что репозиторий в согласованном состоянии.

set -uo pipefail
cd "$(dirname "$0")/.." || exit 1

fail=0
step() { printf '\n=== %s ===\n' "$1"; }

step "1. Пересборка навигации и библиографии"
python3 tools/build_nav.py || fail=1
python3 tools/build_bibliography.py || fail=1

step "2. Состав: docs/ против манифеста"
python3 tools/check_manifest.py || fail=1

step "3. Структура глав, внутренние ссылки, формулы"
python3 tools/check_handbook.py || fail=1

step "4. Покрытие обязательных тем из чек-листа пробелов"
python3 tools/check_coverage.py || fail=1

step "4a. Рендеринг формул на GitHub"
python3 tools/check_math.py || fail=1

step "5. Тренажёр: эталонные решения должны проходить"
HANDBOOK_CHECK_SOLUTIONS=1 python3 -m pytest code/tests -q || fail=1

step "6. Тренажёр: скелеты должны падать"
if python3 -m pytest code/tests -q > /dev/null 2>&1; then
  echo "ОШИБКА: тесты проходят на пустых скелетах — задание решено за читателя"
  fail=1
else
  echo "Скелеты падают, как и задумано."
fi

step "7. Статистика"
python3 tools/stats.py

step "ИТОГ"
if [ "$fail" -eq 0 ]; then
  echo "Все проверки пройдены."
else
  echo "Есть незакрытые проблемы — см. вывод выше."
fi
exit "$fail"
