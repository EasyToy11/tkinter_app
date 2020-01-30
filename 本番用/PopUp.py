import tkinter as tk


class Mainmenu(tk.Frame):
    # f=tk.Frame(master, option)
    # 今回はクラスなので、第一引数にself,第二引数に本来のmasterが引数として入っている。
    def __init__(self, master=None):
        # tk.Frame.__init__(self, master)でも行ける（親のスーパークラスを呼び出しているだけなので）
        # superはsuper(クラス、インスタンス自身self）ともかけるが省略可能
        # initの引数はすーぱクラスのinitの引数を入れる。この場合frameなので、masterとあればoption
        super().__init__(master)

        self.pack()
        master.title("メインメニュー")
        master.geometry("300x300")


if __name__ == '__main__':
    root = tk.Tk()
    main = Mainmenu(root)
    main.mainloop()


