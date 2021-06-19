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

#Main image
bigPhoto = PhotoImage(file="Images/MainImage.PNG")
Label(window, image=bigPhoto, bg="white", borderwidth=0, highlightthickness=0).grid(row=0,column=0)

Label(window, text="Enter course code", bg="black", fg="white", font="none 10 ").grid(row=1, column=0)
textEntry = Entry(window, width=15, bg="white")
textEntry.grid(row=2, column=0)

Label(window, text="Do you want to see the window?(yes/no)", bg="black", fg="white", font="none 10 ").grid(row=3, column=0)
screenEntry = Entry(window, width=15, bg="white")
screenEntry.grid(row=4, column=0)

Button(window, text="Submit", width=6, command=click).grid(row=6, column=0)

Label(window, text="Download Complete!", bg="black", fg="white", font="none 12 ").grid(row=7, column=0)
#To run the window
window.mainloop()