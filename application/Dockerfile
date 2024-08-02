FROM python:3.12

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY pyproject.toml poetry.lock /usr/src/app/

RUN pip3 install --upgrade pip setuptools wheel poetry==1.8.3 && poetry config virtualenvs.create false && rm -rf /root/.cache/pip

COPY . /usr/src/app/

RUN poetry install

CMD uvicorn main:app --reload --workers 1 --host 0.0.0.0 --port 8000
