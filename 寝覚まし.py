import tkinter as tk
import schedule
import time


class SleepTimer:
    def __init__(self):
        self.win = tk.Tk()
        self.a = tk.Label(text="Hello!", font=("", 50))
        self.a.pack(expand=1)
        self.b = tk.Button(text="小さくする")
        self.b.bind("<1>", self.smallscreen)
        self.b.pack()
        self.win.attributes('-fullscreen', True)
        self.ScreenStatus = False
        self.win.bind("<F11>", self.fullscreen)
        self.win.bind("<Escape>", self.smallscreen)

        self.win.mainloop()

    def fullscreen(self, event):
        self.ScreenStatus = True
        self.win.attributes("-fullscreen", self.ScreenStatus)

    def smallscreen(self, event):
        self.ScreenStatus = False
        self.win.attributes("-fullscreen", self.ScreenStatus)


def main():
    schedule.every(7).seconds.do(SleepTimer)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    main()
