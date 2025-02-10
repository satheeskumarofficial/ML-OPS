FROM python:3.11-slim-buster

WORKDIR /docker

COPY requirements.txt ./

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . .

#COPY ./artefacts/classifier.pkl
#ENV FLASK_APP=loan_tap

#CMD ["flask", "run","--host=0.0.0.0","--port=5000"]

CMD ["python3", "-m", "flask", "--app", "loan_tap", "run", "--host=0.0.0.0" ]
