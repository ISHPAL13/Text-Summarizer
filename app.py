import os
import pandas as pd
from PyPDF2 import PdfReader
from flask import Flask, render_template, request, redirect, url_for
import google.generativeai as genai
import pytesseract
from pdf2image import convert_from_path
from PIL import Image

# Configure the Gemini API key
genai.configure(api_key='Enter ur own api key here')  # Replace with your actual API key

app = Flask(__name__)

# Ensure upload directory exists
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Function to read text from PDF files
def read_pdf(file_path):
    text = ""
    with open(file_path, 'rb') as file:
        reader = PdfReader(file)
        for page_num in range(len(reader.pages)):
            text += reader.pages[page_num].extract_text()

    # Use OCR if no text is found (i.e., the PDF contains images)
    if not text.strip():
        text = read_pdf_with_ocr(file_path)
    return text

# Function to read text from images in PDF files using OCR
def read_pdf_with_ocr(file_path):
    text = ""
    images = convert_from_path(file_path)
    for image in images:
        text += pytesseract.image_to_string(image)
    return text

# Function to read text from CSV files
def read_csv(file_path):
    df = pd.read_csv(file_path)
    text = df.to_string(index=False)  # Convert dataframe to string
    return text

# Function to summarize text using Gemini API
def summarize_text_gemini(text):
    prompt = "Summarize the following text:\n\n" + text
    response = genai.generate_text(model='models/text-bison-001', prompt=prompt)
    return response.result

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = file.filename
            file_path = os.path.join(UPLOAD_FOLDER, filename)
            file.save(file_path)

            # Check file type and read text accordingly
            if filename.endswith('.pdf'):
                text = read_pdf(file_path)
            elif filename.endswith('.csv'):
                text = read_csv(file_path)
            else:
                return render_template('index.html', error="Unsupported file type. Please upload a PDF or CSV file.")

            # Call summarize_text_gemini function
            summary = summarize_text_gemini(text)
            return redirect(url_for('loading', summary=summary))
    return render_template('index.html', error="File not uploaded.")

@app.route('/loading')
def loading():
    summary = request.args.get('summary')
    return render_template('loading.html', summary=summary)

@app.route('/result')
def result():
    summary = request.args.get('summary')
    return render_template('result.html', summary=summary)

if __name__ == '__main__':
    app.run(debug=True)
