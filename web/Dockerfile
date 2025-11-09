FROM python:3.10-slim

WORKDIR /app

# requirements.txt に Flask と uWSGI を記載しておく
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# uWSGI で UNIX ソケット経由で起動
CMD ["uwsgi", "--socket", "/tmp/uwsgi.sock", "--module", "app:app", "--chmod-socket=666", "--master", "--processes", "4", "--threads", "2"]

