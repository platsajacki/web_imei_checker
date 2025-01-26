# Web IMEI Checker
Веб-сервис для проверки информации об устройстве по его IMEI-коду. Сервис использует [API](https://imeicheck.net/promo-api) для получения данных о мобильных устройствах и перенаправляет ответ.

На данном этапе проект может быть интрегрирован с Telegram ботом. В системе указывается белый список пользователей бота, которые могут им пользоваться.
Список можно дополнять через API сервиса и через админскую его часть.

## Запуск проекта
1. Создаейте файл `.env` по примеру `env.example`.
2. Запустите билд и запуск контейнеров.
```bash
docker compose up -d
```
3. Проведите миграции.
```bash
docker compose exec web python manage.py migrate
```
4. Скопируйте статику.
```bash
docker compose exec web cp -r /app/staticfiles/. /static/
```
5. Создайте суперпользователя, если нужно.
```bash
docker compose exec web python manage.py createsuperuser
```

## Покрытие тестами

Результаты покрытия тестами для проекта:

| Файл                                      | Строки | Пропущено | Покрытие |
|-------------------------------------------|--------|-----------|----------|
| `src/apps/imei/api/serializers.py`        | 10     | 0         | 100%     |
| `src/apps/imei/api/viewsets.py`           | 11     | 0         | 100%     |
| `src/apps/imei/apps.py`                   | 5      | 0         | 100%     |
| `src/apps/imei/schemas.py`                | 10     | 0         | 100%     |
| `src/apps/imei/services/imei_checker.py`  | 24     | 0         | 100%     |
| `src/apps/imei/urls.py`                   | 4      | 0         | 100%     |
| `src/apps/telegram/admin.py`              | 9      | 0         | 100%     |
| `src/apps/telegram/api/serializers.py`    | 7      | 0         | 100%     |
| `src/apps/telegram/api/viewsets.py`       | 23     | 0         | 100%     |
| `src/apps/telegram/apps.py`               | 5      | 0         | 100%     |
| `src/apps/telegram/models.py`             | 12     | 1         | 92%      |
| `src/apps/telegram/schemas.py`            | 14     | 0         | 100%     |
| `src/apps/telegram/urls.py`               | 7      | 0         | 100%     |
| `src/conftest.py`                         | 40     | 0         | 100%     |
| `src/core/models.py`                      | 6      | 0         | 100%     |
| `src/core/schemas.py`                     | 7      | 0         | 100%     |
| `src/core/services.py`                    | 16     | 2         | 88%      |
| `src/core/settings.py`                    | 47     | 3         | 94%      |
| `src/core/urls.py`                        | 9      | 0         | 100%     |
| **Итого**                                 | **266**| **6**     | **98%**  |
