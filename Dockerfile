FROM python:3.8

MAINTAINER Wecode Backend Developer Y

ENV PYTHONUNBUFFERED 1

COPY requirements.txt /usr/src/recipe_api/
WORKDIR /usr/src/recipe_api
RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/recipe_api
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
