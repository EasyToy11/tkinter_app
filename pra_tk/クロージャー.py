"""
クロージャーとは

クロージャーは関数である。
もう少し突っ込むなら関数の中の関数で、
状態を保持できる関数である。

外部スコープにある変数にアクセスできる関数オブジェクト
"""
def outer():
    # 関数内で関数の宣言
    def inner():
        print('hello')

    # 宣言だけで実行はされないので、実行する。
    inner()


outer()

# 下記で変数speakは関数のような振る舞いをする
# というか関数になる。
speak = lambda:print('OK')
speak()

# 関数を返す関数
def outer():
    def speak():
        print('hey')
    # outerを実行すると関数内にあるspeakを返す
    return speak

# 関数内関数を呼び出して、実行
f = outer()
f()


# printの位置をずらす
def outer():
    a = 'OK!!'
    def speak():
        print(a)

    return speak

f = outer()
f()

# クロージャーを作る(状態を保持できるようにする）
"""
pythonではjavascriptと異なり、外の関数のスコープ変数には
参照できても代入はできない！！

回避法として外側の変数をミュータブル（リストや辞書型、セット）
などの型に定義することで、オブジェクトへの代入ができる。

nolocalというキーワードを使うことで、外側の変数にアクセスできる
クラスのインスタンス変数は同じスコープないなので、普通に代入できる

"""
def example():
    cnt = [0]
    def nakami():
        cnt[0] += 1
        print(cnt)

    return nakami

f = example()
f()
f()
f()
