# https://detail.chiebukuro.yahoo.co.jp/qa/question_detail/q12206588077
import tkinter as tk

class App(tk.Frame):
    def __init__(self,txt,master=None):
        tk.Frame.__init__(self, master)
        a=tk.Frame(master)
        tk.Label(a,text=txt).pack(side=tk.LEFT)
        tk.Button(a,text="Push").pack(side=tk.LEFT)
        a.pack()

# bオブジェクトがウィンドウそのもの
b = App("AAA")
b.mainloop()

# 全体のウィンドウのオブジェクトは root で、
# クラス App を使ってその中に２つのオブジェクト（テキスト＋"Push"ボタンの組み合わせ）を作れます。

root=tk.Tk()
b=App("AAA",master=root)c=App("BBB",master=root)
b.pack()
c.pack()
root.mainloop()

# オブジェクト b が親で、
# オブジェクト b の中にオブジェクト c を作ることになります。

root=tk.Tk()
b=App("AAA",master=root)
c=App("BBB",master=b)
b.pack()
c.pack()
root.mainloop()

