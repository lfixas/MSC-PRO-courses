FROM python:3.12.2

EXPOSE 80

WORKDIR /src

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["flask", "run", "--host=0.0.0.0", "--port=80"]
