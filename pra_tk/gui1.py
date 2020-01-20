import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master):
        # スーパークラスの読み込み
        super().__init__(master)
        # 自分自身の貼り付け
        self.pack()

        self.width = 450
        self.height = 300

        # create window
        master.geometry(str(self.width)+"x"+str(self.height))

        master.title("和の計算")
        # create bg color
        self.master.config(bg="pink")
        # 独自メソッド
        self.createwidgets()

    def createwidgets(self):
        # テキストボックスの作成
        self.entry1 = tk.Entry(width=15)
        self.entry1.place(x=10, y=120)
        self.entry2 = tk.Entry(width=15)
        self.entry2.place(x=180, y=120)
        self.entry3 = tk.Entry(width=15)
        self.entry3.place(x=350, y=120)

        # 記号の追加
        self.label2 = tk.Label(text="+",fg="black",bg="pink",font=("Helvetica",30,"bold"))
        self.label2.place(x=128, y=103)
        self.label3 = tk.Label(text="=", fg="black", bg="pink", font=("Helvetica", 30, "bold"))
        self.label3.place(x=298, y=103)

        self.button1 = tk.Button(text="計算する", command=self.button1Click,width=30)
        self.button1.place(x=110, y=180)


    def button1Click(self):
        if self.entry1.get() != "" and self.entry2.get() != "":
            # 0から最後まで消す
            self.entry3.delete(0,tk.END)
            self.entry3.insert(0,int(self.entry1.get())+int(self.entry2.get()))


def main():
    win = tk.Tk()
    # ウインドウを固定サイズにする
    win.resizable(width=False, height=False)
    app = Application(master=win)
    app.mainloop()


if __name__ == "__main__":
    main()