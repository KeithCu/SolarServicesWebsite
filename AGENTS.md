# Agent Instructions

This document provides instructions for AI agents working on the KC (and the) Sunshine Man -- Solar Service website.

## Project Overview

This is a simple, single-page "brochure" website for a local solar panel maintenance and repair business. It is built with Python and Flask on the backend and standard HTML/CSS with Bootstrap on the frontend.

## Technology Stack

*   **Backend:** Python, Flask
*   **Frontend:** HTML, CSS, Bootstrap 5
*   **Templating:** Jinja2 (via Flask)

## File Structure

*   `app.py`: The main Flask application file. It contains all routing logic.
*   `templates/index.html`: The single HTML file that makes up the entire website.
*   `static/`: This directory contains all static assets:
    *   `style.css`: Custom CSS styles.
    *   Images (`.webp`, `.ico`): All website images and the favicon.
    *   `robots.txt`: Rules for search engine crawlers.
    *   `sitemap.xml`: The sitemap for search engines.
*   `AGENTS.md`: This file.
*   `ROADMAP.md`: A file outlining potential future work.

## How to Run the Application

The application can be run locally using the following command:

```bash
python app.py
```

The Flask application is configured with `debug=False`, which is suitable for a production environment.

## Key Conventions

*   The website is a single page, with navigation links (`#home`, `#about`, etc.) pointing to different sections of `index.html`.
*   All SEO-related files (`robots.txt`, `sitemap.xml`) are served from the `static` folder via dedicated routes in `app.py`.
*   The site uses Bootstrap for its primary styling, with minor overrides in `static/style.css`.