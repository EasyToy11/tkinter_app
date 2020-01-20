import tkinter as tk

# tkのFrameを基底クラスとしてクラスを作る。frameはウィジェットを埋め込む領域を作るもの
class Application(tk.Frame):
    # tk.Frameのmasterの部分を引き継がせたいので、第二引数にmaster
    # master=Noneはウィジェット全体を指す。
    def __init__(self,master=None):
        # クラスを継承する際の注意点として、以下の一文を入れないと、継承元の__init__が
        # オバーライドして継承した意味がなくなる。ので、スーパークラスのinitをするよう
        # 明示的に示す（オーバーライドすることなく継承できる）
        # super()を使う場合、第一引数にselfは必要ない
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