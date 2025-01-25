FROM python:3.12

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir

COPY /src .

RUN python manage.py collectstatic --noinput
