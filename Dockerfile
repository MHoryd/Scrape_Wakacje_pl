FROM python:3.9

WORKDIR /app

COPY app /app/app
COPY config.py /app/config.py
COPY requirements.txt /app/requirements.txt
COPY helpers /app/helpers
COPY Reports /app/Reports
COPY scrape_script /app/scrape_script

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]