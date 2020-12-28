FROM python:3.7

ENV PYTHONDONTWRITEBYTECODE=1 \
  PYTHONUNBUFFERED=1

ARG APP_HOME="/opt/app/app"

RUN mkdir -p ${APP_HOME} \
  && pip install --upgrade pip

WORKDIR ${APP_HOME}

COPY requirements/* ${APP_HOME}/requirements/
RUN pip install -r requirements/local.txt
COPY . ${APP_HOME}
