#  basic version to generate code 

# import qrcode as qr

# code = "secret data"

# img = qr.make(code)

# img.save("E:/giaic-q3-ass/Assignment04/Assigment 00 to 09/qr_code_decode_generator/myqrimage.png")

# generate code and get link

import qrcode , io, base64

qr = qrcode.make("secret code")
print(qr)
buf = io.BytesIO()
qr.save(buf, format="PNG")
image_value = buf.getvalue()
url = "data:image/png;base64,"+ base64.b64encode(image_value).decode("ascii")
print("PNG size :",len(image_value),"bytes")
print(url)


#  read image 

# from PIL import Image
# img = Image.open(io.BytesIO(image_value))
# img.show()
# print(img)





