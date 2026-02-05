FROM python:3.12-slim

RUN python -m venv /venv  
ENV PATH="/venv/bin:$PATH"  

RUN pip install "django<6" 

COPY src /src

WORKDIR /src

# หาบรรทัดสุดท้ายที่เขียนว่า CMD ... แล้วแก้เป็น:
CMD sh -c "python manage.py migrate && python manage.py runserver 0.0.0.0:8888"