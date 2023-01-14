from pydantic import BaseModel, HttpUrl, Field


class BaseUrl(BaseModel):
    target_url: HttpUrl = Field(default='http://www.my-custom.url.com.ua')


