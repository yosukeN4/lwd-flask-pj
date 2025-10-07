FROM public.ecr.aws/docker/library/python:3.12-slim

# AWS Lambda Web Adapterをコピー
COPY --from=public.ecr.aws/awsguru/aws-lambda-adapter:0.9.1 /lambda-adapter /opt/extensions/lambda-adapter

WORKDIR /var/task

# 依存関係ファイルをコピーしてインストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションコードをコピー
COPY app.py .
COPY templates/ templates/
COPY static/ static/

# コンテナがポート8080でリッスンするように設定
EXPOSE 8080

# gunicornを使用してFlaskアプリケーションを実行
CMD ["gunicorn", "-b=:8080", "-w=1", "app:app"]
