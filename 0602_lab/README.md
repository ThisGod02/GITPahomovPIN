# **Отчет по лабораторной работе №6: «GitLab CI/CD: пайплайн сборки, тестирования и развертывания»**

## **Сведения о студенте**
**Дата:** 2026-09-22
**Семестр:** 3 курс, 5 семестр
**Группа:** ПИН-Б-О-24-2
**Дисциплина:** Системы контроля версий
**Студент:** Пахомов Давид Вадимович

### **Структура готового проекта**
```
0602_lab/
├── 0602_lab.md       # Методичка
├── REPORT.md         # Данный отчет
├── app.py            # Flask: / и /health
├── requirements.txt  # flask/pytest/flake8/bandit
├── tests/
│   ├── __init__.py
│   └── test_app.py   # pytest + fixture test_client
└── .gitlab-ci.yml    # lint/build/test/deploy + security_scan
```
### **Ссылка на репозиторий GitLab**
```
https://gitlab.com/pahomov-david/cicd-lab-work
```

### **1. ЦЕЛЬ РАБОТЫ**

> 1. Построить базовый пайплайн (build/test/deploy).
> 2. Добавить линтинг и проверку безопасности.
> 3. Настроить MR pipelines и ручной деплой.
> 4. Защититься от бесконечных циклов через workflow:rules.

### **2. ЗАДАЧИ РАБОТЫ**

> 1. Создано Flask-приложение (`home`, `health`) и pytest-тесты.
> 2. Собран `.gitlab-ci.yml`: lint (flake8+bandit), build (кэш pip), test (JUnit), security_scan (safety, allow_failure), deploy_staging (manual, environment staging).
> 3. Добавлен `workflow:rules` против запуска по тегам.
> 4. Выполнен MR-цикл: lint/test в MR, deploy только на main вручную.

### **3. ХОД ВЫПОЛНЕНИЯ РАБОТЫ**

#### **3.1. Приложение и тесты**
```
pip install -r requirements.txt
python -m pytest tests/ -v
python app.py  # / -> {"message": "Hello, CI/CD!"}
```

#### **3.2. Пайплайн**
```
workflow: never on tags, always otherwise
stages: [lint, build, test, deploy]
lint: flake8 app.py + bandit -r app.py (MR + default branch)
build: pip install --cache-dir, artifacts .cache/pip
test: pytest --junitxml=report.xml, artifacts reports:junit
security_scan: safety check -r requirements.txt (allow_failure)
deploy_staging: nohup python app.py + curl /health, environment staging, when manual, only default branch
git commit -m "ci: add initial CI/CD pipeline" && git push origin main
# GitLab -> Build -> Pipelines: наблюдение за джобами
```

### **4. СКРИНШОТЫ ВЫПОЛНЕНИЯ РАБОТЫ**

> * Локально: `py_compile` чист, структура тестов совпадает с методичкой.
> * В CI: lint ловит стиль/уязвимости, test отдаёт JUnit, staging деплоится вручную с проверкой health.
> * MR pipelines отделены от branch-пайплайнов правилами.

### **5. ОТВЕТЫ НА КОНТРОЛЬНЫЕ ВОПРОСЫ**

#### **1. Что такое GitLab Runner и его типы?**
Агент, исполняющий джобы: shared (общие GitLab), group/project, self-hosted (shell/docker/kubernetes).

#### **2. stages vs jobs?**
`stages` — порядок фаз (lint→build→test→deploy), `jobs` — конкретные задачи внутри стадии, выполняются параллельно.

#### **3. Кэширование зависимостей?**
`cache: paths: [.cache/pip]` + `PIP_CACHE_DIR`, ускоряет `pip install` между запусками.

#### **4. Артефакты между джобами?**
`artifacts: paths/reports` сохраняют файлы (report.xml, venv) и пробрасывают в следующие джобы/скачивание.

#### **5. MR pipelines vs Branch pipelines?**
MR — на событие `merge_request_event` (проверка до слияния), branch — на push в ветку. Разделяются `rules`.

#### **6. Ручной запуск (when: manual)?**
Джоба ждёт кнопки Run в UI: `when: manual` + `rules` на main. Удобно для staging/production.

#### **7. workflow:rules против циклов?**
`workflow: rules: [- if: $CI_COMMIT_TAG, when: never]` не даёт тегу, созданному джобой, породить новый пайплайн.

#### **8. Переменные окружения в CI?**
`variables:` в YAML, Settings → CI/CD → Variables (masked/protected), `environment:` для scope.

#### **9. allow_failure?**
Джоба может падать без красного пайплайна (например, `security_scan` как предупреждение).

#### **10. Пайплайн по расписанию?**
Build → Pipeline schedules → cron (например, nightly security scan).

### **6. ИСПОЛЬЗУЕМЫЕ КОМАНДЫ**
```
pip install -r requirements.txt
python -m pytest tests/ -v --junitxml=report.xml
flake8 app.py --max-line-length=120 --statistics
bandit -r app.py / safety check -r requirements.txt
git add app.py requirements.txt tests/ .gitlab-ci.yml
git commit -m "ci: add initial CI/CD pipeline"
```
### **7. ВЫВОДЫ**

> 1. Построен полный контур lint→build→test→deploy.
> 2. Безопасность встроена (bandit/safety), а не прикручена сбоку.
> 3. MR pipelines + manual deploy дают управляемый релиз.
> 4. Кэш и артефакты ускоряют и документируют сборки.
