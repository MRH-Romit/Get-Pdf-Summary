# PDF Summarizer using Streamlit,NLTK :: Natural Language Toolkit

This project is a simple PDF summarizer built with Streamlit. It allows users to upload a PDF file, extracts the text from the PDF, and generates a summary using NLTK.

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone <repository_url>
2. Navigate to the project directory:

   ```bash
     cd pdf-summarizer
3. install the required dependencies:
     ``` bash
     pip install streamlit
     pip install pdfplumber
     pip install nltk
     
# Usage
1. Run the Streamlit app: 
``` bash
  streamlit run app.py
```
2. Once the app is running, you can upload a PDF file using the file uploader.
3. The app will extract the text from the uploaded PDF file and generate a summary using NLTK.
4. The generated summary will be displayed in the app.

# Dependencies
Streamlit: streamlit
PDF text extraction: pdfplumber
Natural Language Processing: nltk

#File Structure
* app.py: Main Streamlit application script.
* text_extraction.py: Module containing functions for extracting text from PDF files.
* summarization.py: Module containing functions for summarizing text.
* requirements.txt: List of dependencies.

#screenshot
![image](https://github.com/MRH-Romit/Get-Pdf-Summary/assets/125377720/c97d31f1-fd4b-46c1-818c-1341e3e2f62c)

![image](https://github.com/MRH-Romit/Get-Pdf-Summary/assets/125377720/5fef19b0-6bb4-4838-81ef-8d00ea3a9d8d)

