FROM python:3.9-slim

WORKDIR /code

COPY . /code

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .

RUN pip install -r requirements.txt
CMD ["uvicorn", "app_short_redis.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
# in bash:
# $ docker build -t fastapi_url_cutter .    # create image
# $ docker run -d --name mycontainer -p 8005:8000 fastapi_url_cutter
# 8000 - only inside container
# 8005 - we open in browser