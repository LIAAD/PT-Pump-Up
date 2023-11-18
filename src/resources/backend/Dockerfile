FROM python:3.8

SHELL ["/bin/bash", "-c"]

RUN pip install virtualenv

WORKDIR /envs

RUN python -m venv quart

RUN source ./quart/bin/activate

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt -U

ENTRYPOINT ["python", "app.py"]