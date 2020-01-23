import schedule
import time

def job():
    # 定期実行させたい処理
    print('Do Action')

def main():
    # 10秒ごと
    schedule.every(5).seconds.do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)

main()