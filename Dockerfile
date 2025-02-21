FROM python:3.11-slim

COPY . /app

WORKDIR /app

COPY scripts/entrypoint.sh /app/entrypoint.sh

RUN chmod +x /app/entrypoint.sh

RUN pip install -r requirements.txt

ENTRYPOINT ["/app/entrypoint.sh"]