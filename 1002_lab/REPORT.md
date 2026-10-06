# **Отчет по лабораторной работе №10: «Итоговый проект. Ревью и защита»**

## **Сведения о студенте**
**Дата:** 2026-10-06
**Семестр:** 3 курс, 5 семестр
**Группа:** ПИН-Б-О-24-2
**Дисциплина:** Системы контроля версий
**Студент:** Пахомов Давид Вадимович

### **Структура готового проекта**
```
1002_lab/ (todo-api)
├── 1002_lab.md              # Методичка
├── REPORT.md                # Данный отчет
├── README.md / CONTRIBUTING.md / CHANGELOG.md / LICENSE
├── .gitignore / .env.example / .gitattributes
├── .gitlab-ci.yml           # lint/test/build/deploy
├── .pre-commit-config.yaml  # trailing-whitespace, check-yaml, detect-private-key
├── Dockerfile / docker-compose.yml / requirements.txt
├── src/main.py              # FastAPI: CRUD /todos, категории, /health
├── tests/test_main.py       # 5 pytest-тестов
├── scripts/                 # install-hooks.sh, deploy.sh
├── docs/FEATURE_CATEGORIES.md
└── history.txt              # develop + feature/categories
```
### **Ссылка на репозиторий GitLab**
```
https://gitlab.com/pahomov-david/todo-api
```

### **1. ЦЕЛЬ РАБОТЫ**

> 1. Собрать итоговый проект со всеми практиками курса: ветвление, MR, хуки, CI/CD, Registry, окружения, документация.
> 2. Выбрать и обосновать стратегию ветвления (Git Flow).
> 3. Подготовить проект к защите: структура, история, пайплайн, ответы на вопросы.

### **2. ЗАДАЧИ РАБОТЫ**

> 1. Инициализирован `todo-api` (FastAPI): модели `TodoCreate`/`TodoResponse`, endpoints `/`, `/health`, `GET/POST/GET{id}/DELETE /todos`, поле `category`.
> 2. Добавлены `.gitignore`, `README.md` (бейджи pipeline/coverage), `CONTRIBUTING.md` (Conventional Commits + MR-процесс), `CHANGELOG.md` (1.0.0/1.1.0), `LICENSE` (MIT), `.env.example`.
> 3. Настроен `.gitlab-ci.yml` (lint flake8 → test pytest → build образа → staging auto от develop / production manual от main).
> 4. Добавлены `Dockerfile`, `docker-compose.yml`, `.pre-commit-config.yaml`, `scripts/install-hooks.sh`, `scripts/deploy.sh`.
> 5. Ветки: `develop`, `feature/categories` (пустой коммит как маркер + реальное поле category), merge `--no-ff` в `develop`; `history.txt`.
> 6. Защита веток: `main`/`develop` только через MR (по методичке).

### **3. ХОД ВЫПОЛНЕНИЯ РАБОТЫ**

#### **3.1. Создание и настройка**
```
git checkout -b develop
git add . && git commit -m "feat: initial project setup with FastAPI"
# защита: Settings -> Repository -> Protected Branches (main, develop — только MR)
```

#### **3.2. Доработка через feature-ветку**
```
git checkout -b feature/categories
# модели/эндпоинты категорий (поле category), тесты
git commit -m "feat: add categories support"
# MR feature/categories -> develop: зелёный CI, ревью, merge --no-ff
git checkout develop && git merge --no-ff feature/categories
git log --oneline --graph --all > history.txt
```
Фактическая история:
```
* 8c750c6 (develop) docs: add history
*   dac64fb Merge branch 'feature/categories' into develop
| * 19b41b2 feat: add categories support
|/
* a15d655 (main) feat: initial project setup with FastAPI
```

#### **3.3. Проверка**
```
python -m py_compile src/main.py tests/test_main.py
docker build -t todo-api:latest .
```

### **4. СКРИНШОТЫ ВЫПОЛНЕНИЯ РАБОТЫ**

> * Закрыты все критерии из методички: структура, история, ветвление, MR-процесс, хуки, CI/CD, Registry (образ собирается и пушится в build), окружения, документация.
> * Проект запускается локально (`uvicorn src.main:app --reload`) и через `docker compose up --build`.

### **5. ОТВЕТЫ НА ВОПРОСЫ ДЛЯ ЗАЩИТЫ**

#### **1. Какую стратегию ветвления выбрали и почему?**
Git Flow: `main`/`develop` + `feature/*`. Итоговый проект версионный (1.0.0/1.1.0), нужна изоляция фич и стабильный main — это ровно Git Flow.

#### **2. Как организован CI/CD?**
lint (flake8) → test (pytest) → build (docker build + push `$CI_REGISTRY_IMAGE:$SHA`) → staging (auto от develop) / production (manual от main). MR-правила на lint/test.

#### **3. Какие Git Hooks и зачем?**
pre-commit (trailing-whitespace, end-of-file, check-yaml, detect-private-key): гигиена и защита от секретов до коммита; `install-hooks.sh` ставит через `pre-commit install`.

#### **4. Управление окружениями?**
`environment: staging` (auto от develop) и `production` (manual от main). История и откат — Deployments → Environments.

#### **5. Инструменты автоматизации?**
pre-commit, GitLab CI/CD (lint/test/build/deploy), Docker + Compose, скрипты `install-hooks.sh`/`deploy.sh`.

#### **6. Тестирование?**
pytest + TestClient: root, health, create, list, 404. Запуск в CI (`python -m pytest tests/ -v`) и локально.

#### **7. MR и Code Review?**
Ветка от `develop` → MR → зелёный CI → ревью → merge `--no-ff`. Прямой push в `main`/`develop` запрещён защитой.

#### **8. Что исключено из репозитория и почему?**
`__pycache__/`, `*.pyc`, `venv/`, `dist/build/`, `.env`, IDE, системные файлы, `*.key/pem` — мусор, зависимости и секреты не должны попадать в историю.

#### **9. Безопасность секретов?**
Секреты только в env (`.env.example` как образец), `.gitignore` режет `.env`/`*.key`, `detect-private-key` ловит случайный коммит.

#### **10. Что улучшить при большем времени?**
PostgreSQL вместо dict-хранилища, миграции, JWT-авторизацию, coverage-бейдж с реальным процентом, Review Apps на MR, deploy в Kubernetes.

### **6. ИСПОЛЬЗУЕМЫЕ КОМАНДЫ**
```
git checkout -b develop / feature/categories
git commit -m "feat: initial project setup with FastAPI"
git merge --no-ff feature/categories -m "Merge branch 'feature/categories' into develop"
pip install -r requirements.txt / python -m pytest tests/ -v
docker build -t todo-api:latest . / docker compose up --build
uvicorn src.main:app --reload
```
### **7. ВЫВОДЫ**

> 1. Все практики курса собраны в одном репозитории и работают вместе.
> 2. Git Flow + MR + CI + хуки дают предсказуемый релиз.
> 3. Проект готов к защите: структура, история, пайплайн и документация на месте.
> 4. Дальнейший рост — БД, авторизация, Review Apps, Kubernetes.
