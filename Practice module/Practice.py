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
		self.geometry("700x400") #You want the size of the app to be 500x500
		self.resizable(0, 0) #Don't allow resizing in the x or y 
		# the container is where we'll stack a bunch of frames
		# on top of each other, then the one we want visible
		# will be raised above the others
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
		label = tk.Label(self, text="Practice Fingerspelling \n Indian Sign Language Gestures", font=controller.title_font)
		# label.pack(side="top", fill="x", pady=10)
		label.place(relx=.53, rely=.65, anchor="c")
		button1 = tk.Button(self, text="Start", bg="#2ce313", fg="black",width=20,
							command=lambda: controller.show_frame("PageOne"))
		# button2 = tk.Button(self, text="Go to Page Two",command=lambda: controller.show_frame("PageTwo"))
		button1.place(relx=.5, rely=.8, anchor="c")
		# button2.pack(side="top", fill="x", pady=10)


class PageOne(tk.Frame):
	

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
		label = tk.Label(self, text="Perform Gestures in front of the camera \n System will show the alphabet when gesture is detected \n Ensure Proper lighting condition", font=controller.title_font)
		# label.pack(side="top", fill="x", pady=10)
		label.place(relx=.53, rely=.65, anchor="c")

		a_button = tk.Button(self, text="A", bg="#2ce313", fg="black",command=self.detect_a)
		a_button.grid(row=0,column=0, padx=4,pady=310)
		b_button = tk.Button(self, text="B", bg="#2ce313", fg="black",command=self.detect_b)
		b_button.grid(row=0,column=1, padx=4,pady=310)
		c_button = tk.Button(self, text="C", bg="#2ce313", fg="black",command=self.detect_c)
		c_button.grid(row=0,column=2, padx=4,pady=310)
		d_button = tk.Button(self, text="D", bg="#2ce313", fg="black",command=self.detect_d)
		d_button.grid(row=0,column=3, padx=4,pady=310)
		e_button = tk.Button(self, text="E", bg="#2ce313", fg="black",command=self.detect_e)
		e_button.grid(row=0,column=4, padx=4,pady=310)
		f_button = tk.Button(self, text="F", bg="#2ce313", fg="black",command=self.detect_f)
		f_button.grid(row=0,column=5, padx=4,pady=310)
		g_button = tk.Button(self, text="G", bg="#2ce313", fg="black",command=self.detect_g)
		g_button.grid(row=0,column=6, padx=4,pady=310)
		h_button = tk.Button(self, text="H", bg="#2ce313", fg="black",command=self.detect_h)
		h_button.grid(row=0,column=7, padx=4,pady=310)
		i_button = tk.Button(self, text="I", bg="#2ce313", fg="black",command=self.detect_i)
		i_button.grid(row=0,column=8, padx=4,pady=310)
		j_button = tk.Button(self, text="J", bg="#2ce313", fg="black",command=self.detect_j)
		j_button.grid(row=0,column=9, padx=4,pady=310)
		k_button = tk.Button(self, text="K", bg="#2ce313", fg="black",command=self.detect_k)
		k_button.grid(row=0,column=10, padx=4,pady=310)
		l_button = tk.Button(self, text="L", bg="#2ce313", fg="black",command=self.detect_l)
		l_button.grid(row=0,column=11, padx=4,pady=310)
		m_button = tk.Button(self, text="M", bg="#2ce313", fg="black",command=self.detect_m)
		m_button.grid(row=0,column=12, padx=4,pady=310)
		n_button = tk.Button(self, text="N", bg="#2ce313", fg="black",command=self.detect_n)
		n_button.grid(row=0,column=13, padx=4,pady=310)
		o_button = tk.Button(self, text="O", bg="#2ce313", fg="black",command=self.detect_o)
		o_button.grid(row=0,column=14, padx=4,pady=310)
		p_button = tk.Button(self, text="P", bg="#2ce313", fg="black",command=self.detect_p)
		p_button.grid(row=0,column=15, padx=4,pady=310)
		q_button = tk.Button(self, text="Q", bg="#2ce313", fg="black",command=self.detect_q)
		q_button.grid(row=0,column=16, padx=4,pady=310)
		r_button = tk.Button(self, text="R", bg="#2ce313", fg="black",command=self.detect_r)
		r_button.grid(row=0,column=17, padx=4,pady=310)
		s_button = tk.Button(self, text="S", bg="#2ce313", fg="black",command=self.detect_s)
		s_button.grid(row=0,column=18, padx=4,pady=310)
		t_button = tk.Button(self, text="T", bg="#2ce313", fg="black",command=self.detect_t)
		t_button.grid(row=0,column=19, padx=4,pady=310)
		u_button = tk.Button(self, text="U", bg="#2ce313", fg="black",command=self.detect_u)
		u_button.grid(row=0,column=20, padx=4,pady=310)
		v_button = tk.Button(self, text="V", bg="#2ce313", fg="black",command=self.detect_v)
		v_button.grid(row=0,column=21, padx=4,pady=310)
		w_button = tk.Button(self, text="W", bg="#2ce313", fg="black",command=self.detect_w)
		w_button.grid(row=0,column=22, padx=4,pady=310)
		x_button = tk.Button(self, text="X", bg="#2ce313", fg="black",command=self.detect_x)
		x_button.grid(row=0,column=23, padx=4,pady=310)
		y_button = tk.Button(self, text="Y", bg="#2ce313", fg="black",command=self.detect_y)
		y_button.grid(row=0,column=24, padx=4,pady=310)
		z_button = tk.Button(self, text="Z", bg="#2ce313", fg="black",command=self.detect_z)
		z_button.grid(row=0,column=25, padx=4,pady=310)
		


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
	app = PracticeApp()
	app.mainloop()