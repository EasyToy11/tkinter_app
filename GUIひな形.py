import tkinter as tk

# tkのFrameを基底クラスとしてクラスを作る。frameはウィジェットを埋め込む領域を作るもの
class Application(tk.Frame):
    # tk.Frameのmasterの部分を引き継がせたいので、第二引数にmaster
    # master=Noneはウィジェット全体を指す。
    # f=tk.Frame(master, option)
    # 今回はクラスなので、第一引数にself,第二引数に本来のmasterが引数として入っている。
    def __init__(self, master=None):
        # クラスを継承する際の注意点として、以下の一文を入れないと、継承元の__init__が
        # オバーライドして継承した意味がなくなる。ので、スーパークラスのinitをするよう
        # 明示的に示す（オーバーライドすることなく継承できる）
        # super()を使う場合、第一引数にselfは必要ない
        # tk.Frame.__init__(self, master)でも行ける（親のスーパークラスを呼び出しているだけなので）
        # superはsuper(クラス、インスタンス自身self）ともかけるが省略可能
        # initの引数はすーぱクラスのinitの引数を入れる。この場合frameなので、masterとあればoption
        super().__init__(master)
        # 自分自身（Frame)をメインウインドウに張り付け
        self.pack()

        master.geometry("300x300")
        master.title("雛形")


def main():
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()


if __name__ == "__main__":
    main()

# ======================================================================
import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

        master.geometry("300x300")
        master.title("雛形")


if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
