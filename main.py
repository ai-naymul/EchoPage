import tkinter as tk
from pdfhandler import PDFHandler
from audiohandler import AusioHandler


pdf_handler = PDFHandler()
audio_handler = AusioHandler()


window = tk.Tk()
window.geometry('600x600')
window.title("EchoPage: A Python-based PDF to Speech Converter")


## Widgets

welcome_msg = tk.Label(text="Welcome to the EchoPage", font=('Arial', 25, 'bold'))
upload_button = tk.Button(text="Upload File", width=20, height=2, command=pdf_handler.upload_and_process_file)
file_selected_label = tk.Label()
play_audio_btn = tk.Button(text='Click to play the PDF', width=20, height=2, command=audio_handler.process_audio)



## Locations
welcome_msg.grid(row=0,column=0)
upload_button.grid(row=2,column=0)
play_audio_btn.grid(row=3,column=0)






window.mainloop()