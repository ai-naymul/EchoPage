import tkinter as tk
from tkinter import filedialog
import PyPDF2
from gtts import gTTS
import pygame

pygame.mixer.init()


window = tk.Tk()
window.geometry('600x600')
window.title("EchoPage: A Python-based PDF to Speech Converter")


def upload_file():
    file = filedialog.askopenfilename(title='Select Your File(PDF only)')
    if file:
        file_selected_label.config(text=f'File: {file} is selected')
        file_selected_label.grid(row=1, column=0)

        #3 open the file with pypdfreader
        with open(file, 'rb') as f:
            pdf_reader = PyPDF2.PdfReader(f)
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text = page.extract_text()
        ## create a output file in output folder and write the extracted text into the text file
        with open('output/output.txt', 'w', encoding='utf-8') as f:
            f.write(text)
        
        with open("output/output.txt", 'r') as f:
            text_content = f.read()
            tts = gTTS(text=text_content, lang='en')
            tts.save('output/output.mp3')
            file_selected_label.config(text=f'Audio is saved in the output folder')
            file_selected_label.grid(row=1, column=0)
        


def play_audio():
    pygame.mixer.music.load("output/output.mp3")
    pygame.mixer.music.play()



## Widgets

welcome_msg = tk.Label(text="Welcome to the EchoPage", font=('Arial', 25, 'bold'))
upload_button = tk.Button(text="Upload File", width=20, height=2, command=upload_file)
file_selected_label = tk.Label()
play_audio_btn = tk.Button(text='Click to play the PDF', width=20, height=2, command=play_audio)



## Locations
welcome_msg.grid(row=0,column=0)
upload_button.grid(row=2,column=0)
play_audio_btn.grid(row=3,column=0)






window.mainloop()