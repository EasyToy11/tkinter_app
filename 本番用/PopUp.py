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

        # デバック用
        self.sdebug = tk.Button(text="sdisplay")
        self.sdebug.bind("<1>", Sleeptimer.first_sdisplay)
        self.sdebug.grid(row=5, column=0)

        self.wdebug = tk.Button(text="wdisplay")
        self.wdebug.bind("<1>", Working_timer.wdisplay)
        self.wdebug.grid(row=5, column=1)
        # 画面を最小化（閉じておく）にするとずっと動き続けているのか、動かなくなる時がある。
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
        sleep_sub = tk.Toplevel(root)
        stime = tk.Label(sleep_sub, text=now_time)
        stime.pack()
        # とりあえず定型文。ランダムに変わるようにもしたい
        smessage = tk.Label(sleep_sub, text='一回目')
        smessage.pack()
        # return schedule.CancelJob

    # もし2回目以降なら
    def sdisplay(self):
        sleep_sub = tk.Toplevel(root)
        sleep_sub.title("寝覚まし")
        sleep_sub.geometry('200x200')
        stime = tk.Label(sleep_sub, text=now_time)
        stime.pack()

    # 設定画面、メインメニューから来る
    def setting_disp(event):
        sleep_sub = tk.Toplevel(root)
        sleep_sub.title("サブメニュー")
        sleep_sub.geometry("200x200")
        smessage = tk.Label(sleep_sub, text='設定をここでできるようにする。')
        smessage.pack()

# working_timer
class Working_timer():
    # ディスプレイの表示部分
    def wdisplay(self):
        print("test")
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
        print("OK!!!")

    def save_comment(self, event):
        txt = self.entry1.get()
        # txtに内容があるなら処理を続ける
        if len(txt) != 0:
            # 何か記入されてるなら消す
            self.entry1.delete(0, tk.END)

            # ディレクトリーの配置位置をsource_pathで決定する
            source_path = r"C:\\testdir"
            # ディレクトリーがないなら作る
            if os.path.isdir(source_path) is False:
                os.mkdir(source_path)

            is_day = [0] * 2
            # time get
            # そのうちnow_timeで統一
            a = datetime.now()
            file_index = a.day
            dir_index = a.month

            # each path setting
            dir_path = source_path + '\\' + str(dir_index) + '月'
            txt_path = dir_path + '\\' + str(file_index) + '日.txt'
            # 月ごとにディレクトリーを作る。
            if os.path.isdir(dir_path) is False:
                os.mkdir(dir_path)

            # その日なら追記
            if os.path.isfile(txt_path) is True:
                with open(txt_path, mode='a') as f:
                    f.write(f'\n{a.hour}:{a.minute}')
                    f.write('\n' + txt + '\n')
            # その日初めてならファイルを作る
            else:
                with open(txt_path, mode='w') as f:
                    f.write(f'{a.hour}:{a.minute}')
                    f.write('\n' + txt + '\n')

            is_day[0] = dir_index
            is_day[1] = file_index


# スケジュールの処理は一つにまとめる
class Job_management():

    def master_manegement(self):
        # 作業時間時
        self.working_time()
        # 寝る時間一回目
        self.sleeptime_now()
        # 寝る時間繰り返し

    # 寝覚ましの時間かつ、2回目以降の起動の時はここ
    def sleeptime(self):
        schedule.every()
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


