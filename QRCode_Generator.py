##pip install qrcode 6.1

import qrcode
qr = qrcode.QRCode(
    version=2,
    box_size=10,
    border=2,
)
qr.add_data(#Text)
qr.make(fit=True)
qr = qr.make_image(fill_color="black", back_color="white")
qr.save(#Saving Path)
