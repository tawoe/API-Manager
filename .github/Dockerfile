FROM python:3.9.13-slim-bullseye
RUN apt update
RUN apt upgrade -y
RUN apt install python3-psycopg2 python3-tk tk -y
ADD . /app
COPY ./.github/local_settings_container.py /app/apimanager/apimanager/local_settings.py
RUN pip install -r /app/requirements.txt
WORKDIR /app/apimanager
EXPOSE 8000
CMD ["gunicorn", "--bind", ":8000", "--config", "../gunicorn.conf.py", "--workers", "3", "apimanager.wsgi"]