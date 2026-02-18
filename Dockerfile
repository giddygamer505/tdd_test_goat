FROM python:3.12-slim 

RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

RUN python -m venv /venv  
ENV PATH="/venv/bin:$PATH"  

RUN pip install --upgrade pip
RUN pip install "django<6" mysqlclient

COPY src /src
WORKDIR /src

CMD sh -c "sleep 10 && python manage.py migrate && python manage.py runserver 0.0.0.0:8888"