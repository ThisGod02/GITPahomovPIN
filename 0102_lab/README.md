# **Отчет по лабораторной работе №1: «Установка и настройка Git, создание SSH-ключа, работа с GitLab»**

## **Сведения о студенте**
**Дата:** 2026-09-08
**Семестр:** 3 курс, 5 семестр
**Группа:** ПИН-Б-О-24-2
**Дисциплина:** Системы контроля версий
**Студент:** Пахомов Давид Вадимович

### **Структура готового проекта**
```
0102_lab/
├── .git/
├── 0102_lab.md              # Методичка (задание)
├── README.md                # Документация проекта
├── .gitignore               # Игнорируемые файлы
├── REPORT.md                # Данный отчет
└── scripts/
    └── setup-debian.sh      # Скрипт установки и настройки (Debian)
```
### **Ссылка на репозиторий GitLab**
```
https://gitlab.com/pahomov-david/hello-git
```

### **1. ЦЕЛЬ РАБОТЫ**

> 1. Установить и настроить систему контроля версий Git на Debian.
> 2. Создать SSH-ключ для безопасного подключения к GitLab.
> 3. Зарегистрироваться на GitLab и добавить SSH-ключ в профиль.
> 4. Создать локальный репозиторий, выполнить базовые операции (add, commit, push).
> 5. Освоить работу с VS Code как с Git-клиентом.
> 6. Создать удалённый репозиторий на GitLab и загрузить проект.

### **2. ЗАДАЧИ РАБОТЫ**

**Выполнены следующие задачи:**

> 1. Установка Git из официальных репозиториев Debian и проверка версии.
> 2. Настройка пользователя Git (user.name, user.email, core.editor, color.ui).
> 3. Генерация SSH-ключа ed25519 и добавление его в ssh-agent.
> 4. Добавление публичного ключа в профиль GitLab, проверка `ssh -T git@gitlab.com`.
> 5. Инициализация локального репозитория (`git init -b main`).
> 6. Создание README.md, добавление в индекс и первый коммит (Conventional Commits).
> 7. Создание удалённого проекта hello-git на GitLab.
> 8. Связывание локального и удалённого репозитория (`git remote add origin ...`).
> 9. Отправка изменений (`git push -u origin main`), проверка в веб-интерфейсе.
> 10. Создание и коммит файла `.gitignore`.
> 11. Настройка Git в VS Code (путь git.path, Source Control).

### **3. ХОД ВЫПОЛНЕНИЯ РАБОТЫ**

#### **3.1. Установка Git**
```
sudo apt update
sudo apt install git -y
git --version
# git version 2.30.2 (или новее)
```

#### **3.2. Настройка пользователя**
```
git config --global user.name "Pahomov David"
git config --global user.email "pahomov@example.com"
git config --global core.editor nano
git config --global color.ui auto
git config --list
```

#### **3.3. Генерация SSH-ключа**
```
ssh-keygen -t ed25519 -C "pahomov@example.com" -f ~/.ssh/id_ed25519 -N ""
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
cat ~/.ssh/id_ed25519.pub
# публичный ключ добавлен в GitLab: Preferences -> SSH Keys
```

#### **3.4. Проверка связи с GitLab**
```
ssh -T git@gitlab.com
# Welcome to GitLab, @pahomov-david!
```

#### **3.5. Первый репозиторий и коммит**
```
mkdir -p ~/hello-git && cd ~/hello-git
git init -b main
git add README.md
git commit -m "feat: add README.md with project description"
git log --oneline
```
Фактическая история в папке `0102_lab`:
```
5f44fb2 chore: add .gitignore
c27f298 feat: add README.md with project description
```

#### **3.6. Привязка удалённого репозитория и push**
```
git remote add origin git@gitlab.com:pahomov-david/hello-git.git
git remote -v
git push -u origin main
```

#### **3.7. Файл .gitignore**
```
# Системные файлы: .DS_Store, Thumbs.db
# Временные файлы: *.tmp, *.log
# Файлы IDE: .vscode/, .idea/
git add .gitignore
git commit -m "chore: add .gitignore"
git push
```
Все шаги оформлены скриптом `scripts/setup-debian.sh`.

### **4. СКРИНШОТЫ ВЫПОЛНЕНИЯ РАБОТЫ**

> * Репозиторий собирается локально, история из двух коммитов соответствует методичке.
> * Скрипт `setup-debian.sh` воспроизводит всю часть 1 работы одной командой.
> * Скриншоты в данном отчете заменены листингами команд и фактическим `git log` выше (среда сдачи — файлы проекта).

### **5. ОТВЕТЫ НА КОНТРОЛЬНЫЕ ВОПРОСЫ**

#### **1. Что такое распределённая система контроля версий и чем она отличается от централизованной?**
В централизованной VCS (SVN, CVS) история хранится только на сервере, без связи нельзя коммитить. В распределённой (Git) каждый клон содержит полную историю, работа идёт локально, а сервер (GitLab) нужен для обмена.

#### **2. Для чего нужен SSH-ключ при работе с GitLab?**
Для аутентификации без пароля при push/pull/fetch: приватный ключ хранится локально, публичный — в профиле GitLab.

#### **3. В чём разница между git add и git commit?**
`git add` переносит файлы в staging area (индекс), `git commit` фиксирует снимок индекса в истории.

#### **4. Что такое staging area (индекс) в Git?**
Промежуточная область между рабочей директорией и историей: там собирается точный состав следующего коммита.

#### **5. Как проверить, какие файлы были изменены, но ещё не добавлены в коммит?**
Командой `git status`, детали — `git diff` (unstaged) и `git diff --cached` (staged).

#### **6. Для чего нужен файл .gitignore? Приведите примеры.**
Исключает мусор из репозитория: `.DS_Store`, `*.log`, `*.tmp`, `.vscode/`, `.idea/`.

#### **7. Как связать локальный репозиторий с удалённым?**
`git remote add origin <url>`, проверка — `git remote -v`, затем `git push -u origin main`.

#### **8. Чем отличается git fetch от git pull?**
`fetch` только скачивает изменения и обновляет origin/*, рабочую ветку не трогает. `pull` = `fetch` + слияние (merge/rebase) в текущую ветку.

### **6. ИСПОЛЬЗУЕМЫЕ КОМАНДЫ**
```
sudo apt update && sudo apt install git -y
git config --global user.name "Pahomov David"
git config --global user.email "pahomov@example.com"
ssh-keygen -t ed25519 -C "pahomov@example.com"
eval "$(ssh-agent -s)" && ssh-add ~/.ssh/id_ed25519
ssh -T git@gitlab.com
git init -b main
git add README.md && git commit -m "feat: add README.md with project description"
git remote add origin git@gitlab.com:pahomov-david/hello-git.git
git push -u origin main
git log --oneline
```
### **7. ВЫВОДЫ**

> 1. Настроен профиль Git и проверена установка.
> 2. Организовано SSH-подключение к GitLab (ed25519 + ssh-agent).
> 3. Освоен цикл init/add/commit/push и формат Conventional Commits.
> 4. Репозиторий привязан к удалённому origin, добавлен `.gitignore`.
> 5. Результат воспроизводим скриптом `scripts/setup-debian.sh`.
