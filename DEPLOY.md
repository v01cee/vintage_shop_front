# 🚀 Инструкция по деплою для демонстрации заказчику

## Вариант 1: Vercel (Фронтенд) + Render (Бэкенд) - Рекомендуется

Самый простой и быстрый способ показать проект заказчику.

### Шаг 1: Деплой фронтенда на Vercel

1. **Установите Vercel CLI** (опционально, можно через веб-интерфейс):
```bash
npm i -g vercel
```

2. **Создайте файл `vercel.json`** в корне проекта:
```json
{
  "buildCommand": "npm run build",
  "outputDirectory": "dist",
  "devCommand": "npm run dev",
  "installCommand": "npm install",
  "framework": "vite",
  "rewrites": [
    {
      "source": "/api/(.*)",
      "destination": "https://your-backend-url.onrender.com/api/$1"
    },
    {
      "source": "/(.*)",
      "destination": "/index.html"
    }
  ]
}
```

3. **Деплой через веб-интерфейс**:
   - Зайдите на https://vercel.com
   - Войдите через GitHub/GitLab/Bitbucket
   - Нажмите "New Project"
   - Подключите ваш репозиторий
   - Настройки:
     - Framework Preset: Vite
     - Root Directory: ./
     - Build Command: `npm run build`
     - Output Directory: `dist`
   - Нажмите "Deploy"

4. **Настройте переменные окружения** в Vercel:
   - Settings → Environment Variables
   - Добавьте: `VITE_API_URL=https://your-backend-url.onrender.com/api/v1`

### Шаг 2: Деплой бэкенда на Render

1. **Создайте файл `render.yaml`** в папке `backend/`:
```yaml
services:
  - type: web
    name: vintage-shop-backend
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: uvicorn main:app --host 0.0.0.0 --port $PORT
    envVars:
      - key: PYTHON_VERSION
        value: 3.11.0
      - key: CORS_ORIGINS
        value: https://your-frontend-url.vercel.app
```

2. **Деплой через веб-интерфейс**:
   - Зайдите на https://render.com
   - Войдите через GitHub
   - Нажмите "New +" → "Web Service"
   - Подключите ваш репозиторий
   - Настройки:
     - Name: `vintage-shop-backend`
     - Environment: `Python 3`
     - Build Command: `pip install -r requirements.txt`
     - Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
     - Root Directory: `backend`
   - Добавьте Environment Variable:
     - Key: `CORS_ORIGINS`
     - Value: `https://your-frontend-url.vercel.app` (обновите после деплоя фронтенда)
   - Нажмите "Create Web Service"

3. **Обновите CORS в бэкенде** после получения URL:
   - Settings → Environment Variables
   - Обновите `CORS_ORIGINS` с URL вашего фронтенда

### Шаг 3: Обновите API URL во фронтенде

После получения URL бэкенда:
1. В Vercel: Settings → Environment Variables
2. Обновите `VITE_API_URL` на URL вашего бэкенда Render
3. Пересоберите проект (Redeploy)

---

## Вариант 2: Railway (Всё вместе) - Проще всего

Railway позволяет задеплоить и фронтенд, и бэкенд в одном месте.

### Шаг 1: Подготовка

1. **Создайте `railway.json`** в корне проекта:
```json
{
  "$schema": "https://railway.app/railway.schema.json",
  "build": {
    "builder": "NIXPACKS"
  },
  "deploy": {
    "startCommand": "npm run preview",
    "restartPolicyType": "ON_FAILURE",
    "restartPolicyMaxRetries": 10
  }
}
```

2. **Создайте `railway-backend.json`** в папке `backend/`:
```json
{
  "$schema": "https://railway.app/railway.schema.json",
  "build": {
    "builder": "NIXPACKS"
  },
  "deploy": {
    "startCommand": "uvicorn main:app --host 0.0.0.0 --port $PORT",
    "restartPolicyType": "ON_FAILURE",
    "restartPolicyMaxRetries": 10
  }
}
```

### Шаг 2: Деплой

