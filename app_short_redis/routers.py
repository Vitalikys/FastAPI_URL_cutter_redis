from fastapi import APIRouter, Request, HTTPException
from redis import StrictRedis

from app_short_redis.crud import create_random_key
from app_short_redis.schemas import BaseUrl

router = APIRouter()
# redis_client = StrictRedis(host='127.0.0.1', port=63791, db=1) # for local
redis_client = StrictRedis(host='redis', port=6379, db=0)  # for Docker
LOCAL_HOST_URL = 'http://78.27.202.55:8005/'


@router.get('/', name='home page on server starts')
def index():
    return {'API to create short url': 'see: /docs'}


@router.get('/url')
def get_all_urls1():
    try:
        all_urls_response = []
        all_keys = redis_client.keys()
        for key in all_keys:
            one_url_data = {"short_url": key}
            one_url_data.update(redis_client.hgetall(key.decode()))
            all_urls_response.append(one_url_data)
        return all_urls_response
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.post('/url')
def create_url(url: BaseUrl):
    short_url = create_random_key(length=4)

    # checking if url is unique, not in DB
    while redis_client.exists(short_url):
        short_url = create_random_key(length=4)

    redis_client.hset(short_url, 'target_url', url.target_url)
    redis_client.hset(short_url, 'clicks', 0)
    # redis_client.expire(short_url, 2*86400)  # set expire for two days
    return {'target_url': url.target_url,
            'short_url': LOCAL_HOST_URL + short_url,
            'expire at': 'two days'}


@router.get("/{url_keys}/")
def redirect_to_url(url_keys: str, request: Request):
    # db_url_target_url = redis_client.hget(url_keys, "target_url")
    try:
        db_url_target_url = redis_client.hget(name=url_keys, key='target_url')
        db_url_target_url = db_url_target_url.decode()
        if db_url_target_url:
            from starlette.responses import RedirectResponse
            redis_client.hincrby(url_keys, 'clicks', 1)  # add 1 - increment
            return RedirectResponse(db_url_target_url)
    except Exception:
        raise HTTPException(status_code=404, detail=f"URL '{request.url}' doesn't exist")


@router.delete('/url/{url_key}', name='deleting selected url')
def delete_url(url_key: str):
    try:
        redis_client.delete(url_key)
        return {'message': 'url  was deleted'}
    except Exception:
        raise HTTPException(status_code=404, detail=f"URL '{url_key}' doesn't exist")
