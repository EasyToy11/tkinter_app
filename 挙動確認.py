import tkinter as tk
import schedule
import time


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        # 自分自身（Frame)をメインウインドウに張り付け
        self.pack()

        master.geometry("300x300")
        master.title("雛形")

        a = tk.Label(text="ちゃんとできてる？")
        a.pack()


class TimeManager(Application):

    def job(self):
        root = tk.Tk()
        app = Application(master=root)
        app.mainloop()

    def manager(self):
        # 10秒ごと
        schedule.every(5).seconds.do(self.job)

        while True:
            schedule.run_pending()
            time.sleep(1)


def job():
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()


def manager():
    # 10秒ごと
    schedule.every(5).seconds.do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)


manager()