1. Зайдите на https://railway.app
2. Войдите через GitHub
3. Нажмите "New Project" → "Deploy from GitHub repo"
4. Выберите ваш репозиторий
5. Railway автоматически определит два сервиса (фронтенд и бэкенд)
6. Для каждого сервиса:
   - **Фронтенд**: Root Directory = `.`, Build Command = `npm run build`, Start Command = `npm run preview`
   - **Бэкенд**: Root Directory = `backend`, Start Command = `uvicorn main:app --host 0.0.0.0 --port $PORT`
7. Настройте переменные окружения для бэкенда:
   - `CORS_ORIGINS` = URL фронтенда (Railway автоматически создаст URL)

---

## Вариант 3: Netlify (Фронтенд) + Fly.io (Бэкенд)

### Фронтенд на Netlify

1. **Создайте `netlify.toml`** в корне проекта:
```toml
[build]
  command = "npm run build"
  publish = "dist"

[[redirects]]
  from = "/api/*"
  to = "https://your-backend-url.fly.dev/api/:splat"
  status = 200
  force = true

[[redirects]]
  from = "/*"
  to = "/index.html"
  status = 200
```

2. Деплой через https://app.netlify.com (аналогично Vercel)

### Бэкенд на Fly.io

1. **Установите Fly CLI**:
```bash
# Windows (PowerShell)
iwr https://fly.io/install.ps1 -useb | iex
```

2. **Создайте `fly.toml`** в папке `backend/`:
```toml
app = "vintage-shop-backend"
primary_region = "iad"

[build]

[env]
  PORT = "8080"

[http_service]
  internal_port = 8080
  force_https = true
  auto_stop_machines = true
  auto_start_machines = true
  min_machines_running = 0
  processes = ["app"]

[[http_service.checks]]
  interval = "10s"
  timeout = "2s"
  grace_period = "5s"
  method = "GET"
  path = "/health"
```

3. **Деплой**:
```bash
cd backend
fly launch
fly deploy
```

---

## Вариант 4: Docker на VPS (DigitalOcean, AWS, Hetzner)

Если у вас есть VPS сервер:

1. **Подключитесь к серверу**:
```bash
ssh user@your-server-ip
```

2. **Установите Docker и Docker Compose**:
```bash
# Ubuntu/Debian
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh
sudo apt-get install docker-compose-plugin
```

3. **Клонируйте репозиторий**:
```bash
git clone https://github.com/your-username/vintage-shop-front.git
cd vintage-shop-front
```

4. **Обновите `docker-compose.yml`** для продакшена:
```yaml
# Добавьте в начало файла
version: '3.8'

services:
  frontend:
    # ... существующие настройки
    environment:
      - VITE_API_URL=https://your-domain.com/api/v1
    # Добавьте labels для автоматического получения SSL
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.frontend.rule=Host(`your-domain.com`)"
      - "traefik.http.routers.frontend.entrypoints=websecure"
      - "traefik.http.routers.frontend.tls.certresolver=letsencrypt"
```

5. **Запустите**:
```bash
docker-compose up -d --build
```

6. **Настройте домен**:
   - Укажите A-запись вашего домена на IP сервера
   - Используйте Nginx или Traefik для reverse proxy и SSL

---

## Быстрый вариант для демонстрации (5 минут)

### Используйте ngrok для локального демо

1. **Установите ngrok**: https://ngrok.com/download

2. **Запустите проект локально**:
```bash
docker-compose up
```

3. **Создайте туннель**:
```bash
# Для фронтенда
ngrok http 3000

# В другом терминале для бэкенда
ngrok http 8000
```

4. **Обновите CORS в бэкенде** с URL от ngrok

5. **Отправьте заказчику URL** от ngrok (например: `https://abc123.ngrok.io`)

⚠️ **Внимание**: ngrok бесплатный план имеет ограничения, но подходит для краткосрочной демонстрации.

---

## Рекомендации

1. **Для быстрой демонстрации**: Railway или ngrok
2. **Для постоянного деплоя**: Vercel + Render
3. **Для полного контроля**: VPS с Docker

## Полезные ссылки

- [Vercel](https://vercel.com)
- [Render](https://render.com)
- [Railway](https://railway.app)
- [Netlify](https://netlify.com)
- [Fly.io](https://fly.io)
- [ngrok](https://ngrok.com)

