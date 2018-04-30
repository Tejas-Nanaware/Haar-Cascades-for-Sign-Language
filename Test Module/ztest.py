import random
random_alphabets = random.sample(range(1, 26), 5)
arr=[]
# print(random_alphabets)

for x in random_alphabets:
	arr.append(str(chr(x+64))+".py")

print(arr)

# import tkinter as tk

# window = tk.Tk()  #Makes main window
# window.wm_title("Practice Module")
# window.config(background="#FFFFFF")
# root=window

# boardWidth=random_alphabets
# def detect_a():
# 	print("in a")
# def openfile():
# 	for x in random_alphabets:
# 		if(x==1):
# 			detect_a()
		

# for i in boardWidth:
# 	# print(i)
# 	newButton = tk.Button(root, text=chr(i+64),command=openfile)
# 	newButton.grid(row=1, column=i, padx=5, pady=5)

# window.mainloop()