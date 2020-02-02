from bs4 import BeautifulSoup
from .utils import random_string
from .const import uagent
from httpx.exceptions import InvalidURL
import httpx
import aiofiles


class LightShot:
    @staticmethod
    async def get_image() -> str:
        while True:
            url = "http://prnt.sc/" + random_string(6)
            soup = BeautifulSoup((await httpx.get(url)).text, "html.parser")
            try:
                return soup.img["src"]
            except TypeError:
                continue

    @staticmethod
    async def save(url: str, folder_name: str):
        try:
            data = await httpx.get(url, allow_redirects=True, headers=uagent)
            async with aiofiles.open(
                f"{folder_name}/{url.split('/')[-1]}", mode="wb"
            ) as img:
                await img.write(data.content)
        except InvalidURL:
            return
