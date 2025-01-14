FROM python:latest
WORKDIR /app
COPY . /app
RUN pip install fastapi uvicorn psycopg2-binary redis  influxdb-client cryptography
ENV PYTHONPATH=/app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
