import requests
from PIL import Image

URL="http://www.pythonchallenge.com/pc/return/cave.jpg"
proxy = {
    'http': 'child-prc.intel.com:913',
    'https': 'child-prc.intel.com:913',
}

r = requests.get(URL, proxies=proxy, stream=True)
with open("11.jpg", "wb") as handle:
    for data in r.iter_content():
        handle.write(data)

im = Image.open("11.jpg")
width, height = im.size
imdata = list(im.getdata())
print imdata
