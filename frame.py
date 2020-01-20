import os
import tkinter as tk
import datetime

# 初期値のコンストラクタ
comment = "時間を区切って行動しよう！"
source_path = r"C:\Users\n1270242.STCN2\Downloads\timetable"
is_day = [0] * 2

a = datetime.datetime.now()
now_time = '{}年{:02}月{:02}日 {:02}:{:02}'.format(a.year, a.month, a.day, a.hour, a.minute)
txt_index = a.day
dir_index = a.month


# 疑似アラーム機能。23～7時まで。わんちゃん、Scheduleの外部ライブラリーを使う
if 23 <= a.hour:
    comment = "そろそろ寝ろ！！"

if 0 <= a.hour <= 7:
    comment = "pcもスマホもいじらずに寝なさい！！/n寝れないなら英単語を読むこと！！"

# rootの処理
root = tk.Tk()
root.title(u"time manager")
root.geometry('300x200')

# ボタンを押したときの処理
def store_txt(event):
    day_txt = txt.get()
    txt.delete(0, tk.END)
    dir_path = source_path + '\\' + str(dir_index) + '月'
    txt_path = dir_path + '\\' + str(txt_index) + '日.txt'
    # 月ごとにディレクトリーを作る
    if is_day[0] != dir_index and (os.path.isdir(dir_path) is False):
        os.mkdir(dir_path)

    # その日なら追記
    if is_day[1] == txt_index or (os.path.isfile(txt_path) is True):
        with open(txt_path, mode='a') as f:
            f.write(f'\n{a.hour}:{a.minute}')
            f.write('\n' + day_txt + '\n')
    # その日初めてならファイルを作る
    else:
        with open(txt_path, mode='w') as f:
            f.write(f'{a.hour}:{a.minute}')
            f.write('\n' + day_txt + '\n')

    is_day[0] = dir_index
    is_day[1] = txt_index

# ガジェットを各種に配置する
frame1 = tk.Frame(
    root,
    borderwidth=5)

show_time = tk.Label(
    frame1,
    text=now_time,)

show_instructor = tk.Label(
    frame1,
    text="hello")

txt = tk.Entry(width=40)

ex_comment = tk.Label(
    frame1,
    text=comment
)

commit_button = tk.Button(text=u'保存する', width=50)
commit_button.bind("<Button-1>", store_txt)

frame1.grid()
txt.grid()
commit_button.grid()
show_time.grid()
show_instructor.grid()
ex_comment.grid()
root.mainloop()
