from Tkinter import *
import time
import subprocess




####
####
#### FUNCTIONS
####
####

#Function to speak out-loud each inputted command
def say(text):
    subprocess.call(['say', text])


#Clock Function
def RunTheClock():

    global time1
    global time2
    global time3

    global words1
    global words2
    global words3


    #Building Clock Functionality
    time_string = time.strftime("%H:%M:%S")
    clock.config(text=time_string)
    clock.after(200,RunTheClock)

    #Adhering each time to each command
    if time_string == time1:
        say(words1)

    if time_string == time2:
        say(words2)

    if time_string == time3:
        say(words3)


#Building Labels for Each Alarm
def AlarmLabel(position, word, time):
    alarm = Label(position, text=time + " - " + word, font=("times", 70, "italic"))
    return alarm






####
####
#### GUI IS MAIN FUNCTION
####
####



#### INPUTS:

## User Inputs for Commands (inout as string):
words1 = input("enter your first command: ")
words2 = input("enter your second command: ")
words3 = input("enter your third command: ")

#User Inputs for Times (input as string, in military time):
time1 = input("enter the first time: ")
time2 = input("enter the second time: ")
time3 = input("enter the third time: ")





#### BUILDING THE CLOCK LAYOUT:

#popup window for clock
root = Tk()

#putting multiple frames on one blank window, root
clockFrame = Frame(root)
clockFrame.pack()

topFrame = Frame(root)
topFrame.pack()

middleFrame = Frame(root)
middleFrame.pack()

bottomFrame = Frame(root)
bottomFrame.pack()


#Building the Clock Frame
clock = Label(clockFrame, font = ("times", 200, "bold"), bg= "white")


#Building Each Command Frame
alarm1 = AlarmLabel(topFrame, words1, time1)
alarm2 = AlarmLabel(middleFrame, words2, time2)
alarm3 = AlarmLabel(bottomFrame, words3, time3)


#Packing all frames together on same window
clock.pack()
alarm1.pack()
alarm2.pack()
alarm3.pack()




#### START THE CLOCK:

#Call Clock Function
RunTheClock()

#Allow for infinite loop, so clock can run infinitely until user exits out of application
root.mainloop()





