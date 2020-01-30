import tkinter as tk
"""
イベントをきっかけにプログラムが起動されることを
「イベントドリブン(eventdriben)イベント駆動」という
eventdriven型のアプリケーションは以下のような
メインルーチンを持っている

1．初期化
2．イベントの取得
3．イベントの種類によって処理を振り分ける
4．2に戻る。

2から4をイベントループと呼び、ユーザー入力などのイベントを待つ。
3の処理に対応する機能をbindingという
bindingはイベントが発生したときに、それに応じたプログラムを実行する
このプログラムを「イベントハンドラ」とか「コールバック関数」とよぶ

※メインルーチンとは、プログラムのメインの部分のことで、
対比として、メインルーチンから呼び出されるサブルーチンという言葉がある。

"""
# ウインドウの作成
root = tk.Tk()

# textvariable?の文字列版
buff = tk.StringVar()
# set()でデータをセットし、get()でデータの取得
# set()を書き換えることでラベルの表示を変更する（後述）
buff.set("")

label = tk.Label(root, textvariable=buff)
label.pack(anchor='w')


# クロージャー。引数nの値が関数内に保持される
def make_cmd(n):
    return lambda: buff.set('button {} pressed'.format(n))


for x in range(4):
    button = tk.Button(root, text='Button {}'. format(x), command=make_cmd(x))
    # ジオメトリーマネージャーで配置を決定する
    # anchorでどこ寄せか決めて、sideで詰め込む方向を決める。bothで空白いっぱい
    button.pack(side='left')


print(locals())

root.mainloop()
