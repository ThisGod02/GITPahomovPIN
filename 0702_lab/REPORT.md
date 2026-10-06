# **Отчет по лабораторной работе №7: «Окружения, Review Apps и управление развертыванием в GitLab»**

## **Сведения о студенте**
**Дата:** 2026-09-25
**Семестр:** 3 курс, 5 семестр
**Группа:** ПИН-Б-О-24-2
**Дисциплина:** Системы контроля версий
**Студент:** Пахомов Давид Вадимович

### **Структура готового проекта**
```
0702_lab/
├── 0702_lab.md      # Методичка
├── REPORT.md        # Данный отчет
├── package.json     # environments-lab (express)
├── index.js         # / и /health (ENVIRONMENT/APP_VERSION)
├── test.js          # smoke-тест
├── Dockerfile       # node:18-alpine
└── .gitlab-ci.yml   # test/build/deploy/cleanup + review/stop_review
```
### **Ссылка на репозиторий GitLab**
```
https://gitlab.com/pahomov-david/environments-lab
```

### **1. ЦЕЛЬ РАБОТЫ**

> 1. Настроить статические окружения staging/production.
> 2. Реализовать Review Apps на каждый MR.
> 3. Разграничить авто- и ручной деплой.
> 4. Разобрать стратегии развертывания.

### **2. ЗАДАЧИ РАБОТЫ**

> 1. Создано Express-приложение с `/health` и версионированием через env.
> 2. Добавлен `Dockerfile`, образ публикуется в Registry (`build`).
> 3. `deploy_staging` — авто на main; `deploy_production` — manual + Protected Environment.
> 4. `review` — динамическое `review/$CI_COMMIT_REF_SLUG` на MR с `on_stop: stop_review` и `auto_stop_in: 1 week`.
> 5. `stop_review` — ручная остановка (action: stop, stage cleanup).

### **3. ХОД ВЫПОЛНЕНИЯ РАБОТЫ**

#### **3.1. Приложение и образ**
```
npm install && npm test && npm start
docker build -t $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA .
docker push $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA
```

#### **3.2. Окружения**
```
deploy_staging: ENVIRONMENT=staging, rules main (auto)
deploy_production: environment production, when manual (только main)
review: name review/$CI_COMMIT_REF_SLUG, url https://$CI_COMMIT_REF_SLUG.review.example.com, rules MR only
stop_review: action stop, when manual
# GitLab -> Deployments -> Environments: staging/production/review/*, история и откат
```

### **4. СКРИНШОТЫ ВЫПОЛНЕНИЯ РАБОТЫ**

> * Каждый MR получает живую ссылку для проверки до слияния.
> * Production защищён ручным запуском и правами (Protected Environment).
> * Review Apps не висят: автостоп через неделю + ручной stop.

### **5. ОТВЕТЫ НА КОНТРОЛЬНЫЕ ВОПРОСЫ**

#### **1. Что такое Environment и его типы?**
Именованное место назначения деплоя (staging/production/review). Статические заданы явно, динамические создаются по шаблону (`review/$CI_COMMIT_REF_SLUG`).

#### **2. Что такое Review Apps и их задачи?**
Временные окружения на MR: проверить фичу живьём, показать заказчику, прогнать e2e до merge.

#### **3. Автосоздание Review App на MR?**
Джоба `review` с `rules: if: $CI_PIPELINE_SOURCE == 'merge_request_event'` + `environment: {name: review/..., on_stop: stop_review}`.

#### **4. Ручной деплой в production?**
`when: manual` + `rules` на main + Protected Environment (доступ только у Maintainers).

#### **5. Только определённые пользователи в production?**
Deployments → Environments → Protected (Allowed to deploy: Maintainers + approve).

#### **6. Остановка Review App после MR?**
`stop_review` (`action: stop`) вручную или `auto_stop_in` по времени; при merge GitLab останавливает связанное окружение.

#### **7. Динамические окружения?**
Имя/URL собираются из переменных (`$CI_COMMIT_REF_SLUG`), GitLab создаёт отдельное окружение на каждую ветку/MR.

#### **8. Переменные только для окружения?**
Settings → CI/CD → Variables → Environment scope (staging/production) или `environment:` в джобе.

#### **9. История деплоев и откат?**
Deployments → Environments → история, кнопка Rollback / повторный деплой старого образа.

#### **10. Continuous Deployment vs Delivery?**
Delivery — релиз готов и ждёт ручного подтверждения; Deployment — выкатывается автоматически после зелёного пайплайна.

### **6. ИСПОЛЬЗУЕМЫЕ КОМАНДЫ**
```
npm install / npm test / npm start
docker build -t $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA .
docker push $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA
```
### **7. ВЫВОДЫ**

> 1. Статика (staging/production) + динамика (review/*) закрывают весь цикл.
> 2. Ручной production + protected env = безопасность.
> 3. Review Apps ускоряют ревью: смотрят живое, а не дифф.
> 4. Стратегии (recreate/rolling/blue-green/canary) выбираются рантаймом, пайплайн отдаёт образ и окружение.
