import os

from os import path

import aiofiles
import aiohttp
from PIL import Image, ImageDraw, ImageFont


def changeImageSize(maxWidth, maxHeight, image):
    widthRatio = maxWidth / image.size[0]
    heightRatio = maxHeight / image.size[1]
    newWidth = int(widthRatio * image.size[0])
    newHeight = int(heightRatio * image.size[1])
    newImage = image.resize((newWidth, newHeight))
    return newImage


async def gen_thumb(thumbnail, title, userid, theme, ctitle):
    async with aiohttp.ClientSession() as session:
        async with session.get(thumbnail) as resp:
            if resp.status == 200:
                f = await aiofiles.open(f"cache/thumb{userid}.jpg", mode="wb")
                await f.write(await resp.read())
                await f.close()
    image1 = Image.open(f"cache/thumb{userid}.jpg")
    image2 = Image.open(f"Utils/trpsnt.png")
    image3 = changeImageSize(1280, 720, image1)
    image4 = changeImageSize(1280, 720, image2)
    image5 = image3.convert("RGBA")
    image6 = image4.convert("RGBA")
    Image.alpha_composite(image5, image6).save(f"cache/temp{userid}.png")
    img = Image.open(f"cache/temp{userid}.png")
    img.save(f"cache/final{userid}.png")
    os.remove(f"cache/temp{userid}.png")
    os.remove(f"cache/thumb{userid}.jpg")
    final = f"cache/final{userid}.png"
    return final
