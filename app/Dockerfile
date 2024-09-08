FROM python:3.10

WORKDIR /var/www/app

COPY requirements.txt .

VOLUME /var/www/app

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install django_bootstrap5
RUN pip install wcwidth
RUN pip install gunicorn
RUN pip install uwsgi

# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
# CMD ["/bin/bash", ,"-C", "tail -f /dev/null"]
# 永続プロセス
ENTRYPOINT ["tail", "-f", "/dev/null"]
