"""
Python scheduler notifier:
"""


from pygame import mixer
from plyer import notification
import time


def LoopMusic(file, stop):
    mixer.init()
    mixer.music.load(file)
    # -1 to play it on loop
    mixer.music.play(-1)
    while True:
        a = input("Stop here: ")
        if a == stop:
            mixer.music.stop()
            break


def notifier(e):
    notification.notify(title = 'Task Alert!',
                        message = task_dict[e],
                        app_icon = 'icon.ico',
                        timeout = 15
                        )


def LogData(msg):
    with open("healthlog.txt", "a") as f:
        f.write(f"{msg} {time.ctime()} \n")


def current():
    named_tuple = time.localtime()
    time_string = time.strftime("%H:%M", named_tuple)
    return time_string


if __name__ == '__main__':

    water = time.time()
    physical = time.time()

    watertime = 60*60       # 1 hour
    physicaltime = 45*60    # 45 mins

    d = {}
    n = int(input("Enter number of tasks: "))
    for i in range(n):
        task_time = input("Enter time in 24-hour time format <HH:MM>: ")
        notify = input("Enter task or notification message: ")
        d[task_time] = notify

    task_dict = dict(sorted(d.items(), key=lambda x: x[0]))

    while True:

        # time() will give current time and if difference b/w current time
        # and initial time becomes greater than task time, alarm will go off.

        if (time.time() - water) > watertime:
            print("Time to drink water. Enter 'drank' to stop alarm: ")
            LoopMusic('water.mp3', 'drank')
            water = time.time()
            LogData("Hydrated myself on")

        if (time.time() - physical) > physicaltime:
            print("Time to workout. Enter 'done' to stop alarm: ")
            LoopMusic('physical.mp3', 'done')
            physical = time.time()
            LogData("Did physical exercise on")

        e = current()
        if e in task_dict:
            notifier(e)
            print("Press 'ok' to turn off the alarm.")
            LoopMusic("alarm.mp3", "ok")
            LogData(task_dict[e] + ' - task notification on')
            time.sleep(60)
