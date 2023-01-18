from fastapi import APIRouter, responses, Request, Form
from fastapi.templating import Jinja2Templates

from app_short_redis.routers import create_url

router_template = APIRouter()
templates = Jinja2Templates(directory='templates')


@router_template.post('/create_url_template')
def url_short_create(url_name: str = Form(...)):
    print(url_name)
    import requests
    resp_post = requests.post(
        json={"target_url": url_name},
        timeout=5,
        headers={'accept': 'application/json'},
        url='http://78.27.202.55:8004/url'
    )
    return resp_post.json()


@router_template.get('/index', response_class=responses.HTMLResponse)
def main(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})

# @router.get('/index')
# def create_url_form(url: str = Form(...)):  # 'http://www.sexy.url.com.ua'
#     # import requests
#     # resp_post = requests.post(json=data, timeout=5,
#     #                           headers=headers,
#                               # url='http://78.27.202.55:8004/url')
#     create_url(BaseUrl(target_url=url))
#     return {'ok': 1}
