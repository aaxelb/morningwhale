
## BEGIN py_app: our basic python app with (dev-)requirements.txt
FROM python:3.10-alpine as py_app

RUN apk add --no-cache git

COPY requirements.txt /code/requirements.txt
RUN pip install -U pip
RUN pip install -Ur /code/requirements.txt

# everything in . is copied -- use .dockerignore to keep garbage out
RUN mkdir -p /code
COPY . /code
WORKDIR /code

## END py_app


## BEGIN internet_api
FROM py_app AS internet_api

CMD ["python", "manage.py", "run_internet_api"]
## END internet_api


## BEGIN anoana: anonymized analytics
FROM py_app as anoana

CMD ["python", "manage.py", "run_anoana"]
## END anoana
