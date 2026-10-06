# **Отчет по лабораторной работе №9: «Стратегии ветвления в команде. Git Flow, GitLab Flow и Trunk-based Development»**

## **Сведения о студенте**
**Дата:** 2026-10-01
**Семестр:** 3 курс, 5 семестр
**Группа:** ПИН-Б-О-24-2
**Дисциплина:** Системы контроля версий
**Студент:** Пахомов Давид Вадимович

### **Структура готового проекта**
```
0902_lab/
├── 0902_lab.md              # Методичка
├── REPORT.md                # Данный отчет
├── README.md                # gitflow-lab
├── version.txt              # 1.0.1
├── login.py                 # feature/login + hotfix
├── STRATEGY_COMPARISON.md   # таблица сравнения
├── history.txt              # git log --graph --all
└── gitlabflow-lab/
    ├── app.py               # приложение для GitLab Flow
    └── .gitlab-ci.yml       # test + staging/production
```
### **Ссылка на репозиторий GitLab**
```
https://gitlab.com/pahomov-david/gitflow-lab
https://gitlab.com/pahomov-david/gitlabflow-lab
```

### **1. ЦЕЛЬ РАБОТЫ**

> 1. Реализовать Git Flow (develop/feature/release/hotfix, теги).
> 2. Реализовать GitLab Flow (feature от main + окружения).
> 3. Разобрать Trunk-based Development.
> 4. Сравнить стратегии и выбрать подходящую под тип проекта.

### **2. ЗАДАЧИ РАБОТЫ**

> 1. `develop` от `main`, `feature/login` (`login.py: authenticate`), MR в `develop`.
> 2. `release/v1.0` (версия `1.0.0`), слияние в `main` + тег `v1.0.0` и в `develop`.
> 3. `hotfix/auth-fix` (`logout`, версия `1.0.1`), слияние в `main`/`develop` + тег `v1.0.1`.
> 4. Мини-проект `gitlabflow-lab`: feature-ветка от main, CI, staging (авто) / production (manual).
> 5. Таблица `STRATEGY_COMPARISON.md` + защита веток (main — Maintainers/только MR).

### **3. ХОД ВЫПОЛНЕНИЯ РАБОТЫ**

#### **3.1. Git Flow**
```
git checkout -b develop
git checkout -b feature/login   # login.py
git checkout develop && git merge --no-ff feature/login
git checkout -b release/v1.0    # version.txt -> 1.0.0
git checkout main && git merge --no-ff release/v1.0 && git tag v1.0.0
git checkout develop && git merge --no-ff release/v1.0
git checkout main && git checkout -b hotfix/auth-fix  # logout + 1.0.1
git checkout main && git merge --no-ff hotfix/auth-fix && git tag v1.0.1
git checkout develop && git merge --no-ff hotfix/auth-fix
```
Фактический граф (`history.txt`):
```
* b9a8627 (develop) docs: add strategy comparison and gitlab-flow example
*   0a39152 Merge branch 'hotfix/auth-fix' into develop
*   a4b559e (tag: v1.0.1, main) Merge branch 'hotfix/auth-fix' into main
*   b42c172 (tag: v1.0.0) Merge branch 'release/v1.0' into main
*   49b4695 Merge branch 'feature/login' into develop
```

#### **3.2. GitLab Flow**
```
# gitlabflow-lab/app.py от main, feature-ветка, MR
test: py_compile (MR + main)
deploy_staging: auto, only main
deploy_production: manual, only main
# Settings -> Repository -> Protected Branches:
# main: merge Maintainers, push No one
```

### **4. СКРИНШОТЫ ВЫПОЛНЕНИЯ РАБОТЫ**

> * Git Flow дал версионные релизы с изоляцией стабилизации и хотфиксов.
> * GitLab Flow дал деплой через окружения без ветки develop.
> * Trunk-based описан как опция для зрелых команд с фиче-флагами.

### **5. ОТВЕТЫ НА КОНТРОЛЬНЫЕ ВОПРОСЫ**

#### **1. Основные ветки Git Flow?**
`main`, `develop`, `feature/*`, `release/*`, `hotfix/*` (+ теги `v*`).

#### **2. Зачем develop?**
Интеграционная ветка: фичи сливаются туда, `main` хранит только релизы.

#### **3. Создание и слияние релизной ветки?**
`git checkout -b release/v1.0 develop` → версия/доки → merge в `main` (тег) и обратно в `develop`.

#### **4. hotfix vs feature?**
`feature` — новая функциональность от `develop`; `hotfix` — срочный фикс продакшена от `main`, сливается в обе ветки.

#### **5. Ветки GitLab Flow?**
`main` + `feature/*` + ветки окружений (`staging`, `production`) или деплой через `environment:`.

#### **6. Деплой на staging в GitLab Flow?**
Джоба с `environment: staging`, `rules` на main (авто), production — `when: manual`.

#### **7. Суть Trunk-based?**
Одна `main`, короткие ветки (1–2 дня), частые мерджи, фиче-флаги вместо долгоживущих веток.

#### **8. Преимущества фиче-флагов?**
Незавершённый код в main без релиза: включают/выключают фичу в рантайме, безопасные эксперименты.

#### **9. Стратегия для стартапа?**
GitLab Flow или Trunk-based: быстрый деплой через окружения, минимум overhead (обоснование — в STRATEGY_COMPARISON.md).

#### **10. Когда Git Flow?**
Версионные продукты, редкие релизы, большая команда, нужна изоляция релиза и поддержка старых версий.

### **6. ИСПОЛЬЗУЕМЫЕ КОМАНДЫ**
```
git checkout -b develop / feature/login / release/v1.0 / hotfix/auth-fix
git merge --no-ff <branch>
git tag v1.0.0 / git tag v1.0.1
git log --oneline --graph --all > history.txt
```
### **7. ВЫВОДЫ**

> 1. Git Flow — порядок ценой сложности; GitLab Flow — баланс для веба; Trunk-based — скорость ценой дисциплины.
> 2. Теги фиксируют релизы, hotfix чинит прод без остановки разработки.
> 3. Защита веток + MR обязательны в командной работе.
> 4. Выбор стратегии аргументирован таблицей сравнения.
