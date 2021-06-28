import qrcode
#In this we can Customize the Color of the QR Code

qr = qrcode.QRCode(version=1, 
                    error_correction=qrcode.constants.ERROR_CORRECT_L,
                    box_size=50,
                    border=2)


qr.add_data("https://afeefalishan.github.io/Greenmark-site/index.html")
qr.make(fit=True)

img = qr.make_image(fill_color="#FF5200", back_color="white")
img.save("QRColor.png")