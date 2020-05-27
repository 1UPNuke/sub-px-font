from PIL import Image

letters = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ "

for x in range(0, 10):
    im = Image.open('img\letter_0'+str(x)+".png")
    im.save('img\\'+str(ord(letters[x]))+".png")

for x in range(10, 95):
    im = Image.open('img\letter_'+str(x)+".png")
    im.save('img\\'+str(ord(letters[x]))+".png")
