FROM python:3.11-slim
WORKDIR /bot
COPY requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir
COPY . .
CMD ["python3", "-u", "bot.py"]