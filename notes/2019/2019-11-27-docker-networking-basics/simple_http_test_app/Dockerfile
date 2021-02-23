FROM python:3

RUN pip3 install --upgrade pip

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY app.py .

EXPOSE 8080

CMD ["python", "app.py"]
