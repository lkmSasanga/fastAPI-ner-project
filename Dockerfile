FROM python:3.9

WORKDIR /

COPY requirements.txt /requirements.txt

RUN pip install -r requirements.txt

RUN pip install -U pip setuptools wheel

#RUN pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-2.2.5/en_core_web_sm-2.2.5.tar.gz --user

CMD "python -m spacy download en_core_web_sm"

COPY main.py /

COPY ner_of_data.py /

EXPOSE 80

CMD [ "uvicorn", "main:app", "--reload" ]