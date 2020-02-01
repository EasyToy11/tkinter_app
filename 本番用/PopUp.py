import os
import time
import schedule
import tkinter as tk
from datetime import datetime

# 時間はいろいろな画面に使うことも考えて、グローバル変数にする
now_time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")


# メインメニュー。ここからいろいろな画面に派生する
class Mainmenu(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        master.title("メインメニュー")
        master.geometry("300x300")
        # setを使うべきかもしれない。変数timerは、要検討
        self.timer = None
        self.sleepbtn = tk.Button(text='寝覚まし設定')
        # self.sleepbtn.bind("<1>", Sleeptimer.display)
        self.sleepbtn.grid(row=0, column=0)
        self.watchbtn = tk.Button(text='作業設定')
        self.watchbtn.grid(row=1, column=0)
        self.alartbtn = tk.Button(text='アラート設定')
        self.alartbtn.grid(row=0, column=1)
        self.filebtn = tk.Button(text='ファイル設定')
        self.filebtn.grid(row=1, column=1)
        # 画面を最小にするとずっと動き続けているのか、動かなくなる時がある。
        master.after(50, self.time_display)

    def time_display(self):
        self.timer = tk.Label(text=now_time)
        self.timer.grid(row=3, column=1, sticky=tk.W+tk.E)

        self.master.after(50, self.time_display)


# 現在時刻、寝なさいのメッセージ、
# メインウインドウのボタンを押す度にサブウインドウが出るので、後で治す。
# （サブウインドウがあるかどうか判定させる）
class Sleeptimer():
    # もし一回目なら
    def first_sdisplay(self):
        stime = tk.Label(sub, text=now_time)
        stime.pack()
        # とりあえず定型文。ランダムに変わるようにもしたい
        smessage = tk.Label(sub, text='設定をここでできるようにする。')
        smessage.pack()
        return schedule.CancelJob

    # もし2回目以降なら
    def sdisplay(self):
        sub = tk.Toplevel(root)
        sub.title("寝覚まし")
        sub.geometry('200x200')
        stime = tk.Label(sub, text=now_time)
        stime.pack()

    # 設定画面、メインメニューから来る
    def setting_disp(event):
        sub = tk.Toplevel(root)
        sub.title("サブメニュー")
        sub.geometry("200x200")
        smessage = tk.Label(sub, text='設定をここでできるようにする。')
        smessage.pack()


# スケジュールの処理は一つにまとめる
class Job_management():

    # 寝覚ましの時間かつ、2回目以降の起動の時はここ
    # 寝るまで、5分ごとに通知
    def sleeptime_now(self):
        schedule.every(5).minutes.do(Sleeptimer.sdisplay)

        # 条件はTrueでなく、寝るのボタンが押されたときにやめるようにする。
        while True:
            schedule.run_pending()
            time.sleep(1)

    # 寝覚ましの時間以外
    def working_time(self):
        # 寝覚まし以外。30分ごとの進捗を聞く
        schedule.every(30).minutes.do()
        # 寝覚まし。first_sdisplayのほうでjobの削除
        schedule.every().day("10:00").do(Sleeptimer.first_sdisplay)

        while True:
            # 規定時間になったものがあれば実行
            schedule.run_pending()
            time.sleep(1)
            """
            # 一回寝覚ましの時間になったら、寝るように数分後と通知（sleeptime_nowに移動）
            if time> 0:
                False
                self.sleeptime_now()
            """


if __name__ == '__main__':
    root = tk.Tk()
    # mainが親要素
    main = Mainmenu(root)
    main.mainloop()


