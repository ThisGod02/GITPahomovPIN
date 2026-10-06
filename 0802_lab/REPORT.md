# **Отчет по лабораторной работе №8: «Git Submodules, Git LFS и Container Registry в GitLab»**

## **Сведения о студенте**
**Дата:** 2026-09-28
**Семестр:** 3 курс, 5 семестр
**Группа:** ПИН-Б-О-24-2
**Дисциплина:** Системы контроля версий
**Студент:** Пахомов Давид Вадимович

### **Структура готового проекта**
```
0802_lab/
├── 0802_lab.md                 # Методичка
├── REPORT.md                   # Данный отчет
├── .gitmodules                 # libs/shared -> shared-library
├── libs/shared/                # __init__.py, utils.py, README.md
├── .gitattributes              # *.png/jpg/psd/zip/mp4 -> LFS
├── assets/                     # logo.png, banner.jpg, create-assets.py
├── Dockerfile / app.py / requirements.txt
├── .gitlab-ci.yml              # lfs-check/build/test-image/publish/deploy
└── docs/                       # CLONE_WITH_SUBMODULES.md, SUBMODULES_VS_SUBTREE.md
```
### **Ссылка на репозиторий GitLab**
```
https://gitlab.com/pahomov-david/parent-project
```

### **1. ЦЕЛЬ РАБОТЫ**

> 1. Подключить внешний репозиторий как submodule.
> 2. Вынести бинарные файлы в Git LFS.
> 3. Публиковать образы в Container Registry через CI/CD.
> 4. Сравнить submodules и subtree.

### **2. ЗАДАЧИ РАБОТЫ**

> 1. `libs/shared` оформлена как общая библиотека (`format_greeting`, `slugify`), `.gitmodules` указывает на `shared-library`.
> 2. `.gitattributes` отслеживает `*.png/jpg/jpeg/psd/zip/mp4`; `assets/` сгенерированы скриптом.
> 3. Пайплайн: `lfs-check` (ls-files/status) → `build` → `test-image` → `publish` (push SHA + latest) → `deploy` (manual, staging).
> 4. Документированы клонирование с submodules и таблица submodules vs subtree.

### **3. ХОД ВЫПОЛНЕНИЯ РАБОТЫ**

#### **3.1. Submodules**
```
git submodule add git@gitlab.com:pahomov-david/shared-library.git libs/shared
git commit -m "feat: add shared-library submodule"
git clone --recurse-submodules git@gitlab.com:pahomov-david/parent-project.git
cd libs/shared && git pull origin main && cd ../..
git add libs/shared && git commit -m "chore: update shared-library submodule"
```

#### **3.2. LFS**
```
sudo apt install git-lfs -y && git lfs install
git lfs track "*.png" "*.jpg"
python3 assets/create-assets.py
git add .gitattributes assets/
git lfs ls-files && git lfs status
```

#### **3.3. Container Registry**
```
docker build -t $CI_REGISTRY_IMAGE:$CI_COMMIT_SHORT_SHA .
docker login $CI_REGISTRY -u $CI_REGISTRY_USER -p $CI_REGISTRY_PASSWORD
docker push $CI_REGISTRY_IMAGE:$CI_COMMIT_SHORT_SHA
docker tag ... :latest && docker push ... :latest
docker run -d --name registry-lab $CI_REGISTRY_IMAGE:latest
```

### **4. СКРИНШОТЫ ВЫПОЛНЕНИЯ РАБОТЫ**

> * Родительский проект хранит только ссылку на коммит submodule, не его код.
> * Бинарные файлы лежат как LFS-указатели, репозиторий лёгкий.
> * Образы версионируются SHA + latest и деплоятся из Registry.

### **5. ОТВЕТЫ НА КОНТРОЛЬНЫЕ ВОПРОСЫ**

#### **1. Что такое Submodule?**
Ссылка родительского репозитория на конкретный коммит внешнего репозитория (+ `.gitmodules`).

#### **2. Как добавить submodule?**
`git submodule add <url> <path>`, затем `git add .gitmodules <path>` + commit.

#### **3. Как клонировать с submodules?**
`git clone --recurse-submodules <url>` или `git submodule update --init --recursive`.

#### **4. Что такое Git LFS?**
Расширение для крупных файлов: в Git лежит указатель, контент — на LFS-сервере (GitLab поддерживает).

#### **5. Настройка LFS?**
`git lfs install`, `git lfs track "*.psd"`, коммит `.gitattributes`, push.

#### **6. Какие файлы в LFS?**
Бинарные и тяжёлые: `*.png/jpg/psd`, `*.zip`, `*.mp4`, датасеты, шрифты.

#### **7. Container Registry + CI/CD?**
Встроенное хранилище образов GitLab (`$CI_REGISTRY_IMAGE`); CI собирает/тестирует/пушит, деплой тянет образ оттуда.

#### **8. Как опубликовать образ?**
`docker build -t $CI_REGISTRY_IMAGE:$SHA .`, `docker login $CI_REGISTRY`, `docker push ...`.

#### **9. Submodules vs Subtree?**
Submodules хранят связь (нужен `--recurse-submodules`, обновление ссылкой); subtree вливает код (проще потребителю, сложнее отдавать upstream). Таблица — в `docs/SUBMODULES_VS_SUBTREE.md`.

#### **10. Использовать образ в другом проекте?**
`docker login $CI_REGISTRY` + `docker pull $CI_REGISTRY_IMAGE:<tag>` / ссылка в `image:` другого пайплайна.

### **6. ИСПОЛЬЗУЕМЫЕ КОМАНДЫ**
```
git submodule add <url> libs/shared
git clone --recurse-submodules <url>
git submodule update --init --recursive
git lfs install / git lfs track "*.png" / git lfs ls-files
docker build/push/pull + docker login $CI_REGISTRY
```
### **7. ВЫВОДЫ**

> 1. Submodules — для живых зависимостей со своей историей.
> 2. LFS — для бинарных файлов, иначе репозиторий распухает.
> 3. Registry + CI — единый путь образа от сборки до деплоя.
> 4. Выбор submodules/subtree зависит от связанности команд.
