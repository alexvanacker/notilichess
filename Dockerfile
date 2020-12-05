FROM python:3.8 AS builder

RUN python -m venv /opt/venv
ENV PATH=/opt/venv/bin:$PATH

RUN pip install --upgrade pip

COPY requirements.txt .
RUN pip install -r requirements.txt

FROM python:3.8.6-slim-buster
WORKDIR /code

COPY --from=builder /opt/venv /opt/venv
COPY src/ .
COPY .env .

ENV PATH=/opt/venv/bin:$PATH

# -u for unbuffered to see print in logs
CMD ["python", "-u", "bot.py"]
