FROM python:3.7-slim
ADD . /code
WORKDIR /code


RUN pip install --no-cache-dir -r requirements.txt
ENTRYPOINT ["python", "producer.py"]