import time

from fastapi import FastAPI, Request

from app_short_redis.routers import router
from app_short_redis.router_html import router_template

app = FastAPI(
    title='Url Short Maker',
    description="create link with length 5 chars",
    version='0.9.99',
    contact={'name': 'Vitalii Kostyreva', 'tel': '0737776107'}
)


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


app.include_router(router, tags=["Url API core"])
app.include_router(router_template, tags=['html_template'])  # another router, for tml templates
