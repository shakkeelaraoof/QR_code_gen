import qrcode

#Plain QR

#Give the link or Content for the QR Code
img = qrcode.make("https://afeefalishan.github.io/Greenmark-site/index.html")
#Give the file Name and Extention to save 
img.save("QR.png")

