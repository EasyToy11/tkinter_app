import os
import tkinter as tk
from datetime import datetime


class Application(tk.Frame):
    # ウインドの作成
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        master.geometry("500x200")
        master.title("雛形")

        self.createwidgets()
        self.save_comment()
        master.after(50, self.update)

    # ガジェットの作成
    def createwidgets(self):
        label1 = tk.Label(text="テスト")
        label1.pack()

        label2 = tk.Label(text="テスト")
        label2.pack()

        entry1 = tk.Entry(width=40)

    def update(self):
        label3 = tk.Label(text=datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
        label3.place(x=40, y=175)

        # .after(delay, callback=None)
        # は、すべてのtkinterウィジェットに対して定義されたメソッドです。
        self.master.after(50, self.update)

    def save_comment(self):
        source_path = r"C:\Users\n1270242.STCN2\Downloads\timetable"
        is_day = [0] * 2
        a = datetime.now()
        file_index = a.day
        dir_index = a.month
        txt = entry1.get()
        self.entry1.delete(0, tk.END)

        dir_path = source_path + '\\' + str(dir_index) + '月'
        txt_path = dir_path + '\\' + str(file_index) + '日.txt'
        # 月ごとにディレクトリーを作る
        if is_day[0] != dir_index and (os.path.isdir(dir_path) is False):
            os.mkdir(dir_path)

        # その日なら追記
        if is_day[1] == file_index or (os.path.isfile(txt_path) is True):
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



def main():
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()


if __name__ == "__main__":
    main()