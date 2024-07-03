FROM python:latest

COPY . /Auction_project

WORKDIR /Auction_project

RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--reload", "--host=0.0.0.0", "--port=2525" ]