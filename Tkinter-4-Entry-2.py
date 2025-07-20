from tkinter import * 

root = Tk()

entry = Entry(root, width=20)
entry.pack()

def myClick():
    text = entry.get()
    greet = 'Hello ' + text + '!'
    myLabel = Label(root, text= greet)
    myLabel.pack()
    entry.delete(0,END)       # entry delete korar jonno!!!!         0 means koto gul achar thakbe

myButton = Button(root, text= 'Click Me', command= myClick)
myButton.pack()

root.mainloop()