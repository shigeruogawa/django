FROM python:3.10

WORKDIR /var/www/app

COPY requirements.txt .

VOLUME /var/www/app

RUN pip install --no-cache-dir -r requirements.txt
# pj作成
# RUN django-admin startproject mypj .
# アプリ作成
# RUN python manage.py startapp snippets

# COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
