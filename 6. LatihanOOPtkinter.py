import tkinter as tk

main_window = tk.Tk()

label1 = tk.Label(main_window, text="label 1")
label2 = tk.Label(main_window, text="label 2")

button1 = tk.Button(main_window, text="button 1")
button2 = tk.Button(main_window, text="button 2")

# method positioning 
label1.pack()
label2.pack()
button1.pack()
button2.pack()

# method penampilan GUI
main_window.mainloop()