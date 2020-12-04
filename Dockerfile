FROM python:3

WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY src/ .
COPY .env .

# -u for unbuffered to see print in logs
CMD ["python", "-u", "./bot.py"]
