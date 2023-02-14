
import base64

image_path = "App/Offers/image/0.png"


with open(image_path, "rb") as image_file:
     encodes = base64.b64encode(image_file.read())
     

print(encodes)

