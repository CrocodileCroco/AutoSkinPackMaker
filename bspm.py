from PIL import Image
import glob
import uuid
import json
import traceback

pnglist = glob.glob('./skins/*.png')

print(pnglist)

inumber = 0

skinsjson = {"geometry": "skinpacks/skins.json","skins":[],"serialize_name": "EditMe", "localization_name": "EditMe"}



for i in pnglist:
    try:
        skintype = "notslim"
        im = Image.open(i)
        im = im.convert("RGBA")
        print("[V] " + str(i) + " loaded!")
        print(im.size)
        if im.size == (64,64):
            im.save("./output/skin" + str(inumber) + ".png")
            if im.getpixel((54,20)) == (0, 0, 0, 0):
                skintype = "slim"
            if skintype == "slim":
                skinsjson["skins"].append({"localization_name": "Skin " + str(inumber),"geometry": "geometry.humanoid.customSlim","texture": "skin" + str(inumber) + ".png","type": "free"})
            if skintype == "notslim":
                skinsjson["skins"].append({"localization_name": "Skin " + str(inumber),"geometry": "geometry.humanoid.custom","texture": "skin" + str(inumber) + ".png","type": "free"})
    except Exception:
        traceback.print_exc()
    inumber = inumber + 1

skinsjsonfile = open("./output/skins.json","w")
skinsjsonfile.write(json.dumps(skinsjson))
skinsjsonfile.close()

print("Done, go make the manifest.json")
