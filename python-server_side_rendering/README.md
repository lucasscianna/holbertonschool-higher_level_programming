# Python - Server-Side Rendering with Flask

## Description

This project explores **Server-Side Rendering (SSR)** using **Python** and the **Flask** framework. Unlike client-side rendering where the browser builds the page via JavaScript, SSR generates fully formed HTML on the server before sending it to the client — resulting in faster load times, better SEO, and cleaner architecture.

Throughout this project, you will build a Flask application that dynamically generates web pages using the **Jinja2** templating engine, and integrates data from multiple sources: JSON files, CSV files, and SQLite databases.

---

## Learning Objectives

By the end of this project, you should be able to explain, without any external help:

- The concepts of **server-side rendering** and how it differs from **client-side rendering**
- The benefits of SSR in web development (SEO, performance, maintainability)
- How to implement SSR in Python using the **Flask** framework
- How to use the **Jinja2** templating engine to dynamically generate HTML pages
- How to read and display data from **JSON**, **CSV**, and **SQLite** sources
- How to handle **dynamic content** and **user inputs** in web applications

---

## Resources

- [MDN Server-Side Web Development](https://developer.mozilla.org/en-US/docs/Learn/Server-side)
- [Client-side vs Server-side vs Pre-rendering](https://www.toptal.com/front-end/client-side-vs-server-side-pre-rendering)
- [Flask Official Documentation](https://flask.palletsprojects.com/)
- [Jinja2 Documentation](https://jinja.palletsprojects.com/)
- [Python JSON Documentation](https://docs.python.org/3/library/json.html)
- [Python CSV Documentation](https://docs.python.org/3/library/csv.html)
- [Python SQLite Documentation](https://docs.python.org/3/library/sqlite3.html)

---

## Requirements

| Requirement | Detail |
|---|---|
| Language | Python 3 |
| Framework | Flask |
| Templating engine | Jinja2 |
| Data sources | JSON, CSV, SQLite |
| Rendering | Server-side only |

---

## Project Structure
```
python-server_side_rendering/
├── app.py                  # Main Flask application
├── templates/              # Jinja2 HTML templates
│   ├── index.html
│   └── ...
├── static/                 # Static files (CSS, JS, images)
├── data/                   # Data files (JSON, CSV, SQLite)
│   ├── data.json
│   ├── data.csv
│   └── database.db
└── README.md
```

---

## Key Concepts

### Server-Side vs Client-Side Rendering

| | Server-Side Rendering | Client-Side Rendering |
|---|---|---|
| HTML built by | Server (Python/Flask) | Browser (JavaScript) |
| SEO | ✅ Excellent | ⚠️ Limited |
| Initial load | ✅ Fast | ❌ Slower |
| Interactivity | ⚠️ Limited | ✅ Rich |

### Flask Basics
```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title='Home')

if __name__ == '__main__':
    app.run(debug=True)
```

### Jinja2 Templating
```html
<!-- templates/index.html -->
<h1>{{ title }}</h1>

{% for item in items %}
  <li>{{ item.name }}</li>
{% endfor %}

{% if user %}
  <p>Welcome, {{ user }}!</p>
{% endif %}
```

### Reading Data Sources
```python
import json, csv, sqlite3

# JSON
with open('data/data.json') as f:
    data = json.load(f)

# CSV
with open('data/data.csv') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

# SQLite
conn = sqlite3.connect('data/database.db')
cursor = conn.cursor()
cursor.execute('SELECT * FROM items')
rows = cursor.fetchall()
```

---

## How to Run
```bash
# Install dependencies
pip install flask

# Run the application
python3 app.py

# Open in your browser
http://127.0.0.1:5000/
```