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

# v5 - somos hero inline styles + cuidados.jpg image
COPY . .

RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "mysite.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "2"]
