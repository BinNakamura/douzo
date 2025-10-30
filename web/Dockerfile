FROM python:3.11

# 必要なパッケージをインストール
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    gcc \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

# 作業ディレクトリ
WORKDIR /web

# 必要なファイルをコピー
COPY requirements.txt /web/requirements.txt
COPY app.ini /web/app.ini
COPY wsgi.py /web/wsgi.py
COPY apps /web/apps

# Pythonパッケージをインストール
RUN pip install --no-cache-dir -r requirements.txt

# uWSGIを使ってアプリを起動
CMD ["uwsgi", "--ini", "/web/app.ini", "--die-on-term"]
