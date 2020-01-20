import pygame.mixer
import schedule
import time

def Alarm():
    print("時間です")
    Sound()
    exit()

def Sound():
    pygame.mixer.init()
    pygame.mixer.music.load('alerm1.mp3')
    pygame.mixer.music.play(-1)
    input()
    pygame.mixer.music.stop()


print("目覚ましをセットします")
hour = input("時間:")
minute = input("分")
target = f"{hour.zfill(2)}:{minute.zfill(2)}"
print(target+"にアラームをセットしました")

schedule.every().day.at(target).do(Alarm)

while True:
    schedule.run_pending()
    time.sleep(1)

