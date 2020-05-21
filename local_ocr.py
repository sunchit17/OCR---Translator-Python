from PIL import Image
import pytesseract
from googletrans import Translator

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img = Image.open('test.jpeg')

result = pytesseract.image_to_string(img)

p = Translator()
k = p.translate(result,dest='german')
translated = str(k.text)

with open('test.txt',mode='w') as file:
    file.write(result)
    file.write("\n")
    file.write(translated)
    print("Ready!")
