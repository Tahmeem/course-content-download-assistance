from tkinter import *
processComplete = False
def click():
    courseCode = textEntry.get()
    screenOption = screenEntry.get()

def printDone():
    processComplete = True

window = Tk()
window.title("Course Material Downloader")
window.configure(background="black")
window.geometry("600x400")

#Main image
bigPhoto = PhotoImage(file="Images/MainImage.PNG")
windowImage = Label(window, image=bigPhoto, bg="white", borderwidth=0, highlightthickness=0)
windowImage.place(x=300, y=50, anchor="center")

course_code = Label(window, text="Enter course code", bg="black", fg="white", font="none 10 ")
course_code.place(x=300,y=120,anchor="center")
textEntry = Entry(window, width=20, bg="white")
textEntry.place(x=300,y=150,anchor="center")

screenOption = Label(window, text="Do you want to see the window?(yes/no)", bg="black", fg="white", font="none 10 ")
screenOption.place(x=300,y=200,anchor="center")

screenEntry = Entry(window, width=20, bg="white")
screenEntry.place(x=300,y=230,anchor="center")

submitButton = Button(window, text="Submit", width=6, command=click)
submitButton.place(x=300,y=270,anchor = "center")

finalOutput = Label(window, text="Download Complete!", bg="black", fg="white", font="none 12 ")
finalOutput.place(x=300,y=320,anchor = "center")

#To run the window
window.mainloop()