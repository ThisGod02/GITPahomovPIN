# Git Hooks + GitLab CI/CD

- `.githooks/` — `pre-commit` (синтаксис Python + поиск секретов), `commit-msg` (Conventional Commits), `pre-push` (запуск тестов).
- Установка: `bash scripts/install-hooks.sh`.
- `.gitlab-ci.yml` — стадии `lint` / `test` / `build` (+ отчёт о покрытии).
- `test.py`, `requirements.txt` — тестовый модуль и зависимости.
