
try:
    from PIL import Image
except ImportError:
    import Image

import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Anusha\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

def recText(filename):
    text = pytesseract.image_to_string(Image.open(filename))
    return text

info = recText('TEST1.jpg')
print(info)



file = open("New1.txt","a")
file.write(info)
file.close()
print("Written Successful")
