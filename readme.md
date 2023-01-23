### Build a URL Shortener With FastAPI and Redis
######  to use UI use ***/index link

###### project contains contains get_ip

##### start redis in docker :
```shell
    docker run --name my-redis -p 6379x:6379 -d redis
```
start app:
```shell 
$ uvicorn app_short_redis.main:app --reload
```

start redis cli:
```shell 
$ redis-cli -p 6379 -h localhost
> select 1 - 15  # change DB
```

to develop use .env settings

conect to redis
```shell
$ redis-cli -p 6379 -h 78.27.202.55 -a password
```


$ docker build -f ./app/Dockerfile -t fastapi_url_image:latest ./app

$ sudo docker run --name fastapi_urls_cut_redis -p 8005:8000 -d  fastapi_url_image

remove container/image: 
```shell
$ sudo docker container rm fastapi_urls_cut_redis
$ sudo docker image rm fastapi_urls_cut_redis
```


https://www.digitalocean.com/community/tutorials/how-to-install-and-secure-redis-on-ubuntu-22-04

https://www.digitalocean.com/community/tutorials/how-to-use-cron-to-automate-tasks-ubuntu-1804