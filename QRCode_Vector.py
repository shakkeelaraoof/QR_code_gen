import qrcode
import qrcode.image.svg
#QR Code in Vector Form

ab = qrcode.image.svg.SvgPathImage
svg_img = qrcode.make("Hello World!", image_factory=ab)
svg_img.save("SvqQR.svg")

