# app.py
import yaml
from flask import Flask, render_template, send_from_directory
from functools import lru_cache

application = app = Flask(__name__)

# Load configuration
with open('config.yaml', 'r') as f:
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