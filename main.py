import tkinter as tk
from tkinter import filedialog


window = tk.Tk()
window.geometry('600x600')
window.title("EchoPage: A Python-based PDF to Speech Converter")


def upload_file():
    file = filedialog.askopenfilename(title='Select Your File(PDF only)')
    if file:
        print(f'File : {file} is selected')

welcome_msg = tk.Label(text="Welcome to the EchoPage", font=('Arial', 25, 'bold'))
upload_button = tk.Button(text="Upload File", width=20, height=2, command=upload_file)
welcome_msg.grid(row=0,column=0)
upload_button.grid(row=1,column=0)



window.mainloop()