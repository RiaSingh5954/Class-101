import time

def countDown_timer(seconds):
    while seconds>0:
        minutes = int(seconds/60)
        secs = int(seconds%60)
        timer = f'{minutes}:{secs}'
        print(timer)
        seconds -= 1
    print("time up!")

seconds = input("Enter the time in number of seconds :")

countDown_timer(int(seconds))
