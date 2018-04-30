import tkinter as tk
from tkinter import font  as tkfont
from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk
import os

class PracticeApp(tk.Tk):

	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)

		self.title_font = tkfont.Font(family='Helvetica', size=16)
		self.h1_font = tkfont.Font(family='Helvetica', size=16)
		self.body_font = tkfont.Font(family='Helvetica', size=12)
		self.geometry("1024x576") #You want the size of the app to be 500x500
		self.resizable(0, 0) #Don't allow resizing in the x or y 
		# the container is where we'll stack a bunch of frames
		# on top of each other, then the one we want visible
		# will be raised above the others
		self.wm_title("Fingerspelling - Practice Module")
		container = tk.Frame(self)
		container.pack(side="top", fill="both", expand=True)
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		self.frames = {}
		for F in (StartPage, PageOne):
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
		button1 = tk.Button(self, text="►", bg="#1eeeee", fg="black",command=lambda: controller.show_frame("PageOne"), font=controller.h1_font)
		# button2 = tk.Button(self, text="Go to Page Two",command=lambda: controller.show_frame("PageTwo"))
		button1.place(relx=.9, rely=.8, anchor="c")
		# button2.pack(side="top", fill="x", pady=10)


class PageOne(tk.Frame):
	alphabets=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		# create the canvas, size in pixels
		load = Image.open("web_parallax.jpg")
		render = ImageTk.PhotoImage(load)
		# labels can be text or images
		img = Label(self, image=render)
		img.image = render
		img.place(x=0, y=0)

		title_label = tk.Label(self, text="Fingerspelling - Indian Sign Language Training Tool", font=controller.title_font)
		title_label.place(relx=.53, rely=.30, anchor="c")

		label = tk.Label(self, text="Click on the alphabet you want to practice \nA new window will open where you will see the camera feed \nPerform Gestures in front of the camera \nSystem will show a rectangle in front of your hands when gesture is detected \n Ensure Proper lighting condition", font=controller.body_font)
		label.place(relx=.53, rely=.65, anchor="c")

		back_button = tk.Button(self, text="Back", bg="#1eeeee", fg="black",command=lambda: controller.show_frame("StartPage"), font=controller.h1_font)
		back_button.place(relx=.1, rely=.95, anchor="c")

		for i in self.alphabets:		
			a_button = tk.Button(self, text=chr(i+64), bg="#1eeeee", font=controller.h1_font, fg="black",command=lambda i=i: os.system(str(chr(i+64))+".py"), width=2)
			if i==1:
				a_button.grid(row=0,column=i, padx=(17,2.3),pady=450)
			else:
				a_button.grid(row=0,column=i, padx=2.3,pady=450)


if __name__ == "__main__":
	app = PracticeApp()
	app.mainloop()