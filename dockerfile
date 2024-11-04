FROM python:3.10-alpine as builder

RUN apk add --no-cache gcc musl-dev

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.10-alpine

WORKDIR /app

COPY --from=builder /app /app

COPY . .

ENV PYTHONUNBUFFERED=1

CMD ["python", "app.py"]
