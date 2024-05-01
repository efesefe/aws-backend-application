FROM python:3.10-alpine
COPY requirements.txt .
RUN pip install -r requirements.txt
ADD main.py .
ADD test.py .
CMD ["python", "./main.py"] 
