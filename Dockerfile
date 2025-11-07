FROM python:3.12-slim
RUN apt-get update && apt-get install -y curl
WORKDIR /app
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]