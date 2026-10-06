# reset / revert / restore / rebase — шпаргалка

| Команда | История | Когда использовать |
|---|---|---|
| `git reset --soft HEAD~1` | Переписывает | Отмена коммита, изменения остаются в индексе (локально) |
| `git reset --mixed HEAD~1` | Переписывает | Отмена коммита и индексации, изменения в рабочей директории |
| `git reset --hard HEAD~1` | Переписывает | Полная отмена (**опасно**, восстановление через `reflog`) |
| `git revert HEAD` | НЕ переписывает | Безопасная отмена в общих ветках (обратный коммит) |
| `git restore file` | Не трогает | Отмена изменений в рабочей директории |
| `git commit --amend` | Переписывает последний | Исправление сообщения/состава последнего локального коммита |

## Интерактивный rebase (`git rebase -i`)
- `reword` — изменить сообщение; `squash`/`fixup` — объединить; `drop` — удалить; `edit` — остановиться и поправить; `exec` — выполнить команду.
- Золотое правило: **не делать rebase в общих ветках** (`main`, `develop`).
- После переписывания истории своей ветки: `git push --force-with-lease` (безопаснее `--force`).

## Восстановление через reflog
```bash
git reflog
git branch recovery-branch <commit-hash>
```

## Полное удаление файла из истории
```bash
git filter-branch --force --index-filter "git rm --cached --ignore-unmatch secret.txt" --prune-empty -- --all
# современный вариант: git-filter-repo
```

## Выполнено по методичке
Ветка `feature/experiment`: серия коммитов `feat: add file1/2/3`, `reset --soft` с новым сообщением, правка `file2.txt` + `revert`, `amend` для `app.py`, серия из 5 коммитов в `file.txt` со squash последних трёх через `reset --soft`. История — в `history.txt`.
