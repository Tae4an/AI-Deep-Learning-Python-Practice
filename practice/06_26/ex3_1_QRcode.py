# import qrcode
# img = qrcode.make('https://www.naver.com/')
# type(img)  # qrcode.image.pil.PilImage
# img.save("some_file.png")
#-------------------------------------------------
import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('https://www.naver.com/')
qr.make(fit=True)

img = qr.make_image(back_color=(255, 195, 235), fill_color=(55, 95, 35))
