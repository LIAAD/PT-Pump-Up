FROM python:3.8

SHELL ["/bin/bash", "-c"]

RUN pip install virtualenv

WORKDIR /envs

RUN python -m venv flask

RUN source ./flask/bin/activate

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt -U

ENTRYPOINT [ "flask", "run", "--debug", "--host=0.0.0.0", "--port=5000" ]