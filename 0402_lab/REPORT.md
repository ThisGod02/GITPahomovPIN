# **Отчет по лабораторной работе №4: «Управление историей коммитов: rebase, reset, revert и интерактивный rebase»**

## **Сведения о студенте**
**Дата:** 2026-09-15
**Семестр:** 3 курс, 5 семестр
**Группа:** ПИН-Б-О-24-2
**Дисциплина:** Системы контроля версий
**Студент:** Пахомов Давид Вадимович

### **Структура готового проекта**
```
0402_lab/
├── .git/
├── 0402_lab.md   # Методичка
├── REPORT.md     # Данный отчет
├── NOTES.md      # Шпаргалка reset/revert/restore/rebase
├── file1.txt / file2.txt / file3.txt
├── app.py        # Пример для --amend
├── file.txt      # Серия из 5 строк + squash
└── history.txt   # git log --graph --all
```
### **Ссылка на репозиторий GitLab**
```
https://gitlab.com/pahomov-david/collab-project
```

### **1. ЦЕЛЬ РАБОТЫ**

> 1. Освоить отмену изменений: reset, revert, restore.
> 2. Переписывать историю через `git rebase -i`.
> 3. Отличить rebase от merge.
> 4. Безопасно работать с `push --force`.
> 5. Закрепить работу с GitLab после изменения истории.

### **2. ЗАДАЧИ РАБОТЫ**

> 1. Серия коммитов file1–file3, отмена через `reset --soft` с новым сообщением.
> 2. Правка file2 + безопасная отмена через `revert`.
> 3. Исправление опечатки через `commit --amend`.
> 4. Серия из 5 коммитов в file.txt, squash последних трёх через `reset --soft`.
> 5. Описаны reword/squash/drop/edit, `--force-with-lease`, reflog, filter-branch.

### **3. ХОД ВЫПОЛНЕНИЯ РАБОТЫ**

#### **3.1. Reset / revert / restore**
```
git checkout -b feature/experiment
git commit -m "feat: add file1" && git commit -m "feat: add file2" && git commit -m "feat: add file3"
git reset --soft HEAD~1
git commit -m "feat: add file3 with description"
git commit -m "feat: update file2"
git revert HEAD --no-edit
git restore data.txt / git restore --staged data.txt
```

#### **3.2. Amend и squash**
```
git commit -m "feat: add app fumction"
git commit --amend -m "feat: add app function"
for i in 1..5: echo "Строка $i" >> file.txt && git commit -m "feat: add line $i"
git reset --soft HEAD~3
git commit -m "feat: add lines 3-5 (squashed)"
```

#### **3.3. После изменения истории**
```
git push --force-with-lease origin feature/rebase_experiment
# MR feature/rebase_experiment -> main: история чистая
git reflog / git branch recovery-branch <hash>
git filter-branch --force --index-filter "git rm --cached --ignore-unmatch secret.txt" --prune-empty -- --all
```
Фактическая история (`history.txt`):
```
* c3d4efa docs: add rebase notes and history
* d74a041 feat: add lines 3-5 (squashed)
* 58e47c0 feat: add app function
* 714d09a Revert "feat: update file2"
```

### **4. СКРИНШОТЫ ВЫПОЛНЕНИЯ РАБОТЫ**

> * Показана разница «переписывает / не переписывает историю».
> * Интерактивные операции reword/squash/drop/edit описаны и частично выполнены неинтерактивно (эквивалент `reset --soft`).
> * Зафиксировано правило `--force-with-lease` только для своей ветки.

### **5. ОТВЕТЫ НА КОНТРОЛЬНЫЕ ВОПРОСЫ**

#### **1. reset vs revert?**
`reset` двигает HEAD и переписывает историю (локально), `revert` добавляет обратный коммит (безопасно для общих веток).

#### **2. Что делает reset --hard и почему опасен?**
Удаляет коммиты, индекс и рабочие изменения. Данные теряются (спасает только reflog).

#### **3. Что умеет rebase -i?**
reword (сообщение), squash/fixup (объединить), drop (удалить), edit (остановиться и поправить), exec (команда).

#### **4. Как объединить коммиты с сохранением сообщений?**
`git rebase -i`, пометить `squash`, в редакторе оставить нужные сообщения.

#### **5. Как изменить сообщение последнего коммита?**
`git commit --amend -m "новое сообщение"` (или `--no-edit` при добавлении файла).

#### **6. Почему push --force опасен?**
Перезаписывает удалённую историю: чужие коммиты могут потеряться.

#### **7. Что такое --force-with-lease?**
Force с проверкой: упадёт, если remote обновился после последнего fetch.

#### **8. Как восстановить коммит после reset --hard?**
`git reflog` → найти хеш → `git branch recovery-branch <hash>` / `git checkout <hash>`.

#### **9. revert или reset?**
Общая ветка — `revert`; локальная черновая — `reset`.

#### **10. Почему нельзя rebase в общих ветках?**
Меняются хеши уже опубликованных коммитов — у всех коллег разъедется история.

### **6. ИСПОЛЬЗУЕМЫЕ КОМАНДЫ**
```
git reset --soft/--mixed/--hard HEAD~1
git revert HEAD --no-edit
git restore <file> / git restore --staged <file>
git commit --amend -m "..."
git rebase -i HEAD~5 / --continue / --abort / --skip
git push --force-with-lease origin <branch>
git reflog
```
### **7. ВЫВОДЫ**

> 1. Разграничены безопасные и переписывающие операции.
> 2. Освоены amend, revert, soft-reset как squash.
> 3. Сформулировано золотое правило rebase и безопасный force-push.
> 4. Отработано восстановление через reflog.
