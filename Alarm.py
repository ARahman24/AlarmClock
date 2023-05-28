from tkinter import *
import datetime
import time
import winsound


def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        if now == set_alarm_timer:
            print("Time to Wake up")
            winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
            break

def actual_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer)


new_clock = Tk()
new_clock.geometry("600x400")
new_clock.title("Alarm clock") 
l0=Label(new_clock,text="Alarm clock by Abdul Rahman").place(x=420,y=380)
l1=Label(new_clock,text="⏰⏰⏰⏰  ALARM CLOCK  ⏰⏰⏰⏰",font=("Arial",15,"bold")).place(x=90,y=10)
l2=Label(new_clock,text="Enter Time = ",font=("Arial",15)).place(x=10,y=140)
l3=Label(new_clock,text = " Hour     Min        Sec",font=("Arial",15)).place(x = 140,y=110)

hour = StringVar()
min = StringVar()
sec = StringVar()

#Time required to set the alarm clock:
hourTime= Entry(new_clock,textvariable = hour,width = 15).place(x=140,y=146)
minTime= Entry(new_clock,textvariable = min,width = 15).place(x=200,y=146)
secTime = Entry(new_clock,textvariable = sec,width = 15).place(x=280,y=146)

#To take the time input by user:
submit = Button(new_clock,text = "Set Alarm",font=("Arial",15),fg="red",width = 10,command = actual_time).place(x =200,y=200)


new_clock.mainloop()
