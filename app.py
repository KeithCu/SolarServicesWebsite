# app.py
import yaml
import os
from flask import Flask, render_template, send_from_directory
from functools import lru_cache

application = app = Flask(__name__)

# Get the directory of the current script
script_dir = os.path.dirname(__file__)
config_path = os.path.join(script_dir, 'config.yaml')

# Load configuration
with open(config_path, 'r') as f:
    config = yaml.safe_load(f)

@app.route("/")
@lru_cache(maxsize=None)
def home():
    """Renders the main homepage."""
    return render_template("index.html", config=config)

@app.route("/robots.txt")
@lru_cache(maxsize=None)
def robots_txt():
    return send_from_directory(app.static_folder, 'robots.txt')

@app.route("/sitemap.xml")
@lru_cache(maxsize=None)
def sitemap():
    return send_from_directory(app.static_folder, 'sitemap.xml')

if __name__ == "__main__":
    app.run(debug=False)