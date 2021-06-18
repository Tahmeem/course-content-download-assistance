from tkinter import *

window = Tk()
window.title("Course Material Downloader")
window.configure(background="black")

bigPhoto = PhotoImage(file="Images/MainImage.PNG")
Label(window,image=bigPhoto,bg="white",borderwidth=0,highlightthickness=0).grid(row=0,column=0)
window.mainloop()