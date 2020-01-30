class Person:
    def __init__(hoge, name, age):
        hoge.name = name
        hoge.age = age

    def overAge(foo, age):
        return foo.age >= age

    def say(hoo):
        print('私の名前は%sです。' % hoo.name)

taro = Person('太郎', 18)
taro.say()
if taro.overAge(20):
    print('%sは成年です。' % taro.name)
else:
    print('%sは未成年です。' % taro.name)

# taroがselfの実引数として呼び出されている。
# initはオブジェクト生成というコードに現れt内処理をしてから
# Person.__init__(生成したオブジェクト, 18)を呼び出して、
# 最後に生成したオブジェクトを返しているだけになります。
taro = Person('太郎', 18)
Person.say(taro)
if Person.overAge(taro, 20):
    print('%sは成年です。' % taro.name)
else:
    print('%sは未成年です。' % taro.name)