import base64
import io
import cv2
from PIL import Image
import numpy as np

# Data URL (Base64 image string)
data_url = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAASIAAAEiAQAAAAB1xeIbAAABmUlEQVR4nO2YTWrEMAyFn+zALJ0bzFGSm5UeqTdIjjIHKCTLgQQVydYMlEK7aCZ/egsn8XyQR0aWbBHjd/XhDxDglMkpk1Mmp0xOrU1RUQX0cm1Hm2lX9XUKqmHRIHcyAFEneB/ud06NFuN9DXCX10K1vq+TUZFLpnnZG3+QUyanlqCqck2S2keAkD5JZ3gH7sMRqF43NbXU2ttFvvqctzlr+zpB3PPjmYE7lWWwpq9wGopazISeKlA7Xpjf65m24OsMFMumEkh34vfrhOf/4WerxXMONR81CLgwNbdqomaYwT1Fpm27D7umYMfXyNylSR5lGGQtpHy2Ze626j4cgkpSYUfd4sjZKjHT26CJZ11fx4/7p7Sfo+lfl0Fu9HjcL5nvkRUnxhil2MaS9P//jcEpU4l2Fg0xxz0aTfqPHzzuF/32g7aPpXOcy+xUBpV/+0X7OSaSdKONBc051HRbdh8ORXH3OObKjmczvs7QxwTSAO6vnOuv19pXnK1UWmut4MLz/cv7mJMMecZzznc5ZXLK5JTJKdNWqS+A7tjXiaTFygAAAABJRU5ErkJggg=="

# Step 1: Strip base64 prefix
base64_data = data_url.split(",")[1]

# Step 2: Decode base64 to bytes
img_bytes = base64.b64decode(base64_data)
print("Byte length:", len(img_bytes))

# Step 3: Load image from bytes using PIL
img_pil = Image.open(io.BytesIO(img_bytes))

# Step 4: Convert PIL image to OpenCV format
img_cv = cv2.cvtColor(np.array(img_pil), cv2.COLOR_RGB2BGR)

# Step 5: Decode the QR code using OpenCV
detector = cv2.QRCodeDetector()
data, bbox, straight_qrcode = detector.detectAndDecode(img_cv)

# Step 6: Safely handle if QR code is found or not
if data:
    print("Decoded QR Code:", data)
else:
    print("❌ No QR code found in the image.")