from PIL import Image, ImageFilter

img = Image.open("./images/pokedex/charizard.jpg")

print(img.format, img.size, img.mode)

filtered_img = img.filter(ImageFilter.BLUR)
filtered_img.save('./images/pokedex/charizard-blurred.png', 'png')
