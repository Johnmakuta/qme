from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo, showerror, askyesno
from tkinter import filedialog as fd
import qrcode
import platform

def close_window():
    if askyesno(title = 'Close QME', message = 'Are you sure you want to close?'):
        window.destroy()

def generate_qrcode():
    qrcode_data = str(data_entry.get())
    qrcode_name = str(filename_entry.get())
    if qrcode_name == '':
        showerror(title = 'Error', message = 'An error occurred' \
                   '\nThe following is ' \
                    'the cause:\n->Empty filename entry field\n' \
                    'Make sure the filename entry field is filled when generating the QRCode')