# 🖥️ Простой деплой на один сервер (как Django)

Если вы привыкли к Django, где всё работает на одном сервере, вот аналогичные варианты для Vue.js + FastAPI.

## Вариант 1: Один сервер с Nginx (Как Django на VPS)

Это самый похожий на Django вариант - всё на одном сервере.

### Шаг 1: Подготовка сервера

```bash
# Подключитесь к серверу
ssh user@your-server-ip

# Обновите систему
sudo apt update && sudo apt upgrade -y

# Установите необходимые пакеты
sudo apt install -y nginx python3-pip nodejs npm docker.io docker-compose
```

### Шаг 2: Клонируйте проект

```bash
cd /var/www
sudo git clone https://github.com/your-username/vintage-shop-front.git
cd vintage-shop-front
```

### Шаг 3: Настройте Nginx как reverse proxy

Создайте файл `/etc/nginx/sites-available/vintage-shop`:

```nginx
server {
    listen 80;
    server_name your-domain.com www.your-domain.com;

    # Фронтенд (статичные файлы)
    location / {
        root /var/www/vintage-shop-front/dist;
        try_files $uri $uri/ /index.html;
        index index.html;
    }

    # Бэкенд API
    location /api/ {
        proxy_pass http://localhost:8000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_cache_bypass $http_upgrade;
    }

    # Статические файлы
    location ~* \.(js|css|png|jpg|jpeg|gif|ico|svg|woff|woff2|ttf|eot)$ {
        root /var/www/vintage-shop-front/dist;
        expires 1y;
        add_header Cache-Control "public, immutable";
    }
}
```

### Шаг 4: Активируйте конфигурацию

```bash
sudo ln -s /etc/nginx/sites-available/vintage-shop /etc/nginx/sites-enabled/
sudo nginx -t  # Проверка конфигурации
sudo systemctl reload nginx
```

### Шаг 5: Запустите бэкенд

**Вариант A: Через systemd (как Django с gunicorn)**

Создайте `/etc/systemd/system/vintage-shop-backend.service`:

```ini
[Unit]
Description=Vintage Shop Backend
After=network.target

[Service]
User=www-data
Group=www-data
WorkingDirectory=/var/www/vintage-shop-front/backend
Environment="PATH=/var/www/vintage-shop-front/backend/venv/bin"
ExecStart=/var/www/vintage-shop-front/backend/venv/bin/uvicorn main:app --host 127.0.0.1 --port 8000
Restart=always

[Install]
WantedBy=multi-user.target
```

Запустите:
```bash
sudo systemctl daemon-reload
sudo systemctl enable vintage-shop-backend
sudo systemctl start vintage-shop-backend
```

**Вариант B: Через Docker Compose (проще)**

```bash
cd /var/www/vintage-shop-front
docker-compose up -d
```

### Шаг 6: Соберите фронтенд

```bash
cd /var/www/vintage-shop-front
npm install
npm run build
```

### Шаг 7: Настройте SSL (Let's Encrypt)

```bash
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d your-domain.com -d www.your-domain.com
```

Готово! Ваш сайт доступен по `https://your-domain.com`

---

## Вариант 2: PythonAnywhere (Бесплатный хостинг для Python)

PythonAnywhere поддерживает и Python (бэкенд), и статические сайты (фронтенд).

### Шаг 1: Зарегистрируйтесь

1. Зайдите на https://www.pythonanywhere.com
2. Создайте бесплатный аккаунт

### Шаг 2: Загрузите бэкенд

1. В Dashboard → Files
2. Загрузите файлы бэкенда в папку `/home/yourusername/mysite/backend/`
3. В Dashboard → Web → Add a new web app
4. Выберите "Manual configuration" → Python 3.10
5. В "WSGI configuration file" добавьте:

```python
import sys
path = '/home/yourusername/mysite/backend'
if path not in sys.path:
    sys.path.append(path)

from main import app
application = app
```

### Шаг 3: Загрузите фронтенд

1. Соберите фронтенд локально: `npm run build`
2. Загрузите папку `dist` в `/home/yourusername/mysite/static/`
3. В Web → Static files:
   - URL: `/`
   - Directory: `/home/yourusername/mysite/static/dist`

### Шаг 4: Настройте маршруты

В Web → URL configuration добавьте:
- `/api/` → ваш бэкенд
- `/` → статические файлы

---

## Вариант 3: Heroku (Классический вариант)

Heroku работает похоже на Django деплой - один сервис, простая настройка.

### Шаг 1: Установите Heroku CLI

```bash
# Windows
# Скачайте с https://devcenter.heroku.com/articles/heroku-cli
```

### Шаг 2: Подготовьте файлы

**Для бэкенда** создайте `backend/Procfile`:
```
web: uvicorn main:app --host 0.0.0.0 --port $PORT
```

**Для фронтенда** создайте `Procfile`:
```
web: npm run preview
```

И `package.json` добавьте:
```json
{
  "scripts": {
    "preview": "vite preview --host 0.0.0.0 --port $PORT"
  }
}
```

### Шаг 3: Деплой

```bash
# Бэкенд
cd backend
heroku create vintage-shop-backend
git push heroku main

# Фронтенд
cd ..
heroku create vintage-shop-frontend
git push heroku main
```

---

## Вариант 4: Cloudflare Pages + Workers (Бесплатно)

Cloudflare позволяет хостить фронтенд и бэкенд через Workers.

### Фронтенд на Pages

1. Зайдите на https://pages.cloudflare.com
2. Подключите GitHub репозиторий
3. Настройки:
   - Build command: `npm run build`
   - Build output directory: `dist`

### Бэкенд на Workers

1. Зайдите на https://workers.cloudflare.com
2. Создайте новый Worker
3. Используйте готовый шаблон для FastAPI или настройте вручную

---

## Вариант 5: GitHub Pages (Только фронтенд) + Backend отдельно

### Фронтенд на GitHub Pages

1. В настройках репозитория → Pages
2. Source: Deploy from a branch
3. Branch: `gh-pages`
4. Создайте скрипт деплоя:

**`.github/workflows/deploy.yml`**:
```yaml
name: Deploy to GitHub Pages

on:
  push:
    branches: [ main ]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-node@v3
        with:
          node-version: '20'
      - run: npm install
      - run: npm run build
      - uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./dist
```

### Бэкенд отдельно

Используйте любой из вариантов выше (Render, Railway, PythonAnywhere)

---

## Сравнение с Django

| Django | Vue.js + FastAPI |
|--------|------------------|
| `python manage.py runserver` | `npm run dev` (фронт) + `uvicorn main:app` (бэк) |
| `gunicorn` для продакшена | `nginx` + `uvicorn` или Docker |
| Статика через `collectstatic` | Статика через `npm run build` |
| Один процесс | Два процесса (или Docker Compose) |
| `/admin` панель | Нет встроенной админки (нужно делать отдельно) |

## Рекомендация

**Для похожего на Django опыта**:
1. **Локально**: Docker Compose (всё в одном месте)
2. **На сервере**: Nginx + systemd (как Django с gunicorn)
3. **Быстрый деплой**: Railway (всё автоматически)

## Полезные команды для управления

```bash
# Проверка статуса бэкенда (systemd)
sudo systemctl status vintage-shop-backend
sudo systemctl restart vintage-shop-backend
sudo systemctl logs vintage-shop-backend

# Проверка Nginx
sudo nginx -t
sudo systemctl status nginx
sudo systemctl reload nginx

# Просмотр логов
sudo tail -f /var/log/nginx/error.log
sudo journalctl -u vintage-shop-backend -f
```

