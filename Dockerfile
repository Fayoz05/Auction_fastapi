FROM python:latest

ENV PYTHONUNBUFFERED=1

WORKDIR /Auction_project

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--reload", "--host=0.0.0.0", "--port=2525" ]