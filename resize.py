from os import listdir
from os.path import isfile, join
from PIL import Image

mypath = "./img/cropped"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

for file in onlyfiles:
    print("Processing file: " + file)
    basewidth = 125
    img = Image.open('./img/cropped/' + file)
    wpercent = (basewidth/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((basewidth,hsize), Image.ANTIALIAS)
    img.save('./img/resized/' + file)
