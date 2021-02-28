# generates a QR code
# https://github.com/lincolnloop/python-qrcode

import os
import qrcode

# generate QR code
img = qrcode.make("https://www.youtube.com/watch?v=4QKadkOdSQU") # link

# save as file
img.save("qr.png", "PNG")

# open file
os.system("open qr.png")


# short usage at terminal
# qr "https://www.youtube.com/watch?v=4QKadkOdSQU" > test.png