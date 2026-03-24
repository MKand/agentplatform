FROM python:3.11-slim

WORKDIR /app

RUN pip install --no-cache-dir fastmcp

COPY server.py .

ENV PORT=8080

CMD ["python", "server.py"]
