# EchoPage: A Python-based PDF to Speech Converter

EchoPage is a simple Python application that converts PDF text into speech. It uses the tkinter library for the GUI, PyPDF2 to handle PDF files, gTTS (Google Text-to-Speech) to convert text into speech, and pygame to play the audio.

## How to Use

1. Run the `main.py` script to start the application.
2. Click the "Upload File" button to select a PDF file from your system.
3. After selecting a file, the application will automatically read the PDF and save the text.
4. Click the "Click to play the PDF" button to hear the PDF text as speech.

## Code Overview

The application consists of three main files:

- `main.py`: This is the main script that runs the application. It sets up the GUI and handles user interactions.

- `pdfhandler.py`: This script contains the PDFHandler class, which handles uploading a PDF file, reading the text from the PDF, and saving the text.

- `audiohandler.py`: This script contains the AudioHandler class, which converts the saved text into speech and plays the audio.

## Changes Made

The PDFHandler class in `pdfhandler.py` was modified to include a new method [upload_and_process_file](file:///e%3A/Professional%20Python%20Project/EchoPage/pdfhandler.py#23%2C9-23%2C9). This method uploads a file, reads the PDF, and saves the text only after a file has been uploaded.
    ```class PDFHandler:
    # existing code...
    def upload_and_process_file(self):
    self.upload_file()
    if self.file:
    self.read_pdf()
    self.save_text()```


In `main.py`, the command for the upload button was changed to call the new [upload_and_process_file](file:///e%3A/Professional%20Python%20Project/EchoPage/pdfhandler.py#23%2C9-23%2C9) method in PDFHandler.

```upload_button = tk.Button(text="Upload File", width=20, height=2,    command=pdf_handler.upload_and_process_file)```


These changes ensure that the PDF is read and the text is saved only after a file has been uploaded, preventing errors when trying to read a file that hasn't been selected yet.