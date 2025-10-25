FROM python:3.11-slim

WORKDIR /root/douzo/web

RUN pip install --no-cache-dir flask uwsgi

COPY . /root/douzo/web

CMD ["uwsgi", "--ini", "app.ini"]
