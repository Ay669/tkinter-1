from tkinter import *

window = Tk()
window.title('tkinter sample window')
window.geometry('300x300')

# label
greting = Label(text="Hello user", fg='black', bg='white')
# button
button = Button(text='Click me', fg='black', bg='white')
# entry
entry = Entry(fg="yellow", bg="blue",width=50)


greting.pack()
button.pack()
entry.pack()

frame = Frame(master=window, relief=RAISED, borderwidth=5)
frame.pack()
label = Label(master=frame, text="sample frame")
label.pack()

textbox = Text(fg='green', bg='yellow')
textbox.pack()

window.mainloop()