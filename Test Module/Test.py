import tkinter as tk
from tkinter import font  as tkfont
from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk
import os
import random

class TestApp(tk.Tk):

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
		self.wm_title("Fingerspelling - Test Module")
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

		head_label = tk.Label(self, text="Test Indian Sign Language Gestures", font=controller.h1_font)
		head_label.place(relx=.53, rely=.35, anchor="c")
		
		inst_label = tk.Label(self, text="You wil be given random five alphabets to test your gestures \nEnsure your primary webcam is working and room is well illuminated", font=controller.body_font)
		inst_label.place(relx=.53, rely=.65, anchor="c")
		button1 = tk.Button(self, text="►", bg="#1eeeee", fg="black",command=lambda: controller.show_frame("PageOne"), font=controller.h1_font)
		# button2 = tk.Button(self, text="Go to Page Two",command=lambda: controller.show_frame("PageTwo"))
		button1.place(relx=.9, rely=.8, anchor="c")
		# button2.pack(side="top", fill="x", pady=10)


class PageOne(tk.Frame):
	random_alphabets = random.sample(range(1, 26), 5)
	arr=[]
	for x in random_alphabets:
		arr.append(chr(x+64))
	print(arr)
		
	
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		# label = tk.Label(self, text="This is page 1", font=controller.title_font)
		# label.pack(side="top", fill="x", pady=10)
		# button = tk.Button(self, text="Go to the start page",
		#                    command=lambda: controller.show_frame("StartPage"))
		# button.pack()
		# create the canvas, size in pixels
		load = Image.open("web_parallax.jpg")
		render = ImageTk.PhotoImage(load)
		# labels can be text or images
		img = Label(self, image=render)
		img.image = render
		img.place(x=0, y=0)

		title_label = tk.Label(self, text="Fingerspelling - Indian Sign Language Training Tool", font=controller.title_font)
		title_label.place(relx=.53, rely=.30, anchor="c")

		label = tk.Label(self, text="Click on the alphabet you want to test \nA new window will open where you will see the camera feed \nPerform Gestures in front of the camera \nSystem will show a rectangle in front of your hands when gesture is detected \n Ensure Proper lighting condition", font=controller.body_font)
		# label.pack(side="top", fill="x", pady=10)
		label.place(relx=.53, rely=.65, anchor="c")

		back_button = tk.Button(self, text="Back", bg="#1eeeee", fg="black",command=lambda: controller.show_frame("StartPage"), font=controller.h1_font)
		# button2 = tk.Button(self, text="Go to Page Two",command=lambda: controller.show_frame("PageTwo"))
		back_button.place(relx=.1, rely=.95, anchor="c")

		for i in self.random_alphabets:
			a_button = tk.Button(self, text=chr(i+64), bg="#1eeeee", font=controller.h1_font, fg="black",command=lambda: os.system(str(chr(i+64))+".py"), width=2)
			a_button.grid(row=0,column=i, padx=(17,2.3),pady=450)

		# a_button = tk.Button(self, text="A", bg="#1eeeee", font=controller.h1_font, fg="black",command=self.detect_a, width=2)
		# a_button.grid(row=0,column=0, padx=(17,2.3),pady=450)
		# b_button = tk.Button(self, text="B", bg="#1eeeee", width=2, font=controller.h1_font, fg="black",command=self.detect_b)
		# b_button.grid(row=0,column=1, padx=2.3,pady=450)
		# c_button = tk.Button(self, text="C", bg="#1eeeee", width=2, font=controller.h1_font, fg="black",command=self.detect_c)
		# c_button.grid(row=0,column=2, padx=2.3,pady=450)
		# d_button = tk.Button(self, text="D", bg="#1eeeee", width=2, font=controller.h1_font, fg="black",command=self.detect_d)
		# d_button.grid(row=0,column=3, padx=2.3,pady=450)
		# e_button = tk.Button(self, text="E", bg="#1eeeee", width=2, font=controller.h1_font, fg="black",command=self.detect_e)
		# e_button.grid(row=0,column=4, padx=2.3,pady=450)
		# f_button = tk.Button(self, text="F", bg="#1eeeee", width=2, font=controller.h1_font, fg="black",command=self.detect_f)
		# f_button.grid(row=0,column=5, padx=2.3,pady=450)
		# g_button = tk.Button(self, text="G", bg="#1eeeee", width=2, font=controller.h1_font, fg="black",command=self.detect_g)
		# g_button.grid(row=0,column=6, padx=2.3,pady=450)
		# h_button = tk.Button(self, text="H", bg="#1eeeee", width=2, font=controller.h1_font, fg="black",command=self.detect_h)
		# h_button.grid(row=0,column=7, padx=2.3,pady=450)
		# i_button = tk.Button(self, text="I", bg="#1eeeee", width=2, font=controller.h1_font, fg="black",command=self.detect_i)
		# i_button.grid(row=0,column=8, padx=2.3,pady=450)
		# j_button = tk.Button(self, text="J", bg="#1eeeee", width=2, font=controller.h1_font, fg="black",command=self.detect_j)
		# j_button.grid(row=0,column=9, padx=2.3,pady=450)
		# k_button = tk.Button(self, text="K", bg="#1eeeee", width=2, font=controller.h1_font, fg="black",command=self.detect_k)
		# k_button.grid(row=0,column=10, padx=2.3,pady=450)
		# l_button = tk.Button(self, text="L", bg="#1eeeee", width=2, font=controller.h1_font, fg="black",command=self.detect_l)
		# l_button.grid(row=0,column=11, padx=2.3,pady=450)
		# m_button = tk.Button(self, text="M", bg="#1eeeee", width=2, font=controller.h1_font, fg="black",command=self.detect_m)
		# m_button.grid(row=0,column=12, padx=2.3,pady=450)
		# n_button = tk.Button(self, text="N", bg="#1eeeee", width=2, font=controller.h1_font, fg="black",command=self.detect_n)
		# n_button.grid(row=0,column=13, padx=2.3,pady=450)
		# o_button = tk.Button(self, text="O", bg="#1eeeee", width=2, font=controller.h1_font, fg="black",command=self.detect_o)
		# o_button.grid(row=0,column=14, padx=2.3,pady=450)
		# p_button = tk.Button(self, text="P", bg="#1eeeee", width=2, font=controller.h1_font, fg="black",command=self.detect_p)
		# p_button.grid(row=0,column=15, padx=2.3,pady=450)
		# q_button = tk.Button(self, text="Q", bg="#1eeeee", width=2, font=controller.h1_font, fg="black",command=self.detect_q)
		# q_button.grid(row=0,column=16, padx=2.3,pady=450)
		# r_button = tk.Button(self, text="R", bg="#1eeeee", width=2, font=controller.h1_font, fg="black",command=self.detect_r)
		# r_button.grid(row=0,column=17, padx=2.3,pady=450)
		# s_button = tk.Button(self, text="S", bg="#1eeeee", width=2, font=controller.h1_font, fg="black",command=self.detect_s)
		# s_button.grid(row=0,column=18, padx=2.3,pady=450)
		# t_button = tk.Button(self, text="T", bg="#1eeeee", width=2, font=controller.h1_font, fg="black",command=self.detect_t)
		# t_button.grid(row=0,column=19, padx=2.3,pady=450)
		# u_button = tk.Button(self, text="U", bg="#1eeeee", width=2, font=controller.h1_font, fg="black",command=self.detect_u)
		# u_button.grid(row=0,column=20, padx=2.3,pady=450)
		# v_button = tk.Button(self, text="V", bg="#1eeeee", width=2, font=controller.h1_font, fg="black",command=self.detect_v)
		# v_button.grid(row=0,column=21, padx=2.3,pady=450)
		# w_button = tk.Button(self, text="W", bg="#1eeeee", width=2, font=controller.h1_font, fg="black",command=self.detect_w)
		# w_button.grid(row=0,column=22, padx=2.3,pady=450)
		# x_button = tk.Button(self, text="X", bg="#1eeeee", width=2, font=controller.h1_font, fg="black",command=self.detect_x)
		# x_button.grid(row=0,column=23, padx=2.3,pady=450)
		# y_button = tk.Button(self, text="Y", bg="#1eeeee", width=2, font=controller.h1_font, fg="black",command=self.detect_y)
		# y_button.grid(row=0,column=24, padx=2.3,pady=450)
		# z_button = tk.Button(self, text="Z", bg="#1eeeee", width=2, font=controller.h1_font, fg="black",command=self.detect_z)
		# z_button.grid(row=0,column=25, padx=2.3,pady=450)
		


		# button2.pack(side="top", fill="x", pady=10)
	

	def detect_a(self):
		os.system('A.py')
	def detect_b(self):
		os.system('B.py')
	def detect_c(self):
		os.system('C.py')
	def detect_d(self):
		os.system('D.py')
	def detect_e(self):
		os.system('E.py')
	def detect_f(self):
		os.system('F.py')
	def detect_g(self):
		os.system('G.py')
	def detect_h(self):
		os.system('H.py')
	def detect_i(self):
		os.system('I.py')
	def detect_j(self):
		os.system('J.py')
	def detect_k(self):
		os.system('K.py')
	def detect_l(self):
		os.system('L.py')
	def detect_m(self):
		os.system('M.py')
	def detect_n(self):
		os.system('N.py')
	def detect_o(self):
		os.system('O.py')
	def detect_p(self):
		os.system('P.py')
	def detect_q(self):
		os.system('Q.py')
	def detect_r(self):
		os.system('R.py')
	def detect_s(self):
		os.system('S.py')
	def detect_t(self):
		os.system('T.py')
	def detect_u(self):
		os.system('U.py')
	def detect_v(self):
		os.system('V.py')
	def detect_w(self):
		os.system('W.py')
	def detect_x(self):
		os.system('X.py')
	def detect_y(self):
		os.system('Y.py')
	def detect_z(self):
		os.system('Z.py')
	


if __name__ == "__main__":
	app = TestApp()
	app.mainloop()