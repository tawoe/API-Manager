FROM ubi9/python-39
USER root
RUN dnf update -y
RUN dnf  install python3-psycopg2 -y
ADD . /app
COPY ./.github/local_settings_container.py /app/apimanager/apimanager/local_settings.py
RUN pip install -r /app/requirements.txt
USER 501
WORKDIR /app/apimanager
EXPOSE 8000
CMD ["gunicorn", "--bind", ":8000", "--config", "../gunicorn.conf.py", "--workers", "3", "apimanager.wsgi"]