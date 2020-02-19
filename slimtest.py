from PIL import Image

print("Alex")
im = Image.open("./skins/alex.png")
im = im.convert("RGBA")
print(im.getpixel((54,20)))
print("Steve")
im2 = Image.open("./skins/steve.png")
im2 = im2.convert("RGBA")
print(im2.getpixel((54,20)))