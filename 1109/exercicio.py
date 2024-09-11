import redis
import os
import time

r = redis.Redis(host="localhost", port=6379, db=0)

image_path = r"C:\Users\samiracampos-ieg\Downloads\bruninho.jpg"

with open(image_path, "rb") as image_file:
    image_data = image_file.read()
r.set("chave_imagem", image_data)

image_data = r.get('chave_imagem')

temp_image_path = r"C:\Users\samiracampos-ieg\Downloads\temp_image.jpg"

with open(temp_image_path, "wb") as temp_image_file:
    temp_image_file.write(image_data)

os.startfile(temp_image_path)
print("Imagem em bytes: "+str(r.get('chave_imagem')))

time.sleep(5)
os.remove(temp_image_path)
