import tkinter as tk

root = tk.Tk()
root.option_add('*Button.font', ('Arial', 12))
root.option_add('*Button.background', 'cyan')

buff = tk.StringVar()
buff.set("")

label = tk.Label(root, textvariable=buff)
label.pack(anchor='w')


def make_cmd(n):
    return lambda:buff.set('button {} pressed'.format(n))


for x in range(4):
    button = tk.Button(root, text='Button {}'.format(x), command=make_cmd(x))
    button.pack(side='left')

root.mainloop()


