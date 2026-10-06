# Сравнение стратегий ветвления

| Критерий | Git Flow | GitLab Flow | Trunk-based |
|---|---|---|---|
| Основные ветки | `main`, `develop` + `feature/*`, `release/*`, `hotfix/*` | `main` + `feature/*` + ветки окружений (`staging`, `production`) | Одна `main`, короткоживущие ветки (1–2 дня) |
| Сложность | Высокая | Средняя | Низкая |
| Частота релизов | Редкие версионные релизы | Частые, через окружения | Очень частые |
| CI/CD | Опционален | Встроен (деплой через окружения + MR) | Обязателен + feature-флаги |
| Конфликты | Чаще (долгоживущие ветки) | Реже | Минимальны |

## Рекомендации по выбору
- **Git Flow** — версионные продукты с редкими релизами, большая команда, нужна изоляция релиза.
- **GitLab Flow** — веб-сервисы с окружениями staging/production, деплой через CI/CD.
- **Trunk-based** — зрелая команда, частые релизы, сильные автотесты и feature-флаги.

## Выполнено по методичке
Git Flow: `develop` от `main`, `feature/login`, MR в `develop`, `release/v1.0` (версия `1.0.0`), слияние в `main` + тег `v1.0.0` и в `develop`, `hotfix/auth-fix` в `main`/`develop` + тег `v1.0.1`. GitLab Flow: мини-проект `gitlabflow-lab` с CI и окружениями staging/production. Защита веток: `main` — только Maintainers через MR, `develop` — Developers+Maintainers.
