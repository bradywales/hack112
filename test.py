import urllib.request
from PIL import Image

urllib.request.urlretrieve(
  'https://instagram.fagc2-1.fna.fbcdn.net/v/t51.2885-15/e35/253996037_221135660122667_1875755979765985989_n.jpg?_nc_ht=instagram.fagc2-1.fna.fbcdn.net&_nc_cat=1&_nc_ohc=1qSIluxECLoAX_50LMI&tn=A908QXKk3RCPfIQE&edm=AIQHJ4wBAAAA&ccb=7-4&oh=0e23ff82b837c29d38bb21b4c59ddf32&oe=618F5143&_nc_sid=7b02f1&ig_cache_key=MjcwMTMzNjY4NDQ0NzgxNTU0NQ%3D%3D.2-ccb7-4',"./images/gfg.png")

image = Image.open(r"../hack112/images/gfg.png")
newSize = (100,100)
im2 = image.resize(newSize)
im2.save("../hack112/images/gfg.png")
im2.show()