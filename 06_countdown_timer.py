import time
from tkinter import *
from playsound import playsound


window = Tk()
window.geometry('400x300')
window.resizable(0, 0)
#window.config(bg = 'yellow')
window.title('Countdown Timer')
Label(window, text = 'Clock and countdown Timer').pack()


#create current Time
Label(window, font = 'arial 15', text = 'current time:').place(x = 40, y = 70)

curr_time = Label(window, font = 'arial 15', text = '')
curr_time.place(x = 190, y = 70)

def clock():
    clock_time = time.strftime('%H:%M:%S %p')
    curr_time.config(text = clock_time)
    curr_time.after(1000, clock)
    

clock()


# create function to start timer

sec = StringVar()
Entry(window, textvariable = sec, width = 2, font = 'arial 12').place(x = 250, y = 155)
sec.set('00')

mins = StringVar()
Entry(window, textvariable = mins, width = 2, font = 'arial 12').place(x = 225, y = 155)
mins.set('00')

hrs = StringVar()
Entry(window, textvariable = hrs, width = 2, font = 'arial 12').place(x = 200, y = 155)
hrs.set('00')



def countdown():

    times = int(hrs.get())*3600 + int(mins.get())*60 + int(sec.get())

    while times > -1:
        minute, second = (times // 60, times % 60)
        
        hour = 0
        if minute > 60:
            hour, minute = (minute // 60, times % 60)
        
        sec.set(second)
        mins.set(minute)
        hrs.set(hour)
        
        window.update()
        time.sleep(1)
        
        if times == 0:
            playsound('clock_sound.mp3')

            sec.set('00')
            mins.set('00')
            hrs.set('00')
        
        times -= 1

# create bottons
Label(window, text = 'set the time', font = 'arial 15').place(x = 40, y = 150)

Button(window, text = 'Start', bd = '5', command = countdown, font = 'arial 10').place(x = 150, y = 210)

window.mainloop()
