from tkinter import *
from time import *

def display(): # displays time
    time_string = strftime("%I:%M:%S %p") # %Hour:%Minute:%Second %AMorPM | strftime retrieves exact time from time package 
    time_label.config(text=time_string) # changes actual UI to show time

    day_string = strftime("%A") # %DayofWeek 
    day_label.config(text=day_string)

    date_string = strftime("%B %d, %Y")
    date_label.config(text=date_string)

    time_label.after(1000, display) # clock updates after every 1000 milisecond (1 second)

window = Tk()

# display time
time_label = Label(window, font=("Arial", 50), fg="#4CBB17", bg="black") # uses tkinter to display time
time_label.pack()

# day of the week
day_label = Label(window, font=("Arial", 25)) # uses tkinter to display day of week
day_label.pack()

# date
date_label = Label(window, font=("Arial", 25)) # uses tkinter to display date
date_label.pack()

display() # calls on function to display clock which is recursive function to constantly update
window.mainloop()