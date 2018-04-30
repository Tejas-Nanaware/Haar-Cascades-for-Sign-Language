import tkinter as tk
from tkinter import font  as tkfont
from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk
import os
import cv2

class Practice(tk.Tk):

	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)

		self.title_font = tkfont.Font(family='Helvetica', size=18)
		self.h1_font = tkfont.Font(family='Helvetica', size=16)
		self.body_font = tkfont.Font(family='Helvetica', size=12)
		self.geometry("1024x576") #You want the size of the app to be 500x500
		# self.resizable(0, 0) #Don't allow resizing in the x or y 
		# the container is where we'll stack a bunch of frames
		# on top of each other, then the one we want visible
		# will be raised above the others
		self.wm_title("Fingerspelling - Practice Module")
		container = tk.Frame(self)
		container.pack(side="top", fill="both", expand=True)
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		self.frames = {}
		for F in (StartPage, PageTwo):
			page_name = F.__name__
			frame = F(parent=container, controller=self)
			self.frames[page_name] = frame
			# put all of the pages in the same location;
			# the one on the top of the stacking order
			# will be the one that is visible.
			frame.grid(row=0, column=0, sticky="nsew")

		self.show_frame("StartPage")

	def show_frame(self, page_name):
		'''Show a frame for the given page name'''
		frame = self.frames[page_name]
		frame.tkraise()


class StartPage(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		# create the canvas, size in pixels
		# background_image=tk.PhotoImage("web_parallax.jpg")
		# background_label = tk.Label(self, image=background_image)
		# background_label.place(x=0, y=0, relwidth=1, relheight=1)
		load = Image.open("web_parallax.jpg")
		render = ImageTk.PhotoImage(load)

		# labels can be text or images
		img = Label(self, image=render)
		img.image = render
		img.place(x=0, y=0)
		title_label = tk.Label(self, text="Fingerspelling - Indian Sign Language Training Tool", font=controller.title_font)
		title_label.place(relx=.53, rely=.30, anchor="c")

		head_label = tk.Label(self, text="Practice Indian Sign Language Gestures", font=controller.h1_font)
		head_label.place(relx=.53, rely=.35, anchor="c")
		
		inst_label = tk.Label(self, text="Start practicing your gestures today! \nEnsure your primary webcam is working and room is well illuminated", font=controller.body_font)
		inst_label.place(relx=.53, rely=.65, anchor="c")

		# button1 = tk.Button(self, text="►", bg="#2ce313", fg="black",width=20,command=lambda: controller.show_frame("PageOne"))
		button1 = tk.Button(self, text="►", bg="#1eeeee", fg="black",command=lambda: button('hey'), font=controller.h1_font)
		button2 = tk.Button(self, text="Go to Page Two",command=lambda: controller.show_frame("PageTwo"))
		button1.place(relx=.9, rely=.8, anchor="c")
		button2.pack(side="top", fill="x", pady=10)

class PageTwo(tk.Frame):

	def detect_a(self):
		print("a")
		for (x,y,w,h) in A:
			cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
			font = cv2.FONT_HERSHEY_SIMPLEX
			cv2.putText(frame,'A',(x,y+h), font, 4, (0,0,255), 3, cv2.LINE_AA)
	def show_frame(self):
			_, frame = cap.read()
			frame = cv2.flip(frame, 1)
			cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)

			gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
			A_cascade = cv2.CascadeClassifier('../Haar Cascades/Z.xml')
			A = A_cascade.detectMultiScale(gray)


			img = Image.fromarray(cv2image)
			imgtk = ImageTk.PhotoImage(image=img)
			lmain.imgtk = imgtk
			lmain.configure(image=imgtk)
			lmain.after(10, show_frame) 
			sliderFrame = tk.Frame(self, width=1000, height=450)
			sliderFrame.grid(row = 1000, column=0, padx=12, pady=12)

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		# label = tk.Label(self, text="This is page 2", font=controller.title_font)
		# label.place(relx=.53, rely=.65, anchor="c")
		home_button = tk.Button(self, text="Go to the start page",command=lambda: controller.show_frame("StartPage"))
		home_button.place(relx=.9, rely=.9, anchor="c")
		imageFrame = tk.Frame(self, width=1000, height=450)
		imageFrame.grid(row=0, column=0, padx=12, pady=12)
		a_button = tk.Button(self, text="A", bg="#2ce313", fg="black",command=lambda: self.detect_a)
		a_button.grid(row=1,column=0)
        
		# video in frame
		lmain = tk.Label(imageFrame)
		lmain.grid(row=0, column=0)
		cap = cv2.VideoCapture(0)
		self.show_frame(self)

		




if __name__ == "__main__":
	app = Practice()
	app.mainloop()