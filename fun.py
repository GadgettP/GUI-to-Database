import datetime
import time
import winsound
from tkinter import *
import tkinter as tk
from tkcalendar import Calendar
from GUItimer import *



#def myClick():
#    myLabel = Label(root, text="Are you sure you want to set a Reminder?")
#    myLabel.pack()

def set_reminder():
        print("Please enter the date and time for your reminder.")
        year = int(input("Year: "))
        month = int(input("Month: "))
        day = int(input("Day: "))
        hour = int(input("Hour (24-hour format): "))
        minute = int(input("Minute: "))
        reminder_time = datetime.datetime(year, month, day, hour, minute)
        if reminder_time < datetime.datetime.now():
            print("Reminder: You cannot set reminders for past events")
            restart = input('Would you like to set a different Reminder?')
            if restart == "yes":
                main()
            else:
                exit()

def main():
    reminder_time = set_reminder()
    current_time = datetime.datetime.now()
    if current_time >= reminder_time:
        print("Reminder: Your event is happening now!")
        frequency = 777  # frequency in Hz
        duration = 1000  # duration in milliseconds
        winsound.Beep(frequency, duration)
    else:
        time.sleep(1)  # check again in 1 second

root = tk.Tk()

root.geometry("500x500")
root.title("Rhoto")

#myButton = Button(root, text="Set Reminder?", command=main)
#myButton.pack()

#myEntry = tk.Entry(root)
#myEntry.pack()

cal = Calendar(root, selectmode = 'day',
               year = 2020, month = 5,
               day = 22)

cal.pack(pady=20)

def grad_date():
    date.config(text = "Selected Date is: " + cal.get_date())
    if cal.get_date() > datetime.datetime.now():
        print("You cannot set a reminder for a date that has already passed")
    else:
        pass


Button(root, text = "Get Date",
       command = grad_date, ).pack(pady = 20)

 
date = Label(root, text = "")
date.pack(pady = 20)

root.mainloop()


if __name__ == "__main__":
    main()
