# Text Summarizer AI Tool

This is a web-based application that allows users to summarize text from PDF and CSV files using Google's Generative AI API. The application is built using Flask, and it supports uploading files and entering text prompts for summarization.

## Features
- *PDF Summarization*: Upload a PDF file and get a summarized version of the text.
- *CSV Summarization*: Upload a CSV file and get a summarized version of the text.
- *Text Prompt Summarization*: Enter a text prompt directly and receive a summary.

## Technologies Used
- Python
- Flask
- pandas
- PyPDF2
- Google Generative AI API

## Setup Instructions

### Prerequisites
- Python 3.x
- pip (Python package installer)


text-summarization-ai/
│
├── README.md              # Project description and instructions
├── requirements.txt       # List of dependencies
├── app.py                 # Flask application for web interface
│
├── uploads/               # Directory for uploaded files (create if not exists)
│
├── templates/             # HTML templates for Flask app
│   ├── index.html         # Homepage template
│   ├── loading.html       # Loading page template
│   └── result.html        # Result page template
│
├── static/                # Static files for Flask app (CSS, JS, etc.)
│   ├── style.css          # CSS styles for templates
│   └── script.js          # JavaScript for client-side functionality
