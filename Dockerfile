FROM python:3.11.9

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8050

CMD ["python", "main.py"]
