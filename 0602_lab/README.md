# CI/CD-лабораторная (Flask)

`app.py` — эндпоинты `/` и `/health`. `tests/test_app.py` — pytest-тесты. `.gitlab-ci.yml` — стадии `lint` (flake8, bandit) / `build` / `test` (JUnit-отчёт, `security_scan` с `safety`) / `deploy` (staging, ручной запуск). Merge Request pipelines и `workflow:rules` против запуска по тегам — по методичке `0602_lab.md`.

```bash
pip install -r requirements.txt
python -m pytest tests/ -v
python app.py
```
