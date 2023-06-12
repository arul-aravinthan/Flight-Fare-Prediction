FROM python:3.10

COPY requirements.txt /
COPY app.py .
COPY model.pkl .
COPY ct.pkl .
COPY column_order.pkl .

RUN pip install -r requirements.txt

#Run the Application

EXPOSE 8000
ENTRYPOINT ["gunicorn", "-b", "0.0.0.0:8000", "--access-logfile", "-", "--error-logfile", "-", "--timeout", "120"]
CMD ["app:app"]