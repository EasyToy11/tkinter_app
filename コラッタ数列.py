
def collatz(number):
    if number % 2 == 0:
        return number / 2
    else:
        return (3 * number) + 1


while True:
    try:
        print('コラッタ数列。数字を記入する')
        input_number = int(input())
        break
    except ValueError:
        print('数字を入力してください')

while input_number > 1:
    input_number = collatz(input_number)
    print(input_number)

