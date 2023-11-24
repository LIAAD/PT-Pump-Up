FROM python:3.8

SHELL ["/bin/bash", "-c"]

RUN pip install virtualenv

WORKDIR /envs

RUN python -m venv quart

RUN source ./quart/bin/activate

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt -U

ENV QUART_DEBUG=1

ENTRYPOINT ["quart", "run", "--host", "0.0.0.0", "--port", "5000"]