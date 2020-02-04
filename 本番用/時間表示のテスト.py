import tkinter as tk
import schedule
import time


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

        master.geometry("300x300")
        master.title("雛形")
        self.wdebug = tk.Button(text="wdisplay")
        self.wdebug.bind("<1>", Working_timer.wdisplay)
        self.wdebug.pack()


class Working_timer():
    # ディスプレイの表示部分
    def wdisplay(self):
        working_sub = tk.Toplevel(root)
        working_sub.title("作業していますか？")
        working_sub.geometry('200x200')
        working_mes = tk.Label(working_sub, text='作業してますか？\n作業内容を記入してください')
        working_mes.pack()
        self.entry1 = tk.Entry(working_sub, width=40)
        self.entry1.pack()

        self.wbtn = tk.Button(working_sub, text='保存')
        self.wbtn.bind(working_sub, "<1>", Working_timer.test)
        self.wbtn.pack()

    def test(self):
        print('OK!!!')
# スケジュールの処理は一つにまとめる
# 39分ごと、規定時間から30分間続ける


if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()