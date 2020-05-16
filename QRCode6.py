import qrcode
from PIL import Image

face = Image.open('sandy2.jpg').crop((165, 40, 285, 200))

qr_big = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_H
)
qr_big.add_data('upi://pay?pa=dhanakondareddy825@oksbi&pn=Dhanakondareddy%20Polimera&aid=uGICAgICIsLOSDw')
qr_big.make()
img_qr_big = qr_big.make_image(back_color='#00ffff').convert('RGB')

pos = ((img_qr_big.size[0] - face.size[0]) // 2, (img_qr_big.size[1] - face.size[1]) // 2)

img_qr_big.paste(face, pos)
img_qr_big.save('6.png')
