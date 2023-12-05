# this imports everything from the tkinter module
from tkinter import *
# importing the ttk module from tkinter that's for styling widgets
from tkinter import ttk
# importing message boxes like showinfo, showerror, askyesno from tkinter.messagebox
from tkinter.messagebox import showinfo, showerror, askyesno
# importing filedialog from tkinter
from tkinter import filedialog as fd 
# this imports the qrcode module
import qrcode
# this imports the cv2 module
import cv2

# creating the window using the Tk() class
window = Tk()
# creates title for the window
window.title('QR Code Generator-Detector')
# adding the window's icon
window.iconbitmap(window, 'icon.ico')
# dimensions and position of the window
window.geometry('500x480+440+180')
# makes the window non-resizable
window.resizable(height=FALSE, width=FALSE)
# run the main window infinitely
window.mainloop()