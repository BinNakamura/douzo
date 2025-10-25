FROM python:3.11-slim

WORKDIR /root/douzo/web

# --- uWSGI ビルドに必要なパッケージを追加 ---
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    libpcre3 \
    libpcre3-dev \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

# --- Flask & uWSGI をインストール ---
RUN pip install --no-cache-dir flask uwsgi

COPY . /root/douzo/web

CMD ["uwsgi", "--ini", "app.ini"]
