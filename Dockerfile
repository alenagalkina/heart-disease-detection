FROM python:3.8-slim-buster

RUN mkdir -p /usr/src/app/
WORKDIR /usr/src/app/
COPY . /usr/src/app/
COPY requirements.txt .
COPY model.pkl .

RUN pip install -r requirements.txt
EXPOSE 80

CMD ["uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "80"]