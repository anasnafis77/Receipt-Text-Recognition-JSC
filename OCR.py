import pytesseract
from pytesseract import Output
import cv2
import numpy as np
from matplotlib import pyplot as plt
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
path = filedialog.askopenfilename()


path_test = 'test_ocr2.PNG'
image = cv2.imread(path, 1)
img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

img = cv2.copyMakeBorder(img, 5, 5, 5, 5, cv2.BORDER_CONSTANT, value=[0, 0, 0])
img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
image = np.zeros([img.shape[0], img.shape[1], 3])
image[:, :, 0], image[:, :, 1], image[:, :, 2] = (img, img, img)

d = pytesseract.image_to_data(img, output_type=Output.DICT)
n_boxes = len(d['level'])
for i in range(n_boxes):
    (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
    image = cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

extracted_text = pytesseract.image_to_string(img, lang='eng')
print(extracted_text)
text_file = open('text_ocr.txt', 'w')
text_file.write(extracted_text)
text_file.close()
plt.imshow(image)
plt.show()