# **Отчет по лабораторной работе №2: «Ветвление, слияние и разрешение конфликтов в Git»**

## **Сведения о студенте**
**Дата:** 2026-09-10
**Семестр:** 3 курс, 5 семестр
**Группа:** ПИН-Б-О-24-2
**Дисциплина:** Системы контроля версий
**Студент:** Пахомов Давид Вадимович

### **Структура готового проекта**
```
0202_lab/
├── .git/
├── 0202_lab.md     # Методичка
├── REPORT.md       # Данный отчет
├── features.txt    # Основной файл экспериментов
├── diff.txt        # git diff HEAD~2 HEAD
└── history.txt     # git log --oneline --graph --all
```
### **Ссылка на репозиторий GitLab**
```
https://gitlab.com/pahomov-david/hello-git
```

### **1. ЦЕЛЬ РАБОТЫ**

> 1. Освоить ветки: создание, переключение, удаление.
> 2. Выполнять слияние (`git merge`) в разных сценариях.
> 3. Изучить механизм конфликтов и их разрешение.
> 4. Познакомиться с `git rebase` и сравнить со слиянием.
> 5. Закрепить работу с удалённым репозиторием GitLab.

### **2. ЗАДАЧИ РАБОТЫ**

> 1. Создан `features.txt` и базовый коммит.
> 2. Ветка `feature/payment` слита fast-forward.
> 3. Воспроизведён и вручную разрешён конфликт в строке профиля (`feature/profile`).
> 4. Выполнено комплексное задание: фичи 1–3, `diff.txt`, `reset --hard`, исправленная фича, rebase `feature/third` на `main`, merge `--no-ff`, ветка `release`.
> 5. История сохранена в `history.txt`.

### **3. ХОД ВЫПОЛНЕНИЯ РАБОТЫ**

#### **3.1. База и fast-forward**
```
git add features.txt && git commit -m "feat: add features.txt with core features"
git checkout -b feature/payment   # + "4. Оплата через карту"
git checkout main && git merge feature/payment
```

#### **3.2. Конфликт и ручное разрешение**
В `feature/profile` и `main` изменена одна и та же строка «2. Просмотр профиля». При `git merge feature/profile` получены маркеры `<<<<<<< / ======= / >>>>>>>`, оставлен объединённый вариант «Просмотр и настройка профиля (расширенный режим)», затем `git add` + `git commit`.

#### **3.3. Комплексное задание**
```
git commit -m "feat: add first feature"
git commit -m "feat: add second feature"
git checkout -b feature/third   # "третья фича"
git diff HEAD~2 HEAD > diff.txt
git checkout main && git reset --hard HEAD~1
git commit -m "fix: add corrected feature"
git rebase --onto main <oldbase> feature/third
git checkout main && git merge --no-ff feature/third -m "Merge branch 'feature/third' into main"
git branch release
git log --oneline --graph --all > history.txt
```
Фактический граф (`history.txt`):
```
* afb8737 docs: add lab artifacts (diff, history)
*   c5b7fce Merge branch 'feature/third' into main
|\
| * 7cfffe2 feat: add third feature
|/
* 85fa1ff fix: add corrected feature
* d71e78c feat: add first feature
*   ca490e2 Merge branch 'feature/profile' into main
```

### **4. СКРИНШОТЫ ВЫПОЛНЕНИЯ РАБОТЫ**

> * Продемонстрированы fast-forward, трёхстороннее слияние и merge `--no-ff`.
> * Конфликт разрешён вручную с удалением маркеров.
> * Ветка `feature/third` пересажена на актуальный `main` через rebase.

### **5. ОТВЕТЫ НА КОНТРОЛЬНЫЕ ВОПРОСЫ**

#### **1. Что такое ветка в Git и как она реализована технически?**
Лёгкий подвижный указатель на коммит (файл в `.git/refs/heads/`). Коммит сдвигает указатель текущей ветки.

#### **2. В чём разница между git merge и git rebase? Когда что применять?**
Merge сохраняет историю обеих веток и создаёт merge-коммит; rebase переносит коммиты поверх другой ветки, история линейная. Merge — для общих веток, rebase — для локальных feature-веток.

#### **3. Что такое конфликт слияния и как он возникает?**
Когда одна и та же строка изменена в обеих ветках — Git не может выбрать вариант автоматически.

#### **4. Как разрешить конфликт вручную? Маркеры?**
Открыть файл, выбрать нужный вариант, удалить `<<<<<<<` (HEAD), `=======` (разделитель), `>>>>>>>` (имя ветки), затем `git add` и `git commit`.

#### **5. В чём отличие git reset от git revert?**
`reset` переписывает историю (откатывает HEAD), `revert` создаёт новый обратный коммит, историю не трогает. В общих ветках — только `revert`.

#### **6. Что такое fast-forward merge?**
Когда ветка — прямой потомок текущей: указатель просто сдвигается, merge-коммит не создаётся. Трёхстороннее слияние создаёт merge-коммит из двух голов и общего предка.

#### **7. Зачем нужна ветка release в Git Flow?**
Для стабилизации релиза: финальные правки, версия, документация — без остановки разработки в `develop`.

#### **8. Как отправить все локальные ветки в удалённый репозиторий?**
`git push --all origin` (теги — `git push --tags`).

#### **9. Почему rebase опасен на общих ветках?**
Меняет хеши коммитов: у коллег, уже синхронизировавшихся, появятся дубли и расхождение истории.

### **6. ИСПОЛЬЗУЕМЫЕ КОМАНДЫ**
```
git branch / git switch -c / git checkout -b
git merge / git merge --no-ff
git diff HEAD~2 HEAD > diff.txt
git reset --hard HEAD~1
git rebase --onto main <base> feature/third
git log --oneline --graph --all > history.txt
git push --all origin
```
### **7. ВЫВОДЫ**

> 1. Освоены создание веток и все виды слияний.
> 2. Отработано ручное разрешение конфликтов.
> 3. Rebase применён для линеаризации feature-ветки, merge — для общих веток.
> 4. Артефакты `diff.txt` и `history.txt` подтверждают выполнение.
