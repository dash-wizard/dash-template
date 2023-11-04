
FROM python:3.11

COPY . /docker_app

WORKDIR /docker_app

RUN  pip install --upgrade pip

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

EXPOSE 8090

CMD ["python",  "app/src/main.py"]



