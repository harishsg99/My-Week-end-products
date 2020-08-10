import io
from PIL import Image
import pytesseract
from wand.image import Image as wi
import pyttsx3
import SpeechRecognition  as sr
import sys
input = sys.argv[1]
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\tesseract.exe" #Path to the tesseract 

pdf = wi(filename = input, resolution = 300)
pdfImage = pdf.convert('jpeg')

imageBlobs = []

for img in pdfImage.sequence:
	imgPage = wi(image = img)
	imageBlobs.append(imgPage.make_blob('jpeg'))

recognized_text = []

for imgBlob in imageBlobs:
	im = Image.open(io.BytesIO(imgBlob))
	text = pytesseract.image_to_string(im, lang = 'eng')
	recognized_text.append(text)

imageBlobs = str(text)
recognized_text = text
print(recognized_text)
speak(recognized_text)
remember = open('remember.txt','w')
remember.write(text)
remember.close()
