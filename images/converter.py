import sys
import os
from PIL import Image

folder = sys.argv[1]
output = sys.argv[2]

print(folder, output)

if not os.path.exists(f'./images/{output}'):
    os.makedirs(f'./images/{output}')

for filename in os.listdir(f'./images/{folder}'):
    img = Image.open(f'./images/{folder}{filename}')
    cleared_name = os.path.splitext(filename)[0]
    img.save(f'./images/{output}{cleared_name}.png', 'png')
    print(f'{filename} converted')
