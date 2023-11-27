from tkinter import filedialog
import PyPDF2
class PDFHandler:
    def __init__(self):
        self.file = None
        self.text = None
    def upload_file(self):
        self.file = filedialog.askopenfilename(title='Select Your File(PDF only)')
        if not self.file:
            print("No file selected.")
            return
        return self.file
    def read_pdf(self):
        with open(self.file, 'rb') as f:
            pdf_reader = PyPDF2.PdfReader(f)
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                self.text = page.extract_text()
                return self.text
    def save_text(self):
        with open('output/output.txt', 'w', encoding='utf-8') as f:
            f.write(self.text)
    def upload_and_process_file(self):
        self.upload_file()
        if self.file:
            self.read_pdf()
            self.save_text()


