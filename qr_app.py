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
    else:
        if askyesno(title='Confirmation', message=f'Do you want to create a QRCode with the provided information?'):
            try:
                qr = qrcode.QRCode(version = 1, box_size = 6, border = 4)
                qr.add_data(qrcode_data)
                qr.make(fit = True)
                name = qrcode_name + '.png'
                qrcode_image = qr.make_image(fill_color = 'black', back_color = 'white')
                qrcode_image.save(name)
                global Image
                Image = PhotoImage(file=f'{name}')
                image_label1.config(image=Image)
                reset_button.config(state=NORMAL, command=reset)
            except:
                showerror(title='Error', message='Please provide a valid filename')


def reset():
    if askyesno(title='Reset', message='Are you sure you want to reset?'):
        image_label1.config(image='')
        reset_button.config(state=DISABLED)

def open_dialog():
    name = fd.askopenfilename()
    file_entry.delete(0, END)
    file_entry.insert(0, name)

os = platform.system()

window = Tk()
window.title('QME - QR Code Generator')
if os == 'Windows':
    window.iconbitmap(window, 'icon.ico')

window.geometry('500x480+440+180')
window.resizable(height=FALSE, width=FALSE) 

window.protocol('WM_DELETE_WINDOW', close_window)

label_style = ttk.Style()
label_style.configure('TLabel', foreground='#000000', font=('OCR A Extended', 11))
entry_style = ttk.Style()
entry_style.configure('TEntry', font=('Dotum', 15))
button_style = ttk.Style()
button_style.configure('TButton', foreground='#000000', font=('DotumChe', 10))


tab_control = ttk.Notebook(window)
first_tab = ttk.Frame(tab_control)
second_tab = ttk.Frame(tab_control)
tab_control.add(first_tab, text='Basic')
tab_control.add(second_tab, text='Advanced')
tab_control.pack(expand=1, fill="both")

""" Adding Canvas to Each Tab """
# creates the canvas for containing all the widgets in the first tab
first_canvas = Canvas(first_tab, width=500, height=480)
# packing the canvas to the first tab
first_canvas.pack()
# creates the canvas for containing all the widgets in the second tab
second_canvas = Canvas(second_tab, width=500, height=480)
# packing the canvas to the second tab
second_canvas.pack()

"""Widgets for the first tab"""
# creating an empty label
image_label1 = Label(window)
# adding the label to the canvas
first_canvas.create_window(250, 150, window=image_label1)

""" Two Labels and Two Entries """
""" QRcode Data Input """
# creating a ttk label
qrdata_label = ttk.Label(window, text='QRcode Data', style='TLabel')
# creating a ttk entry
data_entry = ttk.Entry(window, width=55, style='TEntry')
# adding the label to the canvas
first_canvas.create_window(70, 330, window=qrdata_label)
# adding the entry to the canvas
first_canvas.create_window(300, 330, window=data_entry)
""" Filename """
# creating a ttk label
filename_label = ttk.Label(window, text='Filename', style='TLabel')
# creating a ttk entry
filename_entry = ttk.Entry(width=55, style='TEntry')
# adding the label to the canvas
first_canvas.create_window(84, 360, window=filename_label)
# adding the entry to the canvas
first_canvas.create_window(300, 360, window=filename_entry)

""" Two Buttons """
# creating the reset button in a disabled mode
reset_button = ttk.Button(window, text='Reset', style='TButton', state=DISABLED)
# creating the generate button
generate_button = ttk.Button(window, text='Generate QRCode', style='TButton',  command=generate_qrcode)
# adding the reset button to the canvas
first_canvas.create_window(300, 390, window=reset_button)
# adding the generate button to the canvas
first_canvas.create_window(410, 390, window=generate_button)




"""Widgets for the second tab"""
# creating the second image label
image_label2 = Label(window)
# creating the data label
data_label = ttk.Label(window)
# adding the second image label to the second_canvas
second_canvas.create_window(250, 150, window=image_label2)
# adding the data label to the canvas
second_canvas.create_window(250, 300, window=data_label)

""" The File Entry and the Browse Button """
# creating the file_entry
file_entry = ttk.Entry(window, width=60, style='TEntry')
# creating the browse button
browse_button = ttk.Button(window, text='Browse', style='TButton', command=open_dialog)

# adding the entry to the second canvas in the second tab
second_canvas.create_window(200, 350, window=file_entry)
# adding the generate button to the second canvas in the second tab
second_canvas.create_window(430, 350, window=browse_button)




window.mainloop()
