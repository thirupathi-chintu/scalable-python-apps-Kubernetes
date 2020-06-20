FROM python:3.6
LABEL maintainer="Thirupathi Peraboina, thirupathiperaboina@gmail.com"
RUN apt-get update
RUN mkdir /app
WORKDIR /app
COPY app /app
#RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]
