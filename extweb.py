import sys,os
app=sys.argv[1]
from PIL import Image
im = Image.new('RGB',(48,48))
for x in range(48):
    for y in range(48):
        im.putpixel((x,y),(20,255,0))

json=f"""
{{
  "manifest_version": 2,
  "name": "{app}",
  "version": "1.0",

  "description": "Ajoute une bordure rouge pleine sur l'ensemble des pages web mozilla.org.",

  "icons": {{
    "48": "icons/border-48.png"
  }},

  "content_scripts": [
    {{
      "matches": ["*://*.*"],
      "js": ["{app}.js"]
    }}
  ]
}}
"""
os.mkdir(f"{app}")
os.mkdir(f"{app}/icons")
im.save(f"{app}/icons/border-48.png")
with open(f"{app}/manifest.json",'w') as f:
    f.write(json)
with open(f"{app}/{app}.js",'w') as f:
    f.write("// test js extension")

