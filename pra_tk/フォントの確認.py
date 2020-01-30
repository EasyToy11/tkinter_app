import tkinter as tk
import tkinter.font as font


class FontChart(tk.Frame):

    Max_Rows = 36
    Font_Size = 8
    # グローバルスコープと関数スコープ内で、rootが定義されているので
    # 警告がでる。気になるならmainを定義してスコープを分ける。
    def __init__(self, root):
        super().__init__(root)
        r = 0
        c = 0

        for color in Font:
            label = tk.Label(self, text=color,
                             font=(color, self.Font_Size, "bold"))
            label.grid(row=r, column=c, sticky="ew")
            r += 1

            if r > self.Max_Rows:
                r = 0
                c += 1

            self.pack(expand=1, fill="both")


if __name__ == '__main__':
    root = tk.Tk()
    root.title("Named Font Chart")
    # font.families()で使えるフォントを見る
    Font = list(font.families())
    app = FontChart(root)
    root.mainloop()
