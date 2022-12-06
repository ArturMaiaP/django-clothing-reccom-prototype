FROM python:3.9-slim
RUN pip install --upgrade pip
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
COPY ./download.py /app/download.py
RUN python3 download.py
COPY ./api /app/api
CMD [ "python3", "-m" , "flask", "--app", "api", "run", "--host=0.0.0.0"]