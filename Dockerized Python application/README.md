# Dockerized Python Application

## Description

This project demonstrates a simple Dockerized Python application.

The application prints:

- Current Python Version
- Current Date
- Current Time

The project uses the official Python 3.12 Slim Docker image.

---

## Project Structure

```
docker-python-app/
│── app.py
│── Dockerfile
│── requirements.txt
│── README.md
```

---

## Prerequisites

- Docker installed
- Git installed

---

## Build Docker Image

```bash
docker build -t python-version-app .
```

---

## Run Docker Container

```bash
docker run --rm python-version-app
```

---

## Sample Output

```
==================================================
Dockerized Python Application
==================================================
Python Version : 3.12.x (main, ...)
Current Date   : 19-06-2026
Current Time   : 14:55:31
==================================================
```

---

## GitHub Repository

Push all project files to your GitHub repository.

Example:

```
https://github.com/your-username/docker-python-app
```

---

## Author

Utkarsh Gupta