# https://www.youtube.com/watch?v=J4wbwvkY4lM


import sys


from Tkinter import *
import time

def tick():

    time_string = time.strftime("%H:%M:%S")
    clock.config(text=time_string)
    clock.after(200,tick)

    global time1
    global time2
    global time3



    if time_string == time1:
        time.sleep(0.99)
        print("wake up")


    if time_string == time2:
        time.sleep(0.99)
        print("time for lunch")

    if time_string == time3:
        time.sleep(0.99)
        print("time for bed")






#popup window for clock
root = Tk()






#putting multiple frames on one blank window, root
topFrame = Frame(root)
topFrame.pack()

bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)


clock = Label(topFrame, font = ("times", 200, "bold"), bg= "white")
alarms = Label(bottomFrame, text = "Hello", font = ("times", 100,))


clock.pack()
alarms.pack()





#bg = background color
#int = size of clock









#These are user inputted values
time1 = "18:54:10"
time2 = "18:54:15"
time3 = "18:54:20"






tick()








root.mainloop()



#TEST2