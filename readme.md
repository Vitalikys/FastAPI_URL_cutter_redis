### Build a URL Shortener With FastAPI and Redis
start redis in docker :
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
$ redis-cli -p 6379 -h 78.27.202.55 -a password


https://www.digitalocean.com/community/tutorials/how-to-install-and-secure-redis-on-ubuntu-22-04