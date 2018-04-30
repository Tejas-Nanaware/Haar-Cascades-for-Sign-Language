import numpy as np
import cv2
import tkinter as tk
import PIL
from PIL import Image, ImageTk

#Set up GUI
window = tk.Tk()  #Makes main window
window.wm_title("Test Module")
window.config(background="#FFFFFF")

#Graphics window
imageFrame = tk.Frame(window, width=700, height=400)
imageFrame.grid(row=0, column=0, padx=10, pady=2)

#Capture video frames
lmain = tk.Label(imageFrame)
lmain.grid(row=0, column=0)
cap = cv2.VideoCapture(0)
def show_frame():
	_, frame = cap.read()
	frame = cv2.flip(frame, 1)
	
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	A_cascade = cv2.CascadeClassifier('../Haar Cascades/I.xml')
	A = A_cascade.detectMultiScale(gray)
	# To display A
	for (x,y,w,h) in A:
		cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
		font = cv2.FONT_HERSHEY_SIMPLEX
		cv2.putText(frame,'I',(x,y+h), font, 4, (0,0,255), 3, cv2.LINE_AA)

	
	cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
	img = Image.fromarray(cv2image)
	imgtk = ImageTk.PhotoImage(image=img)
	lmain.imgtk = imgtk
	lmain.configure(image=imgtk)
	lmain.after(10, show_frame)

#Slider window (slider controls stage position)
sliderFrame = tk.Frame(window, width=600, height=100)
sliderFrame.grid(row = 600, column=0, padx=10, pady=2)


show_frame()  #Display 2
window.mainloop()  #Starts GUI