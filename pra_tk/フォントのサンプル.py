import tkinter as tk

root = tk.Tk()
str = 'Hello World!!、こんにちは！'

tk.Label(root, text=str, font=('Courier', 12)).pack()
tk.Label(root, text=str, font=('Courier', 12),fg='blue').pack()
tk.Label(root, text=str, font=('Courier', 12, 'italic')).pack()
tk.Label(root, text=str, font=('Courier', 12, 'italic'), fg='red').pack()
tk.Label(root, text=str, font=('Courier', 16, 'underline')).pack()
tk.Label(root, text=str, font=('Courier', 16, 'underline'), fg='green').pack()


root.mainloop()

