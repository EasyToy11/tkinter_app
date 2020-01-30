import tkinter as tk
import schedule
import time

# 今の状況、7秒ごとにフルスクリーンでウインドウを出しているところ
class SleepTimer:
    def __init__(self):
        self.win = tk.Tk()
        self.a = tk.Label(text="Hello!", font=("", 50))
        self.a.pack(expand=1)
        self.b = tk.Button(text="小さくする")
        self.b.bind("<1>", self.minutesafter)
        self.b.pack()
        # self.win.attributes('-fullscreen', True)
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

    def minutesafter(self, event):
        self.ScreenStatus = False
        self.win.attributes("-fullscreen", self.ScreenStatus)


 class IntervalScreen:





def main():
    SleepTimer()
    # 最終的には1:00以降などに自動的に表示させるものにする
    # ここでは一回だけ呼び出し、分ごとの表示はクラスで書く。
    """
    schedule.every().day.at("12:00").do(SleepTimer())
    schedule.run_pending()
    time.sleep(1)
    """
if __name__ == '__main__':
    main()
