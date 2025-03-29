from flask import Blueprint, request, render_template
from werkzeug.utils import secure_filename
import os
from translator import translate_text, LANGUAGES  # Import translation function & languages

routes_app = Blueprint("routes_app", __name__)

# Configure upload folder
UPLOAD_FOLDER = r"D:\python files\Internship_tasks\CodeAlpha\LnaguageTranslator\backend\uploads"
ALLOWED_EXTENSIONS = {"txt", "pdf", "docx"}
TEMPLATE_FOLDER = r"D:\python files\Internship_tasks\CodeAlpha\LnaguageTranslator\backend\templates"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    """Checks if the uploaded file is allowed."""
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

@routes_app.route("/")
def home():
    """Renders the file upload form."""
    return render_template("index.html", template_folder=TEMPLATE_FOLDER, languages=LANGUAGES)

import re

def clean_text(text):
    text = re.sub(r"[-_=]{4,}", "", text)  # Remove long dashes and underscores
    text = re.sub(r"\s{2,}", " ", text)  # Remove extra spaces/newlines
    return text.strip()


@routes_app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == "POST":
        uploaded_file = request.files.get("file")
        selected_language = request.form.get("language")
        
        if uploaded_file and selected_language:
            text = uploaded_file.read().decode("utf-8")  # Read file content
            translated_text = translate_text(text, selected_language)  # Translate text

            return render_template("results.html", result=translated_text, language=selected_language)
        
        return "No file uploaded or no language selected", 400  
    

@routes_app.route('/results', methods=['POST'])
def results():
    """Processes file and shows translation results."""
    uploaded_file = request.files.get("file")
    selected_language = request.form.get("language")

    if uploaded_file and selected_language:
        text = uploaded_file.read().decode("utf-8", errors="ignore")  # Read file content
        cleaned_text = clean_text(text)
        translated_text = translate_text(cleaned_text, selected_language) # Translate

        return render_template("results.html", result=translated_text, language=selected_language)
    
    return "No file uploaded or no language selected", 400
