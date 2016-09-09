import glob
import PIL
from PIL import Image

imgpaths = glob.glob('img/*.jpg')
imgpaths

for imgpath in imgpaths:
    imgpath_new = imgpath.replace('img', 'img_resize')
    basewidth = 900
    img = Image.open(imgpath)
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
    img.save(imgpath_new)
