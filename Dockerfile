# ===== Python base image =====
FROM python:3.12-slim

# ===== env settings =====
ENV PYTHONUNBUFFERED=1

# ===== workdir =====
WORKDIR /app

# ===== system deps =====
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# ===== install dependencies =====
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# ===== copy project =====
COPY . /app/

# ===== collect static at build =====
RUN python manage.py collectstatic --noinput

# ===== open port =====
EXPOSE 8000

# ===== run migrations + server =====
CMD sh -c "python manage.py migrate && gunicorn glamping_project.wsgi:application --bind 0.0.0.0:8000 --workers 3"