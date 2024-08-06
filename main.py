import tkinter
from tkinter import ttk

import sv_ttk

DIMENSION = "1600x800"

def main():
	root = tkinter.Tk()

	#set root window size.
	root.geometry(DIMENSION)

	for i in range(4):
		#configure column height and width based on window size
		#root.columnconfigure(i, weight = 1, minsize = 75)
		#root.rowconfigure(i, weight = 1, minsize = 50)
		for j in range(3):
			frame = tkinter.Frame(master=root)

			frame.grid(row=i, column=j, padx=5, pady=5)
			
			label = ttk.Button(master=frame, text=f"Row {i}\nColumn {j}")
			label.pack()

	sv_ttk.set_theme("dark")

	root.mainloop()


if __name__ == '__main__':
    main()