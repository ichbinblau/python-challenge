# answer: http://www.pythonchallenge.com/pc/return/uzi.html

import requests
from PIL import Image

URL="http://huge:file@www.pythonchallenge.com/pc/return/wire.png"
proxy = {
    'http': 'child-prc.intel.com:913',
    'https': 'child-prc.intel.com:913',
}

r = requests.get(URL, proxies=proxy, stream=True)
with open("14.png", "wb") as handle:
    for data in r.iter_content():
        handle.write(data)

im = Image.open("14.png")
width, height = im.size
imdata = list(im.getdata())
print width, height

res = Image.new("RGB", (100, 100))
res_data = res.load()
#print imdata, len(imdata)
    #output.putpixel(get_pixel(i), px)
circle = [(i, i-1, i-1, i-2) for i in range(100, 0, -2)]
print circle
times = reduce(lambda x,y: x+y, circle)

direction = [
    (1, 0), # right
    (0, 1), # down
    (-1, 0), # left
    (0, -1) # up
]

res_pos = (-1, 0)
v = 0 
im_indx = 0

for t in times:
    for step in range(t):
        res_pos = tuple(map(lambda x,y: x+y, res_pos, direction[v]))
        res_data[res_pos] = imdata[im_indx]
        im_indx += 1

    v = (v + 1) % 4

res.save('14-gen.png')


 
