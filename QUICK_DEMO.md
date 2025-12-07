# ⚡ Быстрая демонстрация заказчику (5 минут)

## Вариант 1: ngrok (Самый быстрый - прямо сейчас!)

### Шаг 1: Установите ngrok

1. Скачайте с https://ngrok.com/download
2. Распакуйте и добавьте в PATH (или используйте полный путь)

### Шаг 2: Запустите проект

```bash
# В первом терминале - запустите проект
docker-compose up
```

Дождитесь, пока оба сервиса запустятся (фронтенд на :3000, бэкенд на :8000)

### Шаг 3: Создайте туннели

**Терминал 2 - для фронтенда:**
```bash
ngrok http 3000
```

**Терминал 3 - для бэкенда:**
```bash
ngrok http 8000
```

### Шаг 4: Обновите CORS в бэкенде

1. Скопируйте URL от ngrok для фронтенда (например: `https://abc123.ngrok.io`)
2. Откройте `backend/main.py`
3. Временно добавьте этот URL в `cors_origins`:
```python
cors_origins = os.getenv("CORS_ORIGINS", "http://localhost:3000,http://localhost:3001,http://localhost:5173,https://abc123.ngrok.io").split(",")
```
4. Перезапустите бэкенд в docker-compose

### Шаг 5: Обновите API URL во фронтенде

1. Скопируйте URL от ngrok для бэкенда (например: `https://xyz789.ngrok.io`)
2. Создайте файл `.env` в корне проекта:
```env
VITE_API_URL=https://xyz789.ngrok.io/api/v1
```
3. Пересоберите фронтенд:
```bash
docker-compose restart frontend
```

### Шаг 6: Отправьте заказчику URL

Отправьте заказчику URL от ngrok для фронтенда (например: `https://abc123.ngrok.io`)

⚠️ **Важно**: 
- ngrok бесплатный план дает случайный URL при каждом запуске
- Для постоянного URL нужен платный план или используйте варианты ниже

---

## Вариант 2: Railway (Постоянный URL, 10 минут)

### Шаг 1: Подготовка

1. Зайдите на https://railway.app
2. Войдите через GitHub
3. Нажмите "New Project" → "Deploy from GitHub repo"
4. Выберите ваш репозиторий

### Шаг 2: Настройка сервисов

Railway автоматически определит два сервиса. Для каждого:

**Фронтенд:**
- Root Directory: `.` (корень проекта)
- Build Command: `npm run build`
- Start Command: `npm run preview` (или создайте скрипт для preview)

**Бэкенд:**
- Root Directory: `backend`
- Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`

### Шаг 3: Переменные окружения

Для бэкенда добавьте:
- `CORS_ORIGINS` = URL фронтенда (Railway покажет его после деплоя)

Для фронтенда добавьте:
- `VITE_API_URL` = URL бэкенда + `/api/v1`

### Шаг 4: Получите URL

После деплоя Railway даст вам постоянные URL для обоих сервисов.

---

## Вариант 3: Vercel + Render (Рекомендуется для продакшена)

### Фронтенд на Vercel (5 минут)

1. Зайдите на https://vercel.com
2. Войдите через GitHub
3. "New Project" → выберите репозиторий
4. Настройки:
   - Framework: Vite
   - Build Command: `npm run build`
   - Output Directory: `dist`
5. Environment Variables:
   - `VITE_API_URL` = (заполните после деплоя бэкенда)
6. Deploy!

### Бэкенд на Render (5 минут)

1. Зайдите на https://render.com
2. Войдите через GitHub
3. "New +" → "Web Service"
4. Выберите репозиторий
5. Настройки:
   - Name: `vintage-shop-backend`
   - Environment: `Python 3`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
   - Root Directory: `backend`
6. Environment Variables:
   - `CORS_ORIGINS` = URL вашего фронтенда на Vercel
7. Create!

### Обновите URL

После деплоя бэкенда:
1. Скопируйте URL бэкенда (например: `https://vintage-shop-backend.onrender.com`)
2. В Vercel обновите `VITE_API_URL` = `https://vintage-shop-backend.onrender.com/api/v1`
3. Пересоберите проект (Redeploy)

---

## Какой вариант выбрать?

- **Прямо сейчас (5 мин)**: ngrok
- **Постоянный URL (10 мин)**: Railway
- **Для продакшена**: Vercel + Render

## Полезные команды

### Проверка работы локально перед деплоем

```bash
# Запуск
docker-compose up

# Проверка фронтенда
curl http://localhost:3000

# Проверка бэкенда
curl http://localhost:8000/health
curl http://localhost:8000/api/v1/products
```

### Логи для отладки

```bash
# Логи всех сервисов
docker-compose logs -f

# Логи только бэкенда
docker-compose logs -f backend
```

