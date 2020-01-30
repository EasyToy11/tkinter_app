import tkinter as tk

root = tk.Tk()
root.title('Main')
sub_win = None

def message_window():
    global sub_win
    if sub_win is None or not sub_win.winfo_exists():
        # メインウインドウと連動したウインドウを作る
        sub_win = tk.Toplevel()
        sub_win.title('About')
        tk.Message(sub_win, aspect=200,
                   text='messageのサンプル').pack()


m = tk.Menu(root)
root.configure(menu=m)
m.add_command(label='About', under=0, command=message_window)

tk.Label(root, text=u'メニューを選んでね').pack()
root.mainloop()