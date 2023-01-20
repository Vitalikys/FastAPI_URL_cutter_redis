from fastapi import FastAPI

from app_short_redis.routers import router
from app_short_redis.router_html import router_template

app = FastAPI(
    title='Url Short Maker',
    description="create link with length 5 chars",
    version='0.9.99',
    contact={'name': 'Vitalii Kostyreva', 'tel': '0737776107'}
)

app.include_router(router, tags=["Url API core"])
app.include_router(router_template, tags=['html_template'])  # another router, for tml templates
