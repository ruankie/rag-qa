# Use an official Python runtime as a parent image
FROM python:3.11

WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
