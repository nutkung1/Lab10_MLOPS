FROM python:3.9-slim

WORKDIR /app

# Copy everything in app folder
COPY app/ /app/

# Install exact dependencies
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 9000

CMD ["python", "app.py"]
