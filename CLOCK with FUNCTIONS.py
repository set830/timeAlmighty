import sys


from Tkinter import *
import time





def tick():

    global time1
    global time2
    global time3

    time_string = time.strftime("%H:%M:%S")
    clock.config(text=time_string)
    clock.after(200,tick)


    if time_string == time1:
        time.sleep(0.99)
        print("HI")

    if time_string == time2:
        time.sleep(0.99)
        print("HEY")

    if time_string == time3:
        time.sleep(0.99)
        print("YOOOO")





def Labels(word):
    alarms = Label(bottomFrame, text=word, font=("times", 100,))
    return alarms








####
####
#### GUI IS MAIN FUNCTION
####
####



#User Inputs for words
words1 = input("enter your first command: ")
#"HI"
words2 = input("enter your second command: ")
#"HELLO"
words3 = input("enter your third command: ")
#"WHAT'S UP"



#User Inputs for times
time1 = input("enter the first time: ")
#""19:46:10"
time2 = input("enter the second time: ")
#""19:46:15"
time3 = input("enter the third time: ")
#""19:46:20"






#Assign Alarms to Labels for each Word
#alarm1 = Labels(words1)
#alarm2 = Labels(words2)
#alarm3 = Labels(words3)









#popup window for clock
root = Tk()






#### BUILDING THE CLOCK LAYOUT
#putting multiple frames on one blank window, root
topFrame = Frame(root)
topFrame.pack()

bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)


clock = Label(topFrame, font = ("times", 200, "bold"), bg= "white")
alarms = Labels(words3)


clock.pack()
alarms.pack()










tick()


root.mainloop()




#TEST



