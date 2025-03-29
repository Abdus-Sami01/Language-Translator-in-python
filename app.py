from flask import Flask, render_template
from routes import routes_app  # Import the Blueprint correctly
import os

# Use absolute path to templates and static folders
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Get backend/ directory
TEMPLATE_DIR = os.path.join(BASE_DIR, "../frontend/templates")
STATIC_DIR = os.path.join(BASE_DIR, "../frontend/static")

app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)

# Register the Blueprint
app.register_blueprint(routes_app, url_prefix="/")

# Home route
@app.route('/')
def home():
    return render_template("index.html")  # Correct usage

if __name__ == '__main__':
    app.run(debug=True)
