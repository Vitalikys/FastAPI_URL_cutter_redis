from fastapi import APIRouter, responses, Request, Form
from fastapi.templating import Jinja2Templates

from app_short_redis.routers import create_url, get_all_urls1
from app_short_redis.schemas import BaseUrl

router_template = APIRouter()
templates = Jinja2Templates(directory='templates')


# @router_template.post('/create_url_template')
# def url_short_create(url_name: str = Form(...)):
#     print(url_name)
#     import requests
#     resp_post = requests.post(
#         json={"target_url": url_name},
#         timeout=5,
#         headers={'accept': 'application/json'},
#         url='http://78.27.202.55:8005/url'
#     )
#     return resp_post.json()

@router_template.post('/create_url_template')
def url_short_create(request: Request, url_name: str = Form(...)):
    print('url_name', type(url_name))
    url_base = BaseUrl(target_url=url_name)
    print('url_base', url_base, type(url_base))
    try:
        return create_url(url_base, request=request)
    except Exception as ex:
        print(str(ex))
    return {'short url': 'created'}


@router_template.get('/index', response_class=responses.HTMLResponse)
def main(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})


