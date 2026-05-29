FROM python:3.11-slim

# System dependencies (required for WeasyPrint + mysqlclient)
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpango-1.0-0 \
    libpangoft2-1.0-0 \
    libgdk-pixbuf-xlib-2.0-0 \
    libcairo2 \
    libffi-dev \
    libssl-dev \
    pkg-config \
    default-libmysqlclient-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
# v2 - force cache bust after adding whitenoise
RUN pip install --no-cache-dir -r requirements.txt gunicorn

# v9 - collectstatic at runtime so volume mounts don't hide static files
COPY . .

EXPOSE 8000

CMD ["sh", "-c", "python manage.py collectstatic --noinput; python manage.py migrate --noinput; python manage.py seed_data; gunicorn mysite.wsgi:application --bind 0.0.0.0:8000 --workers 2"]
