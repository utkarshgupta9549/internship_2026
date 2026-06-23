FROM python:3.11-slim

# Install Java
RUN apt-get update && \
    apt-get install -y default-jdk && \
    apt-get clean

ENV JAVA_HOME=/usr/lib/jvm/default-java

# Install PySpark
RUN pip install pyspark

WORKDIR /app

COPY . .

CMD ["python", "app.py"]