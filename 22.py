# borrowed frpm http://blog.idhyt.com/2015/08/13/python-challenge-21-27


import requests
from PIL import Image, ImageDraw, ImageSequence

URL="http://butter:fly@www.pythonchallenge.com/pc/hex/white.gif"
proxy = {
    'http': 'child-prc.intel.com:913',
    'https': 'child-prc.intel.com:913',
}

r = requests.get(URL, proxies=proxy)
r.raise_for_status()
with open("22.gif", "wb") as handle:
    handle.write(r.content)


def copper():
    org_img = Image.open("22.gif")
    new_img = Image.new('RGB', org_img.size, "black")
    new_img_draw = ImageDraw.Draw(new_img)
    x = 0
    y = 0
    # iter over frames
    for s in ImageSequence.Iterator(org_img):
        left, upper, right, lower = org_img.getbbox()
        dx = left - 100
        dy = upper - 100
        x += dx
        y += dy
        if dx == dy == 0:
            x += 20
            y += 30
        new_img_draw.point((x, y))

    new_img.save("22-1.png")

copper()
