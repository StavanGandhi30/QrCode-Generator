##pip install Pillow 8.0.1
##pip install pyzbar 0.1.8

from PIL import Image
from pyzbar.pyzbar import decode

data = decode(Image.open(#QRCode path))
value = str(data[0][0])
text = value.replace("b'","").replace("'","")
print(text)
