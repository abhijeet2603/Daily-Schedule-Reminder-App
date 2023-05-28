import time
import winsound

times = ["09:00","12:15","06:00","08:30"]
activities = ["Break fast time","Lunch time","Meditation time","Dinner time"]

i = 0
count = 0

while True:
    current_time = time.strftime("%H:%M",time.localtime())

    if current_time == times[i]:
        winsound.Beep(4000,1000)
        print(activities[i])
        count = count+1
        if count == 10:
            print("Beep Ends")
            i = i+1
            if i == 4:
                i = 0
            count = 0
