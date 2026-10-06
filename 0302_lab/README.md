# **Отчет по лабораторной работе №3: «Работа с удалёнными репозиториями. Совместная разработка в GitLab»**

## **Сведения о студенте**
**Дата:** 2026-09-12
**Семестр:** 3 курс, 5 семестр
**Группа:** ПИН-Б-О-24-2
**Дисциплина:** Системы контроля версий
**Студент:** Пахомов Давид Вадимович

### **Структура готового проекта**
```
0302_lab/
├── .git/
├── 0302_lab.md        # Методичка
├── REPORT.md          # Данный отчет
├── README.md          # Описание collab-project
├── CONTRIBUTORS.md    # Участники (Ментор + Разработчик)
├── MY_CONTRIBUTION.md # Вклад участника
├── calc.py            # feature/calculator: add/sub
├── test_calc.py       # Тесты калькулятора
├── REMOTES.md         # Шпаргалка по remotes и MR
└── history.txt        # git log --graph --all
```
### **Ссылка на репозиторий GitLab**
```
https://gitlab.com/pahomov-david/collab-project
```

### **1. ЦЕЛЬ РАБОТЫ**

> 1. Освоить remote/fetch/pull/push.
> 2. Изучить модель Fork + Merge Request в GitLab.
> 3. Работать с несколькими remotes (`origin`, `upstream`).
> 4. Освоить Code Review.
> 5. Познакомиться с защитой веток.

### **2. ЗАДАЧИ РАБОТЫ**

> 1. Создан базовый проект `collab-project` с `CONTRIBUTORS.md`.
> 2. Отработан цикл Fork → Clone → feature-ветка → Push → MR → Review → Merge.
> 3. Настроен `upstream`, показана синхронизация форка.
> 4. Выполнено комплексное задание: ветка `feature/calculator`, `calc.py` с `add(a, b)`, MR, синхронизация, `history.txt`.
> 5. Описана защита `main` (только через MR).

### **3. ХОД ВЫПОЛНЕНИЯ РАБОТЫ**

#### **3.1. Базовый репозиторий**
```
git commit -m "docs: add CONTRIBUTORS.md"
```

#### **3.2. Fork + upstream**
```
git clone git@gitlab.com:pahomov-david/collab-project.git
git remote add upstream git@gitlab.com:original-owner/collab-project.git
git remote -v
git checkout -b feature/add_contributor
# правки CONTRIBUTORS.md + MY_CONTRIBUTION.md
git commit -m "docs: add self to contributors"
git push origin feature/add_contributor
# GitLab: New merge request (source feature/add_contributor -> target main)
git checkout main && git fetch upstream && git merge upstream/main && git push origin main
```

#### **3.3. Комплексное задание (калькулятор)**
```
git checkout -b feature/calculator
# calc.py: add(a, b), sub(a, b); test_calc.py
git commit -m "feat: add calculator module"
# push -> MR -> review -> merge
git log --oneline --graph --all > history.txt
```
Фактическая история:
```
* c9cf1f2 docs: add remotes guide and history
*   061e1fe Merge branch 'feature/calculator'
| * 96fa037 feat: add calculator module
*   6ce97cb Merge branch 'feature/add_contributor'
```

### **4. СКРИНШОТЫ ВЫПОЛНЕНИЯ РАБОТЫ**

> * Оба MR-цикла (участник + калькулятор) слиты через `--no-ff`.
> * Файл `REMOTES.md` фиксирует порядок синхронизации форка.
> * Защита веток описана: `main` — Maintainers/только MR.

### **5. ОТВЕТЫ НА КОНТРОЛЬНЫЕ ВОПРОСЫ**

#### **1. Что такое форк и зачем он нужен?**
Серверная копия чужого репозитория в своём аккаунте: changes изолированы, в upstream попадают только через MR.

#### **2. В чём разница между git fetch и git pull?**
`fetch` скачивает без изменения рабочей ветки, `pull` = `fetch` + merge/rebase.

#### **3. Зачем добавлять upstream?**
Чтобы подтягивать изменения оригинала в форк (`fetch upstream` + `merge upstream/main`).

#### **4. Что такое Merge Request и его роль?**
Запрос на вливание ветки: обсуждение, CI, ревью, контролируемое слияние.

#### **5. Этапы MR от создания до слияния?**
Push ветки → New MR → Changes/Review → правки → approve → Merge (commit/squash/rebase) → синхронизация.

#### **6. Что такое Code Review и зачем?**
Проверка кода коллегами: качество, баги, знания. В GitLab — комментарии к строкам во вкладке Changes.

#### **7. Как обновить форк?**
`git fetch upstream; git checkout main; git merge upstream/main; git push origin main`.

#### **8. Что такое защищённые ветки?**
Ограничение прямого push (Settings → Repository → Protected Branches): изменения только через MR, опционально approve и зелёный CI.

#### **9. Merge commit vs Squash vs Rebase and merge?**
Merge commit сохраняет все коммиты + merge-коммит; Squash сжимает в один; Rebase and merge линеаризует без merge-коммита.

#### **10. Как добавить участников в GitLab-проект?**
Settings → Members → Invite member (роль Developer/Maintainer).

### **6. ИСПОЛЬЗУЕМЫЕ КОМАНДЫ**
```
git remote -v / git remote add upstream <url>
git fetch upstream / git pull --rebase upstream main
git checkout -b feature/calculator
git push origin feature/calculator
git log --oneline --graph --all > history.txt
```
### **7. ВЫВОДЫ**

> 1. Освоена модель Fork + MR и два remotes.
> 2. Выполнены ревью-правки (`fix: correct contributors table formatting` по методичке).
> 3. Настроено понимание защиты веток и методов слияния MR.
> 4. Комплексное задание закрыто калькулятором и историей.
