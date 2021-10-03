import qrcode
#In this we can Customize the Color of the QR Code

qr = qrcode.QRCode(version=1, 
                    error_correction=qrcode.constants.ERROR_CORRECT_L,
                    box_size=50,
                    border=2)


qr.add_data("https://github.com/AFEEFALISHAN")
qr.make(fit=True)

img = qr.make_image(fill_color="#00FF00", back_color="7FFD4")
img.save("Dramatic.png")