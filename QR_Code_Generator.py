import qrcode
import qrcode.image.svg

method = "basic"

data = input("Enter the data to be encoded: ")

name_of_file = input("Enter the name of the file: ")

file_type = input("Enter the file type: ")

if method == 'basic':

    factory = qrcode.image.svg.SvgImage
elif method == 'fragment':

    factory = qrcode.image.svg.SvgFragmentImage
elif method == 'path':

    factory = qrcode.image.svg.SvgPathImage

img = qrcode.make(data, image_factory = factory)

if(file_type == 'svg'):
    img.save(name_of_file + '.svg')
elif(file_type == 'png'):
    img.save(name_of_file + '.png')