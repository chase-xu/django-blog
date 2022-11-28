FROM python:3.9

ARG PORT=8080
ARG SECRET_KEY
ARG DEBUG=False

ENV SECRET_KEY=${SECRET_KEY}
ENV PORT=${PORT}
ENV DEBUG=${DEBUG}

WORKDIR /home/app
RUN pip install --upgrade pip
RUN pip install requirements.txt
COPY . /home/app

EXPOSE $PORT
CMD python /blog_posts/manage.py runserver

