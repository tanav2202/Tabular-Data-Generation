FROM debian:latest
RUN apt-get update && apt-get install -y pip python3
WORKDIR /app
COPY requirements.txt  requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD ["python3", "app.py"]
