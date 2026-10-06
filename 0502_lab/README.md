# **Отчет по лабораторной работе №5: «Автоматизация разработки: Git Hooks и GitLab CI/CD»**

## **Сведения о студенте**
**Дата:** 2026-09-18
**Семестр:** 3 курс, 5 семестр
**Группа:** ПИН-Б-О-24-2
**Дисциплина:** Системы контроля версий
**Студент:** Пахомов Давид Вадимович

### **Структура готового проекта**
```
0502_lab/
├── 0502_lab.md              # Методичка
├── REPORT.md                # Данный отчет
├── test.py                  # Тестовый модуль (addition/subtraction)
├── requirements.txt         # Зависимости
├── .gitlab-ci.yml           # lint/test/build/coverage
├── .githooks/
│   ├── pre-commit           # синтаксис Python + поиск секретов
│   ├── commit-msg           # Conventional Commits
│   └── pre-push             # запуск тестов
└── scripts/
    └── install-hooks.sh     # установка хуков
```
### **Ссылка на репозиторий GitLab**
```
https://gitlab.com/pahomov-david/collab-project
```

### **1. ЦЕЛЬ РАБОТЫ**

> 1. Освоить Git Hooks (pre-commit, commit-msg, pre-push).
> 2. Настроить проверку синтаксиса, секретов и формата сообщений.
> 3. Построить базовый GitLab CI/CD пайплайн (lint/test/build).
> 4. Связать хуки и CI в единый контроль качества.

### **2. ЗАДАЧИ РАБОТЫ**

> 1. Написан `pre-commit`: `py_compile` для staged `.py` + grep по секретам (password/secret/token/api_key).
> 2. Написан `commit-msg` с regex Conventional Commits.
> 3. Написан `pre-push` с запуском `test.py` и проверкой `.gitlab-ci.yml`.
> 4. Хуки протестированы (битый синтаксис, секрет, неверный формат — отклоняются).
> 5. Добавлен `scripts/install-hooks.sh` (копирование `.githooks` → `.git/hooks`).
> 6. Создан `.gitlab-ci.yml` (lint/test/build/coverage), `test.py`, `requirements.txt`, коммит `ci: add GitLab CI/CD pipeline and Git hooks`.

### **3. ХОД ВЫПОЛНЕНИЯ РАБОТЫ**

#### **3.1. Хуки**
```
cd .git/hooks
# pre-commit: staged .py -> python3 -m py_compile; grep секретов -> exit 1
chmod +x pre-commit
# commit-msg: ^(feat|fix|docs|style|refactor|perf|test|chore|ci|build)(\(.+\))?: .+
# pre-push: python3 test.py || exit 1
bash scripts/install-hooks.sh
```
Проверки: файл с `SyntaxError` отклонён pre-commit; `password = "..."` отклонён; `commit -m "плохо"` отклонён commit-msg; корректный `test: ...` проходит.

#### **3.2. CI/CD**
```
stages: [lint, test, build]
lint: find . -name "*.py" -exec python3 -m py_compile
test: python3 test.py
build: dist/version.txt + artifacts (30 days), only main
coverage: coverage run/report, only MR
git add .gitlab-ci.yml test.py requirements.txt scripts/ .githooks/
git commit -m "ci: add GitLab CI/CD pipeline and Git hooks"
git push origin feature/git-hooks
# GitLab -> CI/CD -> Pipelines: lint/test/build зелёные; MR показывает CI
```
Факт: `python3 test.py` → `test_addition passed`, `test_subtraction passed`, `All tests passed!`

### **4. СКРИНШОТЫ ВЫПОЛНЕНИЯ РАБОТЫ**

> * Локальные хуки ловят ошибки до push, CI — после push/MR.
> * Формат сообщений enforced и локально, и идейно в CI-культуре.
> * Пайплайн воспроизводим: стадии и `only: [merge_requests, main, develop]`.

### **5. ОТВЕТЫ НА КОНТРОЛЬНЫЕ ВОПРОСЫ**

#### **1. Что такое Git Hooks и какие типы существуют?**
Скрипты в `.git/hooks`, запускаемые Git на событиях: `pre-commit`, `commit-msg`, `pre-push`, `post-commit`, `pre-receive`, `update` и др. Клиентские и серверные.

#### **2. Как создать и установить хук?**
Создать исполняемый файл без расширения в `.git/hooks` (или хранить в `.githooks` + `install-hooks.sh` копирует).

#### **3. Для чего pre-commit?**
Финальная проверка перед коммитом: синтаксис, линтеры, секреты, форматирование.

#### **4. Как проверить формат сообщения?**
Хук `commit-msg` читает `$1` и сверяет первую строку с regex Conventional Commits, иначе `exit 1`.

#### **5. Что такое GitLab CI/CD и его задачи?**
Автоматизация: сборка, тесты, анализ, публикация, деплой по `.gitlab-ci.yml` на runners.

#### **6. Какие стадии выделить?**
lint → test → build → deploy (плюс security/scan, coverage, review).

#### **7. Пайплайн только в MR?**
`only: [merge_requests]` или `rules: - if: $CI_PIPELINE_SOURCE == 'merge_request_event'`.

#### **8. Что такое артефакты?**
Файлы, сохраняемые джобой и передаваемые дальше/скачиваемые: `artifacts: paths: [dist/]`, JUnit-отчёты.

#### **9. Защита ветки с требованием CI?**
Settings → Repository → Protected Branches + «Require successful pipeline» / «Only allow merge if pipeline succeeds».

#### **10. Клиентские vs серверные хуки?**
Клиентские (pre-commit/commit-msg/pre-push) — локально у разработчика; серверные (pre-receive/update) — на GitLab, блокируют push для всех.

### **6. ИСПОЛЬЗУЕМЫЕ КОМАНДЫ**
```
chmod +x .git/hooks/pre-commit
python3 -m py_compile <file>
python3 test.py
bash scripts/install-hooks.sh
git add .gitlab-ci.yml test.py requirements.txt scripts/ .githooks/
git commit -m "ci: add GitLab CI/CD pipeline and Git hooks"
```
### **7. ВЫВОДЫ**

> 1. Хуки закрывают «глупые» ошибки до репозитория.
> 2. CI гарантирует то же самое на сервере для всех.
> 3. Связка pre-commit/commit-msg/pre-push + lint/test/build — минимальный зрелый контур.
> 4. Секреты вынесены в переменные окружения.
