# answer: http://www.pythonchallenge.com/pc/return/romance.html

import requests
import Image, ImageChops


URL="http://huge:file@www.pythonchallenge.com/pc/return/mozart.gif"
proxy = {
    'http': 'child-prc.intel.com:913',
    'https': 'child-prc.intel.com:913',
}

IMG_NAME = r"16.gif"

r = requests.get(URL, proxies=proxy,) #auth=HTTPBasicAuth(USERNAME, PASSWORD))
r.raise_for_status()
with open(IMG_NAME, "wb") as handle:
        handle.write(r.content)

magic = chr(195) # pink color
im = Image.open(IMG_NAME)
width, height = im.size

for y in range(height):
    crop_zone = 0, y, width, y+1
    row = im.crop(crop_zone)
    bs = row.tostring()
    i = bs.index(magic)
    row = ImageChops.offset(row, -i)
    im.paste(row, crop_zone)

im.save('16-gen.gif')
