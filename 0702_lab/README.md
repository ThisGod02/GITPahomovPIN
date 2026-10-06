# Окружения, Review Apps и стратегии развертывания

Node.js + Express (`index.js`), `Dockerfile`, пайплайн: `test` → `build` (образ в Container Registry) → `deploy`.
Статические окружения: `staging` (авто, только `main`), `production` (ручной запуск). Динамические Review Apps: на каждый MR создаётся `review/$CI_COMMIT_REF_SLUG` с автоостановкой через неделю и ручной остановкой (`stop_review`).

```bash
npm install
npm test
npm start
```

Стратегии развертывания: recreate (по умолчанию в примере), rolling (обновление без даунтайма), blue-green и canary — выбираются на стороне рантайма/оркестратора, пайплайн отдаёт проверенный образ и окружение.
