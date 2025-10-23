FROM python:3.10-slim

# タイムゾーン・ロケール
ENV TZ="Asia/Tokyo" \
    LANG="C.UTF-8" \
    LANGUAGE="ja_JP:ja" \
    LC_ALL="C.UTF-8"

# システムパッケージ
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    python3-pip \
    logrotate \
    && rm -rf /var/lib/apt/lists/*

# アプリディレクトリ作成
RUN mkdir -p /root/douzo/web
WORKDIR /root/douzo/web

# Python モジュールインストール
COPY requirements.txt ./
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# アプリコピー
COPY ./ ./

# 起動コマンド
CMD ["uwsgi", "--ini", "app.ini"]

