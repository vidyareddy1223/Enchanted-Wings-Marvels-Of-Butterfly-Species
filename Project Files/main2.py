import matplotlib.pyplot as plt
import requests
from PIL import Image
from io import BytesIO

image_urls = [
    "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/Blue_morpho_butterfly.jpg/800px-Blue_morpho_butterfly.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/6/6b/Monarch_Butterfly_Danaus_plexippus.jpg"
]

for url in image_urls:
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    plt.imshow(img)
    plt.axis('off')
    plt.show()
