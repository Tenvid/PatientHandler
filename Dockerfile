FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./src/

EXPOSE 5000

ENV FLASK_APP=src/patient_handler/main.py
ENV FLASK_ENV=production

CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]
