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
# this imports the cv2 module for image recognition
# import cv2 # not currently using
import platform

os = platform.system()

# creating the window using the Tk() class
window = Tk()
# creates title for the window
window.title('QME - QR Code Generator')
# adding the window's icon
if os == 'Windows':
    window.iconbitmap(window, 'icon.ico')

# dimensions and position of the window
window.geometry('500x480+440+180')
# makes the window non-resizable ie. can't drag it into different shapes. 
window.resizable(height=FALSE, width=FALSE) 

"""Styles for the widgets, labels, entries, and buttons"""
# style for the labels
label_style = ttk.Style()
label_style.configure('TLabel', foreground='#000000', font=('OCR A Extended', 11))
# style for the entries
entry_style = ttk.Style()
entry_style.configure('TEntry', font=('Dotum', 15))
# style for the buttons
button_style = ttk.Style()
button_style.configure('TButton', foreground='#000000', font=('DotumChe', 10))

""" Multi-Tab Setup """
# creating the Notebook widget
tab_control = ttk.Notebook(window)
# creating the two tabs with the ttk.Frame()
first_tab = ttk.Frame(tab_control)
second_tab = ttk.Frame(tab_control)
# adding the two tabs to the Notebook
tab_control.add(first_tab, text='QR Code Generator')
tab_control.add(second_tab, text='QR Code Detector')
# this makes the Notebook fill the entire main window so that its visible
tab_control.pack(expand=1, fill="both")

# run the main window infinitely
window.mainloop()

