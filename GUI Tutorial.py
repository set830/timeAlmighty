#https://www.youtube.com/watch?v=RJB1Ek2Ko_Y&t=7s

from Tkinter import *



#root is a blank window
root = Tk()


#Label() creates text on the root
#1: where do you want label to be placed? on the root
#2: what do you want to write?
#theLabel = Label(root, text = "Hello!!")





#putting multiple frames on one blank window, root
topFrame = Frame(root)
topFrame.pack()

bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)



Label1 = Label(topFrame, text = "Hello!!")
Label2 = Label(bottomFrame, text = "Yooo")


Label1.pack()
Label2.pack()







#When you have GUI, you need it to be open all the time unless its closed
root.mainloop()








