import urllib
import time
import requests
import random
from pytesseract import image_to_string
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from PIL import Image
from StringIO import StringIO


driver = webdriver.Firefox()
driver.get('http://www.xxxxx.com.co')

time.sleep(1)

all_cookies = driver.get_cookies()


url_Captcha= 'http://www.xxxxx.com.co'
cookies = {}
for s_cookie in all_cookies:
	cookies[s_cookie["name"]]=s_cookie["value"]

	r = requests.get(url_Captcha,cookies=cookies)

	i = Image.open(StringIO(r.content))

	i.save('captcha.jpeg')

numero = random.randrange(00000000, 99999999)

campo_nombre = driver.find_element_by_xpath("//*[@id='txtNombre']")
campo_nombre.send_keys("poc")
time.sleep(1)

campo_cedula = driver.find_element_by_xpath("//*[@id='txtCedula']")
campo_cedula.send_keys(str(numero))
time.sleep(1)

campo_telefono = driver.find_element_by_xpath("//*[@id='txtTelefono']")
campo_telefono.send_keys("0000000000")
time.sleep(1)

campo_email = driver.find_element_by_xpath("//*[@id='txtEmail']")
campo_email.send_keys("email" + str(numero) + "@poc.com")
time.sleep(1)

campo_comentario = driver.find_element_by_xpath("//*[@id='txtComentario']")
campo_comentario.send_keys("01000110 01100001 01101001 01101100 00101110 00101110 00101110")
time.sleep(1)

driver.execute_script("window.scrollTo(0,300);")
time.sleep(2)

campo_check = driver.find_element_by_xpath("//*[@id='chkTerminos']")
campo_check.click()
time.sleep(1)

im = Image.open(r'/your-path/captcha.jpeg')

captchatxt = (image_to_string(im))

campo_captcha = driver.find_element_by_xpath("//*[@id='txtCaptcha']")
campo_captcha.send_keys(captchatxt)
time.sleep(3)


boton_enviar = driver.find_element_by_xpath("//*[@id='btnOK']")
boton_enviar.click()
time.sleep(5)

driver.close()