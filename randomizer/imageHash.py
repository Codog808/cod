from PIL import Image
import hashlib

def hexy(decimal):
    conversion = ""
    hexidecimal = "0123456789ABCDEF"
    while decimal > 0:
        remainder = decimal % 16
        conversion = hexidecimal[remainder] + conversion
        decimal = decimal // 16
    return conversion


def main():
    im = Image.open("hash.png")
    im_height, im_width = im.size
    im_pixels = im.load()
    im_pixel_values = [im_pixels[x, y] for x in range(im_width) for y in range(im_height)]
    hash = hexy(sum(r*g*b for r, g, b in im_pixel_values))
    with open("hasg.txt", "w") as f:
        f.write(hash)

    
    


def sha256():
    im = Image.open("hash.png")
    # print(im.format, im.size, im.mode)
    # nuevenary(im)
    with open("hash.png", "rb") as f:
        image_data = f.read()
        sha256 = hashlib.sha256()
        sha256.update(image_data)
    hex_rep = sha256.hexdigest()
    print(hex_rep)
    

class nuevenary:
    def __init__(self, im) -> None:
        self.im = im
    def encode(self):
        height, width = self.im.size
        pixels = self.im.load()
        pixel_values = [pixels[x, y] for x in range(width) for y in range(height)]
        # (65, 34, 63)
        nuevenary = "abcdefghij"
        new_string = "".join(nuevenary[int(a)] for a in "".join(str(x) for x in (r*g*b for r, g, b in pixel_values)))
        with open("encoded.txt",'w') as f:
            f.write(new_string)
        print("success")

    def decode(self, nuevenary_corpus="encoded.txt"):
        with open(nuevenary_corpus) as f:
            corpus = f.read().strip()
        
            



main()
