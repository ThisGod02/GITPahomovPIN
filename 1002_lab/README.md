# Todo API — REST API для управления задачами
Итоговый проект: FastAPI-сервис с Git Flow, CI/CD, Docker и документацией.
## Функциональность
- CRUD задач: создание, просмотр, удаление;
- категории задач;
- health-check (`/health`), автодокументация (`/docs`).
## Запуск
```bash
pip install -r requirements.txt
uvicorn src.main:app --reload
docker compose up --build
```
## CI/CD
lint -> test -> build -> staging (авто) / production (вручную). Ветки main/develop защищены, изменения через MR.
## Автор
Иванов Иван, группа ПИ-301
