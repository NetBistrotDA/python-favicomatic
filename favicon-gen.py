from PIL import Image, ImageOps
import json
from types import SimpleNamespace

infile = "icon.png"

data = '[{"name":"apple-touch-icon-57x57.png","size":[57, 57]},{"name":"apple-touch-icon-60x60.png","size":[60, 60]},{"name":"apple-touch-icon-72x72.png","size":[72, 72]},,{"name":"apple-touch-icon-76x76.png","size":[76, 726]},{"name":"apple-touch-icon-114x114.png","size":[114, 114]},{"name":"apple-touch-icon-120x120.png","size":[120, 120]},{"name":"apple-touch-icon-144x144.png","size":[144, 144]},{"name":"apple-touch-icon-152x152.png","size":[152, 152]},{"name":"favicon.ico","size":[64, 64]},{"name":"favicon-16x16.png","size":[16, 16]},{"name":"favicon-32x32.png","size":[32, 32]},{"name":"favicon-96x96.png","size":[96, 96]},{"name":"favicon-128x128.png","size":[128, 128]},{"name":"favicon-196x196.png","size":[196, 196]},{"name":"mstile-70x70.png","size":[70, 70]},{"name":"mstile-144x144.png","size":[144, 144]},{"name":"mstile-150x150.png","size":[150, 150]},{"name":"mstile-310x150.png","size":[310, 150]},{"name":"mstile-310x310.png","size":[310, 310]}]'

x = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))

im = Image.open(infile)

for y in x:
    # print(y.name.split(".")[1].upper())
    if (y.size[0] != y.size[1]):
        im_adjsted = im.resize((150, 150), Image.ANTIALIAS)
        im_resized = ImageOps.expand(im_resized, (80, 0, 80, 0))
        im_adjsted.save("favicons/"+y.name)
    else:
        im_resized = im.resize(y.size, Image.ANTIALIAS)
    im_resized.save("favicons/"+y.name, y.name.split(".")[1].upper())
