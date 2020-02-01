import tkinter as tk
import schedule
import time


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

        master.geometry("300x300")
        master.title("雛形")


# スケジュールの処理は一つにまとめる
# 39分ごと、規定時間から30分間続ける
class Job_management():
    def

    while True:
        # 規定時間になったものがあれば実行
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()