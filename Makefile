.PHONY: help build check check-fast diagrams links test test-solutions serve stats all

PY ?= python3

help:  ## Показать список команд
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-16s\033[0m %s\n", $$1, $$2}'

build:  ## Пересобрать навигацию (оглавления, index.md, nav в mkdocs.yml) и библиографию
	$(PY) tools/link_sections.py
	$(PY) tools/build_nav.py
	$(PY) tools/build_bibliography.py

render:  ## Отрендерить все формулы и схемы по-настоящему (нужен npm install katex @mermaid-js/mermaid-cli)
	$(PY) tools/check_katex.py
	$(PY) tools/check_mermaid.py

diagrams:  ## Только схемы: отрендерить mermaid и убедиться, что они рисуются
	$(PY) tools/check_mermaid.py

check-fast:  ## Быстрые проверки: состав, структура глав, внутренние ссылки, покрытие тем
	$(PY) tools/check_manifest.py
	$(PY) tools/check_handbook.py
	$(PY) tools/check_order.py
	$(PY) tools/check_coverage.py
	$(PY) tools/check_math.py

check: build check-fast  ## Пересобрать и проверить всё, кроме внешних ссылок
	@git diff --quiet -- docs mkdocs.yml resources || { \
		echo "Навигация или библиография изменились — закоммитьте результат сборки."; exit 1; }

links:  ## Проверить доступность внешних ссылок (нужна сеть)
	$(PY) tools/check_links.py

test:  ## Прогнать тренажёр: скелеты (ожидаемо падают)
	$(PY) -m pytest code/tests -q

test-solutions:  ## Прогнать тренажёр против эталонных решений (должно быть зелено)
	HANDBOOK_CHECK_SOLUTIONS=1 $(PY) -m pytest code/tests -q

serve:  ## Локальный сайт на http://127.0.0.1:8000
	mkdocs serve

stats:  ## Сводка по объёму хендбука
	@$(PY) tools/stats.py

all: check test-solutions stats  ## Полная проверка перед коммитом